import traceback

from gemini_client import generate_with_gemini


def get_learning_recommendations(topic: str) -> str:
    """
    Generates a personalized learning roadmap for a given topic.
    """

    if not topic or not topic.strip():
        return "Please enter a topic you want to learn."

    topic = topic.strip()

    prompt = f"""
You are EduGenie, an AI educational tutor.

The student wants to learn about:

{topic}

Create a clear and personalized learning roadmap.

Structure the response as:

1. Beginner Level
   - Basic concepts
   - Important topics
   - What the student should understand first

2. Intermediate Level
   - Next concepts
   - Practical topics
   - Skills to develop

3. Advanced Level
   - Advanced concepts
   - Projects or practical applications
   - Further topics to explore

4. Suggested Resources
   - Books
   - Videos
   - Tutorials
   - Practice resources

Keep the explanation simple and suitable for a college student.

Do not invent specific URLs.
"""

    try:
        return generate_with_gemini(prompt)

    except Exception as e:
        traceback.print_exc()
        return f"❌ Error in Learning Path: {str(e)}"