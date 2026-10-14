import my_function as fn # Instead of using `my_function` to refer to the file, we use `fn`

def main():
    fn.hello_world()

    print(fn.calculation(10, n3 = 5))

if __name__ == "__main__":
    main()