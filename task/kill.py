import time, random


class Kill:

    def __init__(self, UA):
        self.UA = UA
        # 初始化到九州
        self.UA.click(66, 1845)
        self.UA.click(66, 1845)
        self.UA.click(976, 1835)
        self.UA.click(976, 1835)

    def move(self):
        directions = [
            [219, 631, 883, 639],
            [883, 639, 219, 631],
            [562, 576, 508, 1140],
            [508, 1140, 562, 576],
        ]
        direction = random.choice(directions)
        # direction = directions[2]
        self.UA.d.swipe(
            direction[0], direction[1], direction[2], direction[3], duration=0.1
        )
        time.sleep(1)

    def run(self):
        i = 0
        self.UA.d.click(976, 1835)
        while i < 10:
            pos1 = self.UA.find_image("./tapshot/pj.png", 0.8)
            if pos1:
                self.UA.click(*pos1)
                self.UA.click(548, 1824)
                self.UA.click(548, 1824)
                self.UA.click(356, 1833)
                self.UA.click(737, 1839)
            pos = self.UA.find_image("./tapshot/f.png", 0.8)
            if pos:
                self.UA.click(*pos)
                self.UA.click(548, 1824)
                self.UA.click(356, 1833)
                self.UA.click(737, 1839)

            time.sleep(2)
            self.move()
