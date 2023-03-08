## Communication

We decided to use the asyncio Python package to handle the socket-level communication between machines. This makes it easy to have a listening thread to receive incoming messages and an execution thread to handle our logic. We use asyncio's connection to also send messages to other machines.

### Knowledge of Others

We needed a way for each machine to know about the other machines and were to find them. We decided to hard-code that information into the config.py file. Specifically, each machine picks a port and knows about the other machine's ports, so that it can look for them when trying to make a connection.

### Starting the machines

Because we use sockets to connect each of the machines to each other we have to make sure all three are up and running before they try to connect. To accomplish this, we put each machine to sleep for 2 seconds before their processes begin.

### Issues

1. Initially, our machine 1 was not recieving any messages even though it was being sent them. To solve this we...
