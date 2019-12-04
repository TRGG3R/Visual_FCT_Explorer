from factom import Factomd
import json

factomd = Factomd(
    host='https://api.factomd.net/v2'  # Defaulted to Open Node. Change to your Factomd location
)

# Get latest completed block in the Factom blockchain #
recent_block_keymr = factomd.directory_block_head()['keymr']

# Get latest factoid block keymr from the directory block keymr #
factoid_block = factomd.directory_block_by_keymr(recent_block_keymr)['entryblocklist'][2]['keymr']

# Get the latest transactions #
raw_transactions = factomd.factoid_block_by_keymr(factoid_block)['fblock']['transactions']

# Get the latest directory block height #
directory_block_height = factomd.heights()['directoryblockheight']


# Return the factoid block information #
# noinspection PyShadowingNames
def factoidblock(blockheight=directory_block_height):
    """ blockheight (integer) = Factom Protocol blockheight
            --defaults to latest block"""
    factoid_block: object = factomd.factoid_block_by_height(blockheight)['fblock']
    print(json.dumps(factoid_block, indent=1))


# Create a dict with transaction information ##
# noinspection PyShadowingNames
def transactions(blockheight=directory_block_height):
    """ blockheight (integer) = Factom Protocol blockheight
            --defaults to latest block"""
    transactions = factomd.factoid_block_by_height(blockheight)['fblock']
    tx_dict = {}
    for tx in transactions['transactions']:
        tx_dict.update(tx)
        tx_dict.pop('blockheight')
        tx_dict.pop('outecs')
        tx_dict.pop('rcds')
        tx_dict.pop('sigblocks')
        print(tx_dict)


# Get the input addresses from the factoid transactions #
# noinspection PyShadowingNames,PyTypeChecker
def input_addresses(blockheight=directory_block_height):
    """ blockheight (integer) = Factom Protocol blockheight
            --defaults to latest block"""
    transactions: object = factomd.factoid_block_by_height(blockheight)['fblock']['transactions']
    for result in transactions:
        inputs = result['inputs']
        filtered_inputs = list(filter(None, inputs))  # Filter out empty strings
        for addresses in filtered_inputs:
            input_addresses = addresses['useraddress']
            print(input_addresses)


# Get the input amounts from the factoid transactions #
# noinspection PyShadowingNames,PyTypeChecker
def input_amounts(blockheight=directory_block_height):
    """ blockheight (integer) = Factom Protocol blockheight
            --defaults to latest block"""
    transactions: object = factomd.factoid_block_by_height(blockheight)['fblock']['transactions']
    for amount in transactions:
        inputs = amount['inputs']
        filtered_inputs = list(filter(None, inputs))  # Filter out empty strings
        for in_amount in filtered_inputs:
            input_amounts = in_amount['amount']
            print(input_amounts)


# Get the output addresses from the factoid transactions #
# noinspection PyShadowingNames,PyTypeChecker
def output_addresses(blockheight=directory_block_height):
    """ blockheight (integer) = Factom Protocol blockheight
            --defaults to latest block"""
    transactions: object = factomd.factoid_block_by_height(blockheight)['fblock']['transactions']
    for result in transactions:
        output_addr = result['outputs']
        for out_addr in output_addr:
            output_addresses = out_addr['useraddress']
            print(output_addresses)


# Get the output amounts from the factoid transactions #
# noinspection PyShadowingNames,PyTypeChecker
def output_amounts(blockheight=directory_block_height):
    """ blockheight (integer) = Factom Protocol blockheight
            --defaults to latest block"""
    transactions: object = factomd.factoid_block_by_height(blockheight)['fblock']['transactions']
    for amount in transactions:
        outputs = amount['outputs']
        filtered_outputs = list(filter(None, outputs))  # Filter out empty strings
        for out_amount in filtered_outputs:
            output_amounts = out_amount['amount']
            print(output_amounts)
