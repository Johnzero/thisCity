import time, random
import cv2
import numpy as np


class Logtime:

    def __init__(self, UA):
        self.UA = UA
        # 初始化到九州
        # UA.home()
        # time.sleep(2)
        # self.UA.click(976, 1835)
        # self.UA.click(976, 1835)
        # time.sleep(2)

    def run(self):
        pos = None
        img = cv2.imread("./tapshot/work.png")
        tw, th = img.shape[:2]
        res = cv2.matchTemplate(self.UA.screenshot(), img, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        print(loc)
        # # +int(tw/4) +int(th/4)
        # if len(loc[0]) > 0:
        #     return (loc[1][0] + int(tw / 2)), (loc[0][0] + int(th / 2))
