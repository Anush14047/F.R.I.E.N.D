from dataclasses import dataclass


@dataclass(frozen=True)
class EmotionResult:
    label: str
    confidence: float


KEYWORDS = {
    "stressed": {"stress", "deadline", "pressure", "busy", "tired"},
    "anxious": {"anxious", "worry", "worried", "panic", "nervous", "uncertain"},
    "sad": {"sad", "down", "cry", "heartbroken", "hopeless"},
    "lonely": {"lonely", "alone", "isolated", "nobody"},
    "happy": {"happy", "great", "excited", "joy", "good"},
    "calm": {"calm", "peaceful", "relaxed", "okay", "fine"},
}


def analyze(text: str) -> EmotionResult:
    words = set(text.lower().replace("'", "").split())
    scores = {label: len(words & keywords) for label, keywords in KEYWORDS.items()}
    label, score = max(scores.items(), key=lambda item: item[1])
    if score == 0:
        return EmotionResult("neutral", 0.5)
    return EmotionResult(label, min(0.65 + score * 0.1, 0.95))
