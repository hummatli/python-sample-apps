
print "if else operator ------------------------"
x, y = 10, 100

if (x < y):
    st = 'x is less than y'
elif (x == y):
    st = 'x is equal y'
else:
    st = 'x is greater than y'
print st


#Without braces
if x < y:
    st = 'x is less than y'
elif x == y:
    st = 'x is equal y'
else:
    st = 'x is greater than y'
print st

print "canditional statements-----------------------"
st = "x is less than y" if (x < y) else "x is greater than y"
print st