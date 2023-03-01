
import asyncio
import config
import time
from process import Process

class Machine_2(Process):
    def __init__(self):
        self.my_port = config.PROCESS_2_PORT
        self.port_a = config.PROCESS_1_PORT
        self.port_b = config.PROCESS_3_PORT

        self.process_name = "Machine 2"

        super().__init__()

machine_2 = Machine_2()