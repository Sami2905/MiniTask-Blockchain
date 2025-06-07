"""
Mining Simulation
Demonstrates proof-of-work using a nonce and difficulty.
"""

import hashlib
import time

class Block:
    def __init__(self, data):
        self.timestamp = time.time()
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        print("Mining block...")
        start = time.time()
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()
        end = time.time()
        print(f"Block mined: {self.hash}")
        print(f"Nonce: {self.nonce}, Time: {end - start:.2f} seconds")

block = Block("Some transaction data")
block.mine_block(difficulty=4)
