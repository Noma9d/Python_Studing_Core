from bot_handlers import HANDLERS
from bot_classes import AdressBook


def parse_command(command):
    
    parts = command.split()
    command = parts[0]
    
    if len(parts) > 1:
        command_args = parts[1:]
    else:
        command_args = []

    if parts[0] == 'show' and parts[1] == 'all':
        command_args = []
        command = 'show all'
    return command, command_args


def main():

    while True:
        command_string = input('>>> ').strip().lower()
        
        if len(command_string) == 0:
            print('You are dont write the comamnd')
            continue

        command, command_args = parse_command(command_string)

        if command in HANDLERS:
            try:
                result = HANDLERS[command](*command_args)
                print(result)
            except TypeError:
                print('Invalid input. Please try again.')
        else:
            print(f'{command} command was not found')


if __name__ == '__main__':
    main()