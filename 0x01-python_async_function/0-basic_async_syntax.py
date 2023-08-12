#!/usr/bin/env python3
'''
A asynchronous coroutines that takes an int for sleep time and returns as float
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' The function select a random number and use as sleep time'''
    i = float(random.random() * max_delay)
    await asyncio.sleep(i)
    return i
