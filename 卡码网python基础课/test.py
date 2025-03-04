while True:
    try:
        n = int(input())
        for i in range(n):
            line = list(map(int,input().split()))
        print(line[-1:1:0])
        print(line[0:2:-1])
    
    except:
        break