import pprint

blockchain = [[0]]


def get_last_blockchain_value():
    '''
    Gets the last transaction from the blockchain and returns it
    '''
    return blockchain[-1]


# Creates a Blockchain
def create_blockchain(transaction_value, last_transaction=[0]):
    '''
    Creates a Blockchain
    transaction_value: Takes input from the user of transacted value
    last_transaction: Transactions that were done before the current transaction i.e., the history of all transactions done
    '''
    blockchain.append([last_transaction, transaction_value])
    pprint.pprint(blockchain)


# Take input from user using the loop
for i in range(1, 5):
    user_input_transaction = float(input('Enter the Transaction amount: '))
    create_blockchain(transaction_value=user_input_transaction,
                      last_transaction=get_last_blockchain_value())
