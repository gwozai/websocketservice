import asyncio
import websockets
from utils.logger import setup_logger
from config.config import SERVER_ADDRESS, SERVER_PORT

logger = setup_logger(__name__)

# Define a dictionary to store connected clients and their identifiers
connected_clients = {}
#
# async def handle_client(websocket, path):
#     try:
#         # When a client connects, add it to the dictionary
#         connected_clients[websocket] = websocket.remote_address
#         logger.info(f'New client connected: {websocket.remote_address}. Total online: {len(connected_clients)}')
#         await websocket.send(f'当前在线总人数为: {len(connected_clients)}')
#         # Wait for messages from the client and broadcast them to all other clients
#         async for message in websocket:
#             logger.info(f'Received message from client {websocket.remote_address}: {message}')
#             # Broadcast message to all clients
#             await asyncio.gather(*[client.send(f"{websocket.remote_address}: {message}") for client in connected_clients if client != websocket])
#     except websockets.exceptions.ConnectionClosedError:
#         pass
#     finally:
#         # When a client disconnects, remove it from the dictionary
#         del connected_clients[websocket]
#         logger.info(f'Client {websocket.remote_address} disconnected. Total online: {len(connected_clients)}')
async def handle_client(websocket, path):
    try:
        # When a client connects, add it to the dictionary
        connected_clients[websocket] = websocket.remote_address
        logger.info(f'New client connected: {websocket.remote_address}. Total online: {len(connected_clients)}')
        await websocket.send(f'当前在线总人数为: {len(connected_clients)}')

        # Wait for messages from the client and broadcast them to all other clients
        async for message in websocket:
            logger.info(f'Received message from client {websocket.remote_address}: {message}')
            # Broadcast message to all clients
            await broadcast(message)
    except websockets.exceptions.ConnectionClosedError:
        pass
    finally:
        # When a client disconnects, remove it from the dictionary
        del connected_clients[websocket]
        logger.info(f'Client {websocket.remote_address} disconnected. Total online: {len(connected_clients)}')
async def broadcast(message):
    if connected_clients:
        logger.info(f'Broadcasting message to {len(connected_clients)} clients...')
        await asyncio.gather(*[client.send(f'用户{client.remote_address}{message}') for client in connected_clients])
