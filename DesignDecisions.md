## Communication

We decided to use the asyncio Python package to handle the socket-level communication between machines. This makes it easy to have a listening thread to receive incoming messages and an execution thread to handle our logic. We use asyncio's connection to also send messages to other machines.

### Knowledge of Others

We needed a way for each machine to know about the other machines and were to find them. We decided to hard-code that information into the config.py file. Specifically, each machine picks a port and knows about the other machine's ports, so that it can look for them when trying to make a connection.

### Starting the machines

Because we use sockets to connect each of the machines to each other we have to make sure all three are up and running before they try to connect. To accomplish this, we put each machine to sleep for 2 seconds before their processes begin.

### Issues

1. Initially, our machine 1 was not recieving any messages even though it was being sent them. This was a little surprissing because all three machines run the same code. To solve this we changed the port of machine 1 from 6125 to 6126. It brings up the question of if 6125 is a special port? Based on this website it seems like port 6125 has some special applications https://www.speedguide.net/port.php?port=6125.

### Observations

Generally, it appears that the machine with the lowest internal process time dictates the Logical clocks for all other machines and rarely has to update its own clock more than 1 step.

1. If one machine has an internal process time of 1 and another machine has an instruction time of .17 or .33 than the slow machine will never have an oppertunity to send a message. This because his queue gets clogged up and he can only remove one message every second.

2. If there are machines that are closser in internal process time (eg. .17 and .33). The machine with a process time of .17 will have to deal with messages from .33 although its queue will rarely be clogged.

3. If all three machines have a similar internal process time than none of their queues will be clogged. Machines with say (.5, .5, .33) are able to maintain this desirable state.

4. It seems that if there is one machine with an instruction time of .5 and another with .17 than the .5 machine will have a clogged queue, but will be capable of de-clogging itself if it is lucky!

5. As the expirment progresses, machines that have a much slower instruciton time and thus have a clogged queue suffer from significant drift from when a message was sent from one machine to when it was logged in the slow machine. This is because it has to process all the messages it had before that one.

6. It is noted that as the frequency of internal event decreases the average length of the queue on slow machines becomes exponentially larger. This is due to the fact that the faster machines are sending messages to slow machines more frequenlty, while the slower machines are still processing a new message at the same rate as always.

Column Names:

- Instruction Time: How many operations per second
- Average Logical Clock Jump: Average logical clock adjustment at each tick
- Average Queue Length: Average length of Queue at each tick
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

### We now look at results limiting machines to between 1 and 3 operations per second

Run 1:

| Machine   | Instruction Time | Average Logical Clock Jump | Average Queue Length |
| --------- | ---------------- | -------------------------- | -------------------- |
| Machine 1 | 1/s              | 3.08 s                     | 1.23                 |
| Machine 2 | 3/s              | 1.02 s                     | 0.11                 |
| Machine 3 | 2/s              | 1.51 s                     | 0.29                 |

Run 2:

| Machine   | Instruction Time | Average Logical Clock Jump | Average Queue Length |
| --------- | ---------------- | -------------------------- | -------------------- |
| Machine 1 | 3/s              | 1.0 s                      | 0.08                 |
| Machine 2 | 2/s              | 1.53 s                     | 0.34                 |
| Machine 3 | 1/s              | 3.07 s                     | 1.65                 |

Run 3:

| Machine   | Instruction Time | Average Logical Clock Jump | Average Queue Length |
| --------- | ---------------- | -------------------------- | -------------------- |
| Machine 1 | 1/s              | 3.13 s                     | 1.83                 |
| Machine 2 | 3/s              | 1.08 s                     | 0.17                 |
| Machine 3 | 3/s              | 1.12 s                     | 0.21                 |

### We now look at results with the propability of an internal event at 50% rather than 70%

Run 1:

| Machine   | Instruction Time | Average Logical Clock Jump | Average Queue Length |
| --------- | ---------------- | -------------------------- | -------------------- |
| Machine 1 | 4/s              | 1.32 s                     | 0.38                 |
| Machine 2 | 2/s              | 2.65 s                     | 12.78                |
| Machine 3 | 5/s              | 1.09 s                     | 0.29                 |

Run 2:

| Machine   | Instruction Time | Average Logical Clock Jump | Average Queue Length |
| --------- | ---------------- | -------------------------- | -------------------- |
| Machine 1 | 2/s              | 2.02 s                     | 7.3                  |
| Machine 2 | 4/s              | 2.65 s                     | 0.15                 |
| Machine 3 | 3/s              | 1.39 s                     | 0.56                 |

Run 3:

| Machine   | Instruction Time | Average Logical Clock Jump | Average Queue Length |
| --------- | ---------------- | -------------------------- | -------------------- |
| Machine 1 | 3/s              | 1.7 s                      | 1.49                 |
| Machine 2 | 5/s              | 1.06 s                     | 0.23                 |
| Machine 3 | 4/s              | 1.35 s                     | 0.49                 |

### We now look at results with the propability of an internal event at 0%

Run 1:

| Machine   | Instruction Time | Average Logical Clock Jump | Average Queue Length |
| --------- | ---------------- | -------------------------- | -------------------- |
| Machine 1 | 6/s              | 1.10 s                     | 0.36                 |
| Machine 2 | 3/s              | 2.14 s                     | 44.69                |
| Machine 3 | 6/s              | 1.14 s                     | 0.88                 |

Run 2:

| Machine   | Instruction Time | Average Logical Clock Jump | Average Queue Length |
| --------- | ---------------- | -------------------------- | -------------------- |
| Machine 1 | 1/s              | 5.6 s                      | 63.85                |
| Machine 2 | 3/s              | 1.9 s                      | 21.51                |
| Machine 3 | 6/s              | 1.01 s                     | 0.03                 |

Run 3:

| Machine   | Instruction Time | Average Logical Clock Jump | Average Queue Length |
| --------- | ---------------- | -------------------------- | -------------------- |
| Machine 1 | 3/s              | 1.09 s                     | 0.36                 |
| Machine 2 | 1/s              | 3.3 s                      | 39.32                |
| Machine 3 | 3/s              | 1.12 s                     | 0.53                 |
