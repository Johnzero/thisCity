class Email:

    def __init__(self, UA):
        self.UA = UA
        # 初始化到首页

    def run(self):
        print("-----好友赠送-----")
        # 好友
        self.UA.click(698, 1607)
        # 领取
        self.UA.click(545, 1574)
        self.UA.click(988, 201)
        self.UA.home()
        print("-----日常-----")
        # 日常
        self.UA.click(804, 1601)
        self.UA.click(693, 1685)
        self.UA.click(693, 1685)
        self.UA.click(540, 1547)
        self.UA.click(297, 635)
        self.UA.click(433, 645)
        self.UA.click(415, 635)
        self.UA.click(542, 647)
        self.UA.click(660, 639)
        self.UA.click(770, 641)
        self.UA.click(884, 635)
        print("-----补给-----")
        # 补给
        self.UA.click(893, 1691)
        self.UA.click(822, 854)
        self.UA.click(814, 1136)
        self.UA.click(981, 337)

        # 返回主界面
        self.UA.click(99, 1843)

        # 邮件 系统
        self.UA.click(905, 1603)
        self.UA.click(748, 1574)
        self.UA.click(335, 1574)
        self.UA.click(509, 418)
        # 邮件 战报
        self.UA.click(923, 1706)
        self.UA.click(923, 1706)
        self.UA.click(743, 1574)
        self.UA.click(335, 1568)

        # 返回主界面
        self.UA.click(90, 1843)
