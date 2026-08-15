import uuid

from fastapi import APIRouter, Query

from app.schemas import (
    ChatMessage,
    ChatResponse,
    ChatRequest,
    HistoryMessage,
    HistoryResponse,
)

chat_route = APIRouter()


@chat_route.post("/api/chat")
async def chat(chat_request: ChatRequest) -> ChatResponse:
    return ChatResponse(
        sender_id=chat_request.sender_id,
        message_id=chat_request.message_id if chat_request.message_id else str(uuid.uuid4()),
        messages=[ChatMessage(text="你好")]
    )


@chat_route.get("/api/chat/history")
async def chat_history(sender_id: str = Query(..., description="用户唯一标识")) -> HistoryResponse:
    # 业务逻辑暂未实现，先返回常量用于测试
    return HistoryResponse(
        sender_id=sender_id,
        messages=[
            HistoryMessage(role="user", text="帮我查一下订单状态"),
            HistoryMessage(role="bot", text="好的，我们先处理订单状态查询。"),
            HistoryMessage(role="bot", text="请告诉我你的订单号。"),
        ]
    )
