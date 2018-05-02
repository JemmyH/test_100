#! /usr/bin python3
# _*_ coding:utf-8 _*_
# author: hujiaming
# filename:all_test.py
# python_version: 3.5.2


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
    """
    利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
    """
    score = int(input("请输入分数："))
    if score >= 90:
        print("A")
    elif score >= 60:
        print("B")
    else:
        print("C")


def test12():
    """
    输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
    """
    import string
    word = 0
    space = 0
    number = 0
    str = input("请随便输入一行字符：")
    for index in range(0, len(str) - 1):
        if str[index].isalpha():
            word += 1
        if str[index].isdigit():
            number += 1
        if str[index].isspace():
            space += 1
    print("英文字母个数：", word)
    print("数字个数： ", number)
    print("空格个数： ", space)
    print("其他：", len(str) - word - number - space)


def test13():
    """
    求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
    例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
    """
    s = 0
    a = int(input("请输入基数a："))
    times = int(input("请输入相加的个数："))
    for index in range(1,times + 1):
        s += int(str(a) * index)
    print(s)


def test14():
    """
    一个数如果恰好等于它的因子之和，这个数就称为“完数”。
    例如6=1＋2＋3.编程找出1000以内的所有完数。
    """
    for j in range(1,1001):
        prime = []
        sum = 0
        for index in range(2, j + 1):
            if j % index == 0:
                prime.append(int(j / index))
        for i in range(0,len(prime)):
            sum += prime[i]
        if sum == j:
            print(j)


def test15():
    """
    一球从100米高度自由落下，每次落地后反跳回原高度的一半；
    再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
    """
    n = int(input("请输入次数："))
    print("第{0}次落地共经过了".format(n), 300 - 100 * pow(1/2, n - 2), "米")
    print("第{0}次反弹".format(n), 100 * pow(1/2, n), "米")


def test16():
    """
    猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
    第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。
    到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
    """
    # 第一种方法：常规方法，使用高中数学数列知识可以推导；设第i天剩了ai个桃子，那么容易得知（ai+2）是一个公比为1/2的等比数列，根据a9=1求出a0即可
    a = 1
    for i in range(9,0,-1):
        a = (a+1) * 2
    print(a)
    # 第二种方法：使用位运算符。这个老牛逼了……
    n = 1
    for i in range(9,0,-1):
        n = (n + 1) << 1  # n<<k 表示在n的二进制中加k个0
    print(n)


def test17():
    """
    两个乒乓球队进行比赛，各出三人。
    甲队为a,b,c三人，乙队为x,y,z三人。
    已抽签决定比赛名单。
    有人向队员打听比赛的名单:a说他不和x比，c说他不和x,z比。
    请编程序找出三队赛手的名单
    """
    jia = ['a', 'b', 'c']
    yi = ['x', 'y', 'z']
    for i in range(0,3):
        for j in range(0,3):
            if ((i == 0) and (j == 0) or (i == 2 and j ==0 ) or (i ==2 and j == 2)):
                continue
            else:
                print(jia[i], "<---->", yi[j])


def test18():
    """
    打印出如下图案（菱形）
    *
   ***
  *****
 *******
  *****
   ***
    *
    """
    a = '*'
    for i in range(1, 9, 2):
        print((a * i).center(7, " "))
    for j in range(5, -1, -2):
        print((a * j).center(7, " "))


def test19():
    """
    有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
    """
    sum = 0.0
    for i in range(1, 21):
        sum += (2 * i - 1 / i)
    print(sum)


def test20():
    """
    求1+2!+3!+...+20!的和
    """
    def rec(i):
        if i == 0 or i == 1:
            return 1
        else:
            return i * rec(i -1)
    sum = 0
    for i in range(1,21):
        sum += rec(i)
    print(sum)


def test22():
    """
    利用递归方法求5!。
    """
    def rec(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * rec(n - 1)
    print(rec(5))


def test23():
    """
    利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
    """
    def rec(str, l):
        if l == 0:
            return
        else:
            print(str[l-1])
            rec(str, l -1)

    str = input("请输入5个字符：")
    rec(str, len(str))


def test24():
    """
    有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
    问第4个人岁数，他说比第3个人大2岁。
    问第三个人，又说比第2人大两岁。
    问第2个人，说比第一个人大两岁。
    最后 问第一个人，他说是10岁。
    请问第五个人多大？
    """
    a = 10
    for i in range(1, 5):
        a += 2
    print(a)


def test25():
    """
    给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
    """
    num = input("请输入一个不多于五位的正整数：")
    chin = ['个', '十', '百', '千', '万']
    nu = []
    for i in range(0, len(num)):
        nu.append(num[i])
    if num.isdigit():
        print("位数：", len(nu))
        for i in range(0, len(nu)):
            print("{}为数字是".format(chin[i]), nu[len(nu) - i - 1])
    else:
        print("你输入的不是正整数!")


def test26():
    """
    一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
    """
    num = input("请输入一个五位数：")
    if num[0] == num[4] and num[1] == num[3]:
        print("这个数是回文数")
    else:
        print("非回文数！")


def test27():
    """
    筛选法求100之内的素数
    这个算法贼6！！！！
    """
    a = [0] * 101
    for i in range(2,11):
        for j in range(i + i, 101 ,i):
            a[j] = -1
    for i in range(2, 101):
        if a[i] != -1:
            print(i, end=",")


def test28():
    """
    对十个数排序
    """
    num = input("请输入一个十位数：")
    list = []
    for i in range(0, len(num)):
        list.append(num[i])
    list.sort()
    j = ""
    print(j.join(list))


def test29():
    """
    求一个3*3矩阵对角线元素之和
    """
    matrix = []
    sum = 0
    for i in range(0,3):
        print("请输入第{0}行元素,输入一个确认一个".format(i+1))
        b = 0
        a = input("第{0}行第{1}个元素".format(i+1, b+1))
        c = input("第{0}行第{1}个元素".format(i+1, b+2))
        d = input("第{0}行第{1}个元素".format(i+1, b+3))
        matrix.append([a, c, d])
    for j in range(0,3):
        sum += int(matrix[j][j])
    print(sum)


def test30():
    """
    有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
    """
    list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("已有数组：",list)
    num = int(input("请输入一个数："))
    for i in range(0, len(list)):
        if num <= list[i]:
            list.insert(i,num)
            num = list[len(list) -1]
    print(list)


def test31():
    
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
