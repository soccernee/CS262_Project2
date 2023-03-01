import asyncio
import config
import time
from process import Process

class Machine_1(Process):
    def __init__(self):
        self.my_port = config.PROCESS_1_PORT
        self.port_a = config.PROCESS_2_PORT
        self.port_b = config.PROCESS_3_PORT

        self.process_name = "Machine 1"

        super().__init__()

    def main_loop(self):
        while True:
            print("this is the main loop where queue = ", self.queue)
            time.sleep(self.instruction_time)

            print("sending message to machine_2")
            asyncio.run(self.send_message_to_a())

machine_1 = Machine_1()