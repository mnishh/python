from selenium import webdriver
class run:
    def test_run(self):
         driver = webdriver.Chrome()
         driver.get("https://google.com/")


obj=run()
obj.test_run()