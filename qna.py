from gemini_client import generate_with_gemini


def answer_question_with_gemini(question: str) -> str:
    """
    Answers student questions using Google Gemini.
    """

    if not question or not question.strip():
        return "⚠️ Please enter a question."

    prompt = f"""
You are EduGenie, a helpful AI tutor for college students.

Answer the student's question clearly and accurately.

Student Question:
{question.strip()}

Instructions:
- Explain the answer in simple language.
- Give enough detail for a college student to understand.
- Use examples when useful.
- Use bullet points or headings when appropriate.
- Do not make up facts.
"""

    try:
        answer = generate_with_gemini(prompt)

        if not answer:
            return "⚠️ Gemini returned an empty answer."

        return answer

    except Exception as e:
        return f"⚠️ Error in QnA: {str(e)}"