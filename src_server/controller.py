from gamemaker_handler import GMS2Client
from queue import Queue
from handle_map import MapHandler


class JazzhandsController():
    running: bool                                      # A flag to determine if the program has ended. Facilitates safe termination of threads.
    gamemaker_client: GMS2Client 
    gamemaker_queue: Queue                             # An instance of the client queue. Facilitates sending gesture data to the client object.
    map_handler: MapHandler

    

    def __init__(self) -> None:
        """
        Main function which initiates the client and gesture recognition.
        """
        
        self.create_client()

        # Boolean flag to continuously run the controller until a stopping condition is met.
        self.running = True
        
    def create_client(self) -> None:
        """
        Creates a thread which initialises the client.
        """

        self.gamemaker_client = GMS2Client()
        self.gamemaker_queue: Queue = self.gamemaker_client.client_queue
        self.gamemaker_client.start_thread()


    def mainloop(self) -> None:
        """
        Program Main Loop. Retrieves gesture detections and sends them to GameMaker server.
        """
        while self.running:
            self.update_client()
            # print(message)

            message = ""

            self.try_transmit_to_client(message)
        print("stopped running")

    def update_client(self) -> None:
        """
        Attempt to update the client. Handle keyboard interrupt exceptions.
        """
        pass
    
    def terminate_program(self) -> None:
        """
        Safely end all threads and terminate the main process.
        """
        print("CTRL+C has been pressed. Ending threads.")
        self.gamemaker_client.stop_thread()
        self.running = False
        exit(0)

    def try_transmit_to_client(self, message) -> bool:
        """
        Attempt to send the most recent gesture from gesture_queue to the GMS2 server.
        """

        self.gamemaker_client.send_response(message)



if __name__ == "__main__":
    c = JazzhandsController()
    c.mainloop()