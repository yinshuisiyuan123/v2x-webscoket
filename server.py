import asyncio
import websockets
import json
IP_ADDR = "127.0.0.1"
IP_PORT = "8887"

# 接收从客户端发来的消息并处理，再返给客户端ok
async def serverRecv(websocket):
    while True:
        send_message = " "
        # recv_text = await websocket.recv()
        if websocket.path == "ws://localhost:8887/websocket/v2x/getDangerEvent/":
            with open('resources/getDangerEvent_example.json',encoding='utf8') as fp:
                send_message = json.dumps(json.load(fp))
        elif websocket.path == "ws://localhost:8887/websocket/v2x/getJamEvent/":
            with open(r'resources/getJamEvent_example.json',encoding='utf8') as fp:
                send_message = json.dumps(json.load(fp))
        elif websocket == "ws://localhost:8887/websocket/v2x/getSpeedLimitEvent/":
            with open(r'resources/getSpeedLimitEvent_example.json',encoding='utf8') as fp:
                send_message = json.dumps(json.load(fp))
        await websocket.send(send_message)


# 握手并且接收数据
async def serverRun(websocket, path):
    print(path)

    await serverRecv(websocket)

# main function
if __name__ == '__main__':
    print("======server main begin======")
    server = websockets.serve(serverRun, IP_ADDR, IP_PORT)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()