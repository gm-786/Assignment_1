
from agents import function_tool

@function_tool
def answer_academic_question(question: str) -> str:
    
    return f"The question '{question}' is essential for academic understanding. Please refer to trusted sources and dive deeper into the topic."

@function_tool
def get_study_tip(subject: str) -> str:
    """
    Returns a useful study tip based on the given subject.
    """
    tips = {
        "math": "Solve different types of problems regularly and review your mistakes to improve.",
        "science": "Try to relate scientific concepts to real-life examples for better understanding.",
        "history": "Use mind maps and timelines to organize key dates and events.",
        "english": "Read widely and practice writing essays to improve both vocabulary and grammar."
    }
    return tips.get(subject.lower(), "Stay consistent with your studies, revise regularly, and take effective breaks.")

@function_tool
def summarize_text_content(text: str) -> str:
    """
    Returns a brief summary of the provided text.
    Currently returns the first 200 characters.
    """
    if len(text) <= 200:
        return text
    return text[:200] + "..."
