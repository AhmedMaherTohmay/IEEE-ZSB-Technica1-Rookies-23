import os

def climbingLeaderboard(ranked, player) :
    l = list(set(ranked))        # deleting duplicates by using set method then sorting and reversing
    l.sort()
    l.reverse()
    li = []
    c = len(l) - 1
    for i in (player):
        b = 1
        for j in range(c, -1, -1): # comparing player with oter ranks 
            if i < l[j]:
                c = j
                b = 0
                break
        if(b == 1): 
            li.append(1)    # appending his rank
        elif(b == 0):
           li.append(j + 2)
    return li

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # just getting input

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
