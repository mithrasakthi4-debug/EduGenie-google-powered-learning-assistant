# EduGenie: Google Gemini Powered Learning Assistant 🧠✨

EduGenie is an AI-powered educational web assistant built with **FastAPI** and a clean, responsive **HTML5/CSS3/JavaScript** interface. It assists students and learners across foundational and advanced educational needs using generative AI.

---

## 🌟 Key Features

1. **Ask EduGenie a Question (Q&A Module)**:
   - Ask any academic or general query and receive accurate, concise explanations powered by Google Gemini.
2. **Need an Explanation? (Concept Simplification Module)**:
   - Breaks down complex academic concepts into beginner-friendly explanations for school students.
   - Powered by Hugging Face `MBZUAI/LaMini-Flan-T5-783M` (with cloud Gemini fallback).
3. **Generate a Quiz (Interactive MCQ Generator)**:
   - Automatically generates 3 multiple-choice questions (4 options each) from any passage or topic.
   - Features real-time interactive answer verification with immediate visual feedback (`✅ Correct!` / `❌ Incorrect`).
4. **Summarize a Paragraph (Summarization Module)**:
   - Condenses lengthy educational articles and paragraphs into essential takeaways.
5. **Get Learning Recommendations (Adaptive Roadmap Module)**:
   - Generates tailored learning paths divided into Beginner, Intermediate, and Advanced milestones, complete with curated resources (books, videos, tutorials).

---

## 🏗️ Project Architecture

```text
Gemini-Chatbot/
├── main.py                  # FastAPI server, route controllers & static/template mounting
├── qna.py                   # Question answering logic via Gemini API
├── explanation_module.py    # Concept explanation logic (LaMini-Flan-T5 / Gemini fallback)
├── quiz_module.py           # MCQ generation & markdown JSON cleaner
├── summary_module.py        # Educational text summarization logic
├── learning_path.py         # Adaptive learning curriculum generator
├── requirements.txt         # Project dependencies
├── .env                     # Gemini API key (git-ignored)
├── .env.example             # Template for API key
├── templates/
│   └── index.html           # Interactive frontend UI with dynamic DOM grading
└── static/
    └── style.css            # Clean, modern stylesheet matching project specifications
```

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.10+** (Python 3.12 recommended)
- A **Google Gemini API Key** (obtain free from [Google AI Studio](https://aistudio.google.com/))

### 2. Installation
Clone or navigate to the project directory and install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
Create or edit your `.env` file in the project root:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

### 4. Run the Application
Start the development server using either command:
```bash
python main.py
```
*or*
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 5. Access the Web Interface
Open your browser and navigate to:
```text
http://127.0.0.1:8000
```

---

## 📡 API Endpoints

| Method | Endpoint | Description | Payload / Query |
|---|---|---|---|
| `GET` | `/` | Web interface home page | None |
| `GET` | `/qa` | Question and Answering | `?question=<string>` |
| `POST` | `/explain/` | Concept explanation | `{"topic": "<string>"}` |
| `POST` | `/summarize/` | Text summarization | `{"text": "<string>"}` |
| `POST` | `/quiz` | Multiple-choice quiz generator | `{"text": "<string>"}` |
| `GET` | `/learn/recommendations` | Adaptive learning roadmap | `?topic=<string>` |
