# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wkxi_BNYNxnokFAPKJ-fD75ekAom0yr5
"""

import hashlib
import time
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + previous_hash + str(timestamp) + data
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

def is_chain_valid(blockchain):
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]
        if current_block.hash != calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
            return False
        if current_block.previous_hash != previous_block.hash:
            return False
    return True
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
num_of_blocks_to_add = 10

for i in range(num_of_blocks_to_add):
    new_block_data = f"Block {i + 1} Data"
    new_block = create_new_block(previous_block, new_block_data)
    blockchain.append(new_block)
    previous_block = new_block
    print(f"Block #{new_block.index} has been added to the blockchain!")
    print(f"Hash: {new_block.hash}\n")
is_valid = is_chain_valid(blockchain)
print(f"Is the blockchain valid? {is_valid}")