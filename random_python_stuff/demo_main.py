
def my_func(my_str):
    print(my_str)

def my_main_func():
    print('ducktales woo oo')
    my_func('called from my_main_func')

def print_name():
    print(__name__)

print('outside main')
print_name()


# my_func('WOOO OOO')

if __name__ == '__main__': #boilerplate
    my_func('inside a main')
    my_main_func()
    print_name()

# hackerrank?
