import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions


url='http://10.10.9.9:8080/'
username="21721582"
password="Fuckyou!1314"

def is_login():
    try:
        driver=webdriver.Chrome()
        driver.get(url)
        message=driver.find_element(By.ID,'userMessage').text
        driver.quit()
    except exceptions.NoSuchElementException as e:
        print(e.args)
        return False
    else:
        if message == "您已成功连接校园网!":
            return True
        else:
            return False



def login():
    driver = webdriver.Chrome()
    driver.get(url)
    #输入用户名
    driver.find_element(By.ID,'username').click()
    driver.find_element(By.ID, 'username').clear()
    driver.find_element(By.ID, 'username').send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, 'pwd_tip').click()

    driver.find_element(By.ID, 'pwd').send_keys(password)

    driver.find_element(By.ID,'loginLink').click()
    driver.quit()


def main():
    while True:
        if is_login() :
            print("成功登陆")
            time.sleep(6)
        else:
            try:
                login()
                print("成功登陆")
            except Exception as e:
                print("发生错误")
                print(e.args)
                time.sleep(3)



if __name__ == '__main__':
    main()

