import time


class Hongbao:

    def __init__(self, UA):
        self.UA = UA
        # 初始化到首页
        UA.home()

    def run(self):
        self.UA.click(572, 1706)
        self.UA.click(826, 1854)
        self.UA.click(981, 167)
        # 红包
        self.UA.click(238, 558)
        self.UA.click(533, 1244)
        self.UA.click(533, 216)

        self.UA.click(238, 558)
        self.UA.click(533, 1244)
        self.UA.click(533, 216)

        self.UA.click(238, 558)
        self.UA.click(533, 1244)
        self.UA.click(533, 216)

        self.UA.click(238, 558)
        self.UA.click(533, 1244)
        self.UA.click(533, 216)

        self.UA.click(238, 558)
        self.UA.click(533, 1244)
        self.UA.click(533, 216)
