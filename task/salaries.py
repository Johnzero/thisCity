import time


class Salary:
    def __init__(self, UA):
        self.UA = UA
        # 初始化到首页

    def collection(self):
        self.UA.home()
        # 九州
        self.UA.click(980, 1845)
        time.sleep(4)
        self.UA.click(90, 1868)
        time.sleep(4)
        self.UA.d.swipe(550, 704, 550, 1129, duration=0.1)
        time.sleep(2)
        self.UA.d.swipe(902, 1205, 346, 1205, duration=0.1)
        time.sleep(2)
        self.UA.click(8, 1144)
        self.UA.click(170, 1207)
        self.UA.click(365, 1299)
        self.UA.click(267, 971)
        self.UA.click(453, 1063)
        self.UA.click(633, 1155)
        self.UA.click(540, 839)
        self.UA.click(725, 925)
        self.UA.click(916, 1025)
        self.UA.click(814, 698)
        self.UA.click(1000, 787)

    def run(self):
        print("-----采集-----")
        self.collection()
        print("-----俸禄-----")
        self.salary()

    def salary(self):
        self.UA.home()
        self.UA.click(87, 1845)
        self.UA.click(77, 151)
        time.sleep(1)
        self.UA.click(114, 1104)
        self.UA.click(543, 1190)
        self.UA.click(926, 647)
        self.UA.click(766, 1820)  # 跨服榜
        self.UA.click(546, 1570)  # 县邑评分
        self.UA.click(545, 215)

        self.UA.click(927, 1706)  # 税收
        time.sleep(1)
        self.UA.click(927, 1706)
        time.sleep(1)
        self.UA.click(535, 1555)  # 膜拜
        time.sleep(1)
        self.UA.click(528, 46)
        self.UA.click(528, 46)
        time.sleep(1)
        self.UA.click(879, 1835)  # 排行榜
        time.sleep(1)
        self.UA.click(532, 1559)  # 膜拜
        time.sleep(1)
        self.UA.click(543, 1712)
        time.sleep(1)
        self.UA.click(543, 1712)
        time.sleep(1)
        self.UA.click(549, 1562)
        time.sleep(1)
        self.UA.click(739, 1704)
        time.sleep(1)
        self.UA.click(739, 1704)
        time.sleep(1)
        self.UA.click(573, 1562)
        time.sleep(1)
        self.UA.click(912, 1701)
        time.sleep(1)
        self.UA.click(912, 1701)
        time.sleep(1)
        self.UA.click(587, 1549)
        time.sleep(1)
        self.UA.click(1001, 218)
        time.sleep(1)
        self.UA.click(1001, 218)
        time.sleep(1)
        self.UA.click(90, 1841)
