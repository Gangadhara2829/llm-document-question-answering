import sys
from flask import Flask, render_template, request, jsonify
from PyPDF2 import PdfReader

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Please install google-genai using: pip install google-genai")
    sys.exit(1)

app = Flask(__name__)

# Initialize GenAI Client
# It will automatically pick up GEMINI_API_KEY from environment
try:
    client = genai.Client()
except Exception as e:
    print("\n[Error] Gemini API Key is missing or invalid!")
    print("Ensure you set $env:GEMINI_API_KEY before running this script.")
    sys.exit(1)

def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def answer_question(context_text, question):
    system_prompt = (
        "You are a helpful answering assistant. "
        "Answer the user's question based STRICTLY on the provided text context below. "
        "If the answer cannot be found in the context, clearly state: 'I cannot find the answer in the provided text.' "
        "Do not hallucinate or make up information."
    )
    user_prompt = f"Context text:\n{context_text}\n\nQuestion:\n{question}"
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.0,
                max_output_tokens=500
            )
        )
        return response.text
    except Exception as e:
        return f"A Gemini Error occurred: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get('question', '').strip()
    context_text = request.form.get('context_text', '').strip()
    
    # Handle file upload if present
    uploaded_file = request.files.get('file')
    if uploaded_file and uploaded_file.filename != '':
        # It's a file!
        if uploaded_file.filename.lower().endswith('.pdf'):
            extracted = extract_text_from_pdf(uploaded_file)
            context_text += "\n" + extracted
        else:
            # Assume text file (txt, md, csv)
            file_content = uploaded_file.read().decode('utf-8', errors='ignore')
            context_text += "\n" + file_content
            
    if not context_text.strip():
        return jsonify({"error": "Please provide some context text or upload a document."})
        
    if not question:
        return jsonify({"error": "Please enter a question."})
        
    # Get the AI Answer!
    answer = answer_question(context_text, question)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    print("\n" + "="*50)
    print("Starting Premium Web App QA System...")
    print("http://127.0.0.1:5000/")
    print("="*50 + "\n")
    app.run(debug=True, port=5000)
