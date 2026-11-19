from pydantic import BaseModel, Field, field_validator


class EvaluateRequest(BaseModel):
    """Foydalanuvchi yuboradigan ma'lumot."""

    task: str = Field(min_length=1)
    essay: str

    @field_validator("essay")
    @classmethod
    def essay_must_have_enough_words(cls, value: str) -> str:
        # Bo'sh joylar bo'yicha bo'lib, so'zlarni sanaymiz
        if len(value.split()) < 20:
            raise ValueError("Essay kamida 20 so'zdan iborat bo'lishi kerak")
        return value


class Scores(BaseModel):
    """Har bir ball 0 dan 10 gacha butun son."""

    grammar: int = Field(ge=0, le=10)
    vocabulary: int = Field(ge=0, le=10)
    task_achievement: int = Field(ge=0, le=10)
    coherence: int = Field(ge=0, le=10)


class ErrorItem(BaseModel):
    original: str
    type: str
    correction: str
    explanation_uz: str


class EvaluateResponse(BaseModel):
    """Server qaytaradigan javob."""

    estimated_level: str
    scores: Scores
    errors: list[ErrorItem]
    style_tips_uz: list[str]
    advice_uz: str