import asyncio
import websockets
from config.config import SERVER_ADDRESS, SERVER_PORT
from utils.logger import setup_logger
from server.handlers import handle_client
logger = setup_logger(__name__)

async def main():
    server = await websockets.serve(handle_client, SERVER_ADDRESS, SERVER_PORT)
    logger.info(f"WebSocket server running on {SERVER_ADDRESS}:{SERVER_PORT}...")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
