#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A是一維List, 請撰寫一個function 名叫*get_num_lager_five* 來找出比5大的數字
#
# Input: 一維List, 裡面元素皆為整數
# Output: 一維List, 裡面的元素皆為大於5的整數
def get_num_lager_five(numbers):
    x = []   
    for i in numbers:
        if i > 5:
            x.append(i)
    print x 

A = [5,6,7]

get_num_lager_five(A)
