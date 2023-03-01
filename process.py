import asyncio
import config
import random
import socket
import time



class Process:

    def __init__(self, process_number):
        random.seed()
        self.process_number = process_number
        self.queue = []
        self.connections = []

        self.host = config.SERVER_HOST

        # determine instruction cycles per second
        self.instruction_time = random.randint(1, 10)
        print("instruction time = ", self.instruction_time)

        # create socket to receive incoming messages
        self.init_listen_socket()

        # broadcast to others that the machine is online
        self.send_initial_broadcast()

        # main execution loop
        self.main()

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
        server = await asyncio.start_server(self.handle_client, 'localhost', self.my_port)
        async with server:
            await server.serve_forever()

    def init_listen_socket(self):
        asyncio.run(self.run_server())

    def main(self):
        print("main loop")

        while True:
            print("this is the main loop")
            time.sleep(self.instruction_time)

        # TODO: read 1 message
        
        # TODO: roll dice to maybe send a message
