custom_css = """
    .progress-text {
        display: none !important;
    }

    .gradio-container {
        max-width: 1180px !important;
        width: 100% !important;
        margin: 0 auto !important;
        padding: 0 !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background: #0b1220 !important;
        color: #f4f7fb !important;
    }

    .block {
        background: transparent !important;
    }

    .tabs {
        border-bottom: 1px solid rgba(148, 163, 184, 0.18) !important;
        margin: 0 auto !important;
        max-width: 1040px !important;
        padding-top: 18px !important;
    }

    button[role="tab"] {
        color: rgba(226, 232, 240, 0.8) !important;
        background: transparent !important;
        border: 0 !important;
        border-radius: 10px !important;
        padding: 10px 16px !important;
        font-size: 0.8rem !important;
        letter-spacing: 0.02em !important;
        text-transform: none !important;
        transition: all 0.2s ease !important;
    }

    button[role="tab"][aria-selected="true"] {
        color: #f8fafc !important;
        background: rgba(148, 163, 184, 0.16) !important;
        border-radius: 8px !important;
    }

    button[role="tab"]:hover {
        color: #f8fafc !important;
    }

    #doc-management-tab {
        max-width: 1000px !important;
        margin: 0 auto !important;
        padding: 10px 18px 30px !important;
        box-sizing: border-box !important;
    }

    .library-heading {
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        gap: 16px !important;
        margin-bottom: -2px !important;
    }

    .library-heading-copy {
        min-width: 0 !important;
    }

    .section-kicker {
        font-size: 0.62rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.13em !important;
        color: rgba(148, 163, 184, 0.8) !important;
        text-transform: uppercase !important;
        margin: 0 0 8px !important;
    }

    .library-title {
        font-size: 1.55rem !important;
        line-height: 1.05 !important;
        margin: 0 0 5px !important;
        color: #f8fafc !important;
        font-weight: 700 !important;
    }

    .library-subtitle {
        margin: 0 !important;
        color: rgba(148, 163, 184, 0.8) !important;
        font-size: 0.72rem !important;
        line-height: 1.3 !important;
    }

    .library-ready {
        display: inline-flex !important;
        align-items: center !important;
        gap: 7px !important;
        flex-shrink: 0 !important;
        padding: 7px 11px !important;
        border: 1px solid rgba(52, 211, 153, 0.14) !important;
        border-radius: 999px !important;
        background: rgba(34, 197, 94, 0.1) !important;
        color: #a7f3d0 !important;
        font-size: 0.66rem !important;
        font-weight: 600 !important;
    }

    .library-ready .status-dot {
        width: 6px !important;
        height: 6px !important;
    }

    #upload-card {
        margin-bottom: 12px !important;
    }

    #doc-management-tab #upload-card.gr-group {
        padding: 0 !important;
        border: 0 !important;
        border-radius: 0 !important;
        background: transparent !important;
        margin-bottom: 0 !important;
    }

    #upload-card > div,
    #upload-card .file-upload,
    #upload-card .file-preview {
        padding: 0 !important;
        border: 0 !important;
        border-radius: 0 !important;
        background: transparent !important;
    }

    #upload-card > div,
    #upload-card .form,
    #upload-card .block,
    #upload-card .gradio-group,
    #upload-card .wrap {
        background-color: transparent !important;
    }

    .upload-card-title {
        margin: 0 0 4px !important;
        color: #f1f5f9 !important;
        font-size: 0.84rem !important;
        font-weight: 650 !important;
    }

    .upload-card-copy {
        margin: 0 0 12px !important;
        color: rgba(148, 163, 184, 0.85) !important;
        font-size: 0.65rem !important;
        line-height: 1.4 !important;
    }

    #upload-card .prose {
        max-width: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    #upload-card .html-container {
        padding: 0 !important;
    }

    #documents-upload {
        margin-bottom: 12px !important;
        height: auto !important;
        min-height: 0 !important;
    }

    /* Gradio 6 renders the file drop target as a button without
       aria-dropeffect, so style it by the stable component id instead. */
    #documents-upload,
    #documents-upload > div {
        background: transparent !important;
        border: 0 !important;
    }

    #documents-upload button,
    button#documents-upload {
        position: relative !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        overflow: hidden !important;
        min-height: 0 !important;
        max-height: none !important;
        height: auto !important;
        aspect-ratio: 2.5 / 1 !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
        border: 2px dashed #e5e7eb !important;
        border-radius: 9px !important;
        background: #1a1a1a !important;
        color: #f8fafc !important;
        transition: all 0.2s ease !important;
    }

    #documents-upload button:hover,
    button#documents-upload:hover {
        border-color: rgba(248, 250, 252, 0.9) !important;
        background: #1a1a1a !important;
    }

    #documents-upload button > .wrap,
    button#documents-upload > .wrap {
        position: absolute !important;
        inset: 0 !important;
        width: 100% !important;
        height: 100% !important;
        box-sizing: border-box !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 16px !important;
        padding: 12px !important;
        font-size: 0 !important;
        line-height: 0 !important;
        pointer-events: none !important;
    }

    #documents-upload button > .wrap > :not(.icon-wrap),
    button#documents-upload > .wrap > :not(.icon-wrap) {
        display: none !important;
    }

    #documents-upload button .icon-wrap,
    button#documents-upload .icon-wrap {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        order: -1 !important;
        width: 38px !important;
        height: 38px !important;
        border-radius: 0 !important;
        background: transparent !important;
        color: #f8fafc !important;
    }

    #documents-upload button .icon-wrap svg,
    button#documents-upload .icon-wrap svg {
        width: 36px !important;
        height: 36px !important;
    }

    #documents-upload button > .wrap::after,
    button#documents-upload > .wrap::after {
        order: 1 !important;
        content: "Drop File Here\A – or –\A Click to Upload";
        color: #f8fafc !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        line-height: 1.45 !important;
        text-align: center !important;
        white-space: pre-line !important;
    }

    .gr-button {
        border-radius: 10px !important;
        border: none !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
        box-shadow: none !important;
    }

    .gr-button.primary {
        background: linear-gradient(180deg, #4f8ef7 0%, #3b82f6 100%) !important;
        color: #f8fafc !important;
        min-height: 42px !important;
        font-size: 0.94rem !important;
    }

    .gr-button.primary:hover {
        filter: brightness(1.05) !important;
    }

    #upload-card button.primary {
        min-height: 34px !important;
        font-size: 0.68rem !important;
        background: linear-gradient(180deg, #4f8ef7 0%, #3b82f6 100%) !important;
        color: #f8fafc !important;
        border: 0 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        box-shadow: none !important;
        transition: filter 0.2s ease !important;
    }

    #upload-card button.primary:hover {
        filter: brightness(1.05) !important;
    }

    .gr-button:not(.primary):not(.stop) {
        background: rgba(148, 163, 184, 0.08) !important;
        border: 1px solid rgba(148, 163, 184, 0.2) !important;
        color: #e2e8f0 !important;
    }

    .gr-button:not(.primary):not(.stop):hover {
        background: rgba(148, 163, 184, 0.14) !important;
    }

    .gr-button.stop {
        background: rgba(127, 29, 29, 0.2) !important;
        border: 1px solid rgba(248, 113, 113, 0.28) !important;
        color: #fecaca !important;
    }

    .gr-button.stop:hover {
        background: rgba(127, 29, 29, 0.32) !important;
    }

    #documents-toolbar {
        display: flex !important;
        align-items: flex-end !important;
        justify-content: space-between !important;
        gap: 8px !important;
        margin: 0 !important;
    }

    #documents-toolbar > #documents-summary {
        flex: 1 1 auto !important;
        width: auto !important;
        min-width: 0 !important;
    }

    #documents-toolbar > #documents-search,
    #documents-toolbar > #documents-refresh {
        flex: 0 0 auto !important;
        width: auto !important;
        min-width: 0 !important;
    }

    #documents-summary .prose,
    #documents-search .prose {
        max-width: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    #documents-toolbar .html-container {
        padding: 0 !important;
    }

    .header-action {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        min-height: 31px !important;
        padding: 6px 10px !important;
        border-radius: 8px !important;
        border: 1px solid rgba(148, 163, 184, 0.18) !important;
        background: rgba(15, 23, 42, 0.45) !important;
        color: #cbd5e1 !important;
        font-size: 0.66rem !important;
        cursor: pointer !important;
        white-space: nowrap !important;
    }

    .header-action:hover {
        background: rgba(148, 163, 184, 0.12) !important;
        color: #f1f5f9 !important;
    }

    #file-list-box {
        width: 100% !important;
        background: rgba(15, 23, 42, 0.78) !important;
        border: 1px solid rgba(148, 163, 184, 0.16) !important;
        border-radius: 14px !important;
        padding: 0 !important;
        overflow: hidden !important;
        margin-bottom: 0 !important;
    }

    #file-list-box .html-container,
    #file-list-box .prose {
        max-width: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    .document-list {
        display: flex !important;
        flex-direction: column !important;
        background: transparent !important;
        width: 100% !important;
    }

    .document-row {
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        gap: 12px !important;
        width: 100% !important;
        padding: 11px 14px !important;
        border-bottom: 1px solid rgba(148, 163, 184, 0.12) !important;
        background: transparent !important;
        min-height: 64px !important;
    }

    .document-row:last-child {
        border-bottom: none !important;
    }

    .document-main {
        display: flex !important;
        align-items: center !important;
        gap: 14px !important;
        min-width: 0 !important;
        flex: 1 !important;
    }

    .document-icon {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 36px !important;
        height: 36px !important;
        border-radius: 10px !important;
        background: rgba(96, 165, 250, 0.08) !important;
        color: #bfdbfe !important;
        flex-shrink: 0 !important;
    }

    .document-icon svg {
        width: 20px !important;
        height: 20px !important;
    }

    .document-meta {
        min-width: 0 !important;
    }

    .document-name {
        color: #f8fafc !important;
        font-size: 0.72rem !important;
        font-weight: 600 !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }

    .document-subtext {
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
        margin-top: 3px !important;
        color: rgba(148, 163, 184, 0.8) !important;
        font-size: 0.61rem !important;
    }

    .document-separator {
        opacity: 0.7 !important;
    }

    .document-status {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 8px !important;
        padding: 6px 10px !important;
        border-radius: 999px !important;
        background: rgba(34, 197, 94, 0.14) !important;
        color: #a7f3d0 !important;
        font-size: 0.62rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.01em !important;
        white-space: nowrap !important;
    }

    .status-dot {
        display: inline-block !important;
        width: 7px !important;
        height: 7px !important;
        border-radius: 999px !important;
        background: #34d399 !important;
    }

    .document-menu {
        appearance: none !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 32px !important;
        height: 32px !important;
        border-radius: 8px !important;
        border: 1px solid rgba(148, 163, 184, 0.12) !important;
        background: rgba(15, 23, 42, 0.4) !important;
        color: #cbd5e1 !important;
        font-size: 1.5rem !important;
        line-height: 1 !important;
        cursor: pointer !important;
        flex-shrink: 0 !important;
    }

    .document-list--empty {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        min-height: 64px !important;
        padding: 8px 12px !important;
    }

    .document-empty {
        color: rgba(148, 163, 184, 0.75) !important;
        padding: 8px 12px !important;
        text-align: center !important;
    }

    #document-list-actions {
        justify-content: flex-end !important;
        gap: 8px !important;
        margin-top: 5px !important;
    }

    #document-list-actions button.stop {
        min-height: 30px !important;
        width: auto !important;
        min-width: 112px !important;
        padding: 5px 14px !important;
        font-size: 0.66rem !important;
        border: 1px solid rgba(248, 113, 113, 0.28) !important;
        border-radius: 8px !important;
        background: rgba(127, 29, 29, 0.2) !important;
        color: #fecaca !important;
    }

    #document-list-actions button.stop:hover {
        background: rgba(127, 29, 29, 0.32) !important;
    }

    #library-note {
        margin-top: 64px !important;
        color: rgba(100, 116, 139, 0.85) !important;
        font-size: 0.58rem !important;
        line-height: 1.4 !important;
    }

    #documents-refresh {
        min-height: 31px !important;
        width: auto !important;
        min-width: 82px !important;
        padding: 5px 11px !important;
        font-size: 0.66rem !important;
        border: 1px solid rgba(148, 163, 184, 0.18) !important;
        border-radius: 8px !important;
        background: rgba(148, 163, 184, 0.08) !important;
        color: #cbd5e1 !important;
    }

    #documents-search .header-action {
        width: auto !important;
        min-width: 0 !important;
    }

    #documents-summary {
        min-width: 0 !important;
        flex: 1 1 auto !important;
    }

    .documents-summary h3 {
        margin: 0 !important;
        color: #f8fafc !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        line-height: 1.05 !important;
    }

    .documents-summary p {
        margin: 3px 0 0 !important;
        color: rgba(148, 163, 184, 0.8) !important;
        font-size: 0.61rem !important;
        line-height: 1.3 !important;
    }

    .gr-form {
        gap: 12px !important;
    }

    .gr-button-row {
        justify-content: flex-end !important;
    }

    textarea, input {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid rgba(148, 163, 184, 0.18) !important;
        border-radius: 10px !important;
        color: #f8fafc !important;
    }

    textarea:focus, input:focus {
        border-color: rgba(96, 165, 250, 0.9) !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.12) !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #f8fafc !important;
    }

    * {
        box-shadow: none !important;
    }

    footer {
        visibility: hidden;
    }

    @media (max-width: 640px) {
        #doc-management-tab {
            padding: 20px 14px 22px !important;
        }

        .library-heading {
            align-items: flex-start !important;
            gap: 10px !important;
        }

        .library-title {
            font-size: 1.4rem !important;
        }

        .library-ready {
            padding: 6px 8px !important;
        }

        #upload-card {
            padding: 14px !important;
        }

        #documents-upload button,
        button#documents-upload {
            min-height: 0 !important;
            height: auto !important;
        }

        #documents-upload button > .wrap::after,
        button#documents-upload > .wrap::after {
            font-size: 1.1rem !important;
        }

        #library-note {
            margin-top: 64px !important;
        }

        #documents-toolbar {
            flex-wrap: wrap !important;
            align-items: flex-end !important;
        }

        #documents-summary {
            flex-basis: 100% !important;
        }

        .document-row {
            gap: 8px !important;
            padding: 11px 10px !important;
        }

        .document-main {
            gap: 10px !important;
        }

        .document-status {
            padding: 5px 7px !important;
        }
    }

    /* Dark knowledge-base chat, matching the approved chatbox concept. */
    #chat-tab {
        max-width: 1000px !important;
        margin: 0 auto !important;
        padding: 20px 18px 32px !important;
        box-sizing: border-box !important;
    }

    #chat-card {
        width: 100% !important;
        padding: 24px 30px 16px !important;
        box-sizing: border-box !important;
        border: 1px solid #263140 !important;
        border-radius: 20px !important;
        background: #111923 !important;
    }

    #chat-card > .wrap,
    #chat-card .form,
    #chat-card .block,
    #chat-card .html-container,
    #chat-card .prose {
        background: transparent !important;
    }

    #chat-card .html-container,
    #chat-card .prose {
        max-width: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    #chat-heading-block,
    #chat-heading-block > div,
    #chat-heading-block .html-container,
    #chat-heading-block .prose {
        max-width: none !important;
        margin: 0 !important;
        padding: 0 !important;
        border: 0 !important;
        border-radius: 0 !important;
        outline: 0 !important;
        background: transparent !important;
        box-shadow: none !important;
    }

    .chat-heading {
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        gap: 16px !important;
        padding: 0 4px 18px !important;
        border-bottom: 1px solid #252e3b !important;
    }

    .chat-heading h2 {
        margin: 0 0 7px !important;
        color: #f1f4fa !important;
        font-size: 1.35rem !important;
        line-height: 1.2 !important;
        font-weight: 700 !important;
    }

    .chat-heading p {
        margin: 0 !important;
        color: #8e9aad !important;
        font-size: 0.83rem !important;
    }

    .chat-ready {
        display: inline-flex !important;
        align-items: center !important;
        gap: 8px !important;
        flex-shrink: 0 !important;
        padding: 8px 12px !important;
        border: 1px solid #214536 !important;
        border-radius: 999px !important;
        background: #14251f !important;
        color: #8ee0b6 !important;
        font-size: 0.72rem !important;
        font-weight: 600 !important;
    }

    #chatbot-panel,
    #chatbot-panel > div,
    #chatbot-panel > div > div,
    #chatbot-panel .wrap,
    #chatbot-panel [class*="bubble-wrap"],
    #chatbot-panel [class*="panel-wrap"],
    #chatbot-panel [class*="message-wrap"] {
        background: #111923 !important;
        border: 0 !important;
        outline: 0 !important;
        color: #d7deea !important;
        box-shadow: none !important;
    }

    #chatbot-panel {
        margin: 0 !important;
        padding: 8px 0 2px !important;
    }

    #chatbot-panel .bubble-wrap {
        padding-top: 16px !important;
    }

    #chatbot-panel .bot-row .bot,
    #chatbot-panel .message-row .bot {
        max-width: 82% !important;
        padding: 8px 0 !important;
        border: 0 !important;
        border-radius: 0 !important;
        background: transparent !important;
        color: #d7deea !important;
        box-shadow: none !important;
    }

    #chatbot-panel .user-row .user,
    #chatbot-panel .message-row .user {
        max-width: 82% !important;
        padding: 14px 18px !important;
        border: 1px solid #294875 !important;
        border-radius: 16px !important;
        background: #1b3153 !important;
        color: #edf3ff !important;
        box-shadow: none !important;
    }

    #chatbot-panel .bot .prose,
    #chatbot-panel .user .prose,
    #chatbot-panel .bot .md,
    #chatbot-panel .user .md {
        color: inherit !important;
        opacity: 1 !important;
    }

    #chatbot-panel .avatar-container {
        border-color: #2c3a50 !important;
        background: #1d2b40 !important;
    }

    #chatbot-panel .avatar-container img {
        border-radius: 50% !important;
    }

    #chatbot-panel [class*="placeholder"],
    #chatbot-panel [class*="empty"] {
        border: 0 !important;
        border-radius: 0 !important;
        background: transparent !important;
        color: #8e9aad !important;
        box-shadow: none !important;
    }

    #chatbot-panel a {
        color: #8eb2ff !important;
    }

    /* Dark rich answers: tables, code blocks, and Plotly charts. */
    #chatbot-panel .bot table,
    #chatbot-panel .bot table thead,
    #chatbot-panel .bot table tbody,
    #chatbot-panel .bot table tr,
    #chatbot-panel .bot table th,
    #chatbot-panel .bot table td,
    #chatbot-panel .bot .table-wrap {
        border-color: #303b4c !important;
        color: #d7deea !important;
    }

    #chatbot-panel .bot table {
        width: 100% !important;
        border-collapse: separate !important;
        border-spacing: 0 !important;
        overflow: hidden !important;
        border: 1px solid #303b4c !important;
        border-radius: 10px !important;
        background: #141e2b !important;
    }

    #chatbot-panel .bot table th {
        background: #1b2737 !important;
        color: #edf3ff !important;
        font-weight: 650 !important;
        text-align: left !important;
    }

    #chatbot-panel .bot table th,
    #chatbot-panel .bot table td {
        padding: 9px 12px !important;
        border-right: 1px solid #303b4c !important;
        border-bottom: 1px solid #303b4c !important;
    }

    #chatbot-panel .bot table tr:last-child td {
        border-bottom: 0 !important;
    }

    #chatbot-panel .bot table th:last-child,
    #chatbot-panel .bot table td:last-child {
        border-right: 0 !important;
    }

    #chatbot-panel .bot table tbody tr:nth-child(even) {
        background: #182332 !important;
    }

    #chatbot-panel .bot table tbody tr:nth-child(odd) {
        background: #141e2b !important;
    }

    #chatbot-panel .bot :not(pre) > code {
        padding: 0.14em 0.4em !important;
        border: 1px solid #303b4c !important;
        border-radius: 5px !important;
        background: #182332 !important;
        color: #b9d0ff !important;
    }

    #chatbot-panel .bot pre,
    #chatbot-panel .bot pre code {
        border: 1px solid #303b4c !important;
        border-radius: 10px !important;
        background: #0d141e !important;
        color: #d7deea !important;
    }

    #chatbot-panel .bot blockquote {
        margin-left: 0 !important;
        padding: 4px 0 4px 14px !important;
        border-left: 3px solid #477fe0 !important;
        color: #9eacc0 !important;
    }

    #chatbot-panel .bot .component,
    #chatbot-panel .bot .plot-container,
    #chatbot-panel .bot .js-plotly-plot,
    #chatbot-panel .bot .plotly,
    #chatbot-panel .bot .svg-container {
        max-width: 100% !important;
        border: 1px solid #303b4c !important;
        border-radius: 12px !important;
        background: #151e2a !important;
        color: #d7deea !important;
        overflow: hidden !important;
    }

    #chatbot-panel .bot .main-svg,
    #chatbot-panel .bot .main-svg .bg,
    #chatbot-panel .bot .main-svg .bglayer rect {
        background: #151e2a !important;
        fill: #151e2a !important;
        stroke: #303b4c !important;
    }

    #chatbot-panel .bot .main-svg .xgrid,
    #chatbot-panel .bot .main-svg .ygrid,
    #chatbot-panel .bot .main-svg .xline,
    #chatbot-panel .bot .main-svg .yline,
    #chatbot-panel .bot .main-svg .zerolinelayer path {
        stroke: #344154 !important;
    }

    #chatbot-panel .bot .main-svg .xtick text,
    #chatbot-panel .bot .main-svg .ytick text,
    #chatbot-panel .bot .main-svg .legend text,
    #chatbot-panel .bot .main-svg .gtitle,
    #chatbot-panel .bot .main-svg .g-xtitle,
    #chatbot-panel .bot .main-svg .g-ytitle,
    #chatbot-panel .bot .main-svg .annotation-text {
        fill: #a9b7cb !important;
    }

    #chatbot-panel .bot .modebar-container,
    #chatbot-panel .bot .modebar {
        background: transparent !important;
    }

    #chatbot-panel .bot .modebar-btn path {
        fill: #9aaac0 !important;
    }

    #chat-message-input,
    #chat-message-input > div,
    #chat-message-input .wrap,
    #chat-message-input label,
    #chat-card .input-container {
        background: #151e2a !important;
        border-color: #303b4c !important;
        box-shadow: none !important;
    }

    #chat-message-input {
        border: 1px solid #303b4c !important;
        border-radius: 16px !important;
        padding: 8px 10px !important;
    }

    #chat-message-input textarea {
        min-height: 42px !important;
        max-height: 126px !important;
        padding: 8px 10px !important;
        border: 0 !important;
        border-radius: 10px !important;
        background: transparent !important;
        color: #e5ebf5 !important;
        box-shadow: none !important;
        font-size: 0.92rem !important;
    }

    #chat-message-input textarea::placeholder {
        color: #6f7e93 !important;
        opacity: 1 !important;
    }

    #chat-card .submit-button,
    #chat-card .stop-button {
        width: 40px !important;
        height: 40px !important;
        border-radius: 12px !important;
        background: #3979f2 !important;
        color: #fff !important;
    }

    #chat-card .submit-button:hover:not(:disabled),
    #chat-card .stop-button:hover:not(:disabled) {
        background: #4b88ff !important;
    }

    .chat-footnote {
        padding: 8px 4px 0 !important;
        color: #657287 !important;
        font-size: 0.72rem !important;
    }

    @media (max-width: 640px) {
        #chat-tab {
            padding: 14px 10px 24px !important;
        }

        #chat-card {
            padding: 18px 14px 12px !important;
            border-radius: 16px !important;
        }

        .chat-heading {
            align-items: flex-start !important;
        }

        .chat-heading h2 {
            font-size: 1.12rem !important;
        }

        .chat-ready {
            padding: 6px 8px !important;
            font-size: 0.65rem !important;
        }

        #chatbot-panel .bot-row .bot,
        #chatbot-panel .message-row .bot,
        #chatbot-panel .user-row .user,
        #chatbot-panel .message-row .user {
            max-width: 92% !important;
        }
    }

    /* Gradio's prose wrapper for gr.HTML receives a light surface in some
       themes. Pin the chat heading wrappers to the same dark card surface. */
    #chat-heading-block,
    #chat-heading-block > div,
    #chat-heading-block .prose,
    #chat-heading-block .html-container,
    #chat-heading-block .chat-heading {
        background: #111923 !important;
        background-color: #111923 !important;
    }

    #chat-heading-block,
    #chat-heading-block .prose {
        overflow: hidden !important;
    }

    #chat-heading-block .chat-heading {
        border-bottom: 0 !important;
    }

    #chat-heading-block .prose {
        color: #f1f4fa !important;
    }
"""
