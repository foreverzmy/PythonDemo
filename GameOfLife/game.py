# -*- coding: utf-8 -*-

from time import sleep
from copy import deepcopy
from random import choice
from cell import Cell


WOELD_HIGH = 20  # 世界长度
WOELD_WIDTH = 40  # 世界宽度
ALIVE_CON = 3  # 复活条件
KEEP_CON = 2  # 保有条件


class GameManage(object):
    def __init__(self):
        self.world = self.init_world()
        self.init_alive_cell()

    @staticmethod
    def init_world():
        """世界初始化"""
        world = []
        for pos_x in range(WOELD_WIDTH):
            col = []
            for pos_y in range(WOELD_HIGH):
                col.append(Cell((pos_x, pos_y)))
            world.append(col)
        return world

    def init_alive_cell(self):
        """随机设置存活细胞"""
        for high in self.world:
            for cell in high:
                if choice((0, 1)) == 0:
                    continue
                cell.set_alive()

    def get_neighbors(self, cell):
        """获取邻居存活数量"""
        alive_account = 0
        for x_of in range(-1, 2):
            for y_of in range(-1, 2):
                cx, cy = cell.x + x_of, cell.y + y_of
                if ((cx, cy) == (cell.x, cell.y)) or \
                    (cx < 0 or cx >= WOELD_WIDTH) or \
                        (cy < 0 or cy >= WOELD_HIGH):
                    continue
                if self.world[cx][cy].is_alive:
                    alive_account += 1
        return alive_account

    def display(self):
        print('=' * WOELD_WIDTH)
        for i in range(WOELD_HIGH):
            print(''.join([high[i].display() for high in self.world]))
        print('=' * WOELD_WIDTH)

    def start(self):
        level = 1
        while True:
            print(level)
            self.display()
            new_world = deepcopy(self.world)
            for p_x, width_list in enumerate(self.world):
                for p_y, _ in enumerate(width_list):
                    current_cell = new_world[p_x][p_y]
                    neibor_num = self.get_neighbors(current_cell)
                    if neibor_num == ALIVE_CON:
                        current_cell.set_alive()
                    elif neibor_num != KEEP_CON:
                        current_cell.set_died()
            self.world = new_world
            level += 1
            sleep(1)


if __name__ == '__main__':
    world = GameManage()
    try:
        world.start()
    except KeyboardInterrupt:
        """防止 Ctrl+C 退出报错"""
        pass
