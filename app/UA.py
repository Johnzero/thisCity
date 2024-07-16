import time, os, cv2
from typing import List, Dict, Union, Tuple
import uiautomator2 as u2
import numpy as np
from PIL import Image


class UA:
    def __init__(self, device: str = None, pkg_name: str = None):
        """
        初始化uiautomator2对象
        :param device: 设备ID或IP地址，如果为None则默认连接所有设备
        :param pkg_name: 待测试应用的包名
        """
        self.d = u2.connect(device)
        self.pkg_name = pkg_name
        self.width, self.height = self.d.window_size()
        self.shot = None
        # self.d.swipe_ext(direction)

    def clear_app_data(self):
        """
        清除应用数据
        """
        self.d.app_clear(self.pkg_name)

    def click(self, x: int, y: int):
        """
        点击屏幕上的一个点
        :param x: 点击点的X坐标
        :param y: 点击点的Y坐标
        :param duration: 点击的持续时间
        """
        print(str(x) + ", " + str(y))
        self.d.click(int(x), int(y))
        time.sleep(1)

    def swipe(self, x1: int, y1: int, x2: int, y2: int, duration: float = 0.5):
        """
        在屏幕上滑动
        :param x1: 起始点的X坐标
        :param y1: 起始点的Y坐标
        :param x2: 终止点的X坐标
        :param y2: 终止点的Y坐标
        :param duration: 滑动的持续时间
        """
        self.d.swipe(x1, y1, x2, y2, duration=duration)
        time.sleep(1)

    def home(self):
        """
        模拟按下Home键
        """
        self.click(90, 1868)

        while True:
            pos = self.find_image("./tapshot/验证奖励.png", 0.8)
            if pos:
                self.passYZM()
                time.sleep(2)
                # 确定
                self.click(542, 1344)
            else:
                break

        self.click(90, 1868)
        time.sleep(2)
        self.click(530, 1184)
        time.sleep(2)
        self.click(90, 1868)
        self.click(90, 1868)

    def start_app(self, activity: str = None):
        """
        启动应用
        :param activity: 应用的主Activity名称
        """
        if activity:
            self.d.app_start(self.pkg_name, activity)
        else:
            self.d.app_start(self.pkg_name)
        time.sleep(10)
        # 广告弹窗
        self.click(535, 107)
        # 更新按钮
        self.click(719, 1192)
        # 登录按钮
        self.click(535, 1590)
        time.sleep(10)

    def stop_app(self):
        """
        停止应用
        """
        self.d.app_stop(self.pkg_name)

    def get_current_activity(self) -> str:
        """
        获取当前Activity名称
        :return: 当前Activity名称
        """
        return self.d.current_app().get("activity")

    def screenshot(self, filename: str = None) -> Union[None, np.ndarray]:
        """
        截图并返回截图的numpy数组
        :param filename: 保存截图的文件名，如果为None则不保存
        :return: 截图的numpy数组
        """
        filename = filename or f"./screenshot/screenshot_{time.time()}.png"
        if filename:
            self.d.screenshot().save(filename)
        image_origin = cv2.imread(filename)
        self.shot = filename
        return image_origin

    def find_image(
        self, template: str, threshold: float = 0.8
    ) -> Union[Tuple[int, int], None]:
        """
        在当前屏幕上查找指定图片的位置
        :param template: 模板图片的文件名或numpy数组
        :param threshold: 匹配阈值，取值范围为0到1之间，值越大匹配越严格
        :return: 如果找到则返回图片的左上角坐标，否则返回None
        """
        if isinstance(template, str):
            img = cv2.imread(template)
        else:
            img = template
        tw, th = img.shape[:2]
        res = cv2.matchTemplate(self.screenshot(), img, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        # +int(tw/4) +int(th/4)
        if len(loc[0]) > 0:
            return (loc[1][0] + int(tw / 2)), (loc[0][0] + int(th / 2))
        return None

    def find_image_by_screenshot(
        self, template: str, threshold: float = 0.8, screenshot: str = None
    ) -> Union[Tuple[int, int], None]:
        """
        在当前屏幕上查找指定图片的位置
        :param template: 模板图片的文件名或numpy数组
        :param threshold: 匹配阈值，取值范围为0到1之间，值越大匹配越严格
        :return: 如果找到则返回图片的左上角坐标，否则返回None
        """
        screenshot_read = cv2.imread(screenshot)
        img = cv2.imread(template)
        tw, th = img.shape[:2]
        res = cv2.matchTemplate(screenshot_read, img, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        # for pt in zip(*loc[::-1]):
        #     cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h),(0,255,0), 1)
        # +int(tw/4) +int(th/4)
        if len(loc[0]) > 0:
            return (loc[1][0] + int(tw / 2)), (loc[0][0] + int(th / 2))
        return None

    # def click_image(self, template: str, threshold: float = 0.8, duration: float = 0.1):
    #     """
    #     在当前屏幕上点击指定图片的位置
    #     :param template: 模板图片的文件名或numpy数组
    #     :param threshold: 匹配阈值，取值范围为0到1之间，值越大匹配越严格
    #     :param duration: 点击的持续时间
    #     """
    #     pos = self.find_image(template, threshold)
    #     if pos:
    #         self.click(*pos, duration=duration)

    def clear_app_data(self):
        folder_path = "./screenshot"
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

    def passYZM(self):

        tp = "./tapshot/yz.png"
        # 读取背景图片和缺口图片
        shot = Image.open(self.shot)
        img = shot.crop((100, 500, 1000, 1100))
        filename = f"./screenshot/screenshot_{time.time()}.png"
        img.save(filename)
        bg_img = cv2.imread(filename, 0)
        tp_img = cv2.imread(tp, 0)

        # # 识别图片边缘
        # bg_edge = cv2.Canny(bg_img, 10, 200)
        # tp_edge = cv2.Canny(tp_img, 50, 100)
        # # plt.imshow(bg_edge, cmap="Greys_r")
        # filename = f"./screenshot/screenshot_{time.time()}.png"
        # cv2.imwrite(filename, bg_edge)

        # filename = f"./screenshot/screenshot2_{time.time()}.png"
        # cv2.imwrite(filename, tp_edge)

        # # 转换图片格式
        # bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        # tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

        # filename = f"./screenshot/screenshot_{time.time()}.png"
        # if filename:
        #     bg_pic.save(filename)
        # filename = f"./screenshot/screenshot2_{time.time()}.png"
        # if filename:
        #     tp_pic.save(filename)

        # 缺口匹配
        res = cv2.matchTemplate(bg_img, tp_img, cv2.TM_CCOEFF_NORMED)
        # tl = np.where(res >= 0.6)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
        tl = max_loc  # 左上角点的坐标
        print("---验证---")
        # print(tl[0] + 100)
        # print((910 - 190) / (920 - 350) * (tl[0]) + 120)
        # exit(0)
        if (910 - 190) / (920 - 350) * (tl[0]) + 120 > 750:
            self.d.swipe(
                190, 1119, (910 - 190) / (920 - 350) * (tl[0]) + 140, 1119, 0.5
            )
        else:
            self.d.swipe(
                190, 1119, (910 - 190) / (920 - 350) * (tl[0]) + 120, 1119, 0.5
            )

        os.remove(filename)

        # self.d.swipe(190, 1119, tl[0] + tl[0] / 6, 1119, 0.5)
        # br = (tl[0]+tw,tl[1]+th) # 右下角点的坐标
        # cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2) # 绘制矩形
        # cv2.imwrite(out, bg_img) # 保存在本地

        # 返回缺口的X坐标
        # return tl[0]

        # pos = self.find_image("./tapshot/yz.png", 0.8)
        # print(pos)
