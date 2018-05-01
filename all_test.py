#! /usr/bin python3
# _*_ coding:utf-8 _*_
# author: hujiaming


def test1():
    number = 0
    number_list = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and j != k and i != k:
                    number += 1
                    number_list.append([i, j, k])
    print("个数为：", number)
    print("分别为：", number_list)


def test2():
    while True:  # 使用循环+异常保证输入的是数字
        try:
            profit = int(input("please input profit: "))
        except Exception as e:
            print("请输入正确的数字格式！")
        else:
            break
    profit_range = [1000000, 600000, 400000, 200000, 100000, 0]
    bonus_percent = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    profit1 = profit  # 防止改变父级变量
    for i in range(0, 6):
        if profit1 > profit_range[i]:
            print("the bonus is:", (profit1 - profit_range[i]) * bonus_percent[i])
            profit1 = profit_range[5]  # 保证判断只执行一次


def test3():
    import math
    num = 1
    up = int(input("请输入所求数的个数："))
    while True:
        if math.sqrt(num + 100) - int(math.sqrt(num + 100)) == 0 and math.sqrt(num + 268) - int(math.sqrt(num + 268)) == 0:
            print(num)
            num += 1
        if num >= up:
            break

def test4():
    """
    题目：输入某年某月某日，判断这一天是这一年的第几天？
    """
    import time
    import calendar
    year = int(input("year:"))
    month = int(input("month:"))
    day = int(input("day:"))
    print(time.localtime(calendar.timegm((year, month, day, 0, 0, 0)))[7])


def test5():
    """
    题目：输入三个整数x,y,z，请把这三个数由小到大输出。
    """
    list5 = []
    for index in range(0, 3):
        num = int(input("第{0}个数：".format(index + 1)))
        list5.append(num)
    list5.sort()
    for j in list5:
        print(j, end=" ")


def test6():
    """
    题目：输出9*9口诀
    """
    for index in range(1, 10):
        for j in range(1, index+1):
            print("{0} * {1} =".format(index, j), index*j, end="   ")
        print()


def test7():
    """
    古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
    假如兔子都不死，问每个月的兔子总数为多少？
    """
    day = int(input("请输入月份数："))
    print("第{0}月的兔子总数：".format(day), pow(2, int((day + 1) / 2)))


def test8(num1, num2):
    """
    判断num1与num2之间有多少个素数，并输出所有素数。
    """
    from math import sqrt
    num = [2, 3, 5, 7]
    for index in range(num1, num2):
        if (sqrt(index) != int(sqrt(index))) and (index % 2 != 0) and (index % 3 != 0) and (index % 5 != 0) and (
                index % 7 != 0):
            #  这个地方的判断条件虽然多，但是程序的时间复杂度与空间复杂度比起双重循环都较低
            num.append(index)
    print("素数个数：", len(num))
    for i in num:
        print(i, end="  ")
    print("\n")
    return num


def test9():
    """
    打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
    例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
    """
    for index in range(100,1000):
        hun = index // 100   # // 运算符表示取商
        ten = (index - hun * 100) // 10
        num = index - hun * 100 - ten * 10
        if pow(hun, 3) + pow(ten, 3) + pow(num, 3) == index:
            print(index, end=" ")


def test10():
    """
    将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
    """
    n = int(input("请输入一个整数："))
    print("{0} = ".format(n), end="")
    while n != 1:
        for i in range(2, n+1):
            if n % i == 0:
                n //= i
                if n == 1:
                    print(i)
                else:
                    print("{} * ".format(i), end="")
                break


def test11():
    pass


if __name__ == '__main__':
    name = []
    for i in range(1, 101):
        name.append("test{0}".format(i))
    while True:
        try:
            text = input("请输入题号或命令：")
            if text == "break":
                break
            else:
                test_index = int(text)
                print("将执行", name[test_index-1])
                eval(name[test_index-1])()
        except Exception as e:
            print("error: ", e)
        else:
            print("退出请输入 break ")
