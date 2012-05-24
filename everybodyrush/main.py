# -*- coding: utf-8 -*-
# This is a part of everybodyrush @
# http://github.com/KenjiTakahashi/everybodyrush/
# Karol "Kenji Takahashi" Wozniak (C) 2012
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame
from pygame.locals import QUIT, FULLSCREEN, HWSURFACE
from sys import exit
import os
import cPickle


class Menu(pygame.sprite.Sprite):
    _currentMap = 0

    def __init__(self):
        super(Menu, self).__init__()
        pygame.init()
        try:
            self.settings = cPickle.load(open(
                os.path.expanduser(u'~/.config/everybodyrush/settings'), u'rb'
            ))  # we'll need to deal with MS Windows separately
        except (IOError, AttributeError):
            self.screen = pygame.display.set_mode((0, 0))
        else:
            self.screen = pygame.display.set_mode(self.settings[u'resolution'],
                self.settings[u'fullscreen'] and FULLSCREEN | HWSURFACE or 0
            )
        self.clock = pygame.time.Clock()

    def draw(self):
        info = pygame.display.Info()
        w, h = (info.current_w, info.current_h)

        self.logo = pygame.Surface((w, h / 5))  # use image
        self.logo.fill((255, 0, 255))

        self.me = pygame.Surface((w / 12, w / 12))  # use image
        self.me.fill((255, 255, 0))

        self.he = self.me.copy()  # use image

        self.map = pygame.Surface((w - 5 * (w / 12), h / 5))  # use image based on _currentMap
        self.map.fill((0, 255, 255))

        self.conf = pygame.Surface((2 * w / 12 - 20, h / 5))  # create proper conf
        self.conf.fill((255, 0, 0))

        self.start = pygame.Surface((w / 12, h / 5))
        self.start.fill((0, 255, 0))

        self.screen.blit(self.logo, (0, 0))
        self.screen.blit(self.me, (w / 12, h / 5 + 50))
        self.screen.blit(self.he, (w - 2 * (w / 12), h / 5 + 50))
        self.screen.blit(self.map, (w / 12, h / 5 + w / 12 + 100))
        self.screen.blit(self.conf, (w - 4 * w / 12 + 10, h / 5 + w / 12 + 100))
        self.screen.blit(self.start, (w - 2 * w / 12, h / 5 + w / 12 + 100))

    def run(self):
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            self.draw()
            pygame.display.update()


def run():
    game = Menu()
    game.run()
