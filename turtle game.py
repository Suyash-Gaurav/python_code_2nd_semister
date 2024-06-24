import turtle  # Import the turtle graphics library
import time  # Import the time module for delaying actions

# Game constants
BOARD_SIZE = 3  # Size of the game board (3x3 grid)
EMPTY_CELL = " "  # Representation for an empty cell on the board
PLAYER_X = "X"  # Symbol for player X
PLAYER_O = "O"  # Symbol for player O

# Game state variables
current_player = PLAYER_X  # Variable to keep track of the current player
game_board = [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]  # 2D list to represent the game board
game_over = False  # Flag to indicate if the game is over


# Finite State Machine (FSM) states
class State:
    def on_event(self, event):  # Method to handle events in each state
        pass


# State representing the start of the game
class StartState(State):
    def __init__(self, fsm):
        self.fsm = fsm

    def on_event(self, event):
        if event == "start":  # Transition to PlayingState when receiving the "start" event
            self.fsm.transition(PlayingState)


# State representing the main gameplay
class PlayingState(State):
    def __init__(self, fsm):
        self.fsm = fsm
        self.turtle = turtle.Turtle()  # Create a Turtle object for drawing
        self.turtle.hideturtle()  # Hide the turtle icon
        self.turtle.speed(0)  # Set the drawing speed to the maximum
        self.draw_board()  # Draw the game board
        self.listen_clicks()  # Set up event listeners for mouse clicks

    def draw_board(self):
        # Draw the grid lines of the game board
        self.turtle.penup()
        self.turtle.goto(-150, 150)
        self.turtle.pendown()
        for _ in range(4):
            self.turtle.forward(300)
            self.turtle.left(90)
        self.turtle.penup()
        # Write the symbols (X, O, or empty) on the board
        for x in range(-100, 200, 100):
            for y in range(-100, 200, 100):
                self.turtle.goto(x, y)
                self.turtle.write(game_board[y // 100][x // 100], align="center", font=("Arial", 24, "bold"))

    def listen_clicks(self):
        # Set up event listener for mouse clicks on the board
        turtle.onscreenclick(self.handle_click)
        turtle.listen()

    def handle_click(self, x, y):
        # Handle the mouse click event
        row = int((150 - y) // 100)  # Calculate the row clicked by the player
        col = int((x + 150) // 100)  # Calculate the column clicked by the player
        global current_player  # Declare current_player as global (not necessary here, but just to clarify)
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and game_board[row][col] == EMPTY_CELL and not game_over:
            # Check if the clicked cell is valid and empty
            game_board[row][col] = current_player  # Place the current player's symbol on the board
            self.draw_board()  # Redraw the board with the updated state
            if self.check_winner(current_player):  # Check if the current player has won
                self.fsm.transition(WinState)  # Transition to WinState if the current player wins
            elif self.check_draw():  # Check if the game ends in a draw
                self.fsm.transition(DrawState)  # Transition to DrawState if the game ends in a draw
            else:
                current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X  # Switch players

    def check_winner(self, player):
        # Check if the specified player has won
        for i in range(BOARD_SIZE):
            if all(game_board[i][j] == player for j in range(BOARD_SIZE)) or \
               all(game_board[j][i] == player for j in range(BOARD_SIZE)):
                return True
        if all(game_board[i][i] == player for i in range(BOARD_SIZE)) or \
           all(game_board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)):
            return True
        return False

    def check_draw(self):
        # Check if the game ends in a draw
        return all(EMPTY_CELL not in row for row in game_board)


# State representing the game end with a win
class WinState(State):
    def __init__(self, fsm):
        self.fsm = fsm
        self.turtle = fsm.turtle
        self.turtle.goto(0, 0)
        self.turtle.write(f"Player {current_player} wins!", align="center", font=("Arial", 24, "bold"))
        turtle.ontimer(self.reset_game, 3000)  # Reset the game after 3 seconds

    def reset_game(self):
        # Reset the game state variables and transition to StartState
        global game_board, current_player, game_over
        game_board = [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        current_player = PLAYER_X
        game_over = False
        self.fsm.transition(StartState)


# State representing the game end with a draw
class DrawState(State):
    def __init__(self, fsm):
        self.fsm = fsm
        self.turtle = fsm.turtle
        self.turtle.goto(0, 0)
        self.turtle.write("It's a draw!", align="center", font=("Arial", 24, "bold"))
        turtle.ontimer(self.reset_game, 3000)  # Reset the game after 3 seconds

    def reset_game(self):
        # Reset the game state variables and transition to StartState
        global game_board, current_player, game_over
        game_board = [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        current_player = PLAYER_X
        game_over = False
        self.fsm.transition(StartState)


# Finite State Machine (FSM) for managing game states
class FSM:
    def __init__(self):
        self.state = StartState(self)  # Initialize FSM with StartState
        self.turtle = None

    def transition(self, new_state):
        # Transition to a new state
        self.state = new_state(self)

    def on_event(self, event):
        # Handle an event by passing it to the current state
        self.state.on_event(event)

# Game loop
fsm = FSM()  # Initialize the FSM
fsm.on_event("start")  # Start the game
turtle.mainloop()  # Start the turtle graphics event loop
