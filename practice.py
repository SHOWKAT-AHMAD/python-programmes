"""import random 
cards = ["king","queen","jack","ace"]
random.shuffle(cards)
for card in cards:
    print(card) """
#import statistics
#print(statistics.mean([100,30,24,90,8]))
# sys.argv:provides list that have been typen in promt. line;
#argv: list of strings;
#import sys
#print("hello my name is ",sys.argv[1])
"""import sys
if len(sys.argv)<2:
    sys.exit("too few arguments")
elif len(sys.argv)>2:
    sys.exit("too many arguments")
print("hello my name is ",sys.argv[1])"""
import sys
if len(sys.argv)<2:
    sys.exit("too few arguments")
for arg in sys.argv[1:]:
    print("hello my name is",arg)