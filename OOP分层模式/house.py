"""
说明：数据层：House类，一个house对象表示一个房屋信息
"""


class House:

    def __init__(self, id, name, phone, address, rent, state):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
        self.rent = rent
        self.state = state
        # 构造方法不能有返回值

    # 重写__str__ 按照指定的格式输出对象
    def __str__(self):
        return f"{self.id}\t\t{self.name}\t\t{self.phone}\t\t{self.address}\t\t{self.rent}\t\t{self.state}"
