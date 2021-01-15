# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 13:14:23 2021

"""

import cv2			#	OpenCVライブラリ
import numpy as np		#	Numpyライブラリ
import random
import copy

def fall(windowName,img,img_copy,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball,disp_time,save_flag,img_num):
    loop = 0
    while True:
        flag_moved = False
        
        for gyou in range(12):
            if gyou%2 == 0:
                for retu in range(0,19,2):       #0,2,4,::::18 を流す
                    if ball[gyou][retu] != 0:    #動かそうとしている玉自体が存在することの確認
                        
                        if retu == 0:
                            a_flag = False       #壁なので動けない
                        else:
                            if ball[gyou][retu-2]  != 0:
                                a_flag = False
                            else:
                                a_flag = True    #動ける
                                
                        if retu == 18:
                            d_flag = False       #壁なので動けない
                        else:
                            if ball[gyou][retu+2]  != 0:
                                d_flag = False
                            else:
                                d_flag = True    #動ける
                            
                        if retu == 0 or gyou == 0:
                            b_flag = False       #壁または床なので動けない
                        else:
                            if ball[gyou-1][retu-1]  != 0:
                                b_flag = False
                            else:
                                b_flag = True
                                
                        if retu == 18 or gyou == 0:
                            c_flag = False       #壁または床なので動けない
                        else:
                            if ball[gyou-1][retu+1]  != 0:
                                c_flag = False
                            else:
                                c_flag = True
                                
                        if b_flag == True and c_flag == False and a_flag == True:
                            #b　方向に動かす
                            ball[gyou-1][retu-1] = ball[gyou][retu]
                            ball[gyou][retu] = 0                       #動かした後は空にしておく
                            flag_moved = True
                            retu_moved = retu
                            gyou_moved = gyou
                            retu_moved_to = retu-1
                            gyou_moved_to = gyou-1
                            
                            #描画する
                            disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化
            
                            cv2.imshow(windowName,img)
                            if save_flag == 1:
                                cv2.imwrite('data/'+str(img_num)+'.jpg',img)
                                img_num = img_num+1
                                
                            img = copy.deepcopy(img_copy)
                            key = cv2.waitKey(disp_time)
                            break
                            
                        if c_flag == True and b_flag == False and d_flag == True:
                            #c　方向に動かす
                            ball[gyou-1][retu+1] = ball[gyou][retu]
                            ball[gyou][retu] = 0                       #動かした後は空にしておく
                            flag_moved = True
                            retu_moved = retu
                            gyou_moved = gyou
                            retu_moved_to = retu+1
                            gyou_moved_to = gyou-1
                            
                            #描画する
                            disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化
            
                            cv2.imshow(windowName,img)
                            if save_flag == 1:
                                cv2.imwrite('data/'+str(img_num)+'.jpg',img)
                                img_num = img_num+1
                            img = copy.deepcopy(img_copy)
                            key = cv2.waitKey(disp_time)
                            break
                                
                        if b_flag == True and c_flag == True:
                            #b,cどちらかに動かす
                            hoge = random.randint(0,1)
                            if hoge == 0:
                                #b　方向に動かす
                                ball[gyou-1][retu-1] = ball[gyou][retu]
                                ball[gyou][retu] = 0                       #動かした後は空にしておく
                                flag_moved = True
                                retu_moved = retu
                                gyou_moved = gyou
                                retu_moved_to = retu-1
                                gyou_moved_to = gyou-1
                                
                                #描画する
                                disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化
                
                                cv2.imshow(windowName,img)
                                if save_flag == 1:
                                    cv2.imwrite('data/'+str(img_num)+'.jpg',img)
                                    img_num = img_num+1
                                img = copy.deepcopy(img_copy)
                                key = cv2.waitKey(disp_time)
                                break
                            else:
                                 #c　方向に動かす
                                ball[gyou-1][retu+1] = ball[gyou][retu]
                                ball[gyou][retu] = 0                       #動かした後は空にしておく
                                flag_moved = True
                                retu_moved = retu
                                gyou_moved = gyou
                                retu_moved_to = retu+1
                                gyou_moved_to = gyou-1
                                
                                #描画する
                                disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化
                
                                cv2.imshow(windowName,img)
                                if save_flag == 1:
                                    cv2.imwrite('data/'+str(img_num)+'.jpg',img)
                                    img_num = img_num+1
                                img = copy.deepcopy(img_copy)
                                key = cv2.waitKey(disp_time)
                                break
                            
            if gyou%2 == 1:  #奇数行
                for retu in range(1,18,2):   #1,3,5,::::17 を流す
                    if ball[gyou][retu] != 0:    #動かそうとしている玉自体が存在することの確認
                        if retu == 1:
                            a_flag =True       #壁はあるが，偶数行とは違い動ける
                        else:
                            if ball[gyou][retu-2]  != 0:
                                a_flag = False
                            else:
                                a_flag = True    #動ける
                                
                        if retu == 17:
                            d_flag = True       #壁はあるが，偶数行とは違い動ける
                        else:
                            if ball[gyou][retu+2]  != 0:
                                d_flag = False
                            else:
                                d_flag = True    #動ける
                            
                        if gyou == 0:
                            b_flag = False       #壁または床なので動けない
                        else:
                            if ball[gyou-1][retu-1]  != 0:
                                b_flag = False
                            else:
                                b_flag = True
                        
                        if gyou == 0:
                            c_flag = False       #壁または床なので動けない
                        else:
                            if ball[gyou-1][retu+1]  != 0:
                                c_flag = False
                            else:
                                c_flag = True
                                
                        if b_flag == True and c_flag == False and a_flag == True:
                            #b　方向に動かす
                            ball[gyou-1][retu-1] = ball[gyou][retu]
                            ball[gyou][retu] = 0                       #動かした後は空にしておく
                            flag_moved = True
                            retu_moved = retu
                            gyou_moved = gyou
                            retu_moved_to = retu-1
                            gyou_moved_to = gyou-1
                            
                            #描画する
                            disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化
            
                            cv2.imshow(windowName,img)
                            if save_flag == 1:
                                cv2.imwrite('data/'+str(img_num)+'.jpg',img)
                                img_num = img_num+1
                            img = copy.deepcopy(img_copy)
                            key = cv2.waitKey(disp_time)
                            break
                            
                        if c_flag == True and b_flag == False and d_flag == True:
                            #c　方向に動かす
                            ball[gyou-1][retu+1] = ball[gyou][retu]
                            ball[gyou][retu] = 0                       #動かした後は空にしておく
                            flag_moved = True
                            retu_moved = retu
                            gyou_moved = gyou
                            retu_moved_to = retu+1
                            gyou_moved_to = gyou-1
                            
                            #描画する
                            disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化
            
                            cv2.imshow(windowName,img)
                            if save_flag == 1:
                                cv2.imwrite('data/'+str(img_num)+'.jpg',img)
                                img_num = img_num+1
                            img = copy.deepcopy(img_copy)
                            key = cv2.waitKey(disp_time)
                            break
                                
                        if b_flag == True and c_flag == True:
                            """
                            追加変更
                            aにあるとき　c
                            dにあるとき b
                            どちらにもない，あるとき　ランダム
                            """
                            if a_flag == True :
                                if d_flag == True:
                                    #どちらにもない
                                    #b,cどちらかに動かす
                                    hoge = random.randint(0,1)
                                else:
                                    #d のみある -> b
                                    hoge = 0
                            else:
                                if d_flag == True:
                                    #a　のみある　-> c
                                    hoge = 1
                                else:
                                    #どちらにもある
                                    #b,cどちらかに動かす
                                    hoge = random.randint(0,1)
                                
                            if hoge == 0:
                                #b　方向に動かす
                                ball[gyou-1][retu-1] = ball[gyou][retu]
                                ball[gyou][retu] = 0                       #動かした後は空にしておく
                                flag_moved = True
                                retu_moved = retu
                                gyou_moved = gyou
                                retu_moved_to = retu-1
                                gyou_moved_to = gyou-1
                                
                                #描画する
                                disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化
                
                                cv2.imshow(windowName,img)
                                if save_flag == 1:
                                    cv2.imwrite('data/'+str(img_num)+'.jpg',img)
                                    img_num = img_num+1
                                img = copy.deepcopy(img_copy)
                                key = cv2.waitKey(disp_time)
                                break
                            else:
                                 #c　方向に動かす
                                ball[gyou-1][retu+1] = ball[gyou][retu]
                                ball[gyou][retu] = 0                       #動かした後は空にしておく
                                flag_moved = True
                                retu_moved = retu
                                gyou_moved = gyou
                                retu_moved_to = retu+1
                                gyou_moved_to = gyou-1
                                
                                #描画する
                                disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化
                
                                cv2.imshow(windowName,img)
                                if save_flag == 1:
                                    cv2.imwrite('data/'+str(img_num)+'.jpg',img)
                                    img_num = img_num+1
                                img = copy.deepcopy(img_copy)
                                key = cv2.waitKey(disp_time)
                                break
                            
                if flag_moved == True:
                    break             #次の行には行かず，(0,0)から探索しなおす
                            
        if flag_moved == False:  #一つも動かなかった
            break
    
    
def disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball):
        
    thick = -1        
    ball_size = 16  #半径
    
    #枠表示
    LD_edge = (50,50)  #座標方向がこれのみ，左下原点
    
    LU_edge = (LD_edge[0],home_height - LD_edge[1] - int(11*1.73205*ball_size)-2*ball_size)
    RD_edge = (LD_edge[0] + 20*ball_size,home_height - LD_edge[1])
    cv2.rectangle(img, LU_edge, RD_edge, (255, 0, 0))
    
    for gyou in range(12):
        if gyou%2 == 0:
            for retu in range(0,19,2):       #0,2,4,::::18 を流す
                if ball[gyou][retu] != 0:    #動かそうとしている玉自体が存在することの確認
                    x = ball_size + ball_size *retu
                    y = ball_size + int(1.73205*ball_size*gyou)
                    cv2.circle(img,x_y(home_height,x,y,LD_edge), ball_size, Color_ball(ball[gyou][retu]),thickness=thick ) 
                
                
        if gyou%2 == 1:  #奇数行
            for retu in range(1,18,2):   #1,3,5,::::17 を流す
                if ball[gyou][retu] != 0:    #動かそうとしている玉自体が存在することの確認
                    x = ball_size*2 + ball_size *(retu-1)
                    y = ball_size + int(1.73205*ball_size*gyou)
                    cv2.circle(img,x_y(home_height,x,y,LD_edge), ball_size, Color_ball(ball[gyou][retu]), thickness=thick) 
            
    
    
    #ボールセット表示
    if flag_triangle == True:  #三角
        x=(ball_x+1)*ball_size
        y=ball_size + int(1.73205*ball_size*ball_y)
        
        cv2.circle(img,x_y(home_height,x,y,LD_edge), ball_size, Color_ball(now_ball[0]), thickness=thick)
        cv2.circle(img,x_y(home_height,x+2*ball_size,y,LD_edge), ball_size, Color_ball(now_ball[1]), thickness=thick)
        cv2.circle(img,x_y(home_height,x+ball_size,y+int(1.73205*ball_size),LD_edge), ball_size, Color_ball(now_ball[2]), thickness=thick)
    
    else:#逆三角の時は　一番下基準
        x=(ball_x+1)*ball_size
        y=ball_size + int(1.73205*ball_size*ball_y)
        
        cv2.circle(img,x_y(home_height,x,y,LD_edge), ball_size, Color_ball(now_ball[0]), thickness=thick)
        cv2.circle(img,x_y(home_height,x+ball_size,y+int(1.73205*ball_size),LD_edge), ball_size, Color_ball(now_ball[1]), thickness=thick)
        cv2.circle(img,x_y(home_height,x-ball_size,y+int(1.73205*ball_size),LD_edge), ball_size, Color_ball(now_ball[2]), thickness=thick)
        
    
    #ネクストボールセット表示
    next_ball_position = [50,50]
    cv2.circle(img,(next_ball_position[0],next_ball_position[1]), ball_size, Color_ball(next_ball[0]), thickness=thick) 
    cv2.circle(img,(next_ball_position[0]+2*ball_size,next_ball_position[1]), ball_size, Color_ball(next_ball[1]), thickness=thick) 
    cv2.circle(img,(next_ball_position[0]+ball_size,next_ball_position[1]-int(ball_size * 1.732)), ball_size, Color_ball(next_ball[2]), thickness=thick) 
    
def x_y(home_height,x,y,origin):
    """
    座標系の変換をする，
    originは　左下原点，上yとして
    """
    x_return = origin[0] + x
    y_return = home_height -(origin[1]+y)
    
    return (x_return,y_return)

def Color_ball(hoge):
    if hoge == 1:
        return (0,0,255)
    if hoge == 2:
        return (255,0,0)
    if hoge == 3:
        return (0,255,0)
    if hoge == 4:
        return (0,255,255)
    if hoge == 5:
        return (255,255,255)
    if hoge == 6:
        return (255,255,0)
    if hoge == 7:
        return (0,0,0)
    
    return (0,0,128)


if __name__=="__main__":

    ball=[[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
          [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
          [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
          [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
          [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
          
    
          [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],[0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0]]

    """
    行偶数　：　列偶数
    行奇数　：　列奇数
    ball[行][列]
    """
    
    ball[0][0]=1
    ball[0][2]=3
    ball[0][4]=3
    ball[2][0]=2
    ball[2][2]=4
    ball[2][4]=3
    
    ball[1][5]=3
    ball[0][6]=4
    # ball[2][2]=5
    # ball[2][4]=6
    
    # ball[8][4] = 2
    
    windowName = "game_home"
    cv2.namedWindow(windowName)
    
    img = cv2.imread('BackGround.jpg' )
    img_copy = copy.deepcopy(img)
    cv2.imshow(windowName,img)
    
    home_height,home_width,chanel = img.shape
    
    color_num = 5         #色の数
    
    next_ball = [random.randint(1,color_num+1),random.randint(1,color_num+1),random.randint(1,color_num+1)]
    flag_triangle =False  #逆三角形:False
    ball_x = 10           #逆三角　なら　一番下　　　　三角なら，左下　の玉の座標
    ball_y = 12
    now_ball =[random.randint(1,color_num+1),random.randint(1,color_num+1),random.randint(1,color_num+1)]    
    #逆三角なら　下から反時計回り，　三角なら　左下から反時計回り
    
    disp_time = 1000
    
    disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)
    
    save_flag = 1  #1:保存する
    img_num = 1
    
    cv2.imshow(windowName,img)
    if save_flag == 1:
        cv2.imwrite('data/'+str(img_num)+'.jpg',img)
        img_num = img_num+1
    img = copy.deepcopy(img_copy)
    
    fall(windowName,img,img_copy,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball,disp_time,save_flag,img_num)
    
    
    cv2.destroyAllWindows()