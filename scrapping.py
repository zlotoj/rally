from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import configuration

DRIVER_PATH = 'c:\\chromedriver.exe'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
url = 'https://rally1.rallydev.com/#/%s/custom/478931066124'
# url = 'https://rally1.rallydev.com/#/%s/reports'
# https://rally1.rallydev.com/#/112919413276d/custom/478931066124

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://rally1.rallydev.com')
elem = driver.find_element_by_name("j_username")
elem.clear()
elem.send_keys(configuration.user)

elem = driver.find_element_by_name("j_password")
elem.clear()
elem.send_keys(configuration.password)
driver.find_element_by_id("login-button").click()
#successfully entered URL_2

# driver.get(url % ('112919413276d'))
# xpath='//*/div[1]/a/img'
# try :
#     time.sleep(7)
#     driver.find_element_by_xpath(xpath).click()
# except:
#     pass
def getCycleTime(project) :
    driver.get(url % (project))
    tryCount=0
    cycleTime=0
    time.sleep(2)
    while tryCount < 7 and cycleTime==0:
        time.sleep(1)
        try:
            cycleTime=driver.find_element_by_xpath('//*/tbody/tr[2]/td[3]/div').text
        except:
            tryCount+=1
    return str(cycleTime)

#getCycleTime()
#driver.quit()