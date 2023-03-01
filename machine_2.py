
import config
from process import Process

class Machine_2(Process):
    def __init__(self):
        self.my_port = config.PROCESS_2_PORT
        self.port_a = config.PROCESS_1_PORT
        self.port_b = config.PROCESS_3_PORT

        super().__init__(config.PROCESS_2)

    def send_initial_broadcast(self):
        # TODO: send broadcast to connect with machine 1
        pass

machine_2 = Machine_2()