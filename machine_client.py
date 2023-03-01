import random
import socket
import threading
import time
import config


class MachineClient:
    def __init__(self):
        random.seed()
        self.instruction_time = random.randint(1, 10)
        print("instruction time = ", self.instruction_time)
        self.my_port = config.PROCESS_2_PORT
        self.port_a = config.PROCESS_1_PORT
        self.port_b = config.PROCESS_3_PORT

        
        

        self.user_thread = threading.Thread(target=self.client_main)
        self.user_thread.start()

        self.clientsocket = self.create_client_socket()
        self.open_thread()

    def open_thread(self):
        self.receiving_thread = threading.Thread(target=self.threaded_listen_to_server)
        self.receiving_thread.start()

    def create_client_socket(self):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('localhost', self.port_a))
        return clientsocket
    
    def threaded_listen_to_server(self):
        while True: 
            message, originalMessage = self.listen_to_server_one_time()
            print('\n')
            print(message)
            print("Press enter to continue...")
            
    def listen_to_server_one_time(self):
        bdata, addr = self.clientsocket.recvfrom(1024)
        # parse the response and print the result
        # response = wire_protocol.unmarshal_response(bdata)
        # response_code = response['response_code']
        # message = response['message']
        # user_action = response['response_type']
        # printResponse = self.parse_response(user_action, response_code, message)
        # return printResponse, response

        return bdata, addr
    
    def client_main(self):
        while True:
            print("this is the main loop")
            time.sleep(self.instruction_time)

MachineClient()