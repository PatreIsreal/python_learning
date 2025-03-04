while True:
    try:
        # 获取用户输入的正方形边长
        n = int(input())

        # 循环打印每一行
        for row in range(n):
            if row == 0 or row == n-1:
                # 第一行和最后一行打印完整的“*”
                print("*" * n)
            else:
                # 中间行打印“*”加空格再加“*”
                print("*" + " " * (n-2) + "*")
    except:
        break

        