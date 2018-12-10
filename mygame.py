#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import os
import random
START, PLAY, GAMEOVER = (0, 1, 2)  # ゲーム状態
SCREEN_SIZE = (640, 480)  # 画面サイズ

class Mygame:
    def __init__(self):
        # Pygameを初期化
        pygame.init()
        # SCREEN_SIZEの画面を作成
        screen = pygame.display.set_mode(SCREEN_SIZE)
        # タイトルバーの文字列をセット
        pygame.display.set_caption(u"HelloWorld!")
        # 素材のロード
        self.load_images()
        self.load_sounds()
        # ゲームオブジェクトを初期化
        self.init_game()
        # メインループ開始
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.update()
            self.draw(screen)
            pygame.display.update()
            self.key_hanler()
    def init_game(self):
        """ゲームオブジェクトの初期化"""
        # ゲーム状態
        self.game_state = START
        X_std = 100
        Y_std = 240
        x_load = []
        y_load = []
        i = 0
        time = 0
        load_judge = 0
        load_interval = 0
    def update(self):
        """ゲーム状態の更新"""
        if self.game_state == PLAY:
            self.all.update()
            # 道の正誤判定
            self.load_detection()
            if flag_finish:




# フォントの作成
sysfont = pygame.font.SysFont(None, 100)
sysfont1 = pygame.font.SysFont(None, 30)
sysfont2 = pygame.font.SysFont(None, 20)
sysfont3 = pygame.font.SysFont(None, 80)

# テキストを描画したSurfaceを作成
title = sysfont.render("HelloWorld!", True, (0, 0, 0))
start = sysfont1.render("TAP TO SPACE", True, (0, 0, 0))
end = sysfont.render("Game over", True, (255, 0, 0))
score = sysfont1.render("score", True, (255, 255, 255))

# イメージを用意
playerImg = pygame.image.load("sraim_alpha.png").convert_alpha()
playerImg_rect = playerImg.get_rect()
# print(playerImg_rect.height)

# 初期化2
# print(x_load)
x = X_std
x_move = 20  # 要変更
y = Y_std
y_move = playerImg_rect.height
load_random = 0
new_field = Y_std
while True:
    x_load.append(i)
    y_load.append(Y_std + y_move)
    i += 1
    if i == 641:
        break

# ゲームループ
while True:
    screen.fill((255, 255, 255))   # 画面を白色で塗りつぶす
    flag = False

    # テキストを描画する
    screen.blit(title, (125, 180))
    screen.blit(start, (240, 275))

    pygame.display.update()  # 画面を更新
    # イベント処理

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:  # 終了イベント
            if event.key == K_ESCAPE:
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                flag = True
                break

    if flag:
        break

while True:
    screen.fill((255, 255, 255))
    flag_finish = False
    flag1 = False
    # 距離
    load_length = sysfont2.render(format(int(time/100)), True, (0, 0, 0))
    screen.blit(load_length, (600, 10))
    time += 1

    # 道の生成
    load_random = random.uniform(0, 1000)
    i = 0
    while True:
        y_load[i] = y_load[i+1]
        i += 1
        if i == 640:
            break
    if load_judge == 1:
        load_interval += 1
        if load_interval == 150:
            load_judge = 0
            load_interval = 0
    if load_judge == 0:
        # print(time)
        if new_field == Y_std:
            if load_random < 4:
                new_field = Y_std + y_move
                load_judge = 1
        if new_field == Y_std + y_move:
            if load_random > 4:
                if load_random < 8:
                    new_field = Y_std + y_move + y_move
                    load_judge = 1
            if load_random < 996:
                if load_random > 992:
                    new_field = Y_std
                    load_judge = 1
        if new_field == Y_std + y_move + y_move:
            if load_random > 996:
                new_field = Y_std + y_move
                load_judge = 1
    y_load[640] = new_field
    i = 640
    while True:
        pygame.draw.line(screen, (0, 0, 0), (x_load[i], y_load[i]), (x_load[i] - 1, y_load[i]), 25)
        i -= 1
        if i == -1:
            break

    # キャラの描画
    screen.blit(playerImg, (x, y))

    pygame.display.update()  # ここまで更新

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if y != Y_std - y_move:
                    y -= y_move
            if event.key == K_DOWN:
                if y != Y_std + y_move:
                    y += y_move
        m = 89
        while True:
            m += 1
            if (y + y_move) == y_load[m]:
                break
            if m == 200:
                flag_finish = True
                break
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:  # 終了イベント
            if event.key == K_ESCAPE:
                sys.exit()
    if flag_finish:
        break

while True:
    screen.fill((0, 0, 0))   # 画面を黒色で塗りつぶす
    flag3 = False

    load_length1 = sysfont3.render(format(int(time / 100)), True, (255, 255, 255))

    # テキストを描画する
    screen.blit(end, (125, 180))
    screen.blit(score, (240, 300))
    screen.blit(load_length1, (300, 275))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:  # 終了イベント
            if event.key == K_ESCAPE:
                sys.exit()