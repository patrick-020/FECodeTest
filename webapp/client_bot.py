from websockets.sync.client import connect
import random, time


def hello():
    """
    This is a chatbot that sends "Hello World!" appends with a counter every second
    """
    try:
        counter: int = 1
        with connect("ws://localhost:8000/ws/bot" + str(random.randint(0, 100))) as websocket:
            while True:
                websocket.send(f"Hello world! {counter}")
                message = websocket.recv()
                print(f"{message}", flush=True)
                time.sleep(1)
                counter += 1
    except KeyboardInterrupt:
        print(f"\nChatbot has left the chat, Ciao.")


if __name__ == '__main__':
    hello()

