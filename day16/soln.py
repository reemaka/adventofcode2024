import sys

def read_file():
  f = open('ex.txt', 'r')
  lines = []
  for line in f:
    lines.append(list(line.strip()))
  f.close()
  return lines

def turn_clockwise(i, j, curr_dir):
  if curr_dir == ">":
    return i + 1, j, "v"
  elif curr_dir == "v":
    return i, j - 1, "<"
  elif curr_dir == "<":
    return i - 1, j, "^"
  else:
    return i, j + 1, "^"

def turn_counterclockwise(i, j, curr_dir):
  if curr_dir == ">":
    return i - 1, j, "^"
  elif curr_dir == "^":
    return i, j - 1, "<"
  elif curr_dir == "<":
    return i + 1, j, "v"
  else:
    return i, j + 1, ">"

def go_straight(i, j, curr_dir):
  if curr_dir == ">":
    return i, j + 1
  elif curr_dir == "v":
    return i + 1, j
  elif curr_dir == "<":
    return i, j - 1
  else:
    return i - 1, j


def dfs(i, j, visited, lines, dir):
    if i < 0 or j < 0 or i >= len(lines) or j >= len(lines[0]):
        return 0, False
    if (i, j) in visited:
        return 0, False

    visited.add((i,j))

    if lines[i][j] == "E":
      return 0, True
    elif lines[i][j] == "#":
      return 0, False

    min_score = None
    next_i, next_j= go_straight(i, j, dir)
    straight_score, can_reach = dfs(next_i, next_j, visited.copy(), lines, dir)
    if can_reach:
      straight_score += 1
      min_score = straight_score
    next_i, next_j, next_dir = turn_clockwise(i, j, dir)
    clockwise_score, can_reach = dfs(next_i, next_j, visited.copy(), lines, next_dir)
    if can_reach:
      clockwise_score += 1000
      if min_score:
        min_score = min(min_score, clockwise_score)
      else:
        min_score = clockwise_score
    next_i, next_j, next_dir = turn_counterclockwise(i, j, dir)
    counterclockwise_score, can_reach = dfs(next_i, next_j, visited.copy(), lines, next_dir)
    if can_reach:
      counterclockwise_score += 1000
      if min_score:
        min_score = min(min_score, counterclockwise_score)
      else:
        min_score = counterclockwise_score

    if min_score:
      print(min_score)
      return min_score, True
    else:
      return 0, False

def p1():
  lines = read_file()
  for i, line in enumerate(lines):
    for j, cell in enumerate(line):
      if cell == "S":
        score, can_reach = dfs(i, j, set(), lines, ">")
        print(score)
        return

p1()

    
