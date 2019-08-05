# learntris.py version 0.1

tetI = ". . . .\nc c c c\n. . . .\n. . . .\n"
tetO = "y y\ny y"
tetZ = "r r .\n. r r\n. . ."
tetS = ". g g\ng g .\n. . ."
tetJ = "b . .\nb b b\n. . ."
tetL = ". . o\no o o\n. . ."
tetT = ". m .\nm m m\n. . ."

def run():
  activeTet = ""
  score = 0
  linesCleared = 0
  blankLine = ". . . . . . . . . ."
  lines = list()
  for i in range(22):
    lines.append(blankLine)

  userInput = input().split(" ")
  cmd = userInput[0]

  # while (cmd != 'q'):
  while (userInput[0] != 'q'):
    cmd = userInput[0]
    userInput.pop(0)
    if (cmd == 'p'):      #print entire matrix
      for line in lines:
        print(line)
    elif (cmd == 'g'):    # give info to matrix
      # for line in lines: (this is a shallow copy of line)
      for i in range(22):
        lines[i] = input()
    elif (cmd == 'c'):    #clear
      for i in range(22):
        lines[i] = blankLine
    elif (cmd == "?s"):
      print(score)
    elif (cmd == "?n"):
      print(linesCleared)
    elif (cmd == 's'):    # simulate 1 step
      for i in range(22):
        lineFull = True
        j = 0
        while (j < 10 and lineFull):
          if (lines[i][j * 2] == '.'):
            lineFull = False
          j += 1
        if lineFull:
          lines[i] = blankLine
          score += 100
          linesCleared += 1
    elif (cmd == 't'):
      print(activeTet)
    elif (cmd == "I"):
      activeTet = tetI
    elif (cmd == "O"):
      activeTet = tetO
    elif (cmd == "Z"):
      activeTet = tetZ
    elif (cmd == "S"):
      activeTet = tetS
    elif (cmd == "J"):
      activeTet = tetJ
    elif (cmd == "L"):
      activeTet = tetL
    elif (cmd == "T"):
      activeTet = tetT

    else:
      print("input is: " + cmd)
      break

    if (len(userInput) == 0):
      userInput = input().split(" ")
    # cmd = userInput[0]
  # end while loop


run()