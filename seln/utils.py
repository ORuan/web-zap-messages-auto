from selenium import webdriver
import time
import chromedriver_autoinstaller
from seln.config import create_workspace
import uuid
import threading
from core.settings import BASE_DIR
# OA016913717BR
#user_agent = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}


class AutomationWhatsApp():
    def __init__(self, content=False, numbers=False, uuid_user=False):
        self.content = content
        self.numbers = numbers
        if uuid_user == False:
            id_folder = uuid.uuid4()
            self.uuid_user=create_workspace(id_folder)



    def init(self):
        # Check if the current version of chromedriver exists
        try:
            path_install = chromedriver_autoinstaller.install()
        except Exception as err:
            print('Error in instalation', err)

        try:
            options = webdriver.ChromeOptions()
            #options.add_argument('--headless')
            options.add_argument(f'user-data-dir={BASE_DIR}/seln/data/{self.uuid_user}')
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
        except Exception as err:
            print('Error in initialization', err)


    def import_contacts():
        contact, unsaved_Contacts
        Contact = []
        unsaved_Contacts = []
        fp = open("contacts.txt", "r")
        while True:
            line = fp.readline()
            con = ' '.join(line.split())
            if con and con.isdigit():
                unsaved_Contacts.append(int(con))
            elif con:
                Contact.append(con)
            if not line:
                break


    def _open(self):
        driver = self.init()
        driver.execute_script(
            "navigator.__defineGetter__('userAgent', function () {return 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'});")
        driver.execute_script("return navigator.userAgent;")
        return driver

    def send(self, type):
        driver = self._open()
        def text_message(driver):
            try:
                chat_box = driver.find_elements_by_xpath(
                    '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                chat_box[0].send_keys(self.content)
                botao_enviar = driver.find_element_by_xpath(
                    "//span[@data-icon='send']")
                botao_enviar.click()
            except IndexError:
                print('QR code deve ser lido')
                time.sleep(5)
                chat_box = driver.find_elements_by_xpath(
                    '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                chat_box[0].send_keys(self.content)
                botao_enviar = driver.find_element_by_xpath(
                    "//span[@data-icon='send']")
                botao_enviar.click()
            except Exception as err:
                print('Erro no envio da mensagem', err)
                driver.close()

        def send_file(driver):
            doc_filename = f'{BASE_DIR}/oi.pptx'

            # Attachment Drop Down Menu
            clipButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span')
            clipButton.click()
            
            time.sleep(1)
            # To send a Document(PDF, Word file, PPT)
            # This makes sure that gifs, images can be imported through documents folder and they display
            # properly in whatsapp web.
            if doc_filename.split('.')[1]=='pdf'or doc_filename.split('.')[1]=='docx'or doc_filename.split('.')[1]=='pptx':
                try:
                    docButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[3]/button')
                    docButton.click()
                except Exception as err:
                    # Check for traceback errors with XML imports
                    print(err)
            else:
                try: 
                    # IMG attatchment button
                    docButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button')
                    docButton.click()
                except Exception as err:
                    # Check for traceback errors with XML imports
                    print(err)
            time.sleep(1)
            docPath = os.getcwd() + "/Documents/" + doc_filename
            # Changed whatsapp send button xml link.
            whatsapp_send_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
            whatsapp_send_button.click()
            print('File sent')

        def audio_message(driver):
            try:
                btn_audio = driver.find_elements_by_xpath(
                    '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/div/span/button/span')
                chat_box[0].send_keys(self.content)
                botao_enviar = driver.find_element_by_xpath(
                    "//span[@data-icon='send']")
                botao_enviar.click()
            except IndexError:
                print('QR code deve ser lido')
            except Exception as err:
                print('Erro no envio da mensagem', err)

        for number in self.numbers:
            try:
                driver.get(f'https://web.whatsapp.com/send?phone={number}')
                time.sleep(5)
            except IndexError:
                print('Tentando novamente - IndexError:', err)
                time.sleep(3)
            except Exception as err:
                print(err)

            if type==1:
                try:
                    text_message(driver)
                except Exception as err:
                    print(err)
            elif type==2:
                try:
                    audio_message(driver)
                except Exception as err:
                    print(err)
            elif type==3:
                try:
                    send_file(driver)
                except Exception as err:
                    print(err)
            elif type==4:
                pass