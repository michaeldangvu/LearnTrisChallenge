# learntris.py version 0.1

BLANK_LINE = ". . . . . . . . . ."

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
spawnPosition = {
  "I" : 6,
  "O" : 8,
  "Z" : 6,
  "S" : 6,
  "J" : 6,
  "L" : 6,
  "T" : 6
}

def hasCollision(lines, orientedTet, xpos, ypos):
  xTetDimension = len(orientedTet[0])
  yTetDimension = len(orientedTet)


def printActive(lines, orientedTet, xpos, ypos):
  xTetDimension = len(orientedTet[0])
  yTetDimension = len(orientedTet)
  liveLines = list(lines)

  yLimit = ypos + yTetDimension
  if (yLimit > 23):
    yLimit = yLimit - 2
  elif (yLimit > 22):
    yLimit = yLimit - 1
  for y in range(ypos, yLimit):
    # get line number of tetramino
    tetLevel = orientedTet[y - ypos]
    # liveLines[y] = lines[y][:xpos] + tetLevel + lines[y][xpos + xTetDimension:]
    
    liveLines[y] = lines[y][:xpos]
    for i in range(len(tetLevel) // 2 + 1):
      column = i * 2
      if (tetLevel[column] != '.'):   # only copy active tetramino values
        liveLines[y] += tetLevel[column] + " "
      elif ((xpos + column) < 19):   
        liveLines[y] += lines[y][xpos + column] + " "
    liveLines[y] += lines[y][xpos + xTetDimension + 1:]
    # liveLines[y] = liveLines[y][:19] # trim line length to 19 caused by TetOffset
  
  for line in liveLines:
    print(line)

def updateLines(lines, orientedTet, xpos, ypos):
  xTetDimension = len(orientedTet[0])
  yTetDimension = len(orientedTet)
  yLimit = ypos + yTetDimension
  # if (yLimit) > 23:
  #   yLimit = yLimit - 2
  # elif (yLimit) > 22:
  #   yLimit = yLimit - 1
  if yLimit > 22:
    yLimit = 22
  for y in range(ypos, yLimit):
    # get line number of tetramino, only the ones inside matrix
    tetLevel = orientedTet[y - ypos]
    # lines[y] = lines[y][:xpos] + tetLevel + lines[y][xpos + xTetDimension:]
    currentLine = lines[y]
    lines[y] = currentLine[:xpos]
    for i in range(len(tetLevel) // 2 + 1):
      column = i * 2
      if(tetLevel[column] != '.'):    # tetramino position is not blank
        lines[y] += tetLevel[column] + " "
      # is blank, but only do if sum is less than 19 (index OoB)
      elif ((xpos + column) < 19):    
        lines[y] += currentLine[xpos + column] + " "
    lines[y] += currentLine[xpos + xTetDimension + 1:]
    # print("line: " + lines[y])

def xOverflow(direction, xpos, activeTet):
  if (direction == 'r'):
    xOffsetRight = 18 - (xpos + len(activeTet[0]))
    for level in activeTet:
      if (level[xOffsetRight] != '.'):
        return False
  elif (direction == 'l'):
    xOffsetLeft = -1 * xpos
    for level in activeTet:
      if (level[xOffsetLeft] != '.'):
        return False
  return True

def yOverflow(ypos, activeTet):
  offset = 22 - (ypos + len(activeTet) + 1)
  if offset < 0:
    for i in range(len(activeTet[offset]) // 2 + 1):
      if (activeTet[offset][i * 2] != '.'):
        return False
  return True

def parseInput(inStr):
  userInput = list()
  while (len(inStr) > 0):
    if (inStr[0] == " "):
      inStr = inStr[1:]
    elif (inStr[0] == "?"):
      userInput.append(inStr[:2])
      inStr = inStr[2:]
    else:
      userInput.append(inStr[:1])
      inStr = inStr[1:]
  return userInput

def run():
  lines = list()
  for i in range(22):
    lines.append(BLANK_LINE)
  xpos = 0
  ypos = 0
  activeOrientation = 0
  activeTet = ""
  score = 0
  linesCleared = 0

    
  userInput = parseInput(input())
  cmd = userInput[0]

  # userInput = input().split(" ")
  # cmd = userInput[0]

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
        lines[i] = BLANK_LINE
    elif (cmd == "?s"):
      print(score)
    elif (cmd == "?n"):
      print(linesCleared)
    elif (cmd == 's'):    # simulate 1 step
      for i in range(22):
        lineFull = True # full line means we should clear and replace with '.'
        j = 0
        while (j < 10 and lineFull):
          if (lines[i][j * 2] == '.'):
            lineFull = False
          j += 1
        if lineFull:
          lines[i] = BLANK_LINE
          score += 100
          linesCleared += 1
    elif (cmd == 't'):  # print active tetramino
      print(activeTet[activeOrientation])
    elif (cmd == "I"):
      activeOrientation = 0
      xpos = spawnPosition["I"]
      ypos = 0
      activeTet = tetI
    elif (cmd == "O"):
      activeOrientation = 0
      xpos = spawnPosition["O"]
      ypos = 0
      activeTet = tetO
    elif (cmd == "Z"):
      activeOrientation = 0
      xpos = spawnPosition["Z"]
      ypos = 0
      activeTet = tetZ
    elif (cmd == "S"):
      activeOrientation = 0
      xpos = spawnPosition["S"]
      ypos = 0
      activeTet = tetS
    elif (cmd == "J"):
      activeOrientation = 0
      xpos = spawnPosition["J"]
      ypos = 0
      activeTet = tetJ
    elif (cmd == "L"):
      activeOrientation = 0
      xpos = spawnPosition["L"]
      ypos = 0
      activeTet = tetL
    elif (cmd == "T"):
      activeOrientation = 0
      xpos = spawnPosition["T"]
      ypos = 0
      activeTet = tetT
    elif (cmd == ")"):  # rotate tetramino right
      activeOrientation = (activeOrientation + 1) % 4
    elif (cmd == "("):  # rotate left
      activeOrientation = (4 + activeOrientation - 1) % 4
    elif (cmd == ";"):  # print blank line
      print()
    elif (cmd == "P"): # print matrix with active tetramino
      orientedTet = activeTet[activeOrientation].upper().split("\n")
      printActive(lines, orientedTet, xpos, ypos)

      # orientedTet = activeTet[activeOrientation].upper().split("\n")
      # xTetDimension = len(orientedTet[0])
      # yTetDimension = len(orientedTet)
      # liveLines = list(lines)

      # yLimit = ypos + yTetDimension
      # if (yLimit > 23):
      #   yLimit = yLimit - 2
      # elif (yLimit > 22):
      #   yLimit = yLimit - 1
      # for y in range(ypos, yLimit):
      #   # get line number of tetramino
      #   tetLevel = orientedTet[y - ypos]
      #   # liveLines[y] = lines[y][:xpos] + tetLevel + lines[y][xpos + xTetDimension:]
        
      #   liveLines[y] = lines[y][:xpos]
      #   for i in range(len(tetLevel) // 2 + 1):
      #     column = i * 2
      #     if (tetLevel[column] == '.'):   # only copy active tetramino values
      #       liveLines[y] += lines[y][xpos + column] + " "
      #     else:
      #       liveLines[y] += tetLevel[column] + " "
      #   liveLines[y] += lines[y][xpos + xTetDimension + 1:]
      #   # liveLines[y] = liveLines[y][:19] # trim line length to 19 caused by TetOffset
      
      # for line in liveLines:
      #   print(line)
    elif (cmd == "<"):
      if (xpos > 0):
        xpos -= 2
    elif (cmd == ">"):
      orientedTet = activeTet[activeOrientation].upper().split("\n")
      if (xpos + len(orientedTet[0]) < 19 or xOverflow('r', xpos, orientedTet)):
        xpos += 2
    elif (cmd == "v"):
      orientedTet = activeTet[activeOrientation].upper().split("\n")
      if (ypos + len(orientedTet) < 22 or yOverflow(ypos, orientedTet)):
        ypos = ypos + 1
      else:
        updateLines(lines, orientedTet, xpos, ypos)
    elif (cmd == "V"):      
      orientedTet = activeTet[activeOrientation].split("\n")
      ypos = 22 - len(orientedTet)
      while (yOverflow(ypos, orientedTet)):
        ypos += 1
      updateLines(lines, orientedTet, xpos, ypos)

    else:
      print("input is: " + cmd)
      break

    userInput.pop(0)
    if (len(userInput) == 0):
      # userInput = input().split(" ")
      userInput = parseInput(input())
    # cmd = userInput[0]
  # end while loop


run()