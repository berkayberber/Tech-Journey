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
    max_moves = 6
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


def heuristic(board, player):
    def in_target_zone(piece, target_zone):
        return piece in target_zone

    white_pieces_in_target = sum(
        1 for i in range(16) for j in range(16) if board[i][j] == 'W' and (i, j) in Target_White)
    black_pieces_in_target = sum(
        1 for i in range(16) for j in range(16) if board[i][j] == 'B' and (i, j) in Target_Black)

    white_proximity = sum(
        min(abs(i - ti) + abs(j - tj) for (ti, tj) in Target_White) for i in range(16) for j in range(16) if
        board[i][j] == 'W')
    black_proximity = sum(
        min(abs(i - ti) + abs(j - tj) for (ti, tj) in Target_Black) for i in range(16) for j in range(16) if
        board[i][j] == 'B')

    white_score = white_pieces_in_target * 10 - white_proximity
    black_score = black_pieces_in_target * 10 - black_proximity

    if player == 'white':
        return white_score - black_score
    else:
        return black_score - white_score


# Minimax with alpha-beta pruning
def minimax(board, depth, maximizing_player, alpha, beta, player):
    if depth == 0:
        return heuristic(board, player), None

    best_move = None

    if maximizing_player:
        max_eval = -math.inf
        possible_moves = generate_possible_moves(board, "white")
        for move in possible_moves:
            new_board = apply_move(board, move)
            eval, _ = minimax(new_board, depth - 1, False, alpha, beta, "black")
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        possible_moves = generate_possible_moves(board, "black")
        for move in possible_moves:
            new_board = apply_move(board, move)
            eval, _ = minimax(new_board, depth - 1, True, alpha, beta, "white")
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move


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
            possible_moves = generate_possible_moves(Board1, current_player)

            if possible_moves:
                possible_moves = generate_possible_moves(Board1, current_player)
                _, best_move = minimax(Board1, 3, False, float('-inf'), float('inf'), 'black')
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

            break
        score_w = heuristic(Board1, 'white')
        score_b = heuristic(Board1, 'black')
        print(score_b)
        print(score_w)
        if check_end(move_count):
            # Check if the score condition is met after each move
            if score_w > abs(score_b):
                print("White player wins based on score difference!")
                break
            elif score_b > abs(score_w):
                print("Black player wins based on score difference!")
                break
            else:

                print("Maximum moves reached.scores are tie Game over!")
elif n == 2:

    while True:

        display_board(Board1)
        print(f"{current_player.capitalize()}'s turn")
        n1 = input("Enter y for another moves for both Ai ?")
        if n1 == "y" or n1 == "Y":
            if current_player == 'white':
                possible_moves = generate_possible_moves(Board1, "white")

                if possible_moves:
                    possible_moves = generate_possible_moves(Board1, "white")
                    _, best_move = minimax(Board1, 3, True, float('-inf'), float('inf'), 'white')
                    result = move_piece(*best_move, current_player)

                else:
                    print("No possible moves for AI.")
                    break
            else:
                possible_moves = generate_possible_moves(Board1, "black")

                if possible_moves:
                    possible_moves = generate_possible_moves(Board1, "black")
                    _, best_move = minimax(Board1, 3, False, float('-inf'), float('inf'), 'black')
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

        score_w = heuristic(Board1, 'white')
        score_b = heuristic(Board1, 'black')

        if check_end(move_count):
            # Check if the score condition is met after each move
            if score_w > abs(score_b):
                print("White player wins based on score difference!")
                break
            elif score_b > abs(score_w):
                print("Black player wins based on score difference!")
                break
            else:

                print("Maximum moves reached. scores are tie Game over!")
else:
    print("X")
