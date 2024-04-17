import asyncio
import websockets
import logging
import os
import configparser

# Load configuration from environment variables or configuration file
config = configparser.ConfigParser()
config.read('config.ini')

SERVER_ADDRESS = os.getenv("SERVER_ADDRESS", config.get('Server', 'address', fallback="localhost"))
SERVER_PORT = int(os.getenv("SERVER_PORT", config.get('Server', 'port', fallback=8765)))
LOG_LEVEL = os.getenv("LOG_LEVEL", config.get('Logging', 'level', fallback="INFO"))

# Configure logging
logging.basicConfig(level=LOG_LEVEL)

# Define a dictionary to store connected clients and their identifiers
connected_clients = {}

async def handle_client(websocket, path):
    try:
        # When a client connects, add it to the dictionary
        connected_clients[websocket] = None
        logging.info(f'New client connected. Total online: {len(connected_clients)}')

        # Wait for messages from the client and broadcast them to all other clients
        async for message in websocket:
            logging.info(f'Received message from client: {message}')
            await asyncio.gather(*[client.send(message) for client in connected_clients if client != websocket])
    except websockets.exceptions.ConnectionClosedError:
        pass
    finally:
        # When a client disconnects, remove it from the dictionary
        del connected_clients[websocket]
        logging.info(f'Client disconnected. Total online: {len(connected_clients)}')

async def main():
    server = await websockets.serve(handle_client, SERVER_ADDRESS, SERVER_PORT)
    logging.info(f"WebSocket server running on {SERVER_ADDRESS}:{SERVER_PORT}...")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
