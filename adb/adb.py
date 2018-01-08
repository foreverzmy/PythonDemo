# -*- coding: utf-8 -*-
"""
adb 操作封装
"""
import os


class Adb():
    """
    adb 操作的封装

    Methods
    _______
    click : 点击操作
    swipe : 滑动操作
    install : 安装 apk 文件
    uninstall : 卸载软件
    pull : 从设备上下载文件到电脑
    push : 从电脑上发送文件到设备
    screencap : 手机截屏
    """

    @staticmethod
    def click(x, y):
        """
        点击

        Parameters
        ----------
        x : 横坐标
        y : 纵坐标
        """
        cmd = 'adb shell input tap %s %s' % (x, y)
        os.system(cmd)

    @staticmethod
    def swipe(x1, y1, x2, y2, duration):
        """
        滑动

        Parameters
        ----------
        x1 : 起点横坐标
        y1 : 起点纵坐标
        x2 : 终点横坐标
        y2 : 终点纵坐标
        duration : 滑动时间(ms)
        """
        cmd = 'adb shell input swipe %s %s %s %s %s' % (x1, y1, x2, y2,
                                                        duration)
        os.system(cmd)

    @staticmethod
    def screencap(img_name):
        """
        手机截屏

        Parameters
        ----------
        img_name : 截屏保存的文件名
        """
        cmd = 'adb shell screencap -p /sdcard/%s.png' % (img_name)
        os.system(cmd)

    @staticmethod
    def install(apk):
        """
        安装 apk 应用

        Parameters
        ----------
        apk : apk 文件绝对路径
        """
        cmd = 'adb install -r %s' % (apk)
        os.system(cmd)

    @staticmethod
    def uninstall(app):
        """
        卸载应用

        Parameters
        ----------
        app : 应用名称
        """
        cmd = 'adb uninstall %s' % (app)

    @staticmethod
    def pull(remote, local):
        """
        从设备上下载文件到电脑

        Parameters
        ----------
        remote : 远程路径
        local : 本地路径
        """
        cmd = 'adb pull %s %s' % (remote, local)
        os.system(cmd)

    @staticmethod
    def push(local, remote):
        """
        从电脑上发送文件到设备

        Parameters
        ----------
        remote : 远程路径
        local : 本地路径
        """
        cmd = 'adb push %s %s' % (local, remote)
        os.system(cmd)
