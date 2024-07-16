import time, random
from datetime import datetime, timedelta
import pytesseract
import cv2
from PIL import Image


class Cut:

    def __init__(self, UA):
        self.UA = UA
        # 初始化到九州
        UA.home()
        time.sleep(2)
        self.UA.click(976, 1835)
        self.UA.click(976, 1835)
        self.UA.click(976, 1835)
        time.sleep(4)

    def test(self):
        img = Image.open(self.shot).crop((332, 1305, 486, 1361))
        filename = f"./screenshot/screenshot_{time.time()}.png"
        img.save(filename)
        image_origin = cv2.imread(filename)
        words = pytesseract.image_to_string(image_origin, lang="eng")
        print(words)

    def run(self):
        directions = [
            [219, 631, 883, 639],
            [883, 639, 562, 576],
            [562, 576, 508, 1140],
            [508, 1140, 562, 576],
            [219, 631, 562, 576],
            [562, 576, 883, 639],
            [883, 639, 508, 1140],
            [508, 1140, 219, 631],
        ]
        pos = None
        while pos == None:
            self.UA.screenshot()
            screenshot = self.UA.shot
            pos = self.UA.find_image_by_screenshot(
                "./tapshot/BigFarm.png", 0.8, screenshot
            )
            if pos is None:
                pos = self.UA.find_image_by_screenshot(
                    "./tapshot/7BigFarm.png", 0.8, screenshot
                )
            # if pos is None:
            #     pos = self.UA.find_image_by_screenshot(
            #         "./tapshot/BigWood.png", 0.8, screenshot
            #     )
            # if pos is None:
            #     pos = self.UA.find_image_by_screenshot(
            #         "./tapshot/7BigWood.png", 0.8, screenshot
            #     )
            print(pos)

            pos2 = self.UA.find_image_by_screenshot(
                "./tapshot/验证奖励.png", 0.8, screenshot
            )

            if pos2:
                self.UA.passYZM()
                self.UA.click(542, 1344)

            if pos:
                self.UA.click(*pos)
                time.sleep(2)
                # 分享
                self.UA.click(896, 1340)
                self.UA.click(637, 1441)
                # 采集
                posCut = self.UA.find_image("./tapshot/cut.png", 0.8)
                if posCut:
                    self.UA.click(*posCut)
                    # 补兵
                    self.UA.click(347, 1827)
                    # 切换
                    self.UA.click(984, 1653)
                    self.UA.click(286, 1030)
                    for i in range(10):
                        self.UA.click(230, 787)
                        self.UA.click(318, 743)
                        self.UA.click(315, 902)

                    time.sleep(1)
                    # 返回
                    self.UA.click(497, 34)
                    self.UA.click(78, 1845)
                    time.sleep(1)
                    # 点采集
                    self.UA.click(*pos)
                    time.sleep(1)

                    # log

                    # 前往采集
                    self.UA.click(*posCut)
                    self.UA.click(727, 1827)

                    break
                else:
                    continue
            else:
                direction = random.choice(directions)
                # direction = directions[2]
                self.UA.d.swipe(
                    direction[0], direction[1], direction[2], direction[3], duration=0.1
                )
                time.sleep(1)
