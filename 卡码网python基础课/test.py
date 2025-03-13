# Shape类
class Shape:
    def __init__(self, shape_type):
        self.type = shape_type
     
    def calculate_area(self):
        pass
#  Rectangle类，包含 width 和 height, 计算面积的方法
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
 
    def calculate_area(self):
        return self.width * self.height
# Circle类，包含 radius, 计算面积的方法 
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
 
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
         
shapes = []
 
while True:
    data = input().split()
    shape_type = data[0]
    # 处理输出
    if shape_type == "end":
        break

    if shape_type == "rectangle":
        # 获取输入的width/height, 将之转换成整数
        width, height = int(data[1]), int(data[2])
        # 新建一个对象，append到列表中
        shapes.append(Rectangle(width, height))
    elif shape_type == "circle":
        # 获取输入的radius, 将之转换成整数
        radius = int(data[1])
        # 新建一个对象，append到列表中
        shapes.append(Circle(radius))
 
for shape in shapes:
    # 不同类别的对象调用同一个方法，有不同的处理逻辑
    print(f"{shape.type} area: {shape.calculate_area():.2f}")