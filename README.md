# Document Question Answering System

Live Demo: [https://llm-document-question-answering.vercel.app/](https://llm-document-question-answering.vercel.app/)

A Python-based web application that allows users to upload documents (PDF, TXT, MD) and query them using Large Language Models.

## Features

* **File Support:** Parse and extract text from `.pdf`, `.txt`, and `.md` files.
* **Modern Interface:** Responsive, dark-themed frontend built with standard HTML/CSS.
* **Language Model Integration:** Uses the Google Gemini API (`gemini-2.5-flash`) for fast and accurate context processing.
* **Hallucination Prevention:** Strict prompt engineering ensures the model only answers questions if the answer exists within the provided document context.

## Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Gangadhara2829/llm-document-question-answering.git
   cd llm-document-question-answering
   ```

2. **Install dependencies:**
   Make sure you have Python 3.x installed.
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API key:**
   Get an API key from Google AI Studio and set it in your environment:
   
   *Windows:*
   ```powershell
   $env:GEMINI_API_KEY="your_api_key_here"
   ```
   *Mac/Linux:*
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```
   Access the server at `http://127.0.0.1:5000`

## Implementation Details

The application uses a retrieval and context-injection approach rather than model fine-tuning. When a document is uploaded, the backend extracts its raw text and appends the user's query. This payload is wrapped in strict system instructions ensuring the AI relies exclusively on the provided context before returning a response to the frontend.
