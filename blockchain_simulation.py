"""
Blockchain Simulation
Creates a basic blockchain with 3 blocks.
"""

import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_data.encode()).hexdigest()

    def __str__(self):
        return f"Index: {self.index}\nData: {self.data}\nHash: {self.hash}\nPrevHash: {self.previous_hash}\n"

# Genesis block
genesis_block = Block(0, "Genesis Block", "0")

# Chain with 3 blocks
block1 = Block(1, "Block 1 Data", genesis_block.hash)
block2 = Block(2, "Block 2 Data", block1.hash)

# Display blocks
for blk in [genesis_block, block1, block2]:
    print(blk)
