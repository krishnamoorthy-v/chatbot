# 🤖 Chatbot with Better UI

A modern chatbot built using **LangChain** and **MCP** to integrate tools like **Web Search** and **RAG (Retrieval-Augmented Generation)**.  
It features a **Streamlit UI** for interaction, a **FastAPI backend** for orchestration, and a robust memory + persistence layer.

---

## 🚀 Core Features

- **Tool Calling (Web Search)** – Fetches real-time information when required  
- **RAG (Retrieval-Augmented Generation)** – Grounds responses using internal knowledge  
- **Redis-based Temporary Memory** – Fast in-memory conversation context  
- **Bulk Persistence to MongoDB** – Optimized long-term storage  
- **dashboard** - Model and user based token usage cost consumption shown
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
````

## Rate limiting

- An in-memory rate limiter is applied via LangChain to regulate outgoing requests. This throttling mechanism reduces the likelihood of HTTP 429 (Too Many Requests) errors by ensuring request throughput stays within the provider’s rate limits.
```mermaid
    A[Incoming Requests] --> B[Rate Limiter]
    B --> C[FIFO Queue]
    C --> D[Execute Request]
    D --> E[LLM/API Response]
    
    %% Notes
    B:::limit
    C:::queue
    D:::exec

classDef limit fill:#f9f,stroke:#333,stroke-width:1px;
classDef queue fill:#bbf,stroke:#333,stroke-width:1px;
classDef exec fill:#bfb,stroke:#333,stroke-width:1px;
    
```



