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

class Mygame:
    def __init__(self):
        # Pygameを初期化
        pygame.init()

        # SCREEN_SIZEの画面を作成
        screen = pygame.display.set_mode(SCREEN_SIZE)

        # タイトルバーの文字列をセット
        pygame.display.set_caption(u"HelloWorld!")

        # 素材のロード
        self.load_images()  # 画像
        self.load_sounds()  # 音楽

        # ゲーム状態の初期化
        self.game_state = START

        # 値の初期化
        self.init_game()

        # メインループ開始
        # clock = pygame.time.Clock()
        while True:
            # clock.tick(10)
            self.draw(screen)        # 画面の描画
            pygame.display.update()  # 画面の更新
            self.key_handler()       # イベントの発生

    def init_game(self):
        """値の初期化"""
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

    def draw(self, screen):
        """描画"""
        if self.game_state == START:
            """プレイ画面"""
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
            """プレイ画面"""
            # 画面を白色で塗りつぶす
            screen.fill((255, 255, 255))

            # ゲーム中のBGM
            if self.time == 0:  # スタート時に再生
                pygame.mixer.music.load("zangyousenshi.mp3")
                pygame.mixer.music.play(-1)  # ループ再生

            # scoreを描画
            sysfont2 = pygame.font.SysFont(None, 20)
            load_length = sysfont2.render(format(int(self.time / 100)), True, (0, 0, 0))
            screen.blit(load_length, (600, 10))
            self.time += 1  # 更新のたびに追加

            # 道の生成
            self.make_load(screen)

            # キャラの描画
            screen.blit(self.playerImg, (self.x, self.y))

            # キャラの移動
            self.key_handler_play()

            # 道の正誤判定
            self.load_detection()

            # プレイの終了処理
            if self.flag_finish:
                self.game_state = GAMEOVER
                # BGMの停止
                pygame.mixer.music.stop()

        elif self.game_state == GAMEOVER:
            """リザルト画面"""
            # 画面を黒色で塗りつぶす
            screen.fill((0, 0, 0))

            # result画面のbgm
            if self.flag_endBgm == False:  # 最初だけ読み込む
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

            # スコアの表示
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
            # ゲームの強制終了
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # ゲームの終了
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            # ゲーム状態の変更及びそれに伴う値の初期化・bgm停止
            elif event.type == KEYDOWN and event.key == K_SPACE:
                # 値の初期化
                self.init_game()

                # 画面の切り替え効果音再生
                self.sceneSwitch_sound.play()

                if self.game_state == START:       # スタート画面からの移動
                    self.game_state = PLAY

                elif self.game_state == GAMEOVER:  # リスタート
                    self.game_state = PLAY
                    # ゲームオーバー中のBGMの停止
                    pygame.mixer.music.stop()

    def key_handler_play(self):
        """キャラの移動に関するキーハンドラー"""
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # 一番上に位置しているとき以外に上への移動
                if event.key == K_UP or event.key == K_RIGHT or event.key == K_d:
                    if self.y != Y_std - y_move:
                        self.y -= y_move
                        # キャラの移動効果音再生
                        self.charSwitch_sound.play()

                # 一番下に位置しているとき以外に下へ移動
                if event.key == K_DOWN or event.key == K_LEFT or event.key == K_a:
                    if self.y != Y_std + y_move:
                        self.y += y_move
                        # キャラの移動効果音再生
                        self.charSwitch_sound.play()

    def make_load(self, screen):
        """道の生成"""
        i = 0

        # 右のピクセルの線を左のピクセルにコピー
        # x=640の値が更新のたびにだんだん左へ移動
        while True:
            self.y_load[i] = self.y_load[i + 1]
            i += 1
            if i == 640:
                break

        # 最低限の道の幅を用意
        if self.load_judge == 1:
            self.load_interval += 1
            if self.load_interval == 150:
                self.load_judge = 0
                self.load_interval = 0

        # randomの値によって道の生成を変える
        # x=640に値を代入
        elif self.load_judge == 0:
            self.make_load_random()

        # x=640に次の生成分の値を代入
        self.y_load[640] = self.new_field

        # 道の描画
        self.draw_load(screen)

    def make_load_random(self):
        """ランダムに道を生成する"""
        load_random = random.uniform(0, 1000)

        # 上から中央へ
        if self.new_field == Y_std:
            if load_random < 4:
                self.new_field = Y_std + y_move
                self.load_judge = 1

        # 中央から
        elif self.new_field == Y_std + y_move:
            # 中央から下へ
            if load_random > 4 and load_random < 8:
                self.new_field = Y_std + y_move + y_move
                self.load_judge = 1
            # 中央から上へ
            elif load_random < 996 and load_random > 992:
                self.new_field = Y_std
                self.load_judge = 1

        # 下から中央へ
        elif self.new_field == Y_std + y_move + y_move:
            if load_random > 996:
                self.new_field = Y_std + y_move
                self.load_judge = 1

    def draw_load(self, screen):
        i = 640
        while True:
            pygame.draw.line(screen, (0, 0, 0), (self.x_load[i], self.y_load[i]),
                             (self.x_load[i] - 1, self.y_load[i]), 25)
            i -= 1
            if i == -1:
                break

    def load_detection(self):
        """正誤判定"""
        # プレイヤーと道の正誤判定
        # キャラの位置から-10~+100までを判断
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