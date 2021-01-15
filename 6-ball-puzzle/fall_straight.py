# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:02:08 2021

"""
import cv2			#	OpenCVライブラリ
import copy
import random


from fall import disp_ball
from fall import fall

def fall_straight(windowName,img,img_copy,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball,disp_time,save_flag,img_num,start_x,start_y,color_num):
    """
    衝突するまで直線落下させる．
    """
    if flag_triangle == True:    #三角の落下
        flag_fall = 0   #0:衝突無し　　1：真下 2：左　3右 4:左右にある
        """
        衝突まで直線落下
        """
        while True:
            if ball_y == 0:
                break             #床についている
                
            else:
                if ball_x > 0:
                    if ball[ball_y-1][ball_x-1] !=0:  #左下にある
                        flag_fall = 1
                        break
                    
                if ball[ball_y-1][ball_x] !=0:    #左真下にある
                    flag_fall = 2
                    break
                    
                if ball[ball_y-1][ball_x+1] !=0:  #中央にある
                    flag_fall = 3
                    break
                    
                if ball[ball_y-1][ball_x+2] != 0:  #右真下にある
                    flag_fall = 4
                    break
                    
                if ball_x < 16:
                    if ball[ball_y-1][ball_x+3] !=0:  #右下にある
                        flag_fall = 5
                        break
                    
                    
            if flag_fall == 0:
                ball_y=ball_y -1

                #描画する
                disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化
                if save_flag == 1:
                    cv2.imwrite('data/'+str(img_num)+'.jpg',img)
                    img_num = img_num+1
                cv2.imshow(windowName,img)
                img = copy.deepcopy(img_copy)
                cv2.waitKey(disp_time)
           
                
        """
        衝突状態で場合わけ
        0:床　　　　　　　　　　　-> 状態により　0.5左右どちらかにずらす
        1:真下           -> 　0.5左右どちらかにずらす
        2,3:右下or左下    ->何もせず固定
        """       
        if flag_fall == 0 or flag_fall == 2 or flag_fall == 4 :
            if ball_y %2 == 0:
                if ball_x %2 != 0: #0.5個ずれている． エラーが出ないよう，とりあえずずらしておく
                    if ball_x>=9:
                        ball_x =ball_x -1
                    else:
                        ball_x = ball_x + 1
            else:
                if ball_x %2 == 0: #0.5個ずれている． エラーが出ないよう，とりあえずずらしておく
                    if ball_x>=9:
                        ball_x =ball_x -1
                    else:
                        ball_x = ball_x + 1
                
            
            ball[ball_y][ball_x] = now_ball[0]
            ball[ball_y][ball_x+2] = now_ball[1]
            ball[ball_y+1][ball_x+1] = now_ball[2]
        
        elif flag_fall == 1 or flag_fall == 3 or flag_fall == 5:
            ball[ball_y][ball_x] = now_ball[0]
            ball[ball_y][ball_x+2] = now_ball[1]
            ball[ball_y+1][ball_x+1] = now_ball[2]
        
    
    elif flag_triangle == False: #逆三角
        flag_fall = 0     #0:衝突無し　　1：真下 2：左　3右 4:左右にある
        """
        衝突まで直線落下
        """
        while True:
            if ball_y == 0:
                break             #床についている
                
            else:
                
                if (ball_y-1)%2 == 0:        #偶数行　　，偶数列にある
                    if ball_x %2 ==0:        #偶数列にボールがある，下にあるか確認
                        if ball[ball_y-1][ball_x] !=0:  #下にある
                            flag_fall = 1
                            break
                    else:                    #奇数列にボールがある，右下・左下にあるか確認
                       
                        if ball[ball_y-1][ball_x-1] !=0:  #左下にある
                            if ball[ball_y-1][ball_x+1] !=0: #右下にもある
                                flag_fall = 4
                                break
                            else:
                                flag_fall = 2
                                break                            
                        else:
                            if ball[ball_y-1][ball_x+1] !=0: #右下にある
                                flag_fall = 3
                                break
                            
                else:                        #奇数行 ,奇数列にボールがある
                    if ball_x %2 ==1:        #奇数列にボールがある，下にあるか確認
                        if ball[ball_y-1][ball_x] !=0:  #下にある
                            flag_fall = 1
                            break
                    
                    else:                    #偶数列にボールがある，右下・左下にあるか確認
                       
                        if ball[ball_y-1][ball_x-1] !=0:  #左下にある
                            if ball[ball_y-1][ball_x+1] !=0: #右下にもある
                                flag_fall = 4
                                break
                            else:
                                flag_fall = 2
                                break                            
                        else:
                            if ball[ball_y-1][ball_x+1] !=0: #右下にある
                                flag_fall = 3
                                break
                        
            if flag_fall == 0:
                ball_y=ball_y -1

                #描画する
                disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化

                cv2.imshow(windowName,img)
                if save_flag == 1:
                    cv2.imwrite('data/'+str(img_num)+'.jpg',img)
                    img_num = img_num+1
                img = copy.deepcopy(img_copy)
                cv2.waitKey(disp_time)
                
        """
        衝突状態で場合わけ
        0:床　　　　　　　　　　　-> 状態により　0.5左右どちらかにずらす
        1:真下           -> 　0.5左右どちらかにずらす
        2,3:右下or左下    ->何もせず固定
        """
        if flag_fall == 0:     #衝突無しでwhile ループを抜けた　->床についている
            if ball_x %2 != 0: #床についているが0.5個ずれている． エラーが出ないよう，とりあえずずらしておく
                if ball_x>=9:
                    ball_x =ball_x -1
                else:
                    ball_x = ball_x + 1
            
            ball[ball_y][ball_x] = now_ball[0]
            ball[ball_y+1][ball_x+1] = now_ball[1]
            ball[ball_y+1][ball_x-1] = now_ball[2]
        
        elif flag_fall == 1:  #真下にある．　0.5個ずれ　エラーが出ないよう，とりあえずずらしておく
            if ball_x>=9:
                ball_x =ball_x -1
            else:
                ball_x = ball_x + 1
            
            ball[ball_y][ball_x] = now_ball[0]
            ball[ball_y+1][ball_x+1] = now_ball[1]
            ball[ball_y+1][ball_x-1] = now_ball[2]
        
        elif flag_fall == 2 or flag_fall == 3 or flag_fall == 4: #左　または　右　にある．　特に何も考えず，固定                
            
            ball[ball_y][ball_x] = now_ball[0]
            ball[ball_y+1][ball_x+1] = now_ball[1]
            ball[ball_y+1][ball_x-1] = now_ball[2]
            

    #描画する
    disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)  #ball map,now ball, next ball 描画を関数化
    if save_flag == 1:
        cv2.imwrite('data/'+str(img_num)+'.jpg',img)
        img_num = img_num+1
    cv2.imshow(windowName,img)
    img = copy.deepcopy(img_copy)
    cv2.waitKey(disp_time)
            
    """
    次のボールの生成
    """
    now_ball = next_ball
    next_ball = [random.randint(1,color_num+1),random.randint(1,color_num+1),random.randint(1,color_num+1)]
    flag_triangle =False  #逆三角形:False
    ball_x = start_x            #逆三角　なら　一番下　　　　三角なら，左下　の玉の座標
    ball_y = start_y
    
    return img_num,now_ball,next_ball,flag_fall
    

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
    
    # ball[0][0]=1
    # ball[0][2]=3
    # ball[0][4]=3
    # ball[2][0]=2
    # ball[2][2]=4
    # ball[2][4]=3
    
    # ball[1][5]=3
    # ball[0][6]=4
    # ball[2][2]=5
    # ball[2][4]=6
    
    # ball[8][4] = 2
    
    ball[0][8] = 1
    
    windowName = "game_home"
    cv2.namedWindow(windowName)
    
    img = cv2.imread('BackGround.jpg' )
    img_copy = copy.deepcopy(img)
    cv2.imshow(windowName,img)
    
    home_height,home_width,chanel = img.shape
    
    color_num = 5         #色の数
    
    next_ball = [random.randint(1,color_num+1),random.randint(1,color_num+1),random.randint(1,color_num+1)]
    flag_triangle =True  #逆三角形:False
    start_x = 9
    start_y = 12    
    ball_x = start_x           #逆三角　なら　一番下　　　　三角なら，左下　の玉の座標
    ball_y = start_y
    
    now_ball =[random.randint(1,color_num+1),random.randint(1,color_num+1),random.randint(1,color_num+1)]    
    #逆三角なら　下から反時計回り，　三角なら　左下から反時計回り
    
    disp_time = 500
    
    disp_ball(img,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball)
    
    save_flag = 1  #1:保存する 0:保存しない dataファイルに保存される
    img_num = 1    #保存名称用変数
    
    cv2.imshow(windowName,img)
    if save_flag == 1:
        cv2.imwrite('data/'+str(img_num)+'.jpg',img)
        img_num = img_num+1
    img = copy.deepcopy(img_copy)
    
    
    img_num,now_ball,next_ball,flag_fall = fall_straight(windowName,img,img_copy,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball,disp_time,save_flag,img_num,start_x,start_y,color_num)
    
    
    print(flag_fall)
    print(ball)
    
    fall(windowName,img,img_copy,ball,home_height,flag_triangle,ball_x,ball_y,next_ball,now_ball,disp_time,save_flag,img_num)
    
    cv2.destroyAllWindows()