# Uses python3
import sys

def segments(starts,ends):
  d = []
  for i in range(len(starts)):
    d.append([starts[i],ends[i]])
  d.sort()
  return d

def fast_count_segments(starts, ends, points):
  seg = segments(starts,ends)
  p = sorted(points)
  counter = [0]*len(points)
  n = 0
  for i in range(len(points)):
    cnx = 0
    for j in range(n,len(seg)):
      if (seg[j][0] <= p[i]) and (p[i] <= seg[j][1]):
        cnx += 1
        n += 1
      else:
        break
    inx = points.index(p[i])
    counter[inx] = cnx
  return counter

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')