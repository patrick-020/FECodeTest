from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import Set

app = FastAPI()
usernames: Set[str] = set()

html: str = """
                <!DOCTYPE html>
                <html>
                    <head>
                        <title>Online Chat Room</title>
                    </head>
                    <body>
                        <div class="outter">
                            <h1>Online Chat Room</h1>
                            <h2>Welcome client <span id="client-id"></span></h2>
                            <div class="container">
                                <ul id='messages'></ul>
                            </div>
                            <form action="" onsubmit="sendMessage(event)">
                                <table>
                                <tr>
                                    <td>
                                        <input type="text" id="messageInput" 
                                            placeholder="Please type in your message here...">
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                    <input type="submit" value="Submit">
                                    </td>
                                </tr>
                                </table> 
                            </form>
                            
                        </div>
                        <style>
                            h1, h2 {
                                font-family: Arial, sans-serif;
                                text-align: center;
                            }
                            
                            table, tr, td {
                                width: 100%;
                            }
                            
                            span {
                                font-family: Arial, sans-serif;
                            }
                            
                            div.container {
                                text-align: center;
                                border: 1.5px solid grey;
                                border-radius: 5px;
                                background-color: #eceff1
                            }
                            
                            div.outter {
                                border-radius: 5px;
                                background-color: #F0FFFF;
                                padding: 20px;
                            }
                            
                            input[type=text] {            
                                width: 60%;
                                padding: 12px 20px;
                                margin: 8px 0;
                                box-sizing: border-box;
                                display: inline-block;
                                border: none;
                                border-radius: 4px;
                                border-bottom: 2px solid grey;
                                background-color: white;
                                background-position: 10px 10px;
                                background-repeat: no-repeat;
                                padding-left: 40px;
                                float: right;
                            }
                                        
                            input[type=text]:focus {
                                border: none;
                            }
                            
                            input[type=submit] {
                                width: 30%;
                                background-color: #1e90ff;
                                color: white;
                                padding: 14px 20px;
                                margin: 8px 0;
                                border: none;
                                border-radius: 4px;
                                cursor: pointer;
                                float: right;
                            }
                            
                            input[type=submit]:hover {
                                background-color: #1974d2;
                            }
                                    
                            ul {
                                width: 90%;
                                font-family: Arial, sans-serif;
                                height: 300px;
                                overflow-y: auto !important;
                                border: 1px;
                                flex-direction: column-reverse;
                                display: inline-block;
                            }
                            
                            li {
                                padding-top: 10px;
                                padding-bottom: 10px;
                                padding-left: 10px;
                                text-align: left;
                                border-bottom: 1px solid #ddd;
                            }
                                        
                            li:nth-child(even) {
                                background-color: #f9f9f9;
                            }
                            
                            li:nth-child(odd) {
                                background-color: #DDDDDD;
                            }
                            
                            li:hover {
                                background-color: #f1f1f1;
                            }
                            
                        </style>
                        <script>
                            var client_id = Math.floor(Math.random() * 10000) + 1;
                            document.querySelector("#client-id").textContent = client_id;
                            var webSocket = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
                            webSocket.onmessage = function(event) {
                                var messages = document.getElementById('messages')
                                var message = document.createElement('li')
                                var messageText = document.createTextNode(event.data)
                                message.appendChild(messageText)
                                messages.appendChild(message)
                                messages.scrollTop = messages.scrollHeight;
                            };
                            function sendMessage(event) {
                                var input = document.getElementById("messageInput")
                                if (input.value != '') {
                                    webSocket.send(input.value)
                                } else {
                                    alert("Please do not send empty message.")
                                }
                                input.value = ''
                                event.preventDefault()
                            }
                        </script>
                    </body>
                </html>
            """


class ConnectionManager:
    def __init__(self):
        self.connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    if username in usernames:
        print(f"The Client {username} already existed.")
        await websocket.close(reason="Client already existed. Please use another name.")
    else:
        usernames.add(username)
        try:
            while True:
                data = await websocket.receive_text()
                await manager.broadcast(f"Client {username}: {data}")
        except WebSocketDisconnect:
            manager.disconnect(websocket)
            await manager.broadcast(f"Client {username} has left.")
