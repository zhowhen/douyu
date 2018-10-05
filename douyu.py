# <--zhowhen-->
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup as bs

class DouYu(unittest.TestCase):

    # 初始化方法
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.number = 0

    # 测试方法，必须以test开头
    def testDouyu(self):
        self.driver.get('https://www.douyu.com/directory/all')
        while True:
            soup = bs(self.driver.page_source, 'lxml')
            # 房间名，返回列表
            names = soup.find_all('h3', {'class': 'ellipsis'})
            # 观看人数，返回列表
            nums = soup.find_all('span', {'class': 'dy-num fr'})
            # zip(name,num)将name和num合并成一个元组：[(1,2),(3,4)]
            for name, num in zip(names, nums):
                print('观众人数：%s\t房间名：%s'% (num.text.strip(), name.text.strip()))
                self.number += 1
            if self.driver.page_source.find('shark-pager-disable-next') != -1:
                break
            self.driver.find_element_by_class_name('shark-pager-next').click()

    # 测试结束执行的方法
    def tearDown(self):
        self.driver.quit()
        print(self.number)

if __name__ == '__main__':
    # 启动测试模块
    unittest.main()