from enum import Enum
from blockchain import blockexplorer


latest_block = blockexplorer.get_latest_block()
attrs = vars(latest_block)
print ', '.join("%s: %s" % item for item in attrs.items())