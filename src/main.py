from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import UnexpectedAlertPresentException
# user information => email, ID, PW
from userInfo import User
from login import insta_log_in, camp_log_in
from pywinauto.keyboard import send_keys
import time
import datetime

# writing log file
now_time = datetime.datetime.now()
fi = open("./script_log.txt", 'a', encoding='UTF8')
fi.write(str(now_time) + '\n')
fi.close()

# CONSTANTS!
user = User()
INSTA_ID = user.getInstaID()
INSTA_PW = user.getInstaPW()
CAMP_ID = user.getCampID()
CAMP_PW = user.getCampPW()
# "fn_cafeCreateCheck('number','이름','입영일자','생년월일','number','number','number')" 형식의 정보를 직접! 더캠프 홈페이지에서 찾으셔야 합니다...!!
FINDING_CAFE_SCRIPT = "fn_cafeCreateCheck()"
INSTA_URL = "https://www.instagram.com/?hl=ko"
CAMP_URL = "https://www.thecamp.or.kr/eduUnitCafe/viewEduUnitCafeMain.do"

options = webdriver.ChromeOptions()

options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
options.add_argument("window-size=1920x1080")

driver = webdriver.Chrome(options=options)


def alert_accept():
    try:
        alert = driver.switch_to_alert()
        print("alert : " + alert.text)
        time.sleep(0.5)
        if str(alert.text).find("개설된 카페가 있습니다") != -1:
            fi = open("./script_log.txt", 'a', encoding='UTF8')
            fi.write("개설된 카페가 있습니다\n")
            fi.close()
            alert.accept()
            return True
        else:
            alert.accept()
            return False
    except UnexpectedAlertPresentException:
        print("Hum..., continue?")
        return False
    except NoAlertPresentException:
        print("Ummm...no alert...!")
        return False


# log-in THE CAMP and check if my letter address (cafe) was opened!
driver.get(CAMP_URL)
time.sleep(5)
camp_log_in(driver, CAMP_ID, CAMP_PW)
print("checking soldier info...")
driver.execute_script(FINDING_CAFE_SCRIPT)

temp = 0

while True:
    time.sleep(0.5)
    if alert_accept() == True:
        break
    else:
        temp += 1

    if temp == 50:
        print("There's no new cafe... This program will be quit")
        driver.quit()
        quit()

# log-in Instagram and post my letter address
options = webdriver.ChromeOptions()
mobile_emulation = {
    "deviceName": "Galaxy S5"
}
options.add_argument(
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
options.add_argument("window-size=500,10000")
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=options)

driver.get(INSTA_URL)
time.sleep(5)
insta_log_in(driver, INSTA_ID, INSTA_PW)
# to avoid pop up! move to wrong page
driver.get("https://www.instagram.com/data._selenium_py")

# upload image file!
print("selecting image...")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//div[@data-testid="new-post-button"]')))
upload_button = driver.find_element_by_xpath(
    '//div[@data-testid="new-post-button"]')
upload_button.click()
time.sleep(3)
# 인스타에 게시할 사진 경로(절대경로)를 작성해주세요!
send_keys('C:\\Users\\ljjun\\soldier_info.jpg')
time.sleep(1)
send_keys('{VK_RETURN}')
time.sleep(3)
driver.find_element_by_class_name('UP43G').click()
time.sleep(2)

# writing texts
print("writing texts...")
posting_texts = open("./assets/posting_texts.txt", "r", encoding='UTF8')
text_area = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea')
input_form = ActionChains(driver).move_to_element(text_area).click()
input_form.pause(2)

line = posting_texts.readline()
while line:
    input_form.send_keys(line)

    line = posting_texts.readline()

input_form.pause(2)
input_form.send_keys(Keys.ENTER)
input_form.perform()

driver.find_element_by_class_name('UP43G').click()
time.sleep(1)
print("uploaded successfully!")
fi = open("./script_log.txt", 'a', encoding='UTF8')
fi.write("인스타 게시글을 성공적으로 업로드하였습니다\n")
fi.close()
fi = open("./mission_clear.txt", 'w', encoding='UTF8')
fi.write("mission_clear\n")
fi.close()
time.sleep(5)
driver.quit()
