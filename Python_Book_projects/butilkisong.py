# -*- coding: cp866 -*-


word = "���뫮�"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "���� � 誠��")
    print(beer_num, word, "����")
    print("���쬨 ����")
    print("���� �� ����")
    if beer_num == 1:
        print("����� ��� ���뫮� ���� � 誠��")
    else:
        new_num = beer_num-1
        if new_num >= 11 and new_num <= 19:
            word = "���뫮�"
        else:
            if new_num % 10 == 1:
                word = "���뫪�"
            elif new_num % 10 in (2, 3, 4):
                word = "���뫪�"
            else:
                word = "���뫮�"
        print(new_num, word, "���� � 誠��")
    print()
