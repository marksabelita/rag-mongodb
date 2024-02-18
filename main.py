from fastapi.responses import Response, StreamingResponse
from fastapi import FastAPI
from models.questions_models import QuestionParamsModel
from utils.chatbot import ChatBot
app = FastAPI()


@app.post("/chat-stream")
def chatStream(question: QuestionParamsModel, response: Response):
    response.headers["Content-Type"] = "text/event-stream"
    chatbot = ChatBot()

    return StreamingResponse(chatbot.ask(question.question), media_type="text/event-stream")
