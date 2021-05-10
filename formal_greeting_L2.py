def make_formal_greeting(name, title):
    return ("This is %s, the %s" % (name, title))

def ask_for_user_info():
    name = input("What is your name? ")
    title = input("What is your title? ")
    return [name, title]
    
def ask_for_user_info_dictionary():
    name = input("What is your name? ")
    title = input("What is your title? ")
    return {
        "name": name,
        "title": title
    }
    
user_info_list = ask_for_user_info()
greeting_list = make_formal_greeting(user_info[0], user_info[1])
print(greeting_list)
    
user_info_dict = ask_for_user_info_dictionary()
greeting_dict = make_formal_greeting(user_info["name"], user_info["title"])
print(greeting_dict)