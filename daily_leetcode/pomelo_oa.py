#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'summarize' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING inputJSON as parameter.
#

import json
class Account:
    def __init__(self, creditLimit):
        self.availCredit = creditLimit
        self.payableBalance = 0
        self.pendingTxn = {} # {{'time': time, 'amount': amount}}
        self.settledTxn = {} # {{'starttime': time, 'finishedtime': finishedtime,'amount': amount}}
        
    def authorize_txn(self, txnId, amount, time):
        if amount > self.availCredit: return # ??? TODO: if authorization fails
        self.availCredit -= amount
        new_txn = {'time': time, 'amount': amount}
        self.pendingTxn[txnId] = new_txn
    
    def settle_txn(self, txnId, amount, time):
        auth_txn_amount = self.pendingTxn[txnId]['amount']
        auth_txn_time = self.pendingTxn[txnId]['time']
        if auth_txn_amount != amount:
            self.availCredit = self.availCredit + auth_txn_amount - amount
        self.payableBalance += amount
            
        del self.pendingTxn[txnId]
        new_txn = {'starttime': auth_txn_time, 'finishedtime': time,'amount': amount}
        self.settledTxn[txnId] = new_txn
    
    def clear_txn(self, txnId):
        if txnId not in self.pendingTxn:
            return # TODO: trying to clear a transaction that doesn't exist
        amount = self.pendingTxn[txnId]['amount']
        del self.pendingTxn[txnId]
        self.availCredit += amount
        
    def initiate_payment(self, txnId, amount, time): # amount is always negative
        self.payableBalance += amount
        new_txn = {'amount': amount, "time": time}
        self.pendingTxn[txnId] = new_txn
        
    def post_payment(self, txnId, time):
        amount = self.pendingTxn[txnId]['amount']
        self.availCredit -= amount # available credit goes up
        starttime = self.pendingTxn[txnId]['time']
        del self.pendingTxn[txnId]
        new_txn = {'starttime': starttime, 'finishedtime': time, 'amount': amount}
        self.settledTxn[txnId] = new_txn
        
    def cancel_payment(self, txnId):
        if txnId not in self.pendingTxn:
            return # TODO: trying to cancel a payment that doesn't exist
        amount = self.pendingTxn[txnId]['amount']
        del self.pendingTxn[txnId]
        self.payableBalance -= amount
        
def summarize(inputJSON):
    data = json.loads(inputJSON)
    creditLimit = data['creditLimit']
    acc = Account(creditLimit)
    events = data['events']
    
    for event in events:
        eventType = event['eventType']
        time = event['eventTime']
        txnId = event['txnId']
        
        if eventType == 'TXN_AUTHED':
            amount = event['amount']
            acc.authorize_txn(txnId, amount, time)
        elif eventType == 'TXN_SETTLED':
            amount = event['amount']
            acc.settle_txn(txnId, amount, time)
        elif eventType == 'TXN_AUTH_CLEARED':
            acc.clear_txn(txnId)
        elif eventType == 'PAYMENT_INITIATED':
            amount = event['amount']
            acc.initiate_payment(txnId, amount, time)
        elif eventType == 'PAYMENT_POSTED':
            acc.post_payment(txnId, time)
        elif eventType == 'PAYMENT_CANCELED':
            acc.cancel_payment(txnId)
        else:
            print("wrong eventType: ", eventType)
            
    print("available credit: ", acc.availCredit)
    print("payable balance: ", acc.payableBalance)
    print("pending transactions: ", acc.pendingTxn)
    print("settled transactions: ", acc.settledTxn)
    ### Available credit
    creditstr = ''
    if acc.availCredit >= 0:
        creditstr = 'Available credit: $' + str(acc.availCredit)
    else:
        creditstr = 'Available credit: -$' + str(abs(acc.availCredit))
    ### Pending transactions
    payablestr = ''
    if acc.payableBalance >= 0:
        payablestr = 'Payable balance: $' + str(acc.payableBalance)
    else:
        payablestr = 'Payable balance: -$' + str(abs(acc.payableBalance))
        
    # Pending transactions
    l_pending = list(acc.pendingTxn)
    pending = []
    for tx in l_pending:
        print(tx)
        pending.append((acc.pendingTxn[tx]['time'], tx, acc.pendingTxn[tx]['amount']))
    pending.sort(reverse=True)
    print('pending: ', pending)
    pendingstr = ''
    for tx in pending:
        txnId = tx[1]
        time = tx[0]
        amount = tx[2]
        if amount >= 0:
            pendingstr += f"{txnId}: ${amount} @ time {time}\n"
        else:
            amount = abs(amount)
            pendingstr += f"{txnId}: -${amount} @ time {time}\n"
    
    
    # settled transactions
    l_settled = list(acc.settledTxn)
    settled = []
    for tx in l_settled:
        print(tx)
        settled.append((acc.settledTxn[tx]['starttime'], acc.settledTxn[tx]['finishedtime'], tx, acc.settledTxn[tx]['amount']))
    settled.sort(reverse=True)
    settled = settled[:3]
    print('settled: ', settled)
    settledstr = ''
    for tx in settled:
        txnId = tx[2]
        starttime = tx[0]
        finishedtime = tx[1]
        amount = tx[3]
        if amount >= 0:
            settledstr += f"{txnId}: ${amount} @ time {starttime} (finalized @ time {finishedtime})\n"
        else:
            amount = abs(amount)
            settledstr += f"{txnId}: -${amount} @ time {starttime} (finalized @ time {finishedtime})\n"

    
    return creditstr + '\n' + payablestr + '\n\n' + 'Pending transactions:\n' + pendingstr + '\n' + 'Settled transactions:\n' + settledstr.rstrip()
            
            
            
            
            
            
            
            
            
            
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inputJSON = input()

    result = summarize(inputJSON)

    fptr.write(result + '\n')

    fptr.close()
