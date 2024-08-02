
import select, sys, threading, time
from websockets.sync.client import connect
from websockets.exceptions import ConnectionClosedOK
from threading import Event

"""
How to use:
This is a client programming runs on terminal side. It can also communicate with the web browser side of users. Below 
are a few steps to run this program.
1. Run "python client_terminal.py" in its folder location on terminal;
2. Enter your user name;
3. If the user name has been used, the connection will fail;
4. After connects to server, messages from other users will be be displayed on terminal;
5. If user wants to sent a message, user will need to hit "Enter" key once, then type in the message, then hit "Enter"
    again to send out the message;
6. When user is typing in message, terminal will stop display other uses' messages until current user sends out message.

Design & implementation:
I used 2 threads here to handling display and input messages. The thread for displaying message, namely thread4display,
will be constantly running until it get blocked by user input event. The input event is listened by another thread, 
namely "thread4input". These 2 threads are communicating through threading.Event() object.
"""

connection_error: Event = Event()


def display_to_console(pause_event, websocket):
    """
    This function is used for print message received to terminal console
    """
    try:
        while True:
            if pause_event.is_set():
                message = websocket.recv()
                print(f"{message}", flush=True)
            else:
                pause_event.wait()
    except ConnectionClosedOK as e:
        connection_error.set()
        print(f"Connection error: {e.reason}")
        sys.exit(0)


def has_input():
    """
    This method is for checking if there aws any input event triggered.
    """
    input_ready, _, _ = select.select([sys.stdin], [], [], 0)
    return input_ready


def listen_for_enter(pause_event, websocket):
    """
    This method is for sending message when user hits the "Enter" key. The thread that listens keyboard events(
    "thread4input" will execute, and the thread for displaying("thread4display") will be blocked, until user finishes
    input.
    """
    while True:
        if has_input():
            # Reads the first char, to capture if user hits the "Enter" key
            ch = sys.stdin.read(1)
            if ch == '\n':
                # If there is connection error sent from server side, client program will quit.
                if connection_error.is_set():
                    print(f"Bye.")
                    sys.exit(0)
                else:
                    # If the connection fine, then set the pause_event internal flag as False, so the thread for
                    # displaying("thread4display") will be blocked, until use finishes input.
                    pause_event.clear()
                    input_value = input("Please type in your messages: ")
                    print(f"Input value is: {input_value}\n", flush=True)
                    websocket.send(input_value)
                    # Reset pause_event internal flag as True, so  the thread for displaying("thread4display") will
                    # be able to execute.
                    pause_event.set()
                    continue
        else:
            time.sleep(0.1)  # 避免 CPU 占用过高


def main():
    client_name = input("Enter your client name: ")
    # print(f"hi {client_name}")

    with connect("ws://localhost:8000/ws/" + client_name) as websocket:
        pause_event = Event()
        pause_event.set()
        # Create and start the thread("thread4display") for displaying messages received to terminal.
        output_thread = threading.Thread(target=display_to_console, args=(pause_event, websocket), daemon=True)
        output_thread.start()

        # Create and start the thread("thread4input") for listening the client keyboard input event
        listener_thread = threading.Thread(target=listen_for_enter, args=(pause_event, websocket), daemon=True)
        listener_thread.start()

        try:
            output_thread.join()
            listener_thread.join()
        except KeyboardInterrupt:
            print(f"\nCiao.")


if __name__ == "__main__":
    main()
