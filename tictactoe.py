def print_board(board):
      for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
          print("-----------")

    def check_winner(board):
      # Check rows
      for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
          return board[i]
      
      # Check columns
      for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
          return board[i]
      
      # Check diagonals
      if board[0] == board[4] == board[8] != " ":
        return board[0]
      if board[2] == board[4] == board[6] != " ":
        return board[2]
      
      # Check for tie
      if " " not in board:
        return "Tie"
      
      return None

    def main():
      board = [" "] * 9
      current_player = "X"

      print("Welcome to Tic Tac Toe!")
      print("Enter positions (1-9) as shown below:")
      print_board([str(i+1) for i in range(9)])
      print("\nLet's begin!\n")

      while True:
        print_board(board)
        position = input(f"Player {current_player}, enter your move: ")

        try:
          position = int(position) - 1
          if position < 0 or position > 8:
            raise ValueError()
          
          if board[position] != " ":
            print("That position is already taken!")
            continue

          board[position] = current_player

          winner = check_winner(board)
          if winner:
            print_board(board)
            if winner == "Tie":
              print("It's a tie!")
            else:
              print(f"Player {winner} wins!")
            break

          current_player = "O" if current_player == "X" else "X"

        except ValueError:
          print("Please enter a valid number between 1-9!")

    if __name__ == "__main__":
      main()
