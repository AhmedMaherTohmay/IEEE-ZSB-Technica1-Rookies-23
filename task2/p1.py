import random 
num = str(random.choice(range(000,999))).zfill(3) 
print(num)
print('Enter a 3 digit number ')
hit=0  
miss=0 
attempts=1
while True:
    hit = 0
    miss = 0
    guess = str(input())
    if(guess == num):
        print("Right Guess after", attempts ,"attempts")
        break
    for i in range(3):
        if(guess[i] == num[i]):
            hit += 1
        elif (guess[i] in num):
            miss += 1
    attempts += 1
    print(hit, "hit" ,miss, "miss")
    