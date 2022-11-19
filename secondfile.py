users = {}

def add(name, phone):
    users_0 = {name: phone}
    users.update(users_0)
    return users

def change(name, phone):
    users_0 = {name: phone}
    users.update(users_0)

def phone(name):
    a = users.get(name)
    return a

def show_all():
    print(users)

#def exit_func():
        #

def get_command(x):
    a = command_dict[x]
    return a

def hello_func():
    print("Hello")

command_dict = {
    'hello': hello_func,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
#    'good bye': exit_func,
#    'close': exit_func,
#    'exit': exit_func,

}
def main():

    while True:
        command = input("Enter command: ")
        command_1 = command.split(" ")[0].lower()

        if command_1 not in command_dict:
            command_1 = command.split(" ")[0] + " " + command.split(" ")[1]

        if command_1 == "close" or command_1 == "exit" or command_1 == "good bye":
            break
        handler = get_command(command_1)

        try:

            if command_1 == "phone":
                name_1 = command.split(" ")[1]
                result = handler(name_1)

            elif command_1 == "add" or command_1 == "change":
                name_1 = command.split(" ")[1]
                phone_1 = command.split(" ")[2]
                result = handler(name_1, phone_1)

            else:
                handler()


        except:
            print("error")
            continue

        if result:
            print(result)


if __name__ == '__main__':
    main()