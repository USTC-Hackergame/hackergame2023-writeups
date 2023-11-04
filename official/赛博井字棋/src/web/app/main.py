from flask import Flask, request, make_response, render_template, session, redirect, url_for
from math import inf as infinity
import base64
import OpenSSL

HUMAN = -1
COMP = +1

from secret import secret_key, flag_func

app = Flask(__name__)
app.secret_key = secret_key

app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024

with open("./cert.pem") as f:
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, f.read())

@app.before_request
def check():
    if request.path.startswith('/static/'):
        return
    if request.args.get('token'):
        try:
            token = request.args.get('token')
            id, sig = token.split(":", 1)
            sig = base64.b64decode(sig, validate=True)
            OpenSSL.crypto.verify(cert, sig, id.encode(), "sha256")
            session['token'] = token
        except Exception:
            session['token'] = None
        return redirect(url_for('index'))
    if session.get("token") is None:
        return make_response(render_template("error.html"), 403)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        print("Got POST request")
        board = session.get("board", None)
        if board is None:
            board = [[0 for i in range(3)] for j in range(3)]
        req = request.get_json()
        act = req.get("act", "")
        if act == "getBoard":
            print("Get board")
            return {"board": board}
        elif act == "reset":
            print("Reset board")
            board = [[0 for i in range(3)] for j in range(3)]
            session["board"] = board
            return {"board": board}
        else:
            print("Set move")
            try:
                pos : dict = request.get_json()
                x = int(pos.get("x", ""))
                y = int(pos.get("y", ""))
            except ValueError:
                return {"board": board}
            print(f"Got x={x}, y={y}")
            if x < 0 or x > 2 or y < 0 or y > 2:
                return {"board": board}
            if game_over(board):
                if wins(board, HUMAN):
                    return {"board": board, "msg": flag_func(session["token"])}
                elif wins(board, COMP):
                    return {"board": board, "msg": "You lose! Please reset the game."}
                else:
                    return {"board": board, "msg": "Draw! Please reset the game."}
            board[x][y] = HUMAN
            if game_over(board) and wins(board, HUMAN):
                return {"board": board, "msg": flag_func(session["token"])}
            elif len(empty_cells(board)) == 0:
                return {"board": board, "msg": "Draw!"}
            depth = len(empty_cells(board))
            cx, cy, _ = minimax(board, depth, COMP)
            board[cx][cy] = COMP
            session["board"] = board
            if game_over(board) and wins(board, COMP):
                return {"board": board, "msg": "You lose!"}
            return {"board": board}


def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False

def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(board, x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best
