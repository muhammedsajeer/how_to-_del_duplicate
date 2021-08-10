#Write a python program to find duplicate characters in a string?
import collections
str = 'thequickbrownfoxjeeumpsvrtthooohlazydg'
d = collections.defaultdict(int)
for c in str:
   d[c] +=1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))