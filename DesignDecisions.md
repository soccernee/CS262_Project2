## Communication

We decided to use the asyncio Python package to handle the socket-level communication between machines. This makes it easy to have a listening thread to receive incoming messages and an execution thread to handle our logic. We use asyncio's connection to also send messages to other machines.

### Knowledge of Others

We needed a way for each machine to know about the other machines and were to find them. We decided to hard-code that information into the config.py file. Specifically, each machine picks a port and knows about the other machine's ports, so that it can look for them when trying to make a connection.

### Starting the machines

Because we use sockets to connect each of the machines to each other we have to make sure all three are up and running before they try to connect. To accomplish this, we put each machine to sleep for 2 seconds before their processes begin.

### Issues

1. Initially, our machine 1 was not recieving any messages even though it was being sent them. This was a little surprissing because all three machines run the same code. To solve this we changed the port of machine 1 from 6125 to 6126. It brings up the question of if 6125 is a special port? Based on this website it seems like port 6125 has some special applications https://www.speedguide.net/port.php?port=6125.

### Observations on Initial Regulations (1-6 ticks per second, 70% of internal event if nothing in queue)

Generally, it appears that the machine with the lowest internal process time dictates the Logical clocks for all other machines and rarely has to update its own clock more than 1 step.

1. If one machine has an internal process time of 1 and another machine has an instruction time of .17 or .33 than the slow machine will never have an oppertunity to send a message. This because his queue gets clogged up and he can only remove one message every second.

2. If there are machines that are closser in internal process time (eg. .17 and .33). The machine with a process time of .17 will have to deal with messages from .33 although its queue will rarely be clogged.

3. If all three machines have a similar internal process time than none of their queues will be clogged. Machines with say (.5, .5, .33) are able to maintain this desirable state.

4. It seems that if there is one machine with an instruction time of .5 and another with .17 than the .5 machine will have a clogged queue, but will be capable of de-clogging itself if it is lucky!

Run 1:

| Machine   | Instruction Time | Average Logical Clock Jump | Average Queue Length |
| --------- | ---------------- | -------------------------- | -------------------- |
| Machine 1 | 4/s              | 1.08 s                     | 0.16                 |
| Machine 2 | 1/s              | 4.35 s                     | 13.13                |
| Machine 3 | 4/s              | 1.12 s                     | 0.21                 |

Run 2:

| Machine   | Instruction Time | Average Logical Clock Jump | Average Queue Length |
| --------- | ---------------- | -------------------------- | -------------------- |
| Machine 1 | 5/s              | 1.07 s                     | 0.18                 |
| Machine 2 | 5/s              | 1.09 s                     | 0.19                 |
| Machine 3 | 1/s              | 5.38 s                     | 30.6                 |

Run 3:

| Machine   | Instruction Time | Average Logical Clock Jump | Average Queue Length |
| --------- | ---------------- | -------------------------- | -------------------- |
| Machine 1 | 4/s              | 1.54 s                     | 0.49                 |
| Machine 2 | 6/s              | 1.07 s                     | 0.19                 |
| Machine 3 | 6/s              | 1.09 s                     | 0.20                 |

Run 4:

| Machine   | Instruction Time | Average Logical Clock Jump | Average Queue Length |
| --------- | ---------------- | -------------------------- | -------------------- |
| Machine 1 | 4/s              | 1.08 s                     | 0.26                 |
| Machine 2 | 3/s              | 1.43 s                     | 0.36                 |
| Machine 3 | 4/s              | 1.13 s                     | 0.27                 |

Run 5:

| Machine   | Instruction Time | Average Logical Clock Jump | Average Queue Length |
| --------- | ---------------- | -------------------------- | -------------------- |
| Machine 1 | 3/s              | 1.88 s                     | 0.44                 |
| Machine 2 | 6/s              | 1.003 s                    | 0.08                 |
| Machine 3 | 2/s              | 2.875 s                    | 1.525                |
