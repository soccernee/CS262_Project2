import asyncio
import config
import random
import socket
import time
import _thread


class Process:

    def __init__(self, process_number, port):
        random.seed()
        self.process_number = process_number
        self.port = port
        self.queue = []
        self.connections = []

        self.host = config.SERVER_HOST

        # determine instruction cycles per second
        self.instruction_time = random.randint(1, 10)
        print("instruction time = ", self.instruction_time)

        # create socket to receive incoming messages
        #self.init_listen_socket()
        #asyncio.run(self.run_server())

        # broadcast to others that the machine is online
        #self.send_initial_broadcast()

        # main execution loop
        #self.main()
        _thread.start_new_thread(self.start())

    def start(self):
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', self.port))
            print("Server up on IP: ", 'localhost', " and port: ", self.port )

            s.listen()
            print("Server listening...")
            while True:
                clientsocket, client_addr = s.accept()
                print("Client connected: ", client_addr)
                print("Client IP: ", client_addr[0], " Client Port: ", client_addr[1])
                #Start new thread for each client
                _thread.start_new_thread(self.listen_to_client, (clientsocket, client_addr))
                
    def log(self, message):
        global_time = time.time()
        print("[%d]: %d", global_time, message)

    async def handle_client(self, reader, writer):
        request = None
        while request != 'quit':
            request = (await reader.read(255)).decode('utf8')
            print("request! = ", request)
            self.queue.append(request)
            response = str(eval(request)) + '\n'
            writer.write(response.encode('utf8'))
            await writer.drain()
        writer.close()

    async def run_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', self.port))
        server.listen(8)
        server.setblocking(False)
        loop = asyncio.get_event_loop()

        while True:
            client, _ = await loop.sock_accept(server)
            print(client)


    #def init_listen_socket(self):
        

    def main(self):
        print("main loop")

        while True:
            print("this is the main loop")
            time.sleep(self.instruction_time)

        # TODO: read 1 message
        
        # TODO: roll dice to maybe send a message
