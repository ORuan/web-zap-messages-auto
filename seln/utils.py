from selenium import webdriver
import pdb
import os
import sys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import requests
import io
import json
import chromedriver_autoinstaller

# OA016913717BR
#user_agent = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}


class AutomationWhatsApp():

    def __init__(self, content=False, numbers=False):
        self.content = content
        self.numbers = numbers

    def config(self):
        # Check if the current version of chromedriver exists
        path_install = chromedriver_autoinstaller.install()
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument("user-data-dir=./data/")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-extensions')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('disable-infobars')
        options.add_argument('lang=pt-br')
        return webdriver.Chrome(
            chrome_options=options,
            executable_path=path_install
        )


    def send(self):
        driver = self.config()
        driver.execute_script(
            "navigator.__defineGetter__('userAgent', function () {return 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'});")
        driver.execute_script("return navigator.userAgent;")
        try:
            driver.get(f'https://web.whatsapp.com/send?phone={self.numbers}')
            time.sleep(5)
        except IndexError:
            print('Tentando novamente:', err)
            time.sleep(3)
        except Exception as err:
            print(err)
            pass

        chat_box = driver.find_elements_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        chat_box[0].send_keys(self.content)
        botao_enviar = driver.find_element_by_xpath(
            "//span[@data-icon='send']")
        botao_enviar.click()
        driver.close()