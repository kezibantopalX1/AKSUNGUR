from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    entity_list: List[str]
    results: List[Dict[str, str]]

def analyze_sentiment(text: str) -> SentimentResponse:
    # Bu fonksiyonu gerçek bir duygu analizi ile değiştirin
    # Şu anlık örnekleme olarak basit bir işleme uyguladık
    entities = ["Entity X", "Entity Y"]
    sentiments = [
        {"entity": "Entity X", "sentiment": "olumlu"},
        {"entity": "Entity Y", "sentiment": "olumsuz"}
    ]
    return SentimentResponse(entity_list=entities, results=sentiments)

@app.post("/analyze-sentiment", response_model=SentimentResponse)
async def analyze_sentiment_endpoint(request: SentimentRequest):
    return analyze_sentiment(request.text)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=7230)