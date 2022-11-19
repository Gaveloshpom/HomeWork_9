import sys

exit_words = ('good bye', 'close', 'exit')
users = {

}

def add(name = sys.argv[1], phone = sys.argv[2]):
    users_0 = {name: phone}
    users.update(users_0)
    return users

def change(name = sys.argv[1], phone = sys.argv[2]):
    users_0 = {name: phone}
    users.update(users_0)

def phone(name = sys.argv[1]):
    a = users.get(name)
    print(a)

def show_all():
    print(users)

def exit_func(string_0 = sys.argv[0]):
    if string_0 in exit_words:
        exit()

#def get_command(command_0 = sys.argv[0]):
#    return command_dict[command_0]


command_dict = {
    'hello': print("hello"),
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
}
def main():
    command = input("Enter command: ")

if __name__ == '__main__':
    main()

