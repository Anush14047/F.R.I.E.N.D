from collections.abc import Sequence

from app.safety.screening import SafetyResult, screen
from app.services.emotion import analyze


CRISIS_REPLY = (
    "I’m really sorry you’re carrying this right now. You deserve immediate, human support. "
    "If you may act on these thoughts, call local emergency services now (112 in India) or go "
    "to the nearest emergency department. In India, Tele-MANAS is available at 14416. "
    "I’m an AI, not an emergency service, and I can’t keep you safe alone. Could you move near "
    "someone you trust and tell them plainly that you need support?"
)


def generate_reply(message: str, history: Sequence[dict[str, str]] = ()) -> tuple[str, str, SafetyResult]:
    safety = screen(message)
    if safety.high_risk:
        return CRISIS_REPLY, "safety-escalation", safety

    emotion = analyze(message)
    replies = {
        "stressed": "That sounds like a lot to hold. Would it help to choose one small next step, then take three slow breaths with a longer exhale?",
        "anxious": "Uncertainty can feel loud. Try noticing five things you can see, then tell me which part feels most urgent.",
        "sad": "I’m glad you put this into words. You don’t have to solve everything at once; what would feel gently supportive in the next ten minutes?",
        "lonely": "Feeling alone can be painful. Is there one safe person you could message, even with a simple “I could use company”?",
        "happy": "It’s lovely to hear some positive energy. What is one detail from this moment you’d like to remember?",
        "calm": "That calm is worth noticing. What helped you arrive there, and how might you make a little room for it later?",
        "neutral": "Thanks for checking in. There’s no right mood to have. Would you like to explore what happened today or try a short grounding exercise?",
    }
    return replies[emotion.label], emotion.label, safety
