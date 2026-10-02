import gradio as gr
from core.chat_interface import ChatInterface
from core.document_manager import DocumentManager
from core.rag_system import RAGSystem
import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

def create_gradio_ui():
    rag_system = RAGSystem()
    rag_system.initialize()
    
    doc_manager = DocumentManager(rag_system)
    chat_interface = ChatInterface(rag_system)
    
    def format_file_list():
        files = doc_manager.get_markdown_files()
        if not files:
            return """
            <div class="document-list document-list--empty">
                <div class="document-empty">No documents available in the knowledge base</div>
            </div>
            """

        rows = []
        for file_path in files:
            file_name = os.path.basename(file_path)
            is_markdown = file_name.lower().endswith(".md")
            kind = "Markdown document" if is_markdown else "PDF document"
            rows.append(f"""
            <div class="document-row">
                <div class="document-main">
                    <div class="document-icon" aria-hidden="true">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M7 3.75C6.17157 3.75 5.5 4.42157 5.5 5.25V18.75C5.5 19.5784 6.17157 20.25 7 20.25H17C17.8284 20.25 18.5 19.5784 18.5 18.75V8.25L14.5 3.75H7Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>
                            <path d="M13.5 3.75V8.25H18.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M8.5 12.5H15.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                            <path d="M8.5 16H13.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                        </svg>
                    </div>
                    <div class="document-meta">
                        <div class="document-name">{file_name}</div>
                        <div class="document-subtext"><span>{kind}</span><span class="document-separator">·</span><span>Indexed and ready</span></div>
                    </div>
                </div>
                <div class="document-status"><span class="status-dot"></span>Indexed</div>
                <button type="button" class="document-menu" aria-label="Document actions">⋯</button>
            </div>
            """)

        return "<div class='document-list'>" + "".join(rows) + "</div>"

    def format_documents_summary():
        source_count = len(doc_manager.get_markdown_files())
        source_label = "source" if source_count == 1 else "sources"
        return f"""
        <div class="documents-summary">
            <h3>Your documents</h3>
            <p>{source_count} {source_label} in your knowledge base</p>
        </div>
        """
    
    def upload_handler(files, progress=gr.Progress()):
        if not files:
            return None, format_file_list(), format_documents_summary()
            
        added, skipped = doc_manager.add_documents(
            files, 
            progress_callback=lambda p, desc: progress(p, desc=desc)
        )
        
        gr.Info(f"✅ Added: {added} | Skipped: {skipped}")
        return None, format_file_list(), format_documents_summary()

    def refresh_handler():
        return format_documents_summary(), format_file_list()
    
    def clear_handler():
        try:
            doc_manager.clear_all()
            gr.Info("🗑️ Removed all documents")
        except Exception as exc:
            gr.Error(f"Unable to clear documents: {exc}")
        return format_file_list(), format_documents_summary()
    
    def chat_handler(msg, hist):
        for chunk in chat_interface.chat(msg, hist):
            yield chunk
    
    def clear_chat_handler():
        chat_interface.clear_session()
    
    with gr.Blocks(title="Agentic RAG") as demo:

        with gr.Tab("Documents", elem_id="doc-management-tab"):
            gr.HTML("""
                <div class="library-heading">
                    <div class="library-heading-copy">
                        <div class="section-kicker">DOCUMENT LIBRARY</div>
                        <h2 class="library-title">Manage your knowledge base</h2>
                        <p class="library-subtitle">Add source documents and keep your assistant's knowledge up to date.</p>
                    </div>
                    <div class="library-ready"><span class="status-dot"></span>Ready</div>
                </div>
            """)

            with gr.Group(elem_id="upload-card"):
                gr.Markdown("<div class='upload-card-title'>Add documents</div>")
                gr.HTML("<p class='upload-card-copy'>PDF and Markdown files · Existing files are skipped</p>")
                files_input = gr.File(
                    label="Drop PDF or Markdown files here",
                    file_count="multiple",
                    type="filepath",
                    height=126,
                    show_label=False,
                    elem_id="documents-upload"
                )

                add_btn = gr.Button("Add documents", variant="primary", size="lg")

            with gr.Row(equal_height=True, elem_id="documents-toolbar"):
                documents_summary = gr.HTML(value=format_documents_summary(), elem_id="documents-summary")
                gr.HTML("<button type='button' class='header-action'>⌕&nbsp;&nbsp; Search documents</button>", elem_id="documents-search", scale=0)
                refresh_btn = gr.Button("↻ Refresh", size="sm", scale=0, elem_id="documents-refresh")

            file_list = gr.HTML(value=format_file_list(), elem_id="file-list-box")

            with gr.Row(equal_height=True, elem_id="document-list-actions"):
                clear_btn = gr.Button("Clear all", variant="stop", size="sm", scale=0)

            gr.HTML("<div id='library-note'>Small UI refresh concept · Existing dark theme retained</div>")

            add_btn.click(upload_handler, [files_input], [files_input, file_list, documents_summary], show_progress="corner")
            refresh_btn.click(refresh_handler, None, [documents_summary, file_list])
            clear_btn.click(clear_handler, None, [file_list, documents_summary])
        
        with gr.Tab("Chat", elem_id="chat-tab"):
            with gr.Group(elem_id="chat-card"):
                gr.HTML("""
                    <div class="chat-heading">
                        <div>
                            <h2>Chat with your knowledge base</h2>
                            <p>Ask a question about your uploaded documents</p>
                        </div>
                        <div class="chat-ready"><span class="status-dot"></span>Knowledge ready</div>
                    </div>
                """,
                    elem_id="chat-heading-block",
                    apply_default_css=False,
                    css_template="background: transparent !important; border: 0 !important; padding: 0 !important; box-shadow: none !important;",
                )

                chatbot = gr.Chatbot(
                    value=[{"role": "assistant", "content": "Hello! Ask me a question about your knowledge base."}],
                    height=570,
                    placeholder="",
                    show_label=False,
                    elem_id="chatbot-panel",
                    avatar_images=(None, os.path.join(ASSETS_DIR, "chatbot_avatar.png")),
                    layout="bubble",
                    buttons=["copy"],
                )
                chatbot.clear(clear_chat_handler)

                with gr.Row(elem_id="chat-input-row"):
                    textbox = gr.Textbox(
                        placeholder="Ask a question about your documents...",
                        lines=2,
                        max_lines=5,
                        show_label=False,
                        elem_id="chat-message-input",
                    )
                    submit_btn = gr.Button("Send", variant="primary", min_width=120, elem_id="chat-submit-button")

                def chat_handler(msg, hist):
                    if not msg or not str(msg).strip():
                        return hist, ""

                    history = list(hist or [])
                    history.append({"role": "user", "content": str(msg).strip()})

                    try:
                        response_messages = []
                        for chunk in chat_interface.chat(msg, hist):
                            if isinstance(chunk, str):
                                response_messages = [{"role": "assistant", "content": chunk}]
                            elif isinstance(chunk, list):
                                response_messages = chunk
                            else:
                                response_messages = [{"role": "assistant", "content": str(chunk)}]

                        if response_messages:
                            history.extend(response_messages)
                        else:
                            history.append({"role": "assistant", "content": "⚠️ No response received."})
                    except Exception as exc:
                        history.append({"role": "assistant", "content": f"❌ Error: {exc}"})

                    return history, ""

                textbox.submit(chat_handler, [textbox, chatbot], [chatbot, textbox])
                submit_btn.click(chat_handler, [textbox, chatbot], [chatbot, textbox])
                gr.HTML("<div class='chat-footnote'>Answers are based on your uploaded documents</div>")
    
    return demo
