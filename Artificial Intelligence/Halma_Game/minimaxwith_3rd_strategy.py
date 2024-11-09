import math

file1 = open("input.txt", "r")
a = file1.readlines()
file1.close()
a = [x.rstrip('\n') for x in a]

Board = []
Board1 = [[0 for i in range(0, 16)] for j in range(0, 16)]
Target_White = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (1, 2), (2, 2),
                (3, 2), (0, 3), (1, 3), (2, 3), (0, 4), (1, 4)]
Target_Black = [(14, 11), (15, 11), (13, 12), (14, 12), (15, 12), (12, 13), (13, 13), (14, 13), (15, 13), (11, 14),
                (12, 14), (13, 14), (14, 14), (15, 14), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15)]
for i in range(0, 16):
    Board.append(a[3 + i])
for i in range(0, 16):
    for j in range(0, 16):
        Board1[i][j] = Board[i][j]


def display():
    k = 1
    f = 0
    for i in range(0, 16):
        print(i, " ", end="")
    print("")
    for i in Board1:
        for j in i:

            print(j, " ", end="")
            k += 1

            if k == 17:
                print(f)

                k = 1
                f += 1


def is_valid_move(board, start, end):
    # Board dimensions
    rows = len(board)
    cols = len(board[0])

    # Start and end positions
    start_row, start_col = start
    end_row, end_col = end

    # Ensure start and end positions are within bounds
    if not (0 <= start_row < rows and 0 <= start_col < cols and 0 <= end_row < rows and 0 <= end_col < cols):
        return False

    # Ensure start position has a piece (either 'W' or 'B')
    if board[start_row][start_col] not in ['W', 'B']:
        return False

    # Ensure end position is empty
    if board[end_row][end_col] != '.':
        return False

    # Calculate the move
    d_row = end_row - start_row
    d_col = end_col - start_col

    # Check for valid single-step move (adjacent cells)
    if abs(d_row) <= 1 and abs(d_col) <= 1:
        return True

    # Check for valid jump move (over an adjacent piece)
    if abs(d_row) == 2 and abs(d_col) == 2:
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        if board[mid_row][mid_col] in ['W', 'B']:
            return True

    return False


def check_win(player):
    if player == 'white':
        return all(Board1[row][col] == 'W' for (row, col) in Target_White)
    elif player == 'black':
        return all(Board1[row][col] == 'B' for (row, col) in Target_Black)


def check_end(move_count):
    max_moves = 150
    if move_count >= max_moves:
        return True
    else:
        return False


def generate_possible_moves(board, player):
    possible_moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player[0].upper():  # Assuming player is 'white' or 'black'
                # Check all 8 directions for possible moves
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    new_i, new_j = i + di, j + dj
                    if 0 <= new_i < len(board) and 0 <= new_j < len(board[i]) and board[new_i][new_j] == '.':
                        possible_moves.append((i, j, new_i, new_j))
    return possible_moves


def apply_move(board, move):
    src_row, src_col, dest_row, dest_col = move
    new_board = [list(row) for row in board]
    new_board[dest_row][dest_col] = new_board[src_row][src_col]
    new_board[src_row][src_col] = '.'
    return new_board


def move_piece(src_row, src_col, dest_row, dest_col, player):
    if is_valid_move(Board1, (src_row, src_col), (dest_row, dest_col)):
        Board1[dest_row][dest_col] = Board1[src_row][src_col]
        Board1[src_row][src_col] = "."
        if check_win(player):
            return f"{player.capitalize()} wins!"
        else:
            return True
    else:
        return False


def make_move(board, move):
    src_row, src_col, dest_row, dest_col = move
    if board[src_row][src_col] != '.' and board[dest_row][dest_col] == '.':
        board[dest_row][dest_col] = board[src_row][src_col]
        board[src_row][src_col] = '.'
        return True
    else:
        return False


def distance_to_target(piece_pos, target_list):
    # Calculate the minimum distance of a piece to any target in the target_list
    min_distance = float('inf')
    for target_pos in target_list:
        distance = abs(piece_pos[0] - target_pos[0]) + abs(piece_pos[1] - target_pos[1])
        min_distance = min(min_distance, distance)
    return min_distance


