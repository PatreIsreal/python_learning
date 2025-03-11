class Node:
    def __init__(self, data):
        self.data = data  # 存储节点数据
        self.next = None  # 指向下一个节点，初始为None

class LinkList:
    def __init__(self):
        self.head_node = None  # 头节点，初始为None
        self.length = 0  # 链表长度，初始为0

    def insert(self, data):
        self.length += 1  # 链表长度加1
        new_code = Node(data)  # 创建新节点
        if self.head_node is None:  # 如果链表为空
            self.head_node = new_code  # 新节点作为头节点
            return self.head_node  # 返回头节点

        current_node = self.head_node  # 从头节点开始遍历
        while current_node.next is not None:  # 遍历到链表末尾
            current_node = current_node.next  # 移动到下一个节点

        current_node.next = new_code  # 将新节点连接到链表末尾
        return new_code  # 返回新插入的节点

    def print_link_list(self):
        current_node = self.head_node  # 从头节点开始遍历
        while current_node is not None:  # 当节点不为空时继续遍历
            if current_node.next is not None:  # 如果不是最后一个节点
                print(current_node.data, end=" ")  # 打印数据并用空格分隔
            else:
                print(current_node.data)  # 打印最后一个节点的数据并换行
            current_node = current_node.next  # 移动到下一个节点

while True:
    try:
        n = int(input())  # 读取一个整数n（实际未使用）
        elements = list(map(int, input().split()))  # 读取一行整数并转换为列表
    except:
        break  # 如果输入结束或出错，退出循环

    link_list = LinkList()  # 创建一个新链表

    for data in elements:  # 遍历输入的整数列表
        link_list.insert(data)  # 将每个整数插入到链表中

    link_list.print_link_list()  # 打印整个链表
