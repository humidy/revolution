# -*-coding:utf-8 -*-

"""
记录一些数学规律，用程序中的过程来模拟规律的判断
"""


# 将一个整数的每个位数上的数字打散并依次存入一个列表中，由低位到高位存储
def number_to_list(number):
    """
    :param number:
    :return:
    """
    # 利用列表来存储整数的每个位数的值，从个位开始依次类推
    # 321 -> [1,2,3]
    number_list = list()
    # 判断输入的数是否是整数
    if not isinstance(number, int):
        raise "输入的数字需要时整数"
    # 获取这个整数的绝对值，避免负数的情况
    number = abs(number)
    while number > 0:
        number_list.append(number % 10)
        number = int(number / 10)

    return number_list


def list_to_number(number_list):
    """
    :param number_list:
    :return:
    """
    # 配套number_to_list函数，将列表中的数值还原成原来的整数
    number = 0
    digital = 0
    # 开始生成原来的整数
    for each_number in number_list:
        number += each_number * (10 ** digital)
        digital += 1

    return number


def divided_by_int(number):
    """
    :param number:
    :return:
    """
    number_list = number_to_list(number)
    # 规则一：能被2和5整除的数
    # 如果一个数的末一位数能被2和5整除，这个数就能被2和5整除
    # 获取整数的个位数，用first_digital来表示
    first_digital = number_list[0]
    if first_digital % 2 == 0:
        print("[整除规律]：可以被2整除")

    if first_digital % 5 == 0:
        print("[整除规律]：可以被5整除")

    # 规则二：能被3和9整除的数
    # 一个数各个数位上的数的和能被3或9整除，这个数就能被3或9整除。
    sum_digital = 0
    for each_digital in number_list:
        sum_digital += each_digital
    if sum_digital % 3 == 0:
        print("[整除规律]：可以被3整除")

    if sum_digital % 9 == 0:
        print("[整除规律]：可以被9整除")

    # 规则三：能被4和25整除的数
    # 一个数的末两位数能被4或25整除，这个数就能被4或25整除。
    len_digital = len(number_list)
    if len_digital == 1:
        last_2_digital = number_list[0]
    else:
        last_2_digital = 10 * number_list[1] + number_list[0]

    if last_2_digital % 4 == 0:
        print("[整除规律]：可以被4整除")

    if last_2_digital % 25 == 0:
        print("[整除规律]：可以被25整除")

    # 规则四：能被8和125整除的数
    # 一个数的末三位数能被8或125整除，这个数就能被8或125整除
    # 这里用last_3_digital来存储这个数的末三位数
    if len_digital == 1:
        last_3_digital = number_list[0]
    elif len_digital == 2:
        last_3_digital = 10 * number_list[1] + number_list[0]
    else:
        last_3_digital = 100 * number_list[2] + 10 * number_list[1] + number_list[0]

    if last_3_digital % 8 == 0:
        print("[整除规律]：可以被8整除")

    if last_3_digital % 125 == 0:
        print("[整除规律]：可以被125整除")

    # 规则五：能被7、11和13整除的数
    # 一个数末三位数字所表示的数与末三位以前的数字所表示的数的差（以大减小），能被7、11、13整除，这个数就能被7、11、13整除。
    if len_digital == 1:
        last_3_digital = number_list[0]
        other_digital = 0
        subtraction_digital = last_3_digital - other_digital
    elif len_digital == 2:
        last_3_digital = 10 * number_list[1] + number_list[0]
        other_digital = 0
        subtraction_digital = last_3_digital - other_digital
    elif len_digital == 3:
        last_3_digital = 100 * number_list[2] + 10 * number_list[1] + number_list[0]
        other_digital = 0
        subtraction_digital = last_3_digital - other_digital
    else:
        digital = 0
        last_3_digital = 0
        other_digital = 0
        for each_digital in number_list:
            if digital < 3:
                last_3_digital += each_digital * (10 ** digital)
            else:
                other_digital += each_digital * (10 ** (digital - 3))
            digital += 1
        subtraction_digital = abs(last_3_digital - other_digital)
        print(last_3_digital, other_digital, subtraction_digital)

    if subtraction_digital % 7 == 0:
        print("[整除规律]：能被7整除")
    if subtraction_digital % 11 == 0:
        print("[整除规律]：能被11整除")
    if subtraction_digital % 13 == 0:
        print("[整除规律]：能被13整除")


if __name__ == "__main__":
    divided_by_int(1158)
