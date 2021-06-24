#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def start_chrome():
    # chromedriverのPATHを指定（Pythonファイルと同じフォルダの場合）
    driver_path = './chromedriver'

    # Chrome起動
    driver = webdriver.Chrome(driver_path)
    #driver = webdriver.Chrome(executable_path=driver_path)
    driver.set_window_size(500,500)

    # GoogleログインURL
    url = 'https://www.google.com/accounts?hl=ja-JP'
    driver.get(url)

    return driver

def login_google(driver):#これはなくても良い

    #ログイン情報
    login_id = "[eccアカウントのメールアドレス]"
    login_pw = "[eccアカウントのパスワード]"

    #最大待機時間（秒）
    wait_time = 30

    ### IDを入力
    login_id_xpath = '//*[@id="identifierNext"]'
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, login_id_xpath)))
    driver.find_element_by_name("identifier").send_keys(login_id)
    driver.find_element_by_xpath(login_id_xpath).click()
    # 1秒待機
    time.sleep(1)

    ### パスワードを入力
    login_pw_xpath = '//*[@id="passwordNext"]'
    time.sleep(2)
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, login_pw_xpath)))
    driver.find_element_by_name("password").send_keys(login_pw)
    time.sleep(1) # クリックされずに処理が終わるのを防ぐために追加。
    driver.find_element_by_xpath(login_pw_xpath).click()

def login_form(driver):
    time.sleep(2)
    url="https://forms.office.com/Pages/ResponsePage.aspx?id=T6978HAr10eaAgh1yvlMhF__kSldrNpNvIWhwdsjjRJURUZEVjlIWjM1VjhXMlVaRVJaWVpEVjJZVCQlQCN0PWcu"
    driver.get(url)
    print("ログインページにアクセスしました")
    time.sleep(10)
    EMAILFIELD = (By.ID, "i0116")
    PASSWORDFIELD = (By.ID, "i0118")
    NEXTBUTTON = (By.ID, "idSIButton9")
    login_id = "[10桁@utac.ecc.u-tokyo.ac.jp]"
    login_pw = "[パスワード]"
    #最大待機時間（秒）
    wait_time = 30
    ### IDを入力
    login_id_xpath = '//*[@id="idSIButton9"]'
    # wait for email field and enter email
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(login_id)
    print("IDを入力しました")
    # Click Next
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    print("IDを提出しました")
    time.sleep(7)
    # wait for password field and enter password
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(login_pw)
    driver.find_element_by_id("passwordInput").send_keys(login_pw)
    print("PWを入力しました")
    time.sleep(2)
    # Click Login - same id?
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    driver.find_element_by_id("submitButton").submit()
    print("PWを提出しました")
    time.sleep(6)
    driver.find_element_by_id("idBtn_Back").click()
    print("PWを提出しました")
    time.sleep(6)

def write_form(driver):
    element=driver.find_element_by_name("rc1e8d25040ac4f3d97e729dbef1505b8")
    element.click()#メール
    element = driver.find_element_by_name('r90d51a81a7334f2daef489720c271c85')
    element.click()#キャンパス
    time.sleep(3)
    element = driver.find_element_by_name('r6bc496b7b0df41788aba61d57551f695')
    element.click()#体温  
    time.sleep(3)  
    element = driver.find_elements_by_name('r2c5906bbd69d4b55ae7263ab5b3cb061')
    # print(element)
    # print(len(element))
    # print(element[0])
    if len(element)==1:
        time.sleep(3)
        element = driver.find_elements_by_name('r2c5906bbd69d4b55ae7263ab5b3cb061')
        element[1].click()#症状の有無
    else:
        element[1].click()#症状の有無
    time.sleep(3)
    elem = driver.find_elements_by_class_name("button-content")
    elem[1].click()
    print("Submitted!!!")
    time.sleep(5)
    driver.close()

def main():
    driver = start_chrome() # Chromeを起動
    #login_google(driver) # Googleにログイン
    login_form(driver) # 学内Officeにログイン
    write_form(driver) # Formに記入
