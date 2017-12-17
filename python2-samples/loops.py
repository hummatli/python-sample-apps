x = 0
#while loop
print "while loop -------------"
while x < 5 :
    print x
    x = x + 1


#for loop
print "for loop -------------"
for x in range(5, 10): #10 daxil olmur, sonuncu 9 olur
    print x

print "for loop with collection-------------"
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for d in days:
    print (d)

#break
print "break and continue-------------"
for x in range(5, 10): #10 daxil olmur, sonuncu 9 olur
    #if (x == 7): break
    if (x % 2 == 0): continue
    print x

print "Use enumerate() to get index od item-------------"
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for i, d in enumerate(days):
    print i, d