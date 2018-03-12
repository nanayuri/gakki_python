from hashlib import sha256
from random import random
from time import time


class Block():
    def __init__(self):
        self.index = 0  # 区块的索引
        self.id = str(random())  # 区块的id
        self.nonce = None  # 区块链验证码
        self.timestamp = [time()]  # 时间戳
        self.owner = []  # 所有者列表
        self.transaction = []  # 交易记录
        self.valid = []  # 交易记录验证列表
        self.pre_hash = None  # 上一次交易的hash值

    def mine(self, belong):  # 挖矿，这是获取区块有效性的最重要的手段，区块链货币的价值高低完全取决于挖矿的难易程度
        code = 0
        while True:
            hashed = sha256((self.id + str(code)).encode()).hexdigest()
            if str(hashed).startswith("00000"):  # 校验设置，若要增加挖矿难度，可增加“00000”的长度
                self.valid.append(str(code))
                self.owner.append(belong)
                print("Block generated: id %s, validated code: %s, owner: %s" % (self.id, str(code), belong))
                return str(code)
            code += 1

    def give(self, receiver):  # 交易
        self.index += 1
        self.pre_hash = self.valid[-1]
        self.transaction.append({"sender": self.owner[-1], "receiver": receiver})
        self.owner.append(receiver)
        self.valid.append(sha256((self.pre_hash + str(receiver)).encode()).hexdigest())
        self.timestamp.append(time())

    def self_verify(self):  # 自校验
        if self.index != len(self.transaction):  # 序列号校验
            return False
        for i in range(1, len(self.timestamp)):  # 时间戳校验
            if self.timestamp[i - 1] >= self.timestamp[i]:
                return False
        if not sha256((str(self.id) + self.valid[0]).encode()).hexdigest().startswith("00000"):  # 初始有效性校验
            return False
        for i in range(1, len(self.valid)):  # 交易记录有效性校验
            if sha256((str(self.valid[i - 1]) + str(self.owner[i])).encode()).hexdigest() != self.valid[i]:
                return False
        return True