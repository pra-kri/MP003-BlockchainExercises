# Implementation 2 - Blockchain with Python
# https://bigishdata.com/2017/10/17/write-your-own-blockchain-part-1-creating-storing-syncing-displaying-mining-and-proving-work/

# ^ this was the website I used as a tutorial 
#========================================
import datetime as date
import os
import json
import hashlib


# define the initial class that will  handle the actual blocks

class Block(object):
    def __init__(self, dictionary):
        """
        Need: index, timestamp, data, prev_hash, nonce
        """

        for k, v in dictionary.items():
            setattr(self, k, v)
            #setattr(self, k, v) ---> leads to ---> self.k = v
            # (if the data object allows this.)
        if not hasattr(self, 'hash'):
            self.hash = self.create_self_hash()

    def __dict__(self):
        info = {}
        info['index'] = str(self.index)
        info['timestamp'] = str(self.timestamp)
        info['prev_hash'] = str(self.prev_hash)
        info['hash'] = str(self.hash)
        info['data'] = str(self.data)
        return info


    def __str__(self):
        return "Block<prev_hash: %s, hash: %s>" % (self.prev_hash, self.hash)


# now, to create the first block, just run this function:
def create_first_block():
    # index zero, and prev_hash is None

    block_data = {}
    block_data['index'] = 0
    block_data['timestamp'] = date.datetime.now()
    block_data['data'] = 'First block data'
    block_data['prev_hash'] = None
    block = Block(block_data)

    return block

create_first_block()
