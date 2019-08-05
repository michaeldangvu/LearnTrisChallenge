# learntris.py version 0.1
score = 0
linesCleared = 0
blankLine = ". . . . . . . . . ."
lines = list()
for i in range(22):
  lines.append(blankLine)

def run():
  cmd = input()
  while (cmd != 'q'):
    if (cmd == 'p'):
      for line in lines:
        print(line)
    elif (cmd == 'g'):
      # for line in lines: (this is a shallow copy of line)
      for i in range(22):
        lines[i] = input()
    elif (cmd == 'c'):
      for i in range(22):
        lines[i] = blankLine
    elif (cmd == "?s"):
      print(score)
    elif (cmd == "?n"):
      print(linesCleared)
    elif (cmd == 's'):
      for i in range(22):
        lineFull = True
        j = 0
        while (j < 10 and lineFull):
          if lines[j * 2] == '.':
            lineFull = False
          j += 1
        if lineFull:
          lines[i] = blankLine
          score += 100
          linesCleared += 1

    cmd = input()
  # end while loop

run()