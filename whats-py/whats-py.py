__author__='Darsh Patel'


from os import environ
import _thread as thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")

_data = ""

#Webserver For Serving QR code
class _WebServer(BaseHTTPRequestHandler):
    hostPort = environ.get('PORT', '8080')

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-length', str(len(_data)))
        self.end_headers()
        self.wfile.write(bytes(_data, 'utf-8'))


_webServer = HTTPServer(("", int(_WebServer.hostPort)), _WebServer)

try:
    wd = webdriver.Chrome('/usr/bin/chromedriver')
except Exception:
    print("Cannot Import Chromedriver. Please install chromedriver at /usr/bin/chromedriver")
    exit()


def webLogin():
    print("Please scan QR code for whatsapp web on 127.0.0.1:8080 or the chrome window which opened")
    print(" ")

    while True:
        try:
            wd.get("https://web.whatsapp.com")
            print("Waiting For QR Code To Load")
            element = WebDriverWait(wd, 100).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]/div/img')))
        finally:
            print("Found QR Code")
            image_src = wd.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/img').get_attribute('src')
            _data = '<meta http-equiv="refresh" content="5" /><img src="' + image_src + '">'
            print(_data)
            server_thread = thread.start_new_thread(_webServer.serve_forever, ())
            print("Server Started")
        try:
            print('Waiting For Login')
            element = WebDriverWait(wd, 19).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[2]/div/label/input'))
            )
        except Exception:
            print("Not Logged In, Refreshing")
            continue
        print("Logged in!")
        break
    _data = "<h1> Logged Into Whatsapp Account."
    return True


def checkOnline(contact):
    try:
        wd.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/header/div/div[1]/button').click()
    except Exception:
        pass
    sleep(1)
    try:
        wd.find_element_by_xpath('//*[@id="side"]/div[2]/div/button').click()
    except Exception:
        pass
    try:
        textbox= wd.find_element_by_xpath('//*[@id="side"]/div[2]/div/label/input')
        textbox.send_keys(contact)
        sleep(1)
        wd.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[2]/div/div/div[2]').click()
        if wd.find_element_by_class_name('O90ur').text=='online':
            return True
        else:
            return False
    except Exception:
        return False
    return True


def webLogout():
    try:
        wd.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div').click()
        wd.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[6]').click()
        wd.find_element_by_xpath('//*[@id="app"]/div/span[3]/div/div/div/div/div/div/div[3]/div[2]').click()
    except Exception:
        print("Error Logging Out")
        pass

#Whatsapp Limits Outgoing text speed after 50 messages
def sendText(contact, text, times):
    try:
        wd.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/header/div/div[1]/button').click()
    except Exception:
        pass
    sleep(1)
    try:
        wd.find_element_by_xpath('//*[@id="side"]/div[2]/div/button').click()
    except Exception:
        pass
    try:
        textbox= wd.find_element_by_xpath('//*[@id="side"]/div[2]/div/label/input')
        textbox.send_keys(contact)
        sleep(1)
        wd.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[2]/div/div/div[2]').click()
    except Exception:
        pass
    try:
        for x in range(times):
            wd.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(text)
            wd.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    except Exception:
        pass


#TO-DO

def getStatus(contact):
    pass

def getMessages(contact, number):
    pass

