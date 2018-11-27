#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import os
import random

SCREEN_SIZE = (640, 480)  # 画面サイズ

# Pygameを初期化
pygame.init()
# SCREEN_SIZEの画面を作成
screen = pygame.display.set_mode(SCREEN_SIZE)
# タイトルバーの文字列をセット
pygame.display.set_caption(u"HelloWorld!")

#フォントの作成
sysfont = pygame.font.SysFont(None, 100)
sysfont1 = pygame.font.SysFont(None, 30)

#テキストを描画したSurfaceを作成
title = sysfont.render("HelloWorld!", True, (0, 0, 0))
start = sysfont1.render("TAP TO SPACE", True, (0, 0, 0))

# イメージを用意
playerImg = pygame.image.load("akari_dot2.png").convert_alpha()
playerImg_rect = playerImg.get_rect()
print(playerImg_rect.height)

#初期化
X_std = 100
x_load = 640
x = X_std
x_move = 20  # 要変更
Y_std = 240
y_load = Y_std
y = Y_std
y_move = playerImg_rect.height
load_random = 0

# ゲームループ
while True:
    screen.fill((255,255,255))   # 画面を白色で塗りつぶす
    flag = False

    #テキストを描画する
    screen.blit(title, (125, 180))
    screen.blit(start, (240, 275))

    pygame.display.update()  # 画面を更新
    # イベント処理

    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
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

    # 道の生成
    """
    load_random = random.uniform(0, 1000)
    if y_load == Y_std:
        if load_random < 50:
            while x_load > 0:
                pygame.draw.line(screen, (0, 0, 0), (x_load, y_load), (x_load - 1, y_load), 1)
                x_load -= 1
                if y_load < Y_std + y_move:
                    y_load += 1
        else:
            while x_load > 0:
                pygame.draw.line(screen, (0, 0, 0), (x_load, y_load), (x_load - 1, y_load), 1)
                x_load -= 1
    if y_load == Y_std + y_move:
        if load_random < 50:
            while x_load > 0:
                pygame.draw.line(screen, (0, 0, 0), (x_load, y_load), (x_load - 1, y_load), 1)
                x_load -= 1
                if y_load < Y_std + y_move + y_move:
                    y_load += 1
        else:
            while x_load > 0:
                pygame.draw.line(screen, (0, 0, 0), (x_load, y_load), (x_load - 1, y_load), 1)
                x_load -= 1
        if load_random > 950:
            while x_load > 0:
                pygame.draw.line(screen, (0, 0, 0), (x_load, y_load), (x_load - 1, y_load), 1)
                x_load -= 1
                if y_load > Y_std:
                    y_load -= 1
        else:
            while x_load > 0:
                pygame.draw.line(screen, (0, 0, 0), (x_load, y_load), (x_load - 1, y_load), 1)
                x_load -= 1
    if y_load == Y_std + y_move + y_move:
        if load_random > 950:
            while x_load > 0:
                pygame.draw.line(screen, (0, 0, 0), (x_load, y_load), (x_load - 1, y_load), 1)
                x_load -= 1
                if y_load > Y_std + y_move:
                    y_load -= 1
        else:
            while x_load > 0:
                pygame.draw.line(screen, (0, 0, 0), (x_load, y_load), (x_load - 1, y_load), 1)
                x_load -= 1
    """

    screen.blit(playerImg, (x, y))

    pygame.display.update()

    x_load = 640

    if x_load == 0:
        x_load = 640

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if y != Y_std - y_move:
                    x += x_move
                    y -= y_move
            if event.key == K_DOWN:
                if y != Y_std + y_move:
                    x -= x_move
                    y += y_move

        if event.type == QUIT: sys.exit()
        if event.type == KEYDOWN:  # 終了イベント
            if event.key == K_ESCAPE:
                sys.exit()

                # unko