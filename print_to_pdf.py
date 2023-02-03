from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yaml.loader import SafeLoader
import base64

import json

import os
import datetime

def print_to_pdf(compare_portfolio, filename):

    now = datetime.datetime.now()
    dt_string = now.strftime("%d-%m-%Y")

    dt = datetime.datetime.today()
    month_number = dt.month
    year = dt.year

    month_dict = {1: 'January', 2: 'Febuary', 3: 'March',
    4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September',
    10: 'October', 11: 'November', 12: 'December'}

    for key in month_dict:
        if month_number == key:
            month = month_dict[key]
        else:
            msg = "error"

    filepath = "C:\\Users\\Admin\\Downloads\\securityscorecard" + "\\" + month +"_"+ str(year) + "\\"



    # Open the file and load the file
    with open('cred.yaml') as f:
        conf = yaml.load(f, Loader=SafeLoader)

    username = conf['fb_user']['email']
    password = conf['fb_user']['password']

    from selenium import webdriver

    # driver path
    path = 'C:\\Users\\Admin\\PycharmProjects\\pythonProject\\venv\\webautomation\\chromedriver_win32\\chromedriver.exe'
    # we use chrome as a webdriver

    chrome_options = webdriver.ChromeOptions()
    settings = {"recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}], "selectedDestinationId": "Save as PDF", "version": 2}
    prefs= {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}

    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--enable-print-browser')

    browser = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)
    browser.get(compare_portfolio)

    print("login to website")

    # finding username input field by find_element by id and pass username
    browser.find_element("id","username").send_keys(username)
    # finding password input field by find_element by id and pass password
    browser.find_element("id","password").send_keys(password)
    # finding click button by find_element by name and click to login
    browser.find_element("id","login-button").click()

    browser.maximize_window()

    time.sleep(10)

    print("close panel")

    #xpath = "//*[@id=\"root\"]/div/div[1]/div[1]/div[2]/div/div/form/div[2]/div/div[1]/div/button"
    #xpath = "//*[@id=\"root\"]/div/div[1]/div[1]/div[2]/main/div/div/section/div/div/div[1]/div[1]/div[3]/button"

    xpath = "//*[@id=\"root\"]/div/div[1]/div[1]/div[2]/main/div/div/div/div/section/div/div/div[1]/div[1]/div[3]/button/div"

    browser.find_element("xpath", xpath).click()

    time.sleep(5)

    print("print pdf")

    pdf_data = browser.execute_cdp_cmd("Page.printToPDF", settings)

    output_filepath = filepath + str(dt_string) + '_' + filename

    with open(output_filepath, 'wb') as f:
        f.write(base64.b64decode(pdf_data['data']))

    print("close website")

    browser.close()

    return