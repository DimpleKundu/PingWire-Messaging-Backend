from fastapi import APIRouter, WebSocket, WebSocketDisconnect
router = APIRouter()
# Unlike regular HTTP, WebSockets keep a constant connection open between client & server — perfect for live chat.
# full-duplex protocol
# first request in http before handshake is http


# store active connections
active_connections = []

@router.websocket("/ws/chat/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # broadcast to all
            for connection in active_connections:
                await connection.send_text(f"{username}: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)