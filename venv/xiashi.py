for i in range(4):
    for j in range(i+1):
        if j<=3:
            print('%s=%s'%(j+1,i-j),end = ' ')