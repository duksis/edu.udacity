colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]
# colors =[['green', 'green', 'green'],
#          ['green', 'red', 'red'],
#          ['green', 'green', 'green']]

measurements = ['green', 'green', 'green' ,'green', 'green']
# measurements = ['red','red']

motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
# motions = [[0,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT
p=[[1.0/(len(colors[0])*len(colors))]*len(colors[0])]*len(colors)

def sense(p, Z ):
  q=[]
  for row in range(len(p)):
    q.append([])
    for column in range(len(p[row])):
      if (Z == colors[row][column]):
        q[row].append(p[row][column] * sensor_right)
      else:
        q[row].append(p[row][column] * (1-sensor_right))
  s = 0
  for k in q:
      s +=sum(k)

  for row in range(len(q)):
    for column in range(len(q[row])):
      q[row][column] = q[row][column] / s

  return q

def move(p, U):
  q = []
  for row in range(len(p)):
    q.append([])

    for column in range(len(p[row])):
      s = p_move * p[(row-U[0]) % len(p)][(column-U[1]) % len(p[row])]
      s = s + (1-p_move) * p[row % len(p)][(column) % len(p[row])]
      q[row].append(s)
  return q

for i in range(len(motions)):
  p = move(p,motions[i])
  p = sense(p,measurements[i])

#Your probability array must be printed
#with the following code.

show(p)
