import pprint
import json
from hashlib import sha256

blockchain = []
current_transactions = []
participants = set()
participant_balances = {}


def genesis_block():
    genesis = {
        'previous_hash': 0,
        'index':  0,
        'transactions': []
    }

    blockchain.append(genesis)

# Initialize account value to 0 when the participant transacts for the first time


def initialize_participant_balances(participants):
    for participant in participants:
        if(participant not in participant_balances.keys()):
            participant_balances[participant] = 0


def update_participants(participant_pair):
    participants.add(participant_pair[0])
    participants.add(participant_pair[1])
    initialize_participant_balances(participants)


def check_balance(participant):
    for individual_participant in participant_balances.keys():
        if(individual_participant == participant):
            return participant_balances[participant]
    return 0


def add_transaction(sender, recipient, amount):
    '''
    sender: sender of coins,
    recipient: recipient of coins,
    amount: amount of coins sent in the transaction
    '''

    new_transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    participant_pair = (sender, recipient)
    update_participants(participant_pair)
    print(f'participants: {participants}')

    for participant, balance in participant_balances.items():
        if(participant == sender):
            participant_balances[sender] = participant_balances[sender] - amount
        if(participant == recipient):
            participant_balances[recipient] = participant_balances[recipient] + amount
        print(participant, balance)
        print(type(participant), type(balance))

    current_transactions.append(new_transaction)
    print(f'participants: {participants}')
    print(f'participant_balances: {participant_balances}')
# TODO
# Calculate account balance of each participant in the blockchain
# If account balance is not sufficient, sender cannot send the amount


def hash_block(block_data):
    block_string = json.dumps(block_data).encode('utf-8')
    block_hash = sha256(block_string).hexdigest().upper()

    return block_hash


def mine_block():
    previous_block = blockchain[-1]
    previous_hash = hash_block(previous_block)

    new_block = {
        'previous_hash': previous_hash,
        'index': len(blockchain),
        'transactions': current_transactions
    }

    blockchain.append(new_block)
    print(f'blockchain: {blockchain}')


# mine_block()


def when_to_mine_the_block():
    global current_transactions
    if(len(current_transactions) == 2):
        mine_block()
        current_transactions = []


# when_to_mine_the_block()


def verify_blockchain():
    invalid = 0
    if(len(blockchain) == 0):
        return 'No transactions in the Blockchain to verify'

    elif(len(blockchain) == 1):
        return 'Blockchain has only Genesis Block. Nothing to verify it against'
    else:
        for i in range(0, len(blockchain)-1):

            next_block = blockchain[i+1]
            current_block = blockchain[i]
            # print(f'Previous block: {previous_block}')
            # print(f'Current Block: {current_block}')
            if(hash_block(current_block) != next_block['previous_hash']):
                invalid = 1
    if(invalid == 0):
        return 'Blockchain is Verified'
    else:
        return ' Blockchain has lost it\'s integrity'


# verification_message = verify_blockchain()
# print(verification_message)
# Take input from user using the loop


def get_transaction_details_from_user():
    sender = input('Enter the Sender: ')
    recipient = input('Enter the Recipient: ')
    amount = float(input('Enter the amount of transaction: '))

    return (sender, recipient, amount)


def get_user_input():
    genesis_block()

    stay = True
    while stay:
        when_to_mine_the_block()
        print('Please Choose one of the following options:')
        print('1. Enter a transaction into the Blockchain  - Press 1')
        print('2. Show the whole Blockchain - Press 2')
        print('3. Manipulate the Blockchain - Press 3')
        print('4. Verify Integrity of Blockchain - Press 4')
        print('5. Press 5 to Exit')
        user_choice = int(input('Enter your choice: '))
        if(user_choice == 1):
            sender, recipient, amount = get_transaction_details_from_user()
            # Initializing the participant balances with 1000 if the participant is transacting for the first time
            if(sender not in participant_balances.keys()):
                participant_balances[sender] = 1000
            if(recipient not in participant_balances.keys()):
                participant_balances[recipient] = 1000
            # Check account balance of the sender
            sender_account_balance = check_balance(sender)
            print(sender_account_balance)
            print(participant_balances)
            # If the account balance is not sufficient for the transaction, prompt the user
            if(sender_account_balance < amount):
                print(f'{sender} does not have sufficient balance in their account')
                continue
            add_transaction(sender, recipient, amount)
            print(f'current_transactions: {current_transactions}')
        elif(user_choice == 2):
            print('The Blockchain consists of the following transactions: ')
            print(f'blockchain: {blockchain}')
            print('\n')

        elif(user_choice == 3):
            new_value = float(input('Enter the new value: '))
            position = int(
                input('Enter the block where you want to enter the new transaction: '))
            print(new_value)
            if(position > len(blockchain)):
                print(
                    'The blockchain does not have any transaction at the specified block')
                continue
            else:
                blockchain[position-1] = [new_value]
                # Changing a particular value in the blockchain
            # pprint.pprint(blockchain[1])
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
