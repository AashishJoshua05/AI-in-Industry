import asyncio
import websockets

async def send_message():
    async with websockets.connect("ws://localhost:8765") as websocket:
        print("Connected to server.")
        while True:
            message = input("Enter a message to send to server (type 'exit' to quit): ")
            await websocket.send(message)

            if message == "exit":
                print("Exiting client.")
                break
            
            response = await websocket.recv()
            print(f"Received response from server: {response}")

print("Client is running. Press Ctrl+C to exit.")
asyncio.get_event_loop().run_until_complete(send_message())
