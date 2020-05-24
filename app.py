import time, os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from collections import OrderedDict
import json
from flask import Flask, render_template, Response, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    getnumber = request.form['phonenumber']

    exePath = 'driver/chromedriver.exe'
    logPath = 'driver/chromedriver.log'
    serviceArgs = ['--verbose', '--readable-timestamp', '--append-log']

    service = Service(executable_path=exePath, log_path=logPath, service_args=serviceArgs)
    service.start()
    service.service_url
    service.process.pid

    options = webdriver.ChromeOptions()
    options.add_argument('--profile-directory=pySelenium')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-default-apps')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('-no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--dns-prefetch-disable')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-notifications')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--ignore-urlfetcher-cert-requests')

    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    prefs = {'profile.password_manager_enabled': False, 'credentials_enable_service': False}
    options.add_experimental_option('prefs', prefs)
    caps = options.to_capabilities()
    driver = webdriver.Remote(service.service_url, desired_capabilities=caps)

    # Login truecaller
    driver.get('https://www.truecaller.com/auth/sign-in/')
    #driver.maximize_window()
    time.sleep(5)

    # Login with microsoft
    EMAILFIELD = (By.ID, 'i0116')
    PASSWORDFIELD = (By.ID, 'i0118')
    NEXTBUTTON = (By.ID, 'idSIButton9')
    #driver.get('https://login.live.com')
    driver.get('https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=token&client_id=000000004818BA61&redirect_uri=https://www.truecaller.com/auth/microsoft/callback&scope=openid%20profile%20email%20User.Read%20Contacts.Read')
    #driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys('kallul@hotmail.com')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys('EowynAiza&86')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    time.sleep(5)

    # Now go back to main site for phone number detail
    driver.back()
    page = requests.get("https://www.truecaller.com/")
    page.status_code
    page.content
    #Now parsing truecaller data with beautiful soap
    soup = BeautifulSoup(page.content, 'html.parser')
    #formatted nicely, using the prettify method on the BeautifulSoup object
    soup.prettify()
    list(soup.children)
    [type(item) for item in list(soup.children)]
    html = list(soup.children)[1]
    list(html.children)
    body = list(html.children)[1]
    list(body.children)
    soup.find_all(class_='max-w-sm mx-auto')

    soup.select('div input')
    PHONENUMBER = (By.XPATH, '//*[starts-with(@id, "app")]/nav/div/form/input')
    print(PHONENUMBER)

    soup.select('div button')
    BUTTONSEARCH = (By.XPATH, '//*[starts-with(@id, "app")]/nav/div/form/button')
    print(BUTTONSEARCH)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((PHONENUMBER))).send_keys(getnumber)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((BUTTONSEARCH))).click()

    page = requests.get("https://www.truecaller.com/search/bd/" + getnumber)
    page.status_code
    page.content
    #Now parsing truecaller data with beautiful soap
    soup = BeautifulSoup(page.content, 'html.parser')
    #formatted nicely, using the prettify method on the BeautifulSoup object
    soup.prettify()
    list(soup.children)
    [type(item) for item in list(soup.children)]
    html = list(soup.children)[1]
    list(html.children)
    body = list(html.children)[1]
    list(body.children)
    soup.find_all(class_='max-w-sm mx-auto')

    soup.select('div h1')
    NAMEFINDATT = (By.XPATH, '//*[starts-with(@id, "app")]/main/div/div[1]/div[1]/header/div[2]/h1')
    #if NAMEFINDATT is None:
    #    print('kalke abar try koren')
    try:
        NAMEFIND = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((NAMEFINDATT))).get_attribute("outerHTML")
        print(NAMEFIND)
    except Exception as e:
        #print('kalke abar try koren')
        print("Oops!", e.__class__, "occurred.")

    driver.close()
    driver.quit()
    service.stop()


    html_doc = '''
    <html><head><title>Name: ''' + NAMEFIND + ', Operator:' + 'Operator, email, location and ....' + '''</title></head>
    <body>

    <body>
    <html>
    '''
    soup = BeautifulSoup(html_doc, 'lxml')
    soup.text
    forward_message = (soup.text)
    return render_template('index.html', forward_message=forward_message)



if __name__ == '__main__':
    app.run()