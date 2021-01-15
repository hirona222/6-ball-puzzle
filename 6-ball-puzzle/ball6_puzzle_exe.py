# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:05:39 2021

"""


import cv2			#	OpenCVライブラリ
import copy
import random


from fall import disp_ball
from fall import fall
from fall_straight import fall_straight

from detect import detect_hex
from detect import detect_pyramid
from detect import detect_7ball
from detect import erase

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
    
    
    windowName = "game_home"
    cv2.namedWindow(windowName)
    
    img = cv2.imread('BackGround.jpg' )
    img_copy = copy.deepcopy(img)
    cv2.imshow(windowName,img)
    
    home_height,home_width,chanel = img.shape
    
    """
    初期設定
    """
    
    color_num = 5         #色の数
    
    next_ball = [random.randint(1,color_num+1),random.randint(1,color_num+1),random.randint(1,color_num+1)]
    flag_triangle =True  #逆三角形:False
    start_x = 9
    start_y = 12    
    ball_x = start_x           #逆三角　なら　一番下　　　　三角なら，左下　の玉の座標
    ball_y = start_y
    
    now_ball =[random.randint(1,color_num+1),random.randint(1,color_num+1),random.randint(1,color_num+1)]    
    #逆三角なら　下から反時計回り，　三角なら　左下から反時計回り
    
    disp_time = 100
    
    disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)
    
    save_flag = 1  #1:保存する 0:保存しない dataファイルに保存される
    img_num = 1    #保存名称用変数
    
    cv2.imshow(windowName,img)
    if save_flag == 1:
        cv2.imwrite('data/'+str(img_num)+'.jpg',img)
        img_num = img_num+1
    img = copy.deepcopy(img_copy)
    
    """
    ゲーム開始
    """
    while True:
        
        #ゲーム画面表示
        disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)
        cv2.imshow(windowName,img)
        img = copy.deepcopy(img_copy)
        
        #キーボード入力処理
        key = cv2.waitKey(100)
        
        if key == ord('q'):                 #       end 処理
            break
        
        elif key == ord ('a'):             #左60deg回転
            print("L_rotate")
            if flag_triangle == True:  #三角形
                flag_triangle = False
                #now_ballはそのまま
                ball_x = ball_x + 1
                
            else:                      #逆三角
                flag_triangle = True
                now_ball = [now_ball[2],now_ball[0],now_ball[1]]
                ball_x = ball_x - 1
                
                
        elif key == ord ('s'):             #右60deg回転
            print("R_rotate")
            if flag_triangle == True:  #三角形
                flag_triangle = False
                now_ball = [now_ball[1],now_ball[2],now_ball[0]]
                ball_x = ball_x + 1
                
            else:                      #逆三角
                flag_triangle = True
                #now_ballはそのまま
                ball_x = ball_x - 1
        
        elif key == ord ('w'):             #右60deg回転
            print("rotate")
            if flag_triangle == True:  #三角形
                flag_triangle = False
                
                
            else:                      #逆三角
                flag_triangle = True
                
                
            
        elif key == ord ('j'):             #左0.5移動
            print("L_move")
            if flag_triangle == True:
                if ball_x != 0:
                    ball_x = ball_x -1
            elif flag_triangle == False:
                if ball_x != 1:
                    ball_x = ball_x -1
                
        elif key == ord ('l'):             #右0.5移動
        
            print("R_move")
            if flag_triangle == True:
                if ball_x != 16:
                    ball_x = ball_x +1
            elif flag_triangle == False:
                if ball_x != 17:
                    ball_x = ball_x +1
                
        elif key == ord ('k'):             #落下
            print("fall")
            #直線落下
            img_num,now_ball,next_ball,flag_fall = fall_straight(windowName,img,img_copy,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball,disp_time,save_flag,img_num,start_x,start_y,color_num)
            
            #ボールセット崩し
            fall(windowName,img,img_copy,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball,disp_time,save_flag,img_num)
            
            #ヘキサゴン検出
            color_hex = detect_hex(ball)
            if color_hex != 100:
                #描画する
                disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化
                cv2.putText(img,'Hexagon !!!!!!!!',(300,300),cv2.FONT_HERSHEY_PLAIN,2.0,(255,0,0))
                if save_flag == 1:
                    cv2.imwrite('data/'+str(img_num)+'.jpg',img)
                    img_num = img_num+1
                cv2.imshow(windowName,img)
                img = copy.deepcopy(img_copy)
                cv2.waitKey(disp_time)
                
            #ピラミッド検出            
            color_pyramid = detect_pyramid(ball)
            if color_pyramid != 100:
                #描画する
                disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化
                cv2.putText(img,'Pyramid !!!!!!!!',(300,300),cv2.FONT_HERSHEY_PLAIN,2.0,(255,0,0))
                if save_flag == 1:
                    cv2.imwrite('data/'+str(img_num)+'.jpg',img)
                    img_num = img_num+1
                cv2.imshow(windowName,img)
                img = copy.deepcopy(img_copy)
                cv2.waitKey(disp_time)
                
            
            # 7 ball 検出
            flag,color_7= detect_7ball(ball)
            if flag == True and color_pyramid == 100 and color_hex == 100:
                #描画する
                disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化
                cv2.putText(img,'7 balls',(300,300),cv2.FONT_HERSHEY_PLAIN,2.0,(255,0,0))
                if save_flag == 1:
                    cv2.imwrite('data/'+str(img_num)+'.jpg',img)
                    img_num = img_num+1
                cv2.imshow(windowName,img)
                img = copy.deepcopy(img_copy)
                cv2.waitKey(disp_time)
            
            #削除
            for i in color_7:
                erase(i,ball)
            disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化
            if save_flag == 1:
                cv2.imwrite('data/'+str(img_num)+'.jpg',img)
                img_num = img_num+1
            cv2.imshow(windowName,img)
            img = copy.deepcopy(img_copy)
            cv2.waitKey(disp_time)
            
            #落下
            fall(windowName,img,img_copy,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball,disp_time,save_flag,img_num)
            
            
    cv2.destroyAllWindows()