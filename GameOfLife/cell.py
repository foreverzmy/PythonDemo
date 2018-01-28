"""
创建细胞对象
"""


class Cell(object):
    """
    细胞对象
    """

    def __init__(self, point):
        """point 自身的坐标"""
        self.x, self.y = point
        self.is_alive = False

    def set_alive(self):
        """让细胞复活"""
        self.is_alive = True

    def set_died(self):
        """让细胞死亡"""
        self.is_alive = False

    def display(self):
        """黑白块形式显示细胞"""
        if self.is_alive:
            # return '*'
            return '\033[0;37;47m \033[0m'
        # return ' '
        return '\033[0;30;40m \033[0m'
