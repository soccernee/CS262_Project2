
import config
from process import Process

class Machine_1(Process):
    def __init__(self):
        self.my_port = config.PROCESS_1_PORT
        self.port_a = config.PROCESS_2_PORT
        self.port_b = config.PROCESS_3_PORT

        super().__init__(config.PROCESS_1)
    

    def send_initial_broadcast(self):
        # nothing to do for machine 1
        pass

machine_1 = Machine_1()