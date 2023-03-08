#Write pytests

import asyncio
import config
import time
from machine_1 import Machine_1
from machine_2 import Machine_2
from machine_3 import Machine_3
from process import Process


def main():
    machine_1 = asyncio.create_task(Machine_1())
    machine_2 = asyncio.create_task(Machine_2())
    machine_3 = asyncio.create_task(Machine_3())
    


