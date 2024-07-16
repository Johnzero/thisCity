import time, cv2, random
from typing import List, Dict, Union, Tuple
import numpy as np
from PIL import Image


class Book:
    def __init__(self, UA):
        self.UA = UA
        self.shot = None
        self.is_window = False

        self.UA.home()
        self.UA.click(976, 1835)
        self.UA.click(976, 1835)
        time.sleep(2)
        self.UA.click(90, 1868)
        self.UA.click(90, 1868)
        time.sleep(2)
        self.UA.d.swipe(223, 902, 899, 902, duration=0.1)
        time.sleep(2)
        self.UA.d.swipe(223, 902, 899, 902, duration=0.1)
        time.sleep(2)
        self.UA.d.swipe(223, 902, 1100, 902, duration=0.1)
        # time.sleep(2)
        # self.UA.d.swipe(223, 902, 729, 902, duration=0.1)
        time.sleep(2)
        self.UA.d.swipe(550, 704, 550, 1229, duration=0.1)
        time.sleep(2)

    def task(self):
        screenshot = self.UA.screenshot()
        template = cv2.imread("./tapshot/book.png")  # 0.95
        h, w = template.shape[:2]

        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        pos = None

        loc = np.where(res >= threshold)
        locs = []
        pt = None
        print(loc)
        for pt in zip(*loc[::-1]):
            pos = (pt[0] + int(w / 2), pt[1] + int(h / 2))
            locs.append(pos)

        if len(locs) > 0:
            pt = random.choice(locs)

        if pt:
            self.UA.click(*pt)
            self.job()

            # # 升级
            # self.UA.click(542, 1365)
            # self.UA.click(542, 1365)

            # # 赠送
            # self.UA.click(235, 458)
            # self.UA.click(707, 1403)

            # # self.UA.click(979, 1829)
            # # 首页
            # self.UA.click(102, 1839)
            # self.UA.click(102, 1839)

    def job(self):
        # screenshot = self.UA.screenshot()
        pos = None
        wz_list = [
            "./tapshot/自动.png",
            "./tapshot/派遣.png",
            "./tapshot/验证奖励.png",
        ]

        for wz in wz_list:
            pos = self.UA.find_image_by_screenshot(wz, 0.8, self.UA.shot)
            if pos:
                print(wz + ":" + str(pos))

            if pos and wz == "./tapshot/派遣.png":
                self.UA.click(540, 1388)
                self.UA.click(341, 1518)
                self.UA.click(743, 1524)
                self.UA.click(540, 1562)
            elif pos and wz == "./tapshot/自动.png":
                self.UA.click(518, 1559)
                self.UA.click(518, 1559)
                self.UA.click(981, 1833)
            elif pos and wz == "./tapshot/领取奖励.png":
                self.UA.click(528, 1635)
                self.UA.click(580, 120)
            elif pos and wz == "./tapshot/验证奖励.png":
                self.UA.click(542, 1344)
                self.UA.passYZM()
                self.UA.click(542, 1344)
            elif pos:
                self.UA.click(*pos)

        self.UA.click(695, 19)
        # while True:
        #     posYz = self.UA.find_image("./tapshot/验证奖励.png", 0.8)
        #     if posYz:
        #         self.UA.click(542, 1344)
        #         self.UA.passYz()
        #         self.UA.click(542, 1344)
        #     else:
        #         break

        if pos:
            return True
        else:
            return False

    def run(self):
        print("---Book----")
        r = 0
        while r < 5:
            self.task()
            r = r + 1

    # def click(self, x: int, y: int):
    #     self.UA.click(x, y)
    #     self.shot = self.UA.screenshot()
    #     self.is_window = self.is_window_box()

    #     if self.is_window:
    #         self.shot = self.window_screenshot()
    #     res = self.wzsb()

    #     if res:
    #         self.shot = self.UA.screenshot()

    #     home = self.UA.find_image_by_screenshot("./tapshot/m1.png", 0.8, self.shot)
    #     if home:
    #         return False

    #     return True

    # def is_window_box(self):
    #     wz_list = [
    #         "./tapshot/关闭.png",
    #         "./tapshot/关闭2.png",
    #     ]
    #     is_window = False
    #     for wz in wz_list:
    #         pos = self.UA.find_image_by_screenshot(wz, 0.7, self.shot)
    #         if pos:
    #             is_window = True
    #             print(wz + ":" + str(pos))

    #     return is_window

    def run11(self):
        print("---start----")
        self.UA.home()
        screenshot = self.home_screenshot()
        # screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        # template = cv2.imread("./tapshot/红点1.png")  # 0.95
        # h, w = template.shape[:2]

        # res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        # threshold = 0.6
        # pos = None

        # loc = np.where(res >= threshold)
        # locs = []
        # pt = None

        # for pt in zip(*loc[::-1]):
        #     if abs(pt[0] - (1041 - int(w / 2))) > 10:
        #         pos = (pt[0] + int(w / 2), pt[1] + int(h / 2))
        #         locs.append(pos)

        # if len(locs) > 0:
        #     pt = random.choice(locs)
        # # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
        # # pt = (max_loc[0] + int(w / 2), max_loc[1] + int(h / 2))
        # if pt:
        #     print(pt)
        #     self.click(*pt)
        #     time.sleep(1)
        #     self.shot = self.UA.screenshot()
        #     self.is_window = self.is_window_box()
        #     if self.is_window:
        #         self.shot = self.window_screenshot()
        #         self.wzsb()
        #     else:
        #         self.step2()

        # np.where返回的坐标值(x,y)是(h,w)，注意h,w的顺序
        # loc = np.where(res >= threshold)
        # # for pt in zip(*loc[::-1]):
        # #     bottom_right = (pt[0] + w, pt[1] + h)
        # #     cv2.rectangle(screenshot, pt, bottom_right, (255, 0, 0), 1)
        # # cv2.imshow('img_rgb', screenshot)
        # # cv2.waitKey(3000)

        # for pt in zip(*loc[::-1]):
        #     homePos = (pt[0] + int(w / 2), pt[1] + int(h / 2))
        #     self.UA.click(*homePos)
        #     self.shot = self.screenshot()
        #     self.step2()
        #     self.UA.click(90, 1868)
        #     break

    # def screenshot(self):
    #     screenshot = self.UA.d.screenshot()
    #     filename = f"./screenshot/screenshot_{time.time()}.png"
    #     if filename:
    #         screenshot.save(filename)
    #     screenshot = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    #     return screenshot

    # def window_screenshot(self):
    #     img = self.UA.d.screenshot()
    #     img = img.crop((85, 259, 1011, 1768))
    #     filename = f"./screenshot/screenshot_{time.time()}.png"
    #     img.save(filename)
    #     image_origin = cv2.imread(filename)
    #     return image_origin

    # def home_screenshot(self):
    #     img = self.UA.d.screenshot()
    #     img = img.crop((0, 0, 1065, 1537))
    #     filename = f"./screenshot/screenshot_{time.time()}.png"
    #     img.save(filename)
    #     image_origin = cv2.imread(filename)
    #     return image_origin

    # # 文字识别
    # def wzsb(self):
    #     screenshot = self.shot
    #     pos = None
    #     wz_list = [
    #         "./tapshot/验证奖励.png",
    #         "./tapshot/一键.png",
    #         "./tapshot/百姓筹办.png",
    #         "./tapshot/日常任务.png",
    #         "./tapshot/宝箱.png",
    #         "./tapshot/红色领取.png",
    #         "./tapshot/领取奖励.png",
    #         "./tapshot/领取.png",
    #         "./tapshot/领取白色.png",
    #         "./tapshot/领取3.png",
    #         "./tapshot/领取4.png",
    #         "./tapshot/对号.png",
    #         "./tapshot/膜拜.png",
    #         "./tapshot/免费.png",
    #         "./tapshot/wdjj.png",
    #         "./tapshot/qd.png",
    #         "./tapshot/qz.png",
    #         "./tapshot/wdgj.png",
    #         "./tapshot/物资补给.png",
    #         # "./tapshot/关闭.png",
    #         # "./tapshot/jf.png",
    #     ]

    #     home = self.UA.find_image_by_screenshot("./tapshot/m1.png", 0.8, screenshot)
    #     if home:
    #         return False

    #     for wz in wz_list:
    #         pos = self.UA.find_image_by_screenshot(wz, 0.8, screenshot)
    #         if pos:
    #             print(wz + ":" + str(pos))

    #         if pos and wz == "./tapshot/qz.png":
    #             self.UA.click(540, 1580)
    #             self.UA.click(872, 430)
    #             self.UA.click(872, 430)
    #             self.cancelPop()
    #             self.cancelPop()
    #         elif pos and wz == "./tapshot/物资补给.png":
    #             self.UA.d.swipe(698, 574, 297, 574, duration=0.1)
    #         elif pos and wz == "./tapshot/日常任务.png":
    #             self.UA.click(306, 639)
    #             self.cancelPop()
    #             self.UA.click(421, 635)
    #             self.cancelPop()
    #             self.UA.click(545, 639)
    #             self.cancelPop()
    #             self.UA.click(654, 639)
    #         elif pos and wz == "./tapshot/wdjj.png":
    #             if self.wdjj == False:
    #                 self.UA.click(400, 800)
    #                 self.cancelPop()
    #                 self.UA.click(630, 800)
    #                 self.cancelPop()
    #                 self.UA.click(855, 800)
    #                 self.cancelPop()
    #                 self.UA.click(980, 865)
    #             self.wdjj = True
    #         elif pos and wz == "./tapshot/wdgj.png":
    #             if self.wdgj == False:
    #                 self.UA.click(347, 792)
    #                 self.cancelPop()
    #                 self.UA.click(606, 794)
    #                 self.cancelPop()
    #                 self.UA.click(867, 806)
    #                 self.cancelPop()
    #                 self.UA.click(979, 864)
    #             self.wdgj = True
    #         elif pos and wz == "./tapshot/jf.png":
    #             if self.jf == False:
    #                 self.UA.click(259, 691)
    #                 self.UA.click(259, 691)
    #                 self.cancelPop()

    #                 self.UA.click(468, 689)
    #                 self.UA.click(468, 689)
    #                 self.cancelPop()

    #                 self.UA.click(675, 698)
    #                 self.UA.click(675, 698)
    #                 self.cancelPop()

    #                 self.UA.click(881, 700)
    #                 self.UA.click(881, 700)
    #                 self.cancelPop()

    #                 self.UA.click(979, 864)
    #             self.jf = True
    #         elif pos and wz == "./tapshot/领取奖励.png":
    #             self.UA.click(528, 1635)
    #             self.UA.click(580, 120)
    #         elif pos and wz == "./tapshot/验证奖励.png":
    #             self.UA.click(542, 1344)
    #             self.UA.passYz()
    #             self.UA.click(542, 1344)
    #         elif pos:
    #             if self.is_window:
    #                 self.UA.click(pos[0] + 85, pos[1] + 259)
    #             else:
    #                 self.UA.click(*pos)

    #             self.cancelPop()

    #     # while True:
    #     #     posYz = self.UA.find_image("./tapshot/验证奖励.png", 0.8)
    #     #     if posYz:
    #     #         self.UA.click(542, 1344)
    #     #         self.UA.passYz()
    #     #         self.UA.click(542, 1344)
    #     #     else:
    #     #         break

    #     if pos:
    #         return True
    #     else:
    #         return False

    # def cancelPop(self):
    #     # self.UA.click(474, 94)
    #     # self.UA.click(34, 1042)
    #     time.sleep(1)
    #     self.UA.click(453, 28)
    #     # self.UA.click(1000, 520)
    #     # self.UA.click(542, 508)
    #     time.sleep(1)

    def step2(self):
        for size in self.resize:
            template = cv2.imread("./tapshot/红点level2-2.png")  # 0.8
            template = cv2.resize(template, (size, size), interpolation=cv2.INTER_CUBIC)
            h, w = template.shape[:2]
            res = cv2.matchTemplate(self.shot, template, cv2.TM_CCOEFF_NORMED)

            threshold = 0.7
            loc = np.where(res >= threshold)
            pos = None
            locs = []
            for pt in zip(*loc[::-1]):
                pos = (pt[0] + int(w / 2), pt[1] + int(h / 2))
                locs.append(pos)

            if len(locs) > 0:
                pos = random.choice(locs)

            print(str(pos) + " -------------- " + str(size))

            # print(len(zip(*loc[::-1])))
            # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
            # pos = (max_loc[0] + int(w / 2), max_loc[1] + int(h / 2))
            if any(zip(*loc[::-1])):
                self.rectangle(loc, size)

            if pos and abs(pos[0] - self.lastClick[0]) > 20:
                self.lastClick = pos
                res2 = self.click(*pos)
                print(str(res2) + "22222222222222222")
                if res2:
                    self.step2()
                else:
                    break

            # for pt in zip(*loc[::-1]):
            #     print(pt)
            #     if pt != self.lastClick:
            #         self.lastClick = pt
            #         homePos = (pt[0] + int(w / 2), pt[1] + int(h / 2))
            #         self.UA.click(*homePos)
            #         time.sleep(1)
            #         self.shot = self.screenshot()
            #         self.step2()
            # break
            # self.UA.click(90, 1868)
