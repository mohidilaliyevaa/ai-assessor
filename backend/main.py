from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import ErrorItem, EvaluateRequest, EvaluateResponse, Scores

app = FastAPI(title="AI-Assessor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/writing/evaluate", response_model=EvaluateResponse)
def evaluate_writing(request: EvaluateRequest):
    # Hozircha soxta (hardcoded) javob. Keyin bu yerga haqiqiy AI ulanadi.
    return EvaluateResponse(
        estimated_level="B1",
        scores=Scores(grammar=5, vocabulary=6, task_achievement=7, coherence=6),
        errors=[
            ErrorItem(
                original="I go to school yesterday.",
                type="grammar",
                correction="I went to school yesterday.",
                explanation_uz="'Yesterday' o'tgan vaqtni bildiradi, shuning uchun fe'lning Past Simple shakli (went) ishlatiladi.",
            ),
            ErrorItem(
                original="childrens",
                type="grammar",
                correction="children",
                explanation_uz="'children' o'zi ko'plik shakli, unga -s qo'shilmaydi.",
            ),
        ],
        style_tips_uz=["Har bir fikrga bitta aniq misol qo'shing."],
        advice_uz="Fe'l zamonlarini va ko'plik shakllarini takrorlang.",
    )