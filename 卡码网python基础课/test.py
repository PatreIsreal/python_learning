# 先输入要输入字符串的行数
n = int(input())

# 遍历输入字符串s
for _ in range(n):
    s = input()
    # 创建哈希表，这里一定要将这行代码写在for循环内部，不然会影响其他行的结果
    # 正确的应该是每处理一行的结果再重新清空列表中的数值进行下一次的遍历
    temp = [0] * 26
    for char in s:
        # 找出是哪个字母
        number = ord(char) - ord('a')
        # 对应的频次加一
        temp[number] = temp[number] + 1

    # 找出最高频次是多少
    maxFreq = max(temp)
    
    # 找出所有出现频次等于最高频次的字母
    max_freq_chars = []
    for i in range(26):
        if temp[i] == maxFreq:
            max_freq_chars.append(chr(ord('a') + i))
    
    # 将所有最高频次字母连接成字符串输出
    res = ''.join(max_freq_chars)
    print(res)
