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

# フォントの作成
sysfont = pygame.font.SysFont(None, 100)
sysfont1 = pygame.font.SysFont(None, 30)

# テキストを描画したSurfaceを作成
title = sysfont.render("HelloWorld!", True, (0, 0, 0))
start = sysfont1.render("TAP TO SPACE", True, (0, 0, 0))

# イメージを用意
playerImg = pygame.image.load("sraim_alpha.png").convert_alpha()
playerImg_rect = playerImg.get_rect()
print(playerImg_rect.height)

# 初期化
X_std = 100
Y_std = 240
x_load = []
y_load = []
i = 0
while True:
    x_load.append(i)
    y_load.append(Y_std)
    i += 1
    if i == 641:
        break
# print(x_load)
x = X_std
x_move = 20  # 要変更
y = Y_std
y_move = playerImg_rect.height
load_random = 0
new_field = Y_std

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

    # 道の生成
    load_random = random.uniform(0, 1000)
    i = 0
    while True:
        y_load[i] = y_load[i+1]
        i += 1
        if i == 640:
            break
    if new_field == Y_std:
        if load_random < 1:
            new_field = Y_std + y_move
    if new_field == Y_std + y_move:
        if load_random > 1:
            if load_random < 2:
                new_field = Y_std + y_move + y_move
        if load_random < 999:
            if load_random > 998:
                new_field = Y_std
    if new_field == Y_std + y_move + y_move:
        if load_random > 999:
            new_field = Y_std + y_move
    y_load[640] = new_field
    i = 640
    while True:
        pygame.draw.line(screen, (0, 0, 0), (x_load[i], y_load[i]), (x_load[i] - 1, y_load[i]), 1)
        i -= 1
        if i == -1:
            break

    screen.blit(playerImg, (x, y))

    pygame.display.update()

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

        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:  # 終了イベント
            if event.key == K_ESCAPE:
                sys.exit()
