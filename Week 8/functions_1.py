def function_1():
    print("Hello")
    return 4

def function_2(x):
    print("World")
    return x + 2

def function_3(x):
    print(x)
    
def main():
    print(function_3( function_2( function_1() ) ))
    print(type(function_3( function_2( function_1() ) )))

if __name__ == "__main__":
    main()