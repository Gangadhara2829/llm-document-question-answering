# AI Document Explorer (Web App)

**🌍 Live Demo:** [https://llm-document-question-answering.vercel.app/](https://llm-document-question-answering.vercel.app/)

A premium, modern web application that allows users to upload plain text, Markdown, or PDF documents, or drop in paragraphs directly, and query the document using large language models.

## Features
- 🚀 **Drag & Drop Upload:** Seamlessly drop your `.pdf`, `.txt`, or `.md` files.
- 🎨 **Premium UI:** Cinematic glassmorphism aesthetics.
- ✨ **Document Intelligence:** Utilizes Google's incredibly fast `gemini-2.5-flash` to accurately read PDF documents and answer user questions.
- 🛡️ **Zero Hallucination:** Prompt engineering guarantees the AI explicitly replies "I cannot find the answer" if the information is unavailable in the document.

## Setup Instructions

1. **Clone or Download** this directory.
2. **Install Requirements:** Make sure you have the required python packages installed:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set API Key:** Obtain a free api key from [Google AI Studio](https://aistudio.google.com/) and set it as an environment variable in your terminal.
   
   *Windows (PowerShell):*
   ```powershell
   $env:GEMINI_API_KEY="your_api_key_here"
   ```
   *Mac/Linux (bash/zsh):*
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```

4. **Start the Web Server:**
   ```bash
   python app.py
   ```
5. **Access the Application:**
   Open your browser and navigate to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## How it Works
When a user uploads a PDF or types context, the backend extracts the raw text. Then, it uses **Prompt Injection** to combine the extracted text with the user's question and a strictly constructed system instruction. The AI is ordered to evaluate ONLY the injected text context, thereby giving highly precise information matching your uploaded document!
