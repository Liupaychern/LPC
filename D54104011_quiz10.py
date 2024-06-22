import pygame
from pygame import mixer
import random, math, os
import string

pygame.mixer.pre_init(44100,-16,2,512)
mixer.init()    # 初始化音樂撥放
pygame.init()

# 視窗設定
screen_width = 700
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock() # 時間控制

# 讀取儲存檔案
with open(os.path.join('file','save.txt'),'r') as file:
    SCORE_SAVE = file.readlines()


# 音效設定
dead_sound = pygame.mixer.Sound(os.path.join('music','dead_sound.wav'))
dead_sound.set_volume(0.3)
eat_sound = pygame.mixer.Sound(os.path.join('music','eat_sound.wav'))
eat_sound.set_volume(0.43)

pygame.mixer.music.load(os.path.join('music','background_music.mp3'))
pygame.mixer.music.play(-1,0)
pygame.mixer.music.set_volume(0.5)  

# 變數
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,87)
PINK = (255,140,250)
GREEN_BLUE = (10,209,139)
GREY = (150,150,150)
GREY2 = (130,130,130)
DARK_YELLOW = (228,128,16)

FPS = 15
score = 0

# 蛇設定 (頭、身體還會在主畫面設定初始化)
snake_size = 18
snake_speed = 20
snake_body = [(80,100),(60,100),(40,100)]   # 蛇身體
snake_head = snake_body[0]                  # 蛇頭
snake_len = len(snake_body)      

# 顏色設定
snake_color = PINK
food_color = GREEN_BLUE
score_color = BLACK

# 食物物件
class Food():
    def __init__(self,x,y):
        self.img = pygame.Surface((20,20))
        self.img.fill(food_color)
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        screen.blit(self.img, self.rect)

# 顯示文字函數
def text_draw(text, font, color, x,y):
    img = font.render(text, True, color)
    screen.blit(img, (x,y))

# 遊戲字形設定
score_font = pygame.font.SysFont('Bauhaus 93', 40)  # 分數字形
title_font = pygame.font.SysFont('Bauhaus 93', 70)  # title 字形
rules_font = pygame.font.SysFont('Bauhaus 93', 25)  # rule 字形
start_font = pygame.font.SysFont('Bauhaus 93', 35)  # start 字形
die_font = pygame.font.SysFont('Bauhaus 93', 55)  # start 字形
c_font = pygame.font.SysFont('Bauhaus 93', 25)    # 繼續字形
rank_font = pygame.font.SysFont('Bauhaus 93', 45)
new_record_font = pygame.font.SysFont('Bauhaus 93', 30)

# 遊戲主畫面內容設定
title = 'Greedy Snake'
rules = '[WASD] to control the Snake!'
start = 'PRESS [SPACE] TO START'
Fake_snake = [(520,222),(500,222),(480,222),(460,222)]

# 死亡顯示畫面設定
die = 'YOU ARE DEAD!!'
score_text = 'YOUR SCROE: '
Continue = 'PRESS [SPACE] TO CONTINUE'


# 遊戲迴圈前置設定
running = True
direction = 1       # 預設往右移動
food_check = False  # 確認是否有食物
menu = 0            # 畫面

save = False        # 使否已儲存分數
new_record = 99     # 進到榜單的名次
new_high = False    # 是否破紀錄

