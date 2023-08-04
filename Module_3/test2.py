import sys

def say_hello(name):
    print(f'Hello {name}')

if __name__ == '__main__':
    name = sys.argv[1]
    say_hello('fdvdb')


for arg in sys.argv:
    print(arg)
