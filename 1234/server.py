import asyncio
import websockets
import json
IP_ADDR = "127.0.0.1"
IP_PORT = "8888"

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}
dataStr = json.dumps(data)


# 握手，通过接收hello，发送"123"来进行双方的握手。
async def serverHands(websocket):
    while True:
        recv_text = await websocket.recv()
        print("recv_text=" + recv_text)
        if recv_text == "hello":
            print("connected success")
            await websocket.send("123")
            return True
        else:
            await websocket.send("connected fail")


# 接收从客户端发来的消息并处理，再返给客户端ok
async def serverRecv(websocket):
    while True:
        send_message = " "
        recv_text = await websocket.recv()
        if recv_text == "/websocket/v2x/getDangerEvent/":
            with open(r'C:\Users\administrator1\Desktop\blibli-ws-master\resources\getDangerEvent_example.json',encoding='utf8') as fp:
                dataStr1 = json.dumps(json.load(fp))
                send_message = dataStr1
        elif recv_text == "/websocket/v2x/getJamEvent/":
            with open(r'C:\Users\administrator1\Desktop\blibli-ws-master\resources\getJamEvent_example.json',encoding='utf8') as fp:
                dataStr2 = json.dumps(json.load(fp))
                send_message = dataStr2
        elif recv_text == "/websocket/v2x/getSpeedLimitEvent/":
            with open(r'C:\Users\administrator1\Desktop\blibli-ws-master\resources\getSpeedLimitEvent_example.json',encoding='utf8') as fp:
                dataStr3 = json.dumps(json.load(fp))
                send_message = dataStr3
        await websocket.send(send_message)


# 握手并且接收数据
async def serverRun(websocket, path):
    print(path)
    await serverHands(websocket)

    await serverRecv(websocket)


# main function
if __name__ == '__main__':
    print("======server main begin======")
    server = websockets.serve(serverRun, IP_ADDR, IP_PORT)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()