
try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)
except IOError as e:
    print("Error : {}", e)
except:
    print("Error 2: {}", e)
print("After error") 

