import time


class Zou:

    def __init__(self, UA):
        self.UA = UA
        # 初始化到首页
        UA.home()
        # 州
        self.UA.click(630, 1848)

    def bxzf(self):
        # 宝箱
        self.UA.click(961, 936)
        # 领取
        self.UA.click(746, 1580)
        time.sleep(1)
        self.UA.click(536, 80)
        self.UA.click(536, 80)

        # 捐赠
        self.UA.click(690, 858)

        for i in range(5):
            self.UA.click(320, 1449)
        for i in range(5):
            self.UA.click(758, 1438)

        self.UA.click(339, 698)
        self.cancelPop()

        self.UA.click(540, 700)
        self.cancelPop()

        self.UA.click(722, 698)
        self.cancelPop()

        self.UA.click(899, 695)
        self.cancelPop()

        # 关闭州捐赠
        self.UA.click(991, 314)

    def rwl(self):
        # 任务栏
        self.UA.click(451, 710)

        while True:
            posStepLing = self.UA.find_image("./tapshot/ling.png", 0.8)
            if posStepLing:
                self.UA.click(*posStepLing)
                self.cancelPop()
            else:
                break

        self.UA.click(294, 606)
        self.cancelPop()

        self.UA.click(451, 589)
        self.cancelPop()

        self.UA.click(592, 595)
        self.cancelPop()

        self.UA.click(748, 595)
        self.cancelPop()

        self.UA.click(905, 589)
        self.cancelPop()

        self.UA.click(993, 215)

    def sly(self):
        # 势力院
        self.UA.click(135, 977)
        self.UA.click(991, 314)
        self.UA.click(129, 971)

        self.UA.click(822, 414)
        self.cancelPop()

        self.UA.click(203, 789)
        self.cancelPop()

        self.UA.click(197, 1140)
        self.cancelPop()

        self.UA.click(206, 1378)
        self.cancelPop()

        self.UA.click(743, 1706)
        self.UA.click(545, 1559)
        self.cancelPop()

    def run(self):
        self.bxzf()
        self.rwl()
        self.sly()

    def cancelPop(self):
        time.sleep(2)
        self.UA.click(536, 310)
        time.sleep(1)
