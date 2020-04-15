#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：陈求真
日期：4/15/2020
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(choice_name):
    """
    将游戏对象对应到不同的整数
    """
    if choice_name=="石头":
        player_choice_number=0
    elif choice_name=="史波克":
        player_choice_number=1
    elif choice_name=="纸":
        player_choice_number=2
    elif choice_name=="蜥蜴":
        player_choice_number=3
    elif choice_name=="剪刀":
        player_choice_number=4
    return(player_choice_number)
    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果


def number_to_name(computer_choice_number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if computer_choice_number==0:
        computer_choice_name="石头"
    elif computer_choice_number==1:
        computer_choice_name="史波克"
    elif computer_choice_number==2:
        computer_choice_name="纸"
    elif computer_choice_number==3:
        computer_choice_name="蜥蜴"
    elif computer_choice_number==4:
        computer_choice_name="剪刀"
    return(computer_choice_name)
	
    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果


def rpsls(choice_name):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    
    player_choice_number=name_to_number(choice_name)# 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    computer_choice_number=random.randint(0,4)# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    computer_choice_name=number_to_name(computer_choice_number)# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    print("计算机的选择为%s"%computer_choice_name)# 在屏幕上显示计算机选择的随机对象

    if player_choice_number==0:
        if computer_choice_number==1 or computer_choice_number==2:
            print("计算机赢了")
        elif computer_choice_number==3 or computer_choice_number==4:
            print("您赢了")
        else:
            print("您和计算机出的一样呢")
    if player_choice_number==1:
        if computer_choice_number==2 or computer_choice_number==3:
            print("计算机赢了")
        elif computer_choice_number==0 or computer_choice_number==4:
            print("您赢了")
        else:
            print("您和计算机出的一样呢")
    if player_choice_number==2:
        if computer_choice_number==3 or computer_choice_number==4:
            print("计算机赢了")
        elif computer_choice_number==0 or computer_choice_number==1:
            print("您赢了")
        else:
            print("您和计算机出的一样呢")
    if player_choice_number==3:
        if computer_choice_number==0 or computer_choice_number==4:
            print("计算机赢了")
        elif computer_choice_number==1 or computer_choice_number==2:
            print("您赢了")
        else:
            print("您和计算机出的一样呢")
    if player_choice_number==4:
        if computer_choice_number==0 or computer_choice_number==1:
            print("计算机赢了")
        elif computer_choice_number==2 or computer_choice_number==3:
            print("您赢了")
        else:
            print("您和计算机出的一样呢")
    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”



# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("请输入您的选择:")# 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
choice_name=input()
print("----------------")# 输出"-------- "进行分割
while choice_name!="石头" and choice_name!="史波克" and choice_name!="纸" and choice_name!="蜥蜴" and choice_name!="剪刀":
	print("Error: No Correct Name")
	print("try again")
	choice_name=input()
rpsls(choice_name)


