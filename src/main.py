from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from src.agent import assistant_agent
from langchain.messages import HumanMessage
from src.util.stream_gen import AsyncGen
import asyncio

app = FastAPI(description="Agents")


@app.get("/")
async def health():
    return "hello"


@app.post("/chat/stream")
async def chat_stream(payload: dict):
    prompt = payload.get("prompt", "")
    print("prompt: ", prompt)
    agent = assistant_agent()
    stream = agent.astream(input={"messages": [HumanMessage(prompt)]}, stream_mode="messages")

    stream_gen = AsyncGen(stream)

    return StreamingResponse(
        stream_gen.run(),
        media_type="text/plain"
    )
