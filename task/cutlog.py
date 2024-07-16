import time, random
import cv2
import pytesseract
import numpy as np
from datetime import datetime, timedelta


class Cutlog:

    def __init__(self, UA):
        self.UA = UA
        # 初始化到九州
        # UA.home()
        # time.sleep(2)
        self.UA.click(976, 1835)
        time.sleep(4)

    def run(self):
        img = self.UA.d.screenshot()
        cut = cv2.imread("./tapshot/cuting.png")
        w, h = cut.shape[:2]

        res = cv2.matchTemplate(np.array(img), cut, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.9)
        for pt in zip(*loc[::-1]):
            print(pt[0] + w, pt[1] + h)
            self.UA.click(pt[0] + int(w / 2), pt[1] + int(h / 2))
            time.sleep(2)
            self.UA.click(536, 958)
            time.sleep(2)

            screen = self.UA.d.screenshot()
            imgtime = screen.crop((935, 1685, 1053, 1722))
            filename = f"./screenshot/screenshot_{time.time()}.png"
            imgtime.save(filename)
            image_origin = cv2.imread(filename)
            t = pytesseract.image_to_string(image_origin, lang="chi_sim")
            if "秒" in t:
                t = t.replace(" ", "")
                t_array = t.split("分")
                t1 = float(int(t_array[0]) / 60)
            else:
                t = t.replace(" ", "").replace("分", "")
                t_array = t.split("时")
                t1 = int(t_array[0]) + float(int(t_array[1]) / 60)

            now = datetime.now()
            future = now + timedelta(hours=t1)

            imgip = screen.crop((332, 1305, 486, 1361))
            filename = f"./screenshot/screenshot_{time.time()}.png"
            imgip.save(filename)
            image_origin = cv2.imread(filename)
            ip = pytesseract.image_to_string(image_origin, lang="eng")

            log = open("./log.txt", "a")
            log.write("\n")
            log.write(str(ip) + str(future))
            log.write("\n")
            log.close()

            self.UA.click(66, 1835)
