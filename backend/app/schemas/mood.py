from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class Mood(str, Enum):
    happy = "Happy"
    calm = "Calm"
    neutral = "Neutral"
    stressed = "Stressed"
    sad = "Sad"
    anxious = "Anxious"
    lonely = "Lonely"
    overwhelmed = "Overwhelmed"


class MoodCreate(BaseModel):
    mood: Mood
    journal: str | None = Field(default=None, max_length=2000)


class MoodRead(BaseModel):
    id: int
    mood: Mood
    journal: str | None
    created_at: datetime

    model_config = {"from_attributes": True}


class MoodSummary(BaseModel):
    total: int
    distribution: dict[str, int]
    recent: list[MoodRead]