def evaluation_function(board, player):
    # Initialize scores for white and black players
    white_score = 0
    black_score = 0

    # Calculate scores based on distance of pieces to their respective targets
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'W':
                white_score += distance_to_target((i, j), Target_White)
            elif board[i][j] == 'B':
                black_score += distance_to_target((i, j), Target_Black)

    # Adjust scores based on the player's perspective
    if player == 'white':
        return white_score - black_score
    else:
        return black_score - white_score


def minimax(board, depth, maximizing_player, player):
    if depth == 0:
        return evaluation_function(board, player), None

    best_move = None

    if maximizing_player:
        eval = -math.inf
        possible_moves = generate_possible_moves(board, "white")
        for move in possible_moves:
            new_board = apply_move(board, move)
            temp, _ = minimax(new_board, depth - 1, False, "white")
            if temp > eval:
                eval = temp
                best_move = move

    else:
        eval = math.inf
        possible_moves = generate_possible_moves(board, "black")
        for move in possible_moves:
            new_board = apply_move(board, move)
            temp, _ = minimax(new_board, depth - 1, True, "black")
            if temp < eval:
                eval = temp  # Fix the variable name here
                best_move = move

    return eval, best_move


def display_board(board):
    for row in board:
        print(' '.join(row))


# Initialize the game
current_player = 'white'
move_count = 0
score_w = 0
score_b = 0
print("Enter 1 for human vs ai?")
n = int(input("Enter 2 for Ai vs Ai ?"))
if n == 1:
    while not check_end(move_count):

        display()
        print(f"{current_player.capitalize()}'s turn")

        if current_player == 'white':

            src_row = int(input("Enter the row of your piece to move: "))
            src_col = int(input("Enter the column of your piece to move: "))
            dest_row = int(input("Enter the row to move the piece to: "))
            dest_col = int(input("Enter the column to move the piece to: "))
            result = move_piece(src_row, src_col, dest_row, dest_col, current_player)
        else:
            possible_moves = generate_possible_moves(Board1, 'black')
            Player = "BLACK"

            if possible_moves:
                possible_moves = generate_possible_moves(Board1, 'black')
                score, best_move = minimax(Board1, 3, False, "black")
                result = move_piece(*best_move, Player)


            else:
                print("No possible moves for AI.")
                break

        if result is True:
            move_count += 1
            current_player = 'black' if current_player == 'white' else 'white'
        elif result is False:
            print("Invalid move!")
        else:

            break
        score_w = evaluation_function(Board1, 'white')
        score_b = evaluation_function(Board1, 'black')
        if check_end(move_count):
            # Check if the score condition is met after each move
            if score_w - score_b >= 20:
                print("White player wins based on score difference!")
                break
            elif score_b - score_w >= 20:
                print("Black player wins based on score difference!")
                break
            else:

                print("Maximum moves reached. Game over!")
elif n == 2:
    while True:

        display_board(Board1)
        print(f"{current_player.capitalize()}'s turn")
        n1 = input("Enter y for another moves for both Ai ?")
        if n1 == "y" or n1 == "Y":
            if current_player == 'white':
                possible_moves = generate_possible_moves(Board1, 'white')

                if possible_moves:
                    possible_moves = generate_possible_moves(Board1, 'white')
                    _, best_move = minimax(Board1, 3, True, "white")
                    result = move_piece(*best_move, current_player)


                else:
                    print("No possible moves for AI.")
                    break
            else:
                possible_moves = generate_possible_moves(Board1, 'black')
                Player = "BLACK"

                if possible_moves:
                    possible_moves = generate_possible_moves(Board1, 'black')
                    _, best_move = minimax(Board1, 3, False, "black")
                    result = move_piece(*best_move, current_player)


                else:
                    print("No possible moves for AI.")
                    break

            if result is True:
                move_count += 1
                current_player = 'black' if current_player == 'white' else 'white'
            elif result is False:
                print("Invalid move!")
            else:
                print(result)
                break

        score_w = evaluation_function(Board1, 'white')
        score_b = evaluation_function(Board1, 'black')
        if check_end(move_count):
            # Check if the score condition is met after each move
            if score_w - score_b >= 20:
                print("White player wins based on score difference!")
                break
            elif score_b - score_w >= 20:
                print("Black player wins based on score difference!")
                break
            else:

                print("Maximum moves reached. Game over!")
else:
    print("X")
