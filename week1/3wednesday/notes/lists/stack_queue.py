# Stacks an d Queues

# ****************************************
# Stack - FILO
# ****************************************

bankTeller = []

bankTeller.append('Greet Customer')
print('current todo: %s' %bankTeller)

# Teller completes task
bankTeller.pop()
print('current todo: %s' %bankTeller)

bankTeller.append('Process Deposit')

# Teller answers phone before completing deposit
bankTeller.append('Incoming Phone Call')

# Phone call now drops off, but phone call itself is still on
# as is the deposit
bankTeller.pop()
bankTeller.append('Resolve Phone Call')

print('current todo: %s' %bankTeller)


# ******************************************
# Queue - FIFO
# ******************************************

processor = []

processor.append({'type': 'page', 'path': '', 'header': [], 'cookies': []})
processor.append({'type': 'api', 'function': '', 'parameters': []})
processor.append({'type': 'email', 'subject' : '', 'body': '', 'addresses':[]})


for i in range(len(processor)):
    # pop() - defaults to last
    # however you may pass specific index - 0 based
    item = processor.pop(0)
    print('**********************')
    print('Processing Item', item)
    print('Remaining Queue', processor)
    print('**********************')