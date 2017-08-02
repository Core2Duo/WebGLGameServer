import asyncio
import websockets
import json
import argparse
clients = set()
lock = asyncio.Lock()
message_id = 1

async def handler(websocket, path):
    global message_id

    # This is atomic
    clients.add(websocket)

    try:
        while True:
            message = await websocket.recv()
            try:
                message = json.loads(message)
            except json.JSONDecodeError:
                continue

            username = message.get('username', '')
            text = message.get('text', '')

            if isinstance(username, str) and isinstance(text, str) and username.strip() and text.strip():
                message = {
                    'username': username.strip(),
                    'id': message_id,
                    'text': text.strip(),
                }

                # Increment is not atomic
                async with lock:
                    message_id += 1

                for client in clients:
                    await client.send(json.dumps(message))

    except websockets.ConnectionClosed:
        # This is atomic
        clients.remove(websocket)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Provide host and port for the server")
    parser.add_argument('host')
    parser.add_argument('port')
    args = parser.parse_args()

    start_server = websockets.serve(handler, args.host, args.port)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
