from enum import Enum
from blockchain import blockexplorer
import pprint
import json

def convertToDict(obj):
    attrs = vars(obj)
    sample = {}
    for item in attrs.items():
        key, value = item
        sample[key] = value
    return sample

pp = pprint.PrettyPrinter(indent=2)

blockObj = blockexplorer.get_block('0000000000000000008dd08f62674a12f5e4291030cde5c322735527cb482aa9')

block = convertToDict(blockObj)

block['transactions'] = []

for transaction in blockObj.transactions:
    trans = convertToDict(transaction)
    trans['inputs'] = []
    trans['outputs'] = []
    for input in transaction.inputs:
        trans['inputs'].append(convertToDict(input))
    for output in transaction.outputs:
        trans['outputs'].append(convertToDict(output))
    block['transactions'].append(trans)

with open('test_block_data.json', 'w') as test_output:
    json.dump(block, test_output, indent=2)