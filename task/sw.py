import time


class Sw:

    def __init__(self, UA):
        self.UA = UA
        # # 初始化到首页
        # self.UA.click(976, 1835)
        # self.UA.click(976, 1835)
        # time.sleep(1)

    def run(self):
        self.mh()
        # self.UA.home()
        # self.sc()
        # self.UA.home()
        # self.fl()
        self.gjf()
        self.m()

    def m(self):
        print("-----马-----")
        self.UA.click(90, 1868)
        self.UA.d.swipe(557, 1270, 557, 670, duration=0.1)
        time.sleep(4)
        self.UA.click(763, 800)
        self.UA.click(162, 305)
        time.sleep(2)
        self.UA.click(162, 305)
        self.UA.click(162, 305)
        for i in range(10):
            self.UA.click(879, 933)
        self.UA.click(73, 1839)

    def gjf(self):
        self.UA.home()
        print("-----装备收集-----")
        self.UA.click(976, 1835)
        time.sleep(4)
        self.UA.click(90, 1868)
        time.sleep(2)
        self.UA.d.swipe(223, 902, 899, 902, duration=0.1)
        time.sleep(2)
        self.UA.d.swipe(223, 902, 899, 902, duration=0.1)
        time.sleep(2)
        self.UA.d.swipe(223, 902, 899, 902, duration=0.1)
        time.sleep(2)
        self.UA.d.swipe(223, 902, 729, 902, duration=0.1)
        time.sleep(2)
        self.UA.d.swipe(550, 704, 550, 1229, duration=0.1)
        time.sleep(2)
        self.UA.click(235, 898)
        self.UA.click(170, 314)
        time.sleep(2)
        self.UA.click(545, 526)
        time.sleep(2)
        for i in range(20):
            self.UA.click(879, 969)
        self.UA.click(64, 1843)
        for i in range(20):
            self.UA.click(433, 992)

    def fl(self):
        # home
        self.UA.click(90, 1868)
        self.UA.click(90, 1868)
        # 福利
        self.UA.click(335, 320)
        # 返利
        # self.UA.click(315, 1023)
        self.UA.top_rest()

        # 签到
        self.UA.click(875, 1833)
        self.UA.click(533, 1612)

        self.UA.click(353, 552)
        self.UA.click(353, 552)
        self.UA.click(528, 547)
        self.UA.click(528, 547)

        self.UA.click(713, 551)
        self.UA.click(713, 551)
        self.UA.click(911, 556)
        self.UA.click(911, 556)

    def sc(self):
        # home
        self.UA.click(90, 1868)
        self.UA.click(90, 1868)
        # 商城
        self.UA.click(211, 311)
        # 物资
        self.UA.click(562, 1843)
        self.UA.click(232, 948)
        self.UA.click(604, 577)
        self.UA.click(247, 887)
        self.UA.click(554, 326)
        # 赛季
        self.UA.click(400, 577)
        self.UA.click(247, 887)
        self.UA.click(554, 326)

        # 每周
        self.UA.click(804, 577)
        self.UA.click(241, 984)
        self.UA.click(557, 391)
        self.UA.click(241, 984)
        self.UA.click(557, 391)

        # 互市港
        self.UA.click(719, 1835)

        for i in range(0, 2):
            self.UA.click(223, 892)
            self.UA.click(545, 443)
            self.UA.click(550, 888)
            self.UA.click(545, 443)
            self.UA.click(846, 881)
            self.UA.click(545, 443)

        # 跨海船队
        self.UA.click(403, 585)

        for i in range(0, 1):
            self.UA.click(244, 892)
            self.UA.click(592, 441)
            self.UA.click(545, 309)
            self.UA.click(528, 881)
            self.UA.click(569, 487)

        self.UA.click(855, 877)
        self.UA.click(550, 485)

        # 活跃商店
        self.UA.click(879, 1835)
        self.UA.click(259, 986)
        self.UA.click(542, 228)

    def mh(self):
        print("-----庙会-----")
        self.UA.home()
        self.UA.click(90, 1868)
        self.UA.click(90, 1868)
        self.UA.click(82, 1430)
        self.UA.click(746, 1526)
        time.sleep(2)
        self.UA.click(90, 1868)