# 遊戲迴圈
while(running):
    clock.tick(FPS)
    screen.fill(YELLOW)
    # 取得事件===================================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE) and (menu != 1):
                menu += 1

    # 顯示主菜單=================================
    if menu==0:
        text_draw(title,title_font,PINK, 140,screen_height/4)           # 印出標題
        text_draw(rules,rules_font,GREY, 200,360)                       # 印出規則
        text_draw(start,start_font,GREEN_BLUE, 170,(screen_height/3)*2) # 印出開始
        for i in range(len(Fake_snake)):                                # 印出假蛇
            pygame.draw.rect(screen, snake_color, pygame.Rect(Fake_snake[i][0],Fake_snake[i][1],snake_size, snake_size))

        # 初始化遊戲
        snake_body = [(80,100),(60,100),(40,100)]   # 蛇身體
        snake_head = snake_body[0]                  # 蛇頭
        direction = 1
        food_check = False
        save = False
        score = 0
        new_record = 99
        new_high = False

    # 開始遊戲===================================
    elif menu==1:
        # 生成食物
        if food_check==False:
            x = random.randrange(0,screen_width-20)
            y = random.randrange(0,screen_height-20)
            food = Food(x,y)
            food_check = True

        # 蛇移動和自我碰撞-----------------------------------------------------------------------

        # 取得蛇移動方向
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d] and (direction !=2):    # 往右
            direction = 1  
        if key_pressed[pygame.K_a] and (direction !=1):    # 往左
            direction = 2
        if key_pressed[pygame.K_w] and (direction !=4):    # 往上
            direction = 3
        if key_pressed[pygame.K_s] and (direction !=3):    # 往下
            direction = 4
        
        # 蛇移動
        if direction == 1:
            snake_head = (snake_head[0]+snake_speed, snake_head[1])
        elif direction == 2:
            snake_head = (snake_head[0]-snake_speed, snake_head[1])
        elif direction == 3:
            snake_head = (snake_head[0], snake_head[1]-snake_speed)
        elif direction == 4:
            snake_head = (snake_head[0], snake_head[1]+snake_speed)
        
        # 與自己身體碰撞
        head_rect = pygame.Rect(snake_head[0],snake_head[1],snake_size,snake_size)  # 蛇頭 Rect設定
        for body in snake_body:
            body_rect = pygame.Rect(body[0],body[1],snake_size,snake_size)  # 蛇身 Rect設定
            if pygame.Rect.colliderect(head_rect, body_rect):               # 碰撞產生
                menu = -1
                dead_sound.play()

        # 加蛇頭、去蛇尾
        snake_body.insert(0,snake_head)
        snake_body.pop(len(snake_body)-1)

        # 碰撞--------------------------------------------------------------------------------

        # 與食物碰撞
        if pygame.Rect.colliderect(head_rect, food.rect):
            eat_sound.play()
            if direction == 1:
                snake_head = (snake_head[0]+10, snake_head[1])
            if direction == 2:
                snake_head = (snake_head[0]-10, snake_head[1])
            if direction == 3:
                snake_head = (snake_head[0], snake_head[1]-10)
            if direction == 4:
                snake_head = (snake_head[0], snake_head[1]+10)
            snake_body.insert(0,snake_head)                     # 增加蛇長度
            score += 10                                         # 分數增加
            del food                                            # 刪除食物
            food_check = False

        # 與邊界碰撞
        if snake_head[0]+(snake_size) >= screen_width or snake_head[0]<=0:
            menu = -1
            dead_sound.play()
        if snake_head[1]+(snake_size) >= screen_height or snake_head[1]<=0:
            menu = -1
            dead_sound.play()

        # 螢幕顯示-----------------------------------------------------------------------------
        if food_check==True:                    # 如果食物存在
            food.update()                       # 顯示食物
        snake_len = len(snake_body)             # 蛇長度更新
        for i in range(snake_len):    # 顯示蛇
            pygame.draw.rect(screen, snake_color, pygame.Rect(snake_body[i][0],snake_body[i][1],snake_size, snake_size))
        text_draw(str(score),score_font,score_color,15,10)    # 分數顯示


    # 顯示分數畫面===============================
    elif menu == -1:
        # 儲存分數紀錄(如果有進前五名)
        if save == False:
            change_index = 0
            save_sure = False
            for i in range(5):
                if int(SCORE_SAVE[i]) <= score :           # 如果原始分數<=新分數

                    if int(SCORE_SAVE[i]) == score:        # 相同分數不增加紀錄
                        new_record = i
                        break

                    if i == 4:                             # 如果新分數是第五名
                        SCORE_SAVE[i]=str(score)           # 將新分數加入排行榜(覆蓋原儲存分數) 
                        new_record = i
                        break
                    else:
                        if i == 0:                         # 檢查是否破紀錄
                            new_high = True
                        new_record = i
                        save_sure = True                   # 是否確定儲存
                        change_index = i                   # 要加入排行的名次
                        break


            # 更新儲存分數
            index = 4                                      # 最後排行開始更新
            while save_sure:
                if index == 4:                             # 最後一名(第五名)更新
                    st = SCORE_SAVE[index-1].replace('\n',' ')
                    SCORE_SAVE[index]= st
                    #print(st)
                elif index==change_index:                  # 到達要更換(刷新)的名次
                    SCORE_SAVE[index]=str(score)+'\n'
                    save_sure = False
                else:                                      # 其他名次更新
                    SCORE_SAVE[index]=SCORE_SAVE[index-1]
                index -= 1
                

            # 回傳給檔案
            with open(os.path.join('file','save.txt'),'w') as file:
                file.writelines(SCORE_SAVE)
                
            save = True

        # 顯示畫面
        for i in range(snake_len):              # 顯示蛇死亡狀態
            pygame.draw.rect(screen, snake_color, pygame.Rect(snake_body[i][0],snake_body[i][1],snake_size, snake_size))
        text_draw(die, die_font, RED, 150,50)  # 顯示[死亡]字樣
        text_draw(score_text, score_font, GREEN_BLUE, 150,110)  # 顯示[分數標題]字樣
        text_draw(str(score), score_font, GREEN_BLUE, 430,110)  # 顯示[分數]字樣
        text_draw(Continue, c_font, BLACK, 190,480)  # 顯示[繼續]字樣

        # 顯示排行分數
        for i in range(5):
            n = i+1
            text_draw(f'No.{n}: ', rank_font, GREY2, 160, 170+48*i)
            text_draw(SCORE_SAVE[i].replace('\n',' '), rank_font, GREY2, 280, 170+48*i)
        
        # 顯示新分數在榜單上名次 and 是否破紀錄
        if new_record < 5:
            n = new_record+1
            text_draw(f'No.{n}: ', rank_font, DARK_YELLOW, 160+3, 170+48*new_record+2)
            text_draw(SCORE_SAVE[new_record].replace('\n',' '), rank_font, DARK_YELLOW, 280+3, 170+48*new_record+2)
            if new_high:
                text_draw('# New Record!!', new_record_font, RED, 410, 180)
                text_draw('______________', new_record_font, RED, 410, 183)


        
    # 螢幕更新==================================
    pygame.display.update() 


print(score)
pygame.quit()