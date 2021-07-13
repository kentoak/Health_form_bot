
import pyautogui as pgui
import time
import datetime
import pyperclip
pgui.FAILSAFE=True

def makeKeyEnglish():
    pgui.click(x=1528,y=9,duration=1)#英字にする
    time.sleep(1)
    pgui.click(x=1515,y=33,duration=1)#英字にする

def runAutomator():
    pgui.click(x=1614,y=8,duration=1)#検索バー
    hfa='health_form_auto'
    pyperclip.copy(hfa)
    pgui.hotkey('command', 'v')
    time.sleep(2)
    pgui.hotkey('return')
    time.sleep(650)#700秒メール来るまで待つ

def screenshotHealth():
    pgui.click(x=1570,y=4,duration=1)#gamil
    time.sleep(2)
    pgui.click(x=368,y=209,duration=1)
    time.sleep(2)
    pgui.click(x=1012,y=39,duration=1)
    time.sleep(2)
    d_today = '../healthpics/'+'health-'+str(datetime.date.today()) +'.png'#アンダーバー打てないぽい
    pgui.screenshot(d_today,region=(494,390,1396,1112))
    time.sleep(1)
    pgui.click(x=1621,y=18,duration=1)
    time.sleep(1)
    pgui.click(x=289,y=166,duration=1)

def tweetHealth():
    healthpics='healthpics'
    pyperclip.copy(healthpics)
    pgui.click(x=1614,y=8,duration=1)#検索バー
    time.sleep(1)
    pgui.hotkey('command', 'v')
    #pgui.typewrite(healthpics,0.3)
    time.sleep(3)
    pgui.hotkey('return')
    time.sleep(1)
    pgui.hotkey('option','up')
    pgui.hotkey('option','down')
    pgui.hotkey('command', 'c')
    time.sleep(1)

    pgui.click(x=1614,y=8,duration=1)#検索バー
    time.sleep(2)
    # pgui.hotkey('command', 'a')
    # time.sleep(2)
    pgui.press('backspace')
    pgui.hotkey('return')
    time.sleep(1)
    
    pgui.write("twitter",0.3)
    time.sleep(2)
    pgui.hotkey('return')
    time.sleep(5)
    pgui.click(x=354,y=513,duration=1)
    time.sleep(2)
    pgui.hotkey('command', 'v')
    time.sleep(2)
    date=str(datetime.date.today())
    pyperclip.copy(date)
    pgui.hotkey('command', 'v')
    pgui.click(x=852,y=161,duration=1)#ツイート
    time.sleep(2)
    pgui.click(x=340,y=107,duration=1)

def main():
    makeKeyEnglish()
    runAutomator()
    screenshotHealth()
    tweetHealth()

if __name__=="__main__":
    main()

