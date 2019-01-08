import multiprocessing
import time
k = 0

def spawn():
  global k
  k +=1
  if k == 1:
    for i in range(5):
      print('test!{}{}'.format(i,k))
      time.sleep(.1)
  elif k == 2:
    for i in range(5):
      print('test!{}{}'.format(i,k))
      time.sleep(1)

  elif k == 3:
    for i in range(5):
      print('test!{}{}'.format(i,k))
      time.sleep(.3)



if __name__ == '__main__':
  k = 0
  for i in range(3):
    p = multiprocessing.Process(target=spawn)
    p.start()
