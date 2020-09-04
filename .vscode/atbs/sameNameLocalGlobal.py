def spam():
    global eggs
    eggs = 'spam' # this is  the global

def bacon():
    eggs = 'bacon' # this is a local
    print(eggs)
    
def ham():
    print(eggs) # this is global
    bacon()
eggs = 42 # this is global
spam()
print(eggs)
