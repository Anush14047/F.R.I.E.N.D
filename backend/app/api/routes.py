from collections import Counter

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models import MoodEntry
from app.schemas import MoodCreate, MoodRead, MoodSummary
from app.services.chat import generate_reply

router = APIRouter(prefix="/api")


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    history: list[dict[str, str]] = Field(default_factory=list, max_length=20)


class ChatResponse(BaseModel):
    reply: str
    emotion: str
    safety_escalation: bool


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "mode": "local-demo"}


@router.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    reply, emotion, safety = generate_reply(payload.message, payload.history)
    return ChatResponse(reply=reply, emotion=emotion, safety_escalation=safety.high_risk)


@router.post("/moods", response_model=MoodRead, status_code=status.HTTP_201_CREATED)
def create_mood(payload: MoodCreate, db: Session = Depends(get_db)) -> MoodEntry:
    entry = MoodEntry(mood=payload.mood.value, journal=payload.journal)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


@router.get("/moods", response_model=list[MoodRead])
def list_moods(db: Session = Depends(get_db)) -> list[MoodEntry]:
    return list(db.scalars(select(MoodEntry).order_by(desc(MoodEntry.created_at))).all())


@router.get("/moods/summary", response_model=MoodSummary)
def mood_summary(db: Session = Depends(get_db)) -> MoodSummary:
    entries = list(db.scalars(select(MoodEntry).order_by(desc(MoodEntry.created_at))).all())
    return MoodSummary(
        total=len(entries),
        distribution=dict(Counter(entry.mood for entry in entries)),
        recent=entries[:5],
    )


@router.delete("/moods/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_mood(entry_id: int, db: Session = Depends(get_db)) -> None:
    entry = db.get(MoodEntry, entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail="Mood entry not found")
    db.delete(entry)
    db.commit()
