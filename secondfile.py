users = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError: Enter user name"
        except ValueError:
            return"ValueError: Give me name and phone please"
        except IndexError:
            return"IndexError: invalid index"
        except TypeError:
            return"TypeError"
    return inner


@input_error
def add(data):
    name, phone = create_data(data)
    if name in users:
        raise ValueError('This contact already exist.')
    users[name] = phone
    return f"You added new contact {name}, his phone: {phone}."


@input_error
def change(data):
    name, phone = create_data(data)
    if name in users:
        users_0 = {name: phone}
        users.update(users_0)
        return f"You changed {name}`s phone to {phone}"
    return "Use add command"


@input_error
def phone_search(name):
    if name.strip() not in users:
        raise ValueError("This contact does`t exist")
    a = users.get(name.strip())
    return a


@input_error
def show_all():
    user = ''
    for key, value in users.items():
        user += f'{key} : {value} \n'
    return user


@input_error
def exit_func():
    return 'good bye'


@input_error
def hello_func():
    return "Hello"



def create_data(data):
    new_data = data.strip().split(" ")
    name = new_data[0]
    phone = new_data[1]
    if name.isnumeric():
        raise ValueError("Must be a str, not int/float")
    if not phone.isnumeric():
        raise ValueError("Must be a number, not str")
    return name, phone




def change_input(command):
    command_1 = command
    data = ''
    for key in command_dict:
        if command.strip().lower().startswith(key):
            command_1 = key
            data = command[len(command_1):]
            break
    if data:
        return reaction_func(command_1)(data)
    return reaction_func(command_1)()


def reaction_func(reaction):
    return command_dict.get(reaction, break_func)


def break_func():
    return 'Wrong enter.'


def main():
    while True:
        command = input('Enter command for bot: ')
        result = change_input(command)
        print(result)
        if result == 'good bye':
            break


command_dict = {
    'hello': hello_func,
    'add': add,
    'change': change,
    'phone': phone_search,
    'show all': show_all,
    'good bye': exit_func,
    'close': exit_func,
    'exit': exit_func,

}


if __name__ == '__main__':
    main()
