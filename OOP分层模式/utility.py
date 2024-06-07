"""
说明：工具类：将工具方法写到这里
"""


class Utility:
    @staticmethod
    def read_confirm_select():
        """
        确认用户输入的是(Y/N),不区分大小写
        如果用户输入的不是Y/N 就反复输入
        :return:
        """
        print("请输入你的选择(Y/N),请确认选择:", end="")
        while True:
            key = input()
            if key.lower() == 'y' or key.lower() == 'n':
                break
            else:
                print("选择错误，请重新输入：", end="")
        return key.lower()
