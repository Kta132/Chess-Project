import turtle
s = turtle.getscreen()


def draw_box(board, x, y, size, fill_color):
    board.penup()  # Stop drawing
    board.goto(-x, -y)  # Change where it starts
    board.pendown()  # Begin drawing

    board.fillcolor(fill_color)
    board.begin_fill()

    for i in range(0, 4):
        board.forward(size)  # Draw forward
        board.right(90)  # 90 degree turn

    board.end_fill()  # Fill black or white


def draw_chess_board():
    square_color = "black"
    start_x = -10  # Origin for x
    start_y = -10  # Origin for y
    box_size = 30  # Each square size
    for i in range(0, 8):  # The Chess Board
        for j in range(0, 8):
            draw_box(board, start_x + j * box_size, start_y + i * box_size,
                     box_size, square_color)
            square_color = 'black' if square_color == 'white' else 'white'
        square_color = 'white' if square_color == 'black' else 'black'


board = turtle.Turtle()
draw_chess_board()
turtle.done()
