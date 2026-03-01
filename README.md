# 🤖 Chatbot with Better UI

A modern chatbot built using **LangChain** and **MCP** to integrate tools like **Web Search** and **RAG (Retrieval-Augmented Generation)**.  
It features a **Streamlit UI** for interaction, a **FastAPI backend** for orchestration, and a robust memory + persistence layer.

---

## 🚀 Core Features

- **Tool Calling (Web Search)** – Fetches real-time information when required  
- **RAG (Retrieval-Augmented Generation)** – Grounds responses using internal knowledge  
- **Redis-based Temporary Memory** – Fast in-memory conversation context  
- **Bulk Persistence to MongoDB** – Optimized long-term storage  

---

## 🏗️ Architecture Overview

```mermaid
flowchart TD
    User[User] --> UI[Streamlit UI]
    UI --> Backend[FastAPI Backend]
    Backend --> Manager[Conversation Manager]
    Manager -->|Tool Call| WebSearch[Web Search]
    Manager -->|RAG| VectorStore[RAG Vector Store]
    Manager -->|Memory| Redis[Redis Temporary Memory]
    Manager --> LLM[LLM Response]
    LLM --> RedisAppend[Redis Append Message]
    RedisAppend -->|Every 5 min| MongoDB[MongoDB Bulk Write]
