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

machine_1 = Machine_1()