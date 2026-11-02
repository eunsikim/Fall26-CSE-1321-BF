def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end="|")
        print()
        print("------")

    print("\n")

def main():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    print_board(board)

    board[0][0] = "X"

    print_board(board)

    board[1][1] = "O"

    print_board(board)
    
if __name__ == "__main__":
    main()