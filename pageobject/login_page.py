#!/usr/local/bin/python3.9
# coding=utf-8
'''
登录类
'''
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from common import config


class LoginPage(BasePage):
    # 封装页面元素，统一管理
    file_path = "./data/url.ini"
    config_list = config.read_config(file_path)
    current_url = config_list[0][1]
    username_loc = (By.XPATH, "//input[@type='txt']")
    password_loc = (By.XPATH, "//input[@type='password']")
    submit_loc = (By.XPATH, "//input[@type='button']")

    # 封装页面动作，统一管理
    def login_ecshop(self, username, password):
        # self.open_browser()
        # username = 'mrbird'
        # password = '123456qq'
        self.get(self.current_url)
        self.send_keys(self.username_loc, username)
        self.send_keys(self.password_loc, password)
        self.click(self.submit_loc)