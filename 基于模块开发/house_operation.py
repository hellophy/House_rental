"""
说明：提供对房屋的各种操作
"""
from my_tools import *


# 显示主菜单，让用户选择

def main_menu():
    """
    显示主菜单，让用户选择
    :return: 
    """
    print()
    print("房屋出租系统菜单".center(32, "="))
    print("\t\t\t1 新 增 房 源")
    print("\t\t\t2 查 找 房 屋")
    print("\t\t\t3 删 除 房 屋 信 息")
    print("\t\t\t4 修 改 房 屋 信 息")
    print("\t\t\t5 房 屋 列 表")
    print("\t\t\t6 退      出")


# 显示房屋列表

# 全部变量 即 houses ，存放所有的房屋信息
# 为了测试方便，放一个测试数据到改列表
houses = [{"id": 1, "name": "tim", "phone": "113", "address": "北京", "rent": 800, "state": "未出租"}]


def list_houses():
    """
    显示房屋列表
    :return:
    """
    print("房屋列表".center(60, "="))
    # 打印表头
    print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态（未出租/已出租）")
    # 遍历houses这个列表
    # house就是一个字典{"id":2, "name":"tim","phone":"113","address":"北京","rent":800,"state":"未出租"}
    for house in houses:
        # 取出house的values,并进行遍历显示
        for value in house.values():
            print(value, end="\t\t")
        # 输出一个完整的house信息后，换行
        print()
    print("房屋列表显示完毕".center(60, "="))


# 添加房屋信息

# 全局变量id_counter 记录当前房屋的id
id_counder = 1


def add_house():
    """
    添加房屋信息
    :return:
    """
    print("添加房屋".center(32, "="))
    name = input("姓名：")
    phone = input("电话：")
    address = input("地址：")
    rent = int(input("月租："))
    state = input("状态：")
    # 由系统分配添加的房屋id
    global id_counder
    id_counder += 1
    id = id_counder
    # 构建房屋信息对应的字典，加入到全局houses列表
    house = {"id": id, "name": name, "phone": phone,
             "address": address, "rent": rent, "state": state}
    houses.append(house)
    print("添加房屋成功".center(32, "="))


# 删除房屋信息

def del_house():
    """
    根据id删除房屋信息
    :return:
    """
    print("删除房屋信息".center(32, "="))
    del_id = int(input("请输入待删除房屋的编号（-1退出）："))
    if del_id == -1:
        print("放弃删除房屋信息".center(32, "="))
        return

    # 让用户确认删除(Y/N) ,如果输入的不是Y/N，就一直提示输入
    # while True:
    #     key = input("请输入你的选择(Y/N),请确认选择:")
    #     if key.lower() == 'y' or key.lower() == 'n':
    #         break
    choice = read_confirm_select()

    if choice == 'y':  # 如果真的要删除
        # 根据del_id 去houses列表查找是否存在该房屋[字典]
        house = find_by_id(del_id)
        if house:
            # 执行删除
            houses.remove(house)
            print("删除房屋信息成功".center(32, "="))
        else:
            print("房屋编号不存在，删除失败..".center(32, "="))
    else:
        print("放弃删除房屋信息".center(32, "="))


def find_by_id(find_id):
    """
    根据输入的find_id返回对应的房屋信息(字典)，如果没有就返回None
    :param find_id:
    :return:
    """
    # 遍历houses列表
    for house in houses:
        if house["id"] == find_id:
            return house
    # 如果没有return ，默认就是返回None
    # return None


# 退出

def exit_sys():
    """
    退出系统
    :return:
    """
    # print("请输入你的选择(Y/N),请确认选择:")
    choice = read_confirm_select()
    if choice == 'y':
        return True
    else:
        return False


# 根据id查找房屋信息功能

def find_house():
    """
    根据id查找房屋信息功能
    :return:
    """
    print("查找房屋信息".center(32, "="))
    houes_id = int(input("请输入你要查询的房屋的id值："))
    house = find_by_id(houes_id)
    if house:
        print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态（未出租/已出租）")
        for value in house.values():
            print(value, end="\t\t")
        print()
    else:
        print(f"查找房屋信息id {houes_id}不存在")


def update():
    """
    修改房屋信息
    :return:
    """
    update_id = int(input("请选择要修改的房屋编号（-1表示退出）："))
    if update_id == -1:
        print("你以放弃修改房屋信息".center(32, "="))
        return
    # 根据id查找对应的房屋信息(字典)
    house = find_by_id(update_id)
    if not house:
        print("没有要修改的房屋信息".center(32, "="))
        return
    # # 注意： 如果用户直接回车，表示不修改当前这个信息，保留原来的值
    # name = input(f"姓名({house['name']})：")
    # if len(name) > 0:  # 如果用户输入的有内容
    #     # 表示将接收到的name 赋给house字典 key="name" 对应的值
    #     house['name'] = name
    house['name'] = read_str(f"姓名({house['name']}):", house['name'])
    house['phone'] = read_str(f"电话({house['phone']}):", house['phone'])
    house['address'] = read_str(f"地址({house['address']}):", house['address'])
    house['rent'] = int(read_str(f"租金({house['rent']}):", house['rent']))
    house['state'] = read_str(f"状态({house['state']}):", house['state'])
    print("修改房屋信息成功".center(32, "="))