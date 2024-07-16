import time
import cv2
import numpy as np


class Redbutton2:

    def __init__(self, UA):
        self.UA = UA
        # 初始化到首页
        # UA.home()

    def screenshot(self):
        screenshot = self.UA.d.screenshot()
        filename = f"./screenshot/screenshot_{time.time()}.png"
        if filename:
            screenshot.save(filename)
        screenshot = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        return screenshot

    def home_screenshot(self):
        img = self.UA.d.screenshot()
        img = img.crop((0, 0, 1065, 1653))
        filename = f"./screenshot/screenshot_{time.time()}.png"
        img.save(filename)
        image_origin = cv2.imread(filename)
        return image_origin

    def home_red(self):
        screenshot = self.home_screenshot()
        posStep = self.UA.find_image_by_screenshot(
            "./tapshot/红点2.png", 0.8, screenshot
        )
        if posStep:
            print("Home :" + str(posStep))
            return posStep
        else:
            return None

    def step2(self, red):
        img = self.UA.d.screenshot()
        filename = f"./screenshot/screenshot_{time.time()}.png"
        img.save(filename)
        screenshot = cv2.imread(filename)
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        template = cv2.imread(red, 0)
        h, w = template.shape[:2]

        res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        # 取匹配程度大于%90的坐标
        threshold = 0.7
        # np.where返回的坐标值(x,y)是(h,w)，注意h,w的顺序
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            ptPos = (pt[0] + int(w / 2), pt[1] + int(h / 2))
            print(str(red) + ":" + str(ptPos))
            self.UA.click(*ptPos)
            time.sleep(1)
            screenshot = self.UA.screenshot()
            res = self.wzsb(screenshot)

    def run(self):
        red_list = [
            "./tapshot/红点2.png",
            "./tapshot/红点level2.png",
            "./tapshot/红点level2-2.png",
        ]
        is_redbutton = False
        pos = self.home_red()
        if pos:
            self.UA.click(*pos)
            time.sleep(1)
            for red in red_list:
                self.step2(red)
            # self.cancelPop()
        else:
            self.UA.home()
            # if res:
            #     screenshot = self.screenshot()

        return

        red_list = [
            "./tapshot/红点2.png",
            "./tapshot/红点level2.png",
            "./tapshot/红点level2-2.png",
            # "./tapshot/红点2.png",
            # "./tapshot/红点level2.png",
            # "./tapshot/red免费.png",
            # "./tapshot/red2.png",
            # "./tapshot/redlq3.png",
            # "./tapshot/redmzwz.png",
            # "./tapshot/redzwb.png",
            # "./tapshot/红点签到.png",
            # # "./tapshot/红色排行榜.png",
            # "./tapshot/红色税收.png",
            # "./tapshot/红色未选择.png",
            # # "./tapshot/redlq.png",
            # # "./tapshot/redlq2.png",
        ]
        for red in red_list:
            posStep = self.UA.find_redimages_by_screenshot(red, 0.78, screenshot)
            print(str(red) + ":" + str(posStep))
            if posStep:
                is_redbutton = True
                self.UA.click(*posStep)
                self.cancelPop()
                # self.UA.click(536, 310)
                screenshot2 = self.UA.screenshot()
                res = self.wzsb(screenshot2)
                pos = self.UA.find_image_by_screenshot(
                    "./tapshot/验证奖励.png", 0.8, screenshot2
                )
                if pos:
                    self.UA.passYz()
                    self.UA.click(542, 1344)
                if res:
                    screenshot = self.screenshot()

        if is_redbutton == False:
            self.UA.home()

    def run1(self):
        # pos = self.UA.find_image_by_screenshot(
        #     "./tapshot/red.png", 0.8, self.UA.screenshot()
        # )
        # self.UA.click(*pos)
        # time.sleep(0.5)
        loop = 0
        while loop < 20:
            is_redbutton = False
            screenshot = self.UA.screenshot()

            posStep = self.UA.find_image_by_screenshot(
                "./tapshot/red.png", 0.8, screenshot
            )
            print("posStep")
            print(posStep)
            # and (posStep[1] < 1770)
            if posStep:
                is_redbutton = True
                self.UA.click(*posStep)
                time.sleep(0.5)
                self.UA.click(536, 310)
                time.sleep(0.5)
                screenshot = self.UA.screenshot()

            res = self.wzsb(screenshot)
            if res:
                screenshot = self.UA.screenshot()

            posStep1 = self.UA.find_image_by_screenshot(
                "./tapshot/redxypf.png", 0.8, screenshot
            )
            print("posStep1")
            print(posStep1)
            if (
                posStep1
                and posStep1[0] != 1041
                and posStep1[0] != 1040
                and posStep1[0] != 1042
            ):
                is_redbutton = True
                self.UA.click(*posStep1)
                self.cancelPop()
                # self.UA.click(525, 80)
                screenshot = self.UA.screenshot()

            # if posStep1 and posStep1[0] == 108:
            #     self.UA.click(76, 1845)

            res = self.wzsb(screenshot)
            if res:
                screenshot = self.UA.screenshot()

            posStep2 = self.UA.find_image_by_screenshot(
                "./tapshot/red2.png", 0.8, screenshot
            )
            print("posStep2")
            print(posStep2)
            if posStep2:
                is_redbutton = True
                self.UA.click(*posStep2)
                self.cancelPop()
                screenshot = self.UA.screenshot()

            posStep3 = self.UA.find_image_by_screenshot(
                "./tapshot/redmzwz.png", 0.9, screenshot
            )
            print("posStep3")
            print(posStep3)
            if posStep3:
                is_redbutton = True
                self.UA.click(*posStep3)
                self.cancelPop()
                screenshot = self.UA.screenshot()

            posStep4 = self.UA.find_image_by_screenshot(
                "./tapshot/redlq.png", 0.8, screenshot
            )
            print("posStep4")
            print(posStep4)
            if posStep4:
                is_redbutton = True
                self.UA.click(*posStep4)
                self.cancelPop()
                screenshot = self.UA.screenshot()

            posStep5 = self.UA.find_image_by_screenshot(
                "./tapshot/redzwb.png", 0.8, screenshot
            )
            print("posStep5")
            print(posStep5)
            if posStep5:
                is_redbutton = True
                self.UA.click(*posStep5)
                self.cancelPop()
                screenshot = self.UA.screenshot()

            posStep6 = self.UA.find_image_by_screenshot(
                "./tapshot/redlq2.png", 0.8, screenshot
            )
            print("posStep6")
            print(posStep6)
            if posStep6:
                is_redbutton = True
                self.UA.click(*posStep6)
                self.cancelPop()
                screenshot = self.UA.screenshot()

            # posStep8 = self.UA.find_image_by_screenshot(
            #     "./tapshot/redlq3.png", 0.8, screenshot
            # )
            # print("posStep8")
            # print(posStep8)
            # if posStep8:
            #     is_redbutton = True
            #     self.UA.click(*posStep8)
            #     self.cancelPop()
            #     screenshot = self.UA.screenshot()

            posStepLing = self.UA.find_image_by_screenshot(
                "./tapshot/ling.png", 0.8, screenshot
            )
            print("posStepLing")
            print(posStepLing)
            if posStepLing:
                self.UA.click(*posStepLing)
                self.cancelPop()
                screenshot = self.UA.screenshot()

            if is_redbutton == False:
                self.UA.home()

            loop = loop + 1

        # while True:
        #     posStep = self.UA.find_image_by_screenshot(
        #         "./tapshot/red2.png", 0.8, self.UA.screenshot()
        #     )
        #     posStep2 = self.UA.find_image_by_screenshot(
        #         "./tapshot/redxypf.png", 0.8, self.UA.screenshot()
        #     )

        #     if posStep is None:
        #         break
        #     else:
        #         self.UA.click(*posStep2)
        #         self.UA.click(536, 310)

        # self.UA.click(*posStep2)
        # self.djfs()

    # 文字识别
    def wzsb(self, screenshot):
        pos = None
        wz_list = [
            "./tapshot/宝箱.png",
            "./tapshot/红色领取.png",
            "./tapshot/领取.png",
            "./tapshot/领取3.png",
            "./tapshot/对号.png",
            "./tapshot/膜拜.png",
            "./tapshot/免费.png",
            "./tapshot/wdjj.png",
            "./tapshot/qd.png",
            "./tapshot/qz.png",
            "./tapshot/wdgj.png",
            # "./tapshot/jf.png",
        ]
        for wz in wz_list:
            pos = self.UA.find_image_by_screenshot(wz, 0.7, screenshot)
            if pos and wz == "./tapshot/qz.png":
                self.UA.click(540, 1580)
                self.cancelPop()
                self.UA.click(872, 430)
                self.cancelPop()
            elif pos and wz == "./tapshot/wdjj.png":
                self.UA.click(400, 800)
                self.cancelPop()
                self.UA.click(630, 800)
                self.cancelPop()
                self.UA.click(855, 800)
                self.cancelPop()
                self.UA.click(980, 865)
            elif pos and wz == "./tapshot/wdgj.png":
                self.UA.click(347, 792)
                self.cancelPop()
                self.UA.click(606, 794)
                self.cancelPop()
                self.UA.click(867, 806)
                self.cancelPop()
                self.UA.click(979, 864)
            elif pos and wz == "./tapshot/jf.png":
                self.UA.click(259, 691)
                self.UA.click(259, 691)
                self.cancelPop()

                self.UA.click(468, 689)
                self.UA.click(468, 689)
                self.cancelPop()

                self.UA.click(675, 698)
                self.UA.click(675, 698)
                self.cancelPop()

                self.UA.click(881, 700)
                self.UA.click(881, 700)
                self.cancelPop()

                self.UA.click(979, 864)
            elif pos:
                self.UA.click(*pos)
                self.cancelPop()

            print(wz + ":" + str(pos))

        if pos:
            return True
        else:
            return False

    def cancelPop(self):
        # self.UA.click(474, 94)
        # self.UA.click(34, 1042)
        time.sleep(0.5)
        self.UA.click(1000, 520)
        # self.UA.click(542, 508)
        time.sleep(0.5)

    def djfs(self):
        self.UA.click(344, 800)
        time.sleep(0.5)
        self.UA.click(536, 310)
        time.sleep(0.5)
        self.UA.click(604, 794)
        time.sleep(0.5)
        self.UA.click(536, 310)
        time.sleep(0.5)
        self.UA.click(860, 789)
        time.sleep(0.5)
        self.UA.click(536, 310)
        time.sleep(0.5)
