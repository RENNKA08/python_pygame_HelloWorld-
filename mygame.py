#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
sys.setrecursionlimit(10000)
import random

START, PLAY, GAMEOVER = (0, 1, 2)  # ゲーム状態
SCREEN_SIZE = (640, 480)  # 画面サイズ
X_std = 100
Y_std = 240
x_load = []
y_load = []
y_move = 88
x = X_std
x_move = 20  # 要変更
y = Y_std
new_field = Y_std
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
        # clock = pygame.time.Clock()
        while True:
            # clock.tick(60)
            self.update()
            self.draw(screen)
            pygame.display.update()
            self.key_handler()
    def init_game(self):
        """ゲームオブジェクトの初期化"""
        # ゲーム状態
        self.game_state = START
        i = 0
        time = 0
        load_judge = 0
        load_interval = 0
        load_random = 0
        flag_finish = False
        while True:
            x_load.append(i)
            y_load.append(Y_std + y_move)
            i += 1
            if i == 641:
                break
    def update(self):
        """ゲーム状態の更新"""
        if self.game_state == PLAY:
            self.update()
    def draw(self, screen):
        """描画"""
        if self.game_state == START:
            # 画面を白色で塗りつぶす
            screen.fill((255, 255, 255))
            # タイトルを描画
            sysfont = pygame.font.SysFont(None, 100)
            title = sysfont.render("HelloWorld!", True, (0, 0, 0))
            screen.blit(title, (125, 180))
            # TAPTOSPACE
            sysfont1 = pygame.font.SysFont(None, 30)
            start = sysfont1.render("TAP TO SPACE", True, (0, 0, 0))
            screen.blit(start, (240, 275))
        elif self.game_state == PLAY:
            # 画面を白色で塗りつぶす
            screen.fill((255, 255, 255))
            # scoreを描画
            sysfont2 = pygame.font.SysFont(None, 20)
            load_length = sysfont2.render(format(int(time / 100)), True, (0, 0, 0))
            screen.blit(load_length, (600, 10))
            time += 1
            # 道の生成
            load_random = random.uniform(0, 1000)
            i = 0
            while True:
                y_load[i] = y_load[i + 1]
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
            # キャラの移動
            self.key_handler_PLAY()
            # 道の正誤判定
            self.load_detection()
            if flag_finish:
                self.game_state = GAMEOVER
        elif self.game_state == GAMEOVER:
            # 画面を黒色で塗りつぶす
            screen.fill((0, 0, 0))
            # GameOverを描画
            sysfont = pygame.font.SysFont(None, 100)
            end = sysfont.render("Game Over", True, (255, 0, 0))
            screen.blit(end, (125, 180))
            # scoreを描画
            sysfont1 = pygame.font.SysFont(None, 30)
            score = sysfont1.render("score", True, (255, 255, 255))
            screen.blit(score, (240, 300))
            # load_length
            sysfont3 = pygame.font.SysFont(None, 80)
            load_length1 = sysfont3.render(format(int(time / 100)), True, (255, 255, 255))
            screen.blit(load_length1, (300, 275))
            # TAPTOSPACE
            sysfont1 = pygame.font.SysFont(None, 30)
            start = sysfont1.render("TAP TO SPACE", True, (0, 0, 0))
            screen.blit(start, (240, 275))
    def key_handler(self):
        """キーハンドラー"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                if self.game_state == START:
                    self.game_state = PLAY
                elif self.game_state == GAMEOVER:
                    self.init_game()
                    self.game_state = PLAY
    def key_handler_PLAY(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if y != Y_std - y_move:
                        y -= y_move
                if event.key == K_DOWN:
                    if y != Y_std + y_move:
                        y += y_move
    def load_detection(self):
        """正誤判定"""
        # プレイヤーと道の正誤判定
        m = 89
        while True:
            m += 1
            if (y + y_move) == y_load[m]:
                break
            if m == 200:
                flag_finish = True
                break
    def load_images(self):
        """イメージのロード"""
        playerImg = pygame.image.load("sraim_alpha.png").convert_alpha()
    def load_sounds(self):
        """サウンドのロード"""

if __name__ == "__main__":
    Mygame()