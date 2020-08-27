# Working with 'blocks' of code
name = input()
password = 'swordfish'
if (name == 'Mary' or name == 'mary'):
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')
else:
    print('You are not who I was expecting.')
