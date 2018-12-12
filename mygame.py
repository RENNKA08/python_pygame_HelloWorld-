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
y_move = 88
x_move = 20  # 要変更

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

        # ゲーム状態の初期化
        self.game_state = START

        # 値の初期化
        self.init_game()

        #
        self.flag_restart = False

        # メインループ開始
        # clock = pygame.time.Clock()
        while True:
            # clock.tick(60)
            # self.update()
            self.draw(screen)  # 画面の描画
            pygame.display.update()  # 画面の更新
            self.key_handler()  # イベントの発生

    def init_game(self):
        """ゲームオブジェクトの初期化"""
        self.time = 0
        i = 0
        self.load_judge = 0
        self.load_interval = 0
        self.load_random = 0
        self.flag_finish = False
        self.flag_endBgm = False
        self.new_field = Y_std
        self.x = X_std
        self.y = Y_std
        self.x_load = []
        self.y_load = []
        while True:
            self.x_load.append(i)
            self.y_load.append(Y_std + y_move)
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
            # 背景画像の追加
            # screen.blit(self.backImg, (0, 0))
            # ゲーム中のBGM
            if self.time == 0:
                pygame.mixer.music.load("zangyousenshi.mp3")
                pygame.mixer.music.play(-1)  # ループ再生
            # scoreを描画
            sysfont2 = pygame.font.SysFont(None, 20)
            load_length = sysfont2.render(format(int(self.time / 100)), True, (0, 0, 0))
            screen.blit(load_length, (600, 10))
            self.time += 1
            # 道の生成
            load_random = random.uniform(0, 1000)
            i = 0
            while True:
                self.y_load[i] = self.y_load[i + 1]
                i += 1
                if i == 640:
                    break
            if self.load_judge == 1:
                self.load_interval += 1
                if self.load_interval == 150:
                    self.load_judge = 0
                    self.load_interval = 0
            if self.load_judge == 0:
                # print(time)
                if self.new_field == Y_std:
                    if load_random < 4:
                        self.new_field = Y_std + y_move
                        self.load_judge = 1
                if self.new_field == Y_std + y_move:
                    if load_random > 4:
                        if load_random < 8:
                            self.new_field = Y_std + y_move + y_move
                            self.load_judge = 1
                    if load_random < 996:
                        if load_random > 992:
                            self.new_field = Y_std
                            self.load_judge = 1
                if self.new_field == Y_std + y_move + y_move:
                    if load_random > 996:
                        self.new_field = Y_std + y_move
                        self.load_judge = 1
            self.y_load[640] = self.new_field
            i = 640
            while True:
                pygame.draw.line(screen, (0, 0, 0), (self.x_load[i], self.y_load[i]), (self.x_load[i] - 1, self.y_load[i]), 25)
                i -= 1
                if i == -1:
                    break
            # キャラの描画
            screen.blit(self.playerImg, (self.x, self.y))
            # キャラの移動
            self.key_handler_PLAY()
            # 道の正誤判定
            self.load_detection()
            if self.flag_finish:
                self.game_state = GAMEOVER
                # BGMの停止
                pygame.mixer.music.stop()

        elif self.game_state == GAMEOVER:
            # 画面を黒色で塗りつぶす
            screen.fill((0, 0, 0))
            # result画面のbgm
            if self.flag_endBgm == False:
                pygame.mixer.music.load("orehamou.mp3")
                pygame.mixer.music.play(-1)  # ループ再生
                self.flag_endBgm = True
            # GameOverを描画
            sysfont = pygame.font.SysFont(None, 100)
            end = sysfont.render("Game Over", True, (255, 0, 0))
            screen.blit(end, (135, 180))
            # scoreを描画
            sysfont1 = pygame.font.SysFont(None, 30)
            score = sysfont1.render("score", True, (255, 255, 255))
            screen.blit(score, (250, 300))
            # load_length
            sysfont3 = pygame.font.SysFont(None, 80)
            load_length1 = sysfont3.render(format(int(self.time / 100)), True, (255, 255, 255))
            screen.blit(load_length1, (320, 275))
            # TAPTOSPACE
            start = sysfont1.render("TAP TO SPACE", True, (255, 255, 255))
            screen.blit(start, (240, 350))
            # クレジット表記
            sysfont4 = pygame.font.Font("ipaexg.ttf", 10)
            credit = sysfont4.render("効果音素材：ポケットサウンド – https://pocket-se.info/", True, (255, 255, 255))
            screen.blit(credit, (360, 465))

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
                # 値の初期化
                self.init_game()
                # 画面の切り替え効果音再生
                self.sceneSwitch_sound.play()
                if self.game_state == START:
                    self.game_state = PLAY
                elif self.game_state == GAMEOVER:
                    self.init_game()
                    self.game_state = PLAY
                    # BGMの停止
                    pygame.mixer.music.stop()

    def key_handler_PLAY(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_RIGHT or event.key == K_d:
                    if self.y != Y_std - y_move:
                        self.y -= y_move
                        # キャラの移動効果音再生
                        self.charSwitch_sound.play()
                if event.key == K_DOWN or event.key == K_LEFT or event.key == K_a:
                    if self.y != Y_std + y_move:
                        self.y += y_move
                        # キャラの移動効果音再生
                        self.charSwitch_sound.play()

    def load_detection(self):
        """正誤判定"""
        # プレイヤーと道の正誤判定
        m = 89
        while True:
            m += 1
            if (self.y + y_move) == self.y_load[m]:
                break
            if m == 200:
                self.flag_finish = True
                break

    def load_images(self):
        """イメージのロード"""
        self.playerImg = pygame.image.load("sraim_alpha.png").convert_alpha()
        self.backImg = pygame.image.load("forest.png")

    def load_sounds(self):
        """サウンドのロード"""
        pygame.mixer.quit()
        pygame.mixer.init(44100, 16, 2, 1024)
        # 画面の切り替え効果音
        self.sceneSwitch_sound = pygame.mixer.Sound("sceneswitch2.wav")
        # キャラの移動効果音
        self.charSwitch_sound = pygame.mixer.Sound("jump-anime1.wav")

if __name__ == "__main__":
    Mygame()