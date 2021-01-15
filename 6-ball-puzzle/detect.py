# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:51:41 2021

"""

import cv2			#	OpenCVライブラリ
import copy
import random


def detect_hex(ball):
    """
    ヘキサゴンの検出
    返り値は　色番号
    """
    flag_hex = False
    hex_color = 100
    
    for start_y in range(0,10,1):  # 0,1,2,3,4,~,8,9 まで　　
        if start_y%2 == 0:         #偶数行　　偶数行と奇数行で分割
        
            for start_x in range(2,17,2):  #2,4,6,~,14,16まで
                hoge = ball[start_y][start_x]
                if hoge != 0:
                    if ball[start_y+1][start_x-1] == hoge:
                        if ball[start_y+2][start_x] == hoge:
                            if ball[start_y+2][start_x+2] == hoge:
                                if ball[start_y+1][start_x+3] == hoge:
                                    if ball[start_y][start_x+2] == hoge:
                                        print("hex !!!!!!")
                                        flag_hex = True
                                        hex_color = hoge
                                        break
        else:
            for start_x in range(1,16,2):  #1,3,5,~,13,15まで
                hoge = ball[start_y][start_x]
                if hoge != 0:
                    if ball[start_y+1][start_x-1] == hoge:
                        if ball[start_y+2][start_x] == hoge:
                            if ball[start_y+2][start_x+2] == hoge:
                                if ball[start_y+1][start_x+3] == hoge:
                                    if ball[start_y][start_x+2] == hoge:
                                        print("hex !!!!!!")
                                        flag_hex = True
                                        hex_color = hoge
                                        break
        if flag_hex == True:
            return hex_color
        else:
            return 100  #ダミー

def detect_pyramid(ball):
    """
    ピラミッドの検出
    返り値は　色番号
    """
    flag_pyr = False
    pyr_color = 100
    
    for start_y in range(0,10,1):  # 0,1,2,3,4,~,8,9 まで　　
        if start_y%2 == 0:         #偶数行　　偶数行と奇数行で分割
        
            for start_x in range(0,15,2):  #0,2,4,6,~,14まで
                hoge = ball[start_y][start_x]
                if hoge != 0:
                    if ball[start_y][start_x+2] == hoge:
                        if ball[start_y][start_x+4] == hoge:
                            if ball[start_y+1][start_x+1] == hoge:
                                if ball[start_y+1][start_x+3] == hoge:
                                    if ball[start_y+2][start_x+2] == hoge:
                                        print("pyramid !!!!!!")
                                        flag_pyr = True
                                        pyr_color = hoge
                                        break
        else:
            for start_x in range(1,14,2):  #1,3,5,~,13まで
                hoge = ball[start_y][start_x]
                if hoge != 0:
                    if ball[start_y][start_x+2] == hoge:
                        if ball[start_y][start_x+4] == hoge:
                            if ball[start_y+1][start_x+1] == hoge:
                                if ball[start_y+1][start_x+3] == hoge:
                                    if ball[start_y+2][start_x+2] == hoge:
                                        print("pyramid !!!!!!")
                                        flag_pyr = True
                                        pyr_color = hoge
                                        break
        if flag_pyr == True:
            return pyr_color
        else:
            return 100  #ダミー
        
def detect_7ball(ball):
    color = []
    
    checked_origin=\
            [[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
             [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
             [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
             [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
             [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
             [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0]]     #検索済みは1にする
    
    ball7_flag = False
    
    for start_y in range(0,12,1):  # 0,1,2,3,4,~,8,12 まで　　
        if start_y%2 == 0:         #偶数行　　偶数行と奇数行で分割
            for start_x in range(0,19,2):  #0,2,4,6,~,18まで
                hoge = ball[start_y][start_x]
                if hoge != 0:
                    checked=copy.deepcopy(checked_origin)
                    same=\
                        [[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
                         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
                         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
                         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
                         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
                         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0]]
                    same[start_y][start_x] = 1   
                    num = serch(ball,hoge,checked,same,start_x,start_y,0)
                    
                    if num>=7:
                        checked_origin = copy.deepcopy(same)
                        ball7_flag = True
                        print("7ball!!!!")
                        color.append(hoge)
        
        else:
            for start_x in range(1,18,2):  #1,3,5,~,17まで
                hoge = ball[start_y][start_x]
                if hoge != 0:
                    checked=copy.deepcopy(checked_origin)
                    same=\
                        [[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
                         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
                         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
                         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
                         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
                         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0]]
                    same[start_y][start_x] = 1   
                    num = serch(ball,hoge,checked,same,start_x,start_y,0)
                    
                    if num>=7:
                        checked_origin = copy.deepcopy(same)
                        ball7_flag = True
                        print("7ball!!!!")
                        color.append(hoge)
                    
    return ball7_flag,color
    
def serch(ball,color,checked,same,start_x,start_y,num):
    """
    6方向探索する
    検索した場所は checkedを1にする
    
    再帰的に検索する
    """
    
    if checked[start_y][start_x] == 0:
        
        checked[start_y][start_x] = 1
        
        if ball[start_y][start_x] == color and ball[start_y][start_x] != 0:
            num = num + 1
            
            if start_x > 1:         
                if ball[start_y][start_x-2] == color:
                    same[start_y][start_x-2] = 1
                    num = serch(ball,color,checked,same,start_x-2,start_y,num)
                    
            if start_x > 0 and start_y <=10:
                if ball[start_y+1][start_x-1] == color:
                    same[start_y+1][start_x-1] = 1
                    num = serch(ball,color,checked,same,start_x-1,start_y+1,num)
                    
            if start_x <=17 and start_y <= 10:
                if ball[start_y+1][start_x+1] == color:
                    same[start_y+1][start_x+1] = 1
                    num = serch(ball,color,checked,same,start_x+1,start_y+1,num)
                    
            if start_x<=9:
                if ball[start_y][start_x+2] == color:
                    same[start_y][start_x+2] = 1
                    num = serch(ball,color,checked,same,start_x+2,start_y,num)
                    
            if start_x<=10 and start_y >= 1:
                if ball[start_y-1][start_x+1] == color:
                    same[start_y-1][start_x+1] = 1
                    num = serch(ball,color,checked,same,start_x+1,start_y-1,num)
                    
            if start_x>=1 and start_y >= 1:
                if ball[start_y-1][start_x-1] == color:
                    same[start_y-1][start_x-1] = 1
                    num = serch(ball,color,checked,same,start_x-1,start_y-1,num)
                    
            return num
        
        else:
            return num #変更せず　に戻る
    
    else:
        return num  #変更せず　に戻る
            
    

    
    
def erase(color,ball):
    """
    colorと同色の玉の消去
    """
    for gyou in range(12):
        if gyou%2 == 0:
            for retu in range(0,19,2):       #0,2,4,::::18 を流す
                if ball[gyou][retu] == color:   
                    ball[gyou][retu] = 0
                
                
        if gyou%2 == 1:  #奇数行
            for retu in range(1,18,2):   #1,3,5,::::17 を流す
                if ball[gyou][retu] == color:   
                    ball[gyou][retu] = 0

    

if __name__=="__main__":
    
    ball=[[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
         
   
         [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0]]
    
    """
    #hex
    ball[0][2] = 1
    ball[0][4] = 1
    ball[2][2] = 1
    ball[2][4] = 1
    ball[1][1] = 1
    ball[1][5] = 1
    """
    #pyramid
    ball[0][2] = 1
    ball[0][4] = 1
    ball[0][6] = 1
    ball[1][3] = 1
    ball[1][5] = 1
    ball[2][4] = 1
    
    ball[0][8] = 1
    
    color= detect_hex(ball)
    print(color)
    
    color= detect_pyramid(ball)
    print(color)
    
    flag,color= detect_7ball(ball)
    print(color)
    print(flag)
    
   