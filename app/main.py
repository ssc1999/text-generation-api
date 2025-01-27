from fastapi import FastAPI, HTTPException
from app.schemas import GenerateRequest, GenerateResponse, HistoryResponse, HistoryItem
from app.database import init_db, save_request, fetch_history
from app.models import load_generator

app = FastAPI(title="Text Generation API")

generator = load_generator()

init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Text Generation API!"}


@app.post("/generate", response_model=GenerateResponse)
def generate_text(request: GenerateRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    
    # Generate text
    result = generator(
        request.prompt,
        max_length=request.max_length,
        temperature=request.temperature,
        top_p=request.top_p,
    )
    generated_text = result[0]["generated_text"]

    # Save to history
    save_request(request.prompt, generated_text)

    return GenerateResponse(generated_text=generated_text)


@app.get("/history", response_model=HistoryResponse)
def get_history():
    history_data = fetch_history()
    history = [
        HistoryItem(id=item[0], prompt=item[1], generated_text=item[2])
        for item in history_data
    ]
    return HistoryResponse(history=history)