# -*- coding: utf-8 -*-

from time import time

from utils.printable import Printable


class Block(Printable):
    """ The Block of the Blockchain.

    Attributes:
        :index: The index of the block.
        :previous_hash: The hash of previous block.
        :transactions: The transactions of the block.
        :proof: The proof of the block.
        :timestamp: timestamp...
    """

    def __init__(self, index, previous_hash, transactions, proof, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time() if timestamp is None else timestamp
        self.transactions = transactions
        self.proof = proof
