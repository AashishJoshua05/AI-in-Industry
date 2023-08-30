import asyncio
import websockets

async def handle_client(websocket, path):
    async for message in websocket:
        print(f"Received message from client: {message}")
        
        if message == "exit":
            response = "Server is exiting. Goodbye!"
            await websocket.send(response)
            print("Server is exiting.")
            await websocket.close()
            break
        else:
            response = f"Server received: {message}"
            await websocket.send(response)
            print(f"Sent response to client: {response}")

start_server = websockets.serve(handle_client, "localhost", 8765)

print("Server is running. Press Ctrl+C to exit.")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
