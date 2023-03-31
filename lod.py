import os,time

# 백준 별찍기 19
def print_star(x,y):
    s = ""
    star = 0
    for i in range(x):
        star = 1 - star
        s += "*" if star else " "
    for i in range(y+y-1):
        s += "*" if x%2==0 else " "
    for i in range(x):
        star = 1 - star
        s += " " if star else "*"
    s += "\n"
    return s

def loding():
    for n in range(4):
        n = (n*2)-1
        result = ""
        for i in range(n,0,-1): result += print_star(n-i,i)
        for i in range(2,n+1,1): result += print_star(n-i,i)
        os.system('cls')
        print(result)
        time.sleep(0.3)
    for n in range(4,0,-1):
        n = (n*2)-1
        result = ""
        for i in range(n,0,-1): result += print_star(n-i,i)
        for i in range(2,n+1,1): result += print_star(n-i,i)
        os.system('cls')
        print(result)
        time.sleep(0.3)
