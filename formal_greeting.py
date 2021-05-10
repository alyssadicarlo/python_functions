def make_formal_greeting(name, title):
    return ("This is %s, the %s" % (name, title))

def ask_for_user_info():
    name = input("What is your name? ")
    title = input("What is your title? ")
    print(make_formal_greeting(name, title))
    
ask_for_user_info()