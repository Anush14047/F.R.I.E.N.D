from dataclasses import dataclass


@dataclass(frozen=True)
class SafetyResult:
    high_risk: bool
    matched_signal: str | None = None


CRISIS_SIGNALS = (
    "kill myself",
    "end my life",
    "suicide",
    "self harm",
    "hurt myself",
    "don't want to live",
    "do not want to live",
)


def screen(text: str) -> SafetyResult:
    normalized = " ".join(text.lower().split())
    for signal in CRISIS_SIGNALS:
        if signal in normalized:
            return SafetyResult(True, signal)
    return SafetyResult(False)
