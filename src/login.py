import time

# getting log-in THE CAMP


def camp_log_in(driver, USER_ID, USER_PW):
    print("login start: THE CAMP")
    id_input = driver.find_element_by_xpath(
        '//*[@id="userId"]')
    id_input.click()
    id_input.send_keys(USER_ID)
    time.sleep(0.7)

    pw_input = driver.find_element_by_xpath(
        '//*[@id="userPwd"]')
    pw_input.click()
    pw_input.send_keys(USER_PW)
    time.sleep(0.7)

    login_btn = driver.find_element_by_xpath(
        '//*[@id="emailLoginBtn"]')
    login_btn.click()
    time.sleep(10)

# getting log-in Instagram


def insta_log_in(driver, USER_ID, USER_PW):
    print("login start: Instagram")
    try:
        initial_button = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div/div/div/div[3]/button[1]')
        initial_button.click()
        time.sleep(0.7)
    except:
        time.sleep(0.7)
    id_input = driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div[1]/div[3]/div/label')
    id_input.click()
    id_input.send_keys(USER_ID)
    time.sleep(0.7)

    pw_input = driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div[1]/div[4]/div/label')
    pw_input.click()
    pw_input.send_keys(USER_PW)
    time.sleep(0.7)

    login_btn = driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div[1]/div[6]/button')
    login_btn.click()
    time.sleep(10)
