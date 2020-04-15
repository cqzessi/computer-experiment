#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�4/15/2020
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(choice_name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if choice_name=="ʯͷ":
        player_choice_number=0
    elif choice_name=="ʷ����":
        player_choice_number=1
    elif choice_name=="ֽ":
        player_choice_number=2
    elif choice_name=="����":
        player_choice_number=3
    elif choice_name=="����":
        player_choice_number=4
    return(player_choice_number)
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


def number_to_name(computer_choice_number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if computer_choice_number==0:
        computer_choice_name="ʯͷ"
    elif computer_choice_number==1:
        computer_choice_name="ʷ����"
    elif computer_choice_number==2:
        computer_choice_name="ֽ"
    elif computer_choice_number==3:
        computer_choice_name="����"
    elif computer_choice_number==4:
        computer_choice_name="����"
    return(computer_choice_name)
	
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��


def rpsls(choice_name):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    
    player_choice_number=name_to_number(choice_name)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    computer_choice_number=random.randint(0,4)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    computer_choice_name=number_to_name(computer_choice_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    print("�������ѡ��Ϊ%s"%computer_choice_name)# ����Ļ����ʾ�����ѡ����������

    if player_choice_number==0:
        if computer_choice_number==1 or computer_choice_number==2:
            print("�����Ӯ��")
        elif computer_choice_number==3 or computer_choice_number==4:
            print("��Ӯ��")
        else:
            print("���ͼ��������һ����")
    if player_choice_number==1:
        if computer_choice_number==2 or computer_choice_number==3:
            print("�����Ӯ��")
        elif computer_choice_number==0 or computer_choice_number==4:
            print("��Ӯ��")
        else:
            print("���ͼ��������һ����")
    if player_choice_number==2:
        if computer_choice_number==3 or computer_choice_number==4:
            print("�����Ӯ��")
        elif computer_choice_number==0 or computer_choice_number==1:
            print("��Ӯ��")
        else:
            print("���ͼ��������һ����")
    if player_choice_number==3:
        if computer_choice_number==0 or computer_choice_number==4:
            print("�����Ӯ��")
        elif computer_choice_number==1 or computer_choice_number==2:
            print("��Ӯ��")
        else:
            print("���ͼ��������һ����")
    if player_choice_number==4:
        if computer_choice_number==0 or computer_choice_number==1:
            print("�����Ӯ��")
        elif computer_choice_number==2 or computer_choice_number==3:
            print("��Ӯ��")
        else:
            print("���ͼ��������һ����")
    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�



# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("����������ѡ��:")# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
choice_name=input()
print("----------------")# ���"-------- "���зָ�
while choice_name!="ʯͷ" and choice_name!="ʷ����" and choice_name!="ֽ" and choice_name!="����" and choice_name!="����":
	print("Error: No Correct Name")
	print("try again")
	choice_name=input()
rpsls(choice_name)


