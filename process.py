import asyncio
import config
import random
import time

class Process:

    def __init__(self):
        random.seed()

        self.a_writer = None
        self.b_writer = None
        self.queue = []

        self.host = config.SERVER_HOST

        # determine instruction cycles per second
        self.instruction_time = random.randint(1, 10)
        print("instruction time = ", self.instruction_time)

        self.main()

    async def send_message_to_a(self):
        message = "Hello World From " + self.process_name

        if self.a_writer == None:
            _, self.a_writer = await asyncio.open_connection(
            '127.0.0.1', self.port_a)

        print(f'Send: {message!r}')
        self.a_writer.write(message.encode())
        await self.a_writer.drain()

    async def send_message_to_b(self):
        message = "Hello World From " + self.process_name

        if self.b_writer == None:
            _, self.b_writer = await asyncio.open_connection(
            '127.0.0.1', self.port_b)

        print(f'Send: {message!r}')
        self.b_writer.write(message.encode())
        await self.b_writer.drain()

    async def listen(self, reader, writer):
        print("listen")
        request = None
        while request != 'quit':
            request = (await reader.read(255)).decode('utf8')
            print("request! = ", request)
            self.queue.append(request)

    async def run_server(self):
        print("run_server on port: ", self.my_port)
        server = await asyncio.start_server(self.listen, 'localhost', self.my_port)
        async with server:
            await server.serve_forever()

    async def start_threads(self):
        print("start threads!")

        # run the background task
        _= asyncio.create_task(self.run_server())

        # create a coroutine for the main execution loop
        main_loop = asyncio.to_thread(self.main_loop)

        # execute the loop in a new thread and await the result
        await main_loop

    def main_loop(self):
        print("main_loop!")
        while True:
            print("this is the main loop where queue = ", self.queue)
            time.sleep(self.instruction_time)

        # TODO: read 1 message
        # TODO: roll dice to maybe send a message

    def main(self):
        print("main function")
        asyncio.run(self.start_threads())
