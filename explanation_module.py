# explanation_module.py

# Optional local model
_explain_tokenizer = None
_explain_model = None
_local_model_attempted = False


def _get_local_model():
    """
    Attempts to lazy-load the LaMini-Flan-T5 model.

    If transformers/torch are unavailable or the model cannot be loaded,
    returns (None, None) and Gemini will be used instead.
    """

    global _explain_tokenizer
    global _explain_model
    global _local_model_attempted

    # Already loaded
    if _explain_model is not None and _explain_tokenizer is not None:
        return _explain_tokenizer, _explain_model

    # Already attempted and failed
    if _local_model_attempted:
        return None, None

    _local_model_attempted = True

    try:
        from transformers import (
            AutoTokenizer,
            AutoModelForSeq2SeqLM
        )

        import torch

        model_name = "MBZUAI/LaMini-Flan-T5-783M"

        _explain_tokenizer = AutoTokenizer.from_pretrained(
            model_name
        )

        _explain_model = AutoModelForSeq2SeqLM.from_pretrained(
            model_name
        )

        return _explain_tokenizer, _explain_model

    except Exception as e:

        print(
            "Notice: Local model was not loaded. "
            f"Reason: {e}. Using Gemini instead."
        )

        return None, None


def explain_topic(topic: str) -> str:
    """
    Explains an educational concept in simple language.

    First attempts to use the optional local LaMini-Flan-T5 model.
    If unavailable or inference fails, uses Gemini through the
    centralized gemini_client.py.
    """

    if not topic or not topic.strip():
        return "⚠️ Please enter a topic to explain."

    topic = topic.strip()

    input_text = f"""
Explain the concept of "{topic}" in a simple and clear way
for a college student.

Instructions:
- Start with a simple definition.
- Explain the important points.
- Give a simple example when useful.
- Use bullet points where appropriate.
- Avoid unnecessarily complicated language.
"""

    # ---------------------------------------------------------
    # 1. Try local LaMini-Flan-T5 model
    # ---------------------------------------------------------

    tokenizer, model = _get_local_model()

    if tokenizer is not None and model is not None:

        try:

            inputs = tokenizer(
                input_text,
                return_tensors="pt"
            )

            outputs = model.generate(
                **inputs,
                max_new_tokens=150,
                temperature=0.7,
                top_k=50,
                top_p=0.95,
                do_sample=True,
            )

            explanation = tokenizer.decode(
                outputs[0],
                skip_special_tokens=True
            )

            if explanation:
                return explanation.strip()

        except Exception as local_error:

            print(
                "Local model inference failed. "
                f"Using Gemini instead: {local_error}"
            )

    # ---------------------------------------------------------
    # 2. Gemini fallback
    # ---------------------------------------------------------

    try:

        from gemini_client import generate_with_gemini

        return generate_with_gemini(input_text)

    except Exception as e:

        return f"⚠️ Error in Explanation: {str(e)}"