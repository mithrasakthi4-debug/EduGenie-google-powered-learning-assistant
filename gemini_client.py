import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv(override=True)

MODEL = "gemini-3.5-flash-lite"


def generate_with_gemini(prompt: str, json_mode: bool = False) -> str:

    load_dotenv(override=True)

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Check your .env file."
        )

    client = genai.Client(api_key=api_key.strip())

    config = None

    if json_mode:
        config = {
            "response_mime_type": "application/json"
        }

    # Retry temporary Gemini errors
    for attempt in range(4):

        try:

            print(
                f"Gemini request: {MODEL} "
                f"(attempt {attempt + 1}/4)"
            )

            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config=config
            )

            if response and response.text:
                print("Gemini response received.")
                return response.text.strip()

            raise RuntimeError(
                "Gemini returned an empty response."
            )

        except Exception as error:

            error_text = str(error)

            print("Gemini error:")
            print(error_text)

            # Temporary server error
            if "503" in error_text or "UNAVAILABLE" in error_text:

                if attempt < 3:

                    wait = 2 ** attempt

                    print(
                        f"Gemini temporarily unavailable. "
                        f"Retrying in {wait} seconds..."
                    )

                    time.sleep(wait)
                    continue

                raise RuntimeError(
                    "Gemini is temporarily unavailable. "
                    "Please try again after a few minutes."
                )

            # Other errors
            raise RuntimeError(
                f"Gemini API error: {error_text}"
            ) from error

    raise RuntimeError("Gemini request failed.")