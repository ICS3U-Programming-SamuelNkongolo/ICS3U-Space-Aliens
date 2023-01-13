#!/usr/bin/env python3
#Created by: Samuel Nkongolo
#Created on: Jan, 9 2023
#This program is the "Space Aliens" program on PyBadge

import ugame
import stage


def game_scene():
        # Gets image from file (16x16) and sets it as the stage.
    image_bank_background = stage.Bank.from_bmp16
    ("space_aliens_background.bmp")

    # Display the inmage background
    background = stage.Grid(image_bank_background, 10, 8)

    # Displays the image stage background
    # 60 Frames Per Sec (FPS)

    game = stage.Stage(ugame.display, 60)

    #list of layers for the game (In order left appear first)
    game.layers = [background]

    # Renders all sprites
    # Renders the background
    game.render_block()

    # Placeholder
    while True:
        pass

if __name__ == "__main__":
    game_scene()