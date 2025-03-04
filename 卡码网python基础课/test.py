while True:
    try:
        N = int(input())
        i = 0
        for i in range(N):
            data = int(input()).split()
            if N == 0:
                break
            res = sum(data)
            print(res)
    
    except:
        break