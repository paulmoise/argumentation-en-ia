from typing import List, Union


class Argument:
    def __init__(self, name='', attack=None, attacked_by=None):
        if attacked_by is None:
            attacked_by = []
        if attack is None:
            attack = []
        self.name = name
        self.attack = attack
        self.attacked_by = attacked_by

    def __repr__(self):
        return f"({self.name}, attacked_by = {self.attacked_by}, attack = {self.attack})"

    def is_attacked_by(self, arg):
        return arg.name in self.attacked_by


def arg_exist(arg_name, arguments):
    for arg in arguments:
        if arg.name == arg_name:
            return True
    return False


def get_arg_by_name(name: str, arguments: List[Argument]) -> Union[Argument, None]:
    for arg in arguments:
        if arg.name == name:
            return arg
    return None


def find_selected_args(arguments, selected_args=None):
    if selected_args is None:
        # selected all arguments which not attacked by any other argument
        selected_args = [arg for arg in arguments if not arg.attack]
        arguments = [arg for arg in arguments if arg not in selected_args]

    if not arguments:
        return selected_args

    arg = arguments[0]
    if not set([arg.name for arg in selected_args]).intersection(set(arg.attacked_by)):
        selected_args.append(arg)


if __name__ == '__main__':
    arguments = []
    print('Veuillez entrer les arguments à tester.')
    name = None
    # creation des arguments
    while True:
        name = input('> ')
        if name == 'end':
            break
        while name == '':
            name = input('> ')
        arguments.append(Argument(name))

    print("Veuillez indiquer les relations entre ces arguments.\n")
    print("Les relations respectent le format suivant\n")
    print("a,b")
    print("a,b signifie 'a' attack 'b'")
    print("Saisir 'end' pour terminer")
    print(arguments)
    while True:
        args = input('>')
        if args == 'end':
            break
        while len(args.split(',')) < 2:
            print("Veuillez saisir deux arguments séparés par une virgule!")
            args = input('>')
        arg1, arg2 = args.split(',')
        arg1 = arg1.strip()
        arg2 = arg2.strip()
        print(f'{arg1} attack {arg2}')

        if not arg_exist(arg1, arguments) or not arg_exist(arg2, arguments):
            print("Aucun n'argument avec ce nom trouvé!")
            break

        arg1 = get_arg_by_name(arg1, arguments)
        arg2 = get_arg_by_name(arg2, arguments)
        print(arg1)
        print(arg2)
        arg1.attack.append(arg2.name)
        print(arg1, 11)
        print(arg2, 221)
        arg2.attacked_by.append(arg1.name)
        print(arg1)
        print(arg2)

    print(arguments)
