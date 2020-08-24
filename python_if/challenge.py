print('Would you like to continue? "Yes" or "No"? ')
choice = input()
if choice == 'Yes':
    choice
    print('Continuing...')
    print('Complete!')
elif choice != 'Yes' and choice != 'No':
    choice
    print('Please try again and respond with Yes or No.')
    choice
elif choice == 'No':
    choice
    print('Exiting')
else:
    print('That is all')
