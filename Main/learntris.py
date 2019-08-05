# learntris.py version 0.1

tetI = [
        ". . . .\nc c c c\n. . . .\n. . . .",
        ". . c .\n. . c .\n. . c .\n. . c .",
        ". . . .\n. . . .\nc c c c\n. . . .",
        ". c . .\n. c . .\n. c . .\n. c . ."
        ]
tetO = ["y y\ny y","y y\ny y","y y\ny y","y y\ny y"]
tetZ = [
        "r r .\n. r r\n. . .",
        ". . r\n. r r\n. r .",
        ". . .\nr r .\n. r r",
        ". r .\nr r .\nr . ."
        ]
tetS = [
        ". g g\ng g .\n. . .",
        ". g .\n. g g\n. . g",
        ". . .\n. g g\ng g .",
        "g . .\ng g .\n. g ."  
        ]
tetJ = [
        "b . .\nb b b\n. . .",
        ". b b\n. b .\n. b .",
        ". . .\nb b b\n. . b",
        ". b .\n. b .\nb b ."
        ]
tetL = [
        ". . o\no o o\n. . .",
        ". o .\n. o .\n. o o",
        ". . .\no o o\no . .",
        "o o .\n. o .\n. o ."
        ]
tetT = [
        ". m .\nm m m\n. . .",
        ". m .\n. m m\n. m .",
        ". . .\nm m m\n. m .",
        ". m .\nm m .\n. m ."
        ]

def run():
  xpos = 4
  ypos = 0
  tetOrientation = 0
  activeTet = ""
  score = 0
  linesCleared = 0
  blankLine = ". . . . . . . . . ."
  lines = list(list())
  for i in range(22):
    lines.append(blankLine)
  # for i in range(22):
  #   for j in range(10):
  #     lines[i][j * 2] = "."

  userInput = input().split(" ")
  cmd = userInput[0]

  # while (cmd != 'q'):
  while (userInput[0] != 'q'):
    cmd = userInput[0]
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
      print(activeTet[tetOrientation])
    elif (cmd == "I"):
      tetOrientation = 0
      activeTet = tetI
    elif (cmd == "O"):
      tetOrientation = 0
      activeTet = tetO
    elif (cmd == "Z"):
      tetOrientation = 0
      activeTet = tetZ
    elif (cmd == "S"):
      tetOrientation = 0
      activeTet = tetS
    elif (cmd == "J"):
      tetOrientation = 0
      activeTet = tetJ
    elif (cmd == "L"):
      tetOrientation = 0
      activeTet = tetL
    elif (cmd == "T"):
      tetOrientation = 0
      activeTet = tetT
    elif (cmd == ")"):
      tetOrientation = (tetOrientation + 1) % 4
    elif (cmd == ";"):
      print()
    # elif (cmd == "P"):
    #   for i 

    else:
      print("input is: " + cmd)
      break

    userInput.pop(0)
    if (len(userInput) == 0):
      userInput = input().split(" ")
    # cmd = userInput[0]
  # end while loop


run()