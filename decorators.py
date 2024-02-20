#creating decorators
# they take function as input and return modified version of that function
def announce(f):
    def wrapper():
        print("about to run the function")
        f()
        print("done with the function")
    return wrapper
@announce
def hello():
    print("hello world")
hello()