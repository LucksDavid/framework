from base.base_page import BasePage

class VehiclePage(BasePage):

    #加当前路径，可以只打开一次浏览器
    current_url = 'http://thygps.com/#/main/realTimeMonitoring/realTimeMonitoring'
    top_nav_name = '//*[@id="main"]/section/section/div/header/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]'
    plateNo = '贵A5989656'
    left_nav_name = '//input[@placeholder]'
    def search(self):
        self.get(self.current_url)
        self.click(self.top_nav_name)
        self.clear(self.left_nav_name)
        self.send_keys(self.plateNo)