from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

config = {
    'EMAIL': '20190208@yopmail.com',
    'PASSWORD': 'accfortest0208'
}

login_url = 'http://www.amazon.com/'

def main():
    driver = webdriver.Chrome()
    driver.get(login_url)


if __name__ == '__main__':
    main()