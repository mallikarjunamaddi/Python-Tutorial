T=int(input())
result = []

def getGitList(l, N):
    giftList = [1]
    g = 1
    for j in range(0, N-1):
        if(l[j]<l[j+1]):
            g+=1
        elif(l[j]>l[j+1]):
            g-=1
        else:
            g=1
        giftList.append(g)        
    return giftList


for i in range(T):
    N=int(input())
    l=list(map(int,input().split(" ")))
    giftList = getGitList(l, N)
    smallestGiftCount = min(giftList)
    if(smallestGiftCount>0):
        result.append(sum(giftList))
    else:
        normalizeValue = 1 - smallestGiftCount
        result.append(sum(giftList)+(normalizeValue*N))

print(*result, sep="\n")    


#  2
#  5
#  1 2 1 5 2
#  2
#  1 2  
      
# 5 3 2 1
# 1 0 -1 1
# 3 2  1 3
# 2 5 3 1
# 1 2 1 0
# 2 3 2 1
  
# 2 3 2 1
# 2 1 2 3
# 2  1  2 3

# 5 2 3 5 -q
# 1 0 1 2
# 2 1 2  3

# x x-1 x+1 x+2 => 4x+2
# x+1  x-2  x-1   x 4x-2
# 1 0 -1 -2
# -2  -1  0    1 

#  4a+2 = 4b-2

#  4a-4b = -4

#  b - a = 1

#  a = b+1
#  a-1 = b-2

# a-b =1
# a-b = -3

# a-b=-1

# 4a+2 = y
# 4b-2 = y
# 4a+4b = 2y
# 2a+2b=y