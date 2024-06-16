

import socket
import threading
from queue import Queue
import json

from handle_map import MapHandler
#from chatgpt import *

HOST = "127.0.0.1"
PORT = 7783


class GMS2Client():
    stop_event: threading.Event     # Event to signal the termination of the thread.
    client_queue: Queue             # Queue to transfer data from the subthread to the main thread.
    thread: threading.Thread        # Client thread to maintain client-server connection.

    def __init__(self):
        """
        Initializes stop event & client queue
        """
        # Create an event to signal the subthreads to safely stop execution.
        self.stop_event = threading.Event()
        self.conn = None
        self.next_send = ""
        self.client_queue = Queue()
        self.map_handler = MapHandler()

    def start_thread(self) -> None:
        """
        Initialise & Start the Client thread.
        """

        self.thread = self.create_thread()
        self.thread.start()

    def create_thread(self) -> threading.Thread:
        """
        Create the Client thread.
        Returns: the client thread instance.
        """

        # ',' used in thread args to convert the single argument to a tuple.
        gm_thread: threading.Thread
        gm_thread = threading.Thread(
            target=self.handle_connection_tcp, args=(self.stop_event,)
        )
        return gm_thread
    
    def stop_thread(self) -> None:
        """
        Stop the client thread using the stop_event.
        """

        self.stop_event.set()
        self.thread.join()

    def handle_connection_tcp(self, stop_event:threading.Event) -> bool:
        """
        Initialise the connection to the server.
        Handle message transmission between the client and server.

        Args:
            client_queue: A Queue shared between the client thread and controller. Stores messages to be sent from the client to the server.
            stop_event: A threading.Event instance that will be set once the thread should terminate.
        """

        # Initialise the socket and bind it to the specified host, at the specified port.
        sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.bind((HOST, PORT))
        print("listening")
        sock.listen()

        # Attempt connection to the server.
        try:
            self.conn: socket.socket
            self.conn, _ = sock.accept()
            print("connected gamemaker")

        # Handle socket timeout
        except socket.timeout:
            print("Failed to connect to GMS2 due to timeout.\nTry increasing timeout length in settings.ini")
            return False
        except Exception as e:
            raise e

        with self.conn:  
            self.mainloop(stop_event, self.conn)

    def mainloop(self, stop_event: threading.Event, conn:socket.socket) -> None:
        """
        Send messages to the GMS2 server if any are queued.
        """

        # if the pi has sent an image (pi queue not empty), process it
        while not stop_event.is_set():

            self.send_response("")

            if not self.client_queue.empty():
                pass

        return None

    def receive_data(self, conn):
        # Initialize an empty byte string to accumulate data 

        # Receive 1024 bytes of data
        data = conn.recv(16384)

        data = data.decode('latin-1')

        print(data)

        return data
        
    def send_response(self, response):
            
        if self.conn is None:
            return

        self.conn.send(json.dumps(self.next_send).encode('utf-8') + b'\n')
        reply = self.receive_data(self.conn)
        print(reply)
        if reply == "": pass
        else:

            try:
                reply = reply.split('\x00', 1)[0]
                treply = json.loads(reply)
                if(treply['type'] == "GPT"):
                    #self.next_send = "GPT" + generate_response(treply['prompt']).replace('\n', '').replace('\r', '')
                    self.next_send = ""
                if (treply['type'] == "FLOORPLAN"):
                    
                    print(treply["data"])
                    self.map_handler.parse_map(treply["data"])
                    self.next_send = "GPT You sent a floorplan!"
            except Exception as e:
                
                self.next_send = ""

