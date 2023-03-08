import asyncio
import config
import random
import time
import logging


class Process:

    def __init__(self):
        random.seed()

        # initialize some variables
        self.a_writer = None
        self.b_writer = None
        self.queue = []
        self.host = config.SERVER_HOST
        self.local_clock = 0

        # determine instruction cycles per second
        self.instruction_time = round(1.0 / random.randint(1, 6), 2)

        #Create and configure logger
        logging.basicConfig(filename="{}_log.log".format(self.process_name),
                            format='%(asctime)s %(message)s',
                            filemode='w')
        
        #Get's rid of the asyncio debug messages
        logging.getLogger('asyncio').setLevel(logging.WARNING)
        
        self.logger = logging.getLogger() 
        self.logger.setLevel(logging.DEBUG)

        self.logger.info(':: Logical Clock = {} :: instruction time = {}'.format(str(self.local_clock), self.instruction_time))
        print("instruction time = ", self.instruction_time)


        self.main()

    async def send_message_to_a(self):
        message = "Hello World From " + self.process_name + "," + str(self.local_clock)

        if self.a_writer == None:
            _, self.a_writer = await asyncio.open_connection(
            '127.0.0.1', self.port_a)

        print(f'Send: {message!r}')
        self.logger.info(':: Logical Clock = {} :: Send Message to {} -> {}'.format(str(self.local_clock), self.port_a, message.split(",")[0]))
        self.a_writer.write(message.encode())

        await self.a_writer.drain()

    async def send_message_to_b(self):
        message = "Hello World From " + self.process_name + "," + str(self.local_clock)

        if self.b_writer == None:
            _, self.b_writer = await asyncio.open_connection(
            '127.0.0.1', self.port_b)

        print(f'Send: {message!r}')
        self.logger.info(':: Logical Clock = {} :: Send Message to {} -> {}'.format(str(self.local_clock), self.port_b, message.split(",")[0]))

        self.b_writer.write(message.encode())
        await self.b_writer.drain()

    async def listen(self, reader, writer):
        request = None
        while request != 'quit' or request != '':
            request = (await reader.read(255)).decode('utf8')
            # add incoming message to our queue
            self.queue.append(request)

    async def run_server(self):
        print("server listening on port: ", self.my_port)
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
        #To give us time to startup all the servers    
        time.sleep(2)
        while True:
            time.sleep(self.instruction_time)
            print("This is the main loop where queue = ", self.queue)
            if (len(self.queue) > 0):
                # read a message
                msg = self.queue.pop()
                message, other_time = msg.split(",")
                other_time = int(other_time)
                self.local_clock = max(self.local_clock, other_time) + 1

                self.logger.info(':: Logical Clock = {} :: Queue Length = {} :: Reading Message -> {}'.format(str(self.local_clock), len(self.queue), message))
                
                print("Reading message: ", message)

            else:
                self.local_clock += 1
                #roll dice to maybe send a message
                dice_roll = random.randint(1, 10)

                if dice_roll == 1:
                    asyncio.run(self.send_message_to_a())
                elif dice_roll == 2:
                    asyncio.run(self.send_message_to_b())
                elif dice_roll == 3:
                    asyncio.run(self.send_message_to_a())
                    asyncio.run(self.send_message_to_b())
                else:
                    self.logger.info(':: Logical Clock = {}'.format(str(self.local_clock)) + ' :: No Action to Take!')
                    print("no action to take!")
                        
            
                
            

    def main(self):
        print("main function")
        asyncio.run(self.start_threads())
