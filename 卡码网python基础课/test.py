while True:
    try:
        N = int(input())
        for i in range(N):
            inputs = input().split()
            M = int(inputs[0])
            total = 0
            for j in range(M):
                total += int(inputs[j+1])
            print(total)
        
        if i < N-1:
            print()
    except:
        break