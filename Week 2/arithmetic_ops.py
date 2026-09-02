def main():
    print(type(3 + 7))
    print(type(3 + 7.0))
    print(type(3 + 7.3))
    print(type(3.3 + 7))
    print(type(3.0 + 7.0))

    # This behavior exists for
    # these operations:
    # +
    # -
    # *
    # **
    # //
    # %
    
    print()
    # Division will always yield 
    # a float regardless of the
    # data type of both operands
    print(type(3 / 4))
    print(type(3.0 / 4.0))
    print(type(3 / 4.0))


if __name__ == "__main__":
    main()