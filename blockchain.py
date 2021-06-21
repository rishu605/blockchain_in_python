import pprint

blockchain = []


def get_last_blockchain_value():
    '''
    Gets the last transaction from the blockchain and returns it
    '''
    if(len(blockchain) == 0):
        return None
    return blockchain[-1]


# Creates a Blockchain
def add_transaction(transaction_value, last_transaction=[0]):
    '''
    Creates a Blockchain
    transaction_value: Takes input from the user of transacted value
    last_transaction: Transactions that were done before the current transaction i.e., the history of all transactions done
    '''
    blockchain.append([last_transaction, transaction_value])
    pprint.pprint(blockchain)


def verify_blockchain():
    invalid = 0
    if(len(blockchain) == 0):
        return 'No transactions in the Blockchain to verify'

    elif(len(blockchain) == 1):
        return 'There need to be at least 2 transactions in the Blockchain to verify them'
    else:
        for i in range(0, len(blockchain)-1):

            next_block = blockchain[i+1]
            current_block = blockchain[i]
            # print(f'Previous block: {previous_block}')
            # print(f'Current Block: {current_block}')
            if(current_block != next_block[0]):
                print('Blockchain has lost it\'s integrity')
                invalid = 1
    if(invalid == 0):
        return 'Blockchain is Verified'
    else:
        return ' Blockchain has lost it\'s integrity'


# verification_message = verify_blockchain()
# print(verification_message)
# Take input from user using the loop


def get_user_input():
    stay = True
    while stay:
        print('Please Choose one of the following options:')
        print('1. Enter a transaction into the Blockchain  - Press 1')
        print('2. Show the whole Blockchain - Press 2')
        print('3. Manipulate the Blockchain - Press 4')
        print('4. Verify Integrity of Blockchain - Press 4')
        print('5. Press 5 to Exit')
        user_choice = int(input('Enter your choice: '))
        if(user_choice == 1):
            user_input_transaction = float(
                input('Enter the Transaction amount: '))
            add_transaction(user_input_transaction,
                            get_last_blockchain_value())
        elif(user_choice == 2):
            print('The Blockchain consists of the following transactions: ')
            pprint.pprint(blockchain)
            print('\n')

        elif(user_choice == 3):
            new_value = float(input('Enter the new value: '))
            print(new_value)
            blockchain[1] = [new_value]
            # Changing a particular value in the blockchain
            pprint.pprint(blockchain[1])
            pprint.pprint(blockchain)
        elif(user_choice == 4):
            verification_message = verify_blockchain()
            print(verification_message)
        elif(user_choice == 5):
            print('Thank you. The program will now Exit')
            stay = False
            break
        else:
            print('Wrong Choice. Please enter a valid choice')
            print('\n')


get_user_input()
