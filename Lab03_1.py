#Lab03_2a

for i in range (1,7,1):
    for j in range(1,(i+1),1):
        print j,
        
    print ""
    
print "------------------------"

#Lab03_2b
for i in range (8,1,-1):
    for j in range(1,(i-1),1):
        print j,
        
    print " "

#Lab03_2c
for i in range (1,7,1):
    for k in range (7-i,1,-1):
        print" ",
    for j in range(i,0,-1):
        print j,
    print " "

print "-------------------------"

#Lab03_2d
for i in range (7,0,-1):
    for k in range(7-i,0,-1):
        print " ",
    for j in range (1,i,1):
        print j,
    print ""

#Lab03_2e
for i in range (1,7,1):
    for k in range (7-i,1,-2):
        print" ",
    for j in range(i,0,-1):
        print j,
    print " "
