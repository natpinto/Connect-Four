width = 7
height = 6

name = input("what's your name?")

def init():
  global board
  board = []
  for i in range(height):
    board.append([" "] * width)
  return board 

print("my name is " +name)

def get_move():
  column = int(input("pick a column (1-7)"))

  if (column > 7 or column < 1):
    print("NO")
    column = get_move()
  column -= 1
  column_full = True

  for i in range(height):
    if board [i][column]:
      column_full = False
      break

  if column_full:
    print("try again")
    column = get_move()
  return column


def draw_board():
  print("1,2,3,4,5,6,7")
  for i in init():
    print("|".join(i))

draw_board()
print(get_move())