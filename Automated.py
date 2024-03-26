# Goal: I am going to be automating timesheet cause I am tired of doing that shi bruh


#Import all these because you will need to
# pip install selenium 
# pip install webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

#just do this trust you don't really needs lines 17-18, but do it anyways
options = Options()
options.add_experimental_option("detach", True)

#this means we will be using google chrome web browser
web = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

#right here we are giving the url we want to start off at
web.get("issa secret hehe")
#right here we are maximizing the window we open to fit our screen
web.maximize_window()

#now all the varibale names starting here are all for me, these are to show what kind of buttons and links I am going to be pressing

#insert
#when it comes to buttons you will only see it in parts of 2
#the buttons will have the command find element and then the xpath

#filling
#when it comes to filling stuff in it will be parts of 3
#First I will have what I will type in the box as a variable
#then I will find the xpath of where I am going to place it
#lastly I will insert my string into the place I need it

#sleep
#time.sleep so we let the program rest and let the page fully load so it can find the next xpaths
#everyones time will vary mines takes up to 15seconds

#window
#window is when we open up a new window and we want to stay on that specific window and focus on it

#button
ReturnToConnect = web.find_element("xpath", '//*[@id="connectBox"]/button')
ReturnToConnect.click()

#filling
UserId = "no can do buddy"
User = web.find_element('xpath', '//*[@id="username"]')
User.send_keys(UserId)

#filling
PassId = "yeah nah"
Pass = web.find_element('xpath', '//*[@id="password"]')
Pass.send_keys(PassId)

#insert
ConnectButton = web.find_element('xpath', '//*[@id="login-box"]/form/div[3]/button')
ConnectButton.click()

#sleep
time.sleep(15)

#button
DrexelOneButton = web.find_element('xpath','//*[@id="connectBox"]/div[3]/div[1]/div[1]/a')
DrexelOneButton.click()

#sleep
time.sleep(15)

#button
EmployeeButton = web.find_element('xpath', '//*[@id="layout_13"]/a/span')
EmployeeButton.click()

#button
TimeReportingButton = web.find_element('xpath', '//*[@id="emp-info-sortable"]/div[5]/div/div[1]/span/a')
TimeReportingButton.click()

#sleep
time.sleep(15)

#window
web.switch_to.window(web.window_handles[1])

#sleep
time.sleep(15)

#button
TimeSheetButton = web.find_element('xpath', '/html/body/div[3]/table[1]/tbody/tr[1]/td[2]/a')
TimeSheetButton.click()

#sleep
time.sleep(15)

#button
TimeSheetButton2 =web.find_element('xpath', '/html/body/div[3]/form/table[2]/tbody/tr/td/input')
TimeSheetButton2.click() 

#sleep
time.sleep(15)
"""
I was going to use these because these have the same meaning as what we are coding above, but yk I didn't wanna so yuh

WebDriverWait(web, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[1]/td[2]/a'))).click()

WebDriverWait(web, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/form/table[2]/tbody/tr/td/input'))).click()

"""



#NOW WE ARE STARTING THE ACTUAL AUTOMATION PART!
#Part 1

#first step- find the start button day(we only do this step once)
#Second step- find the first box you want to fill and fill that in
#Third step- find the second box you want to fill and fill that in
#fourth step- find the next day button and press that
#fifth step- repeat that step 10 times 

#Part 1.5

#First step- skip saturday, so when you get to saturday just press next day
#Second step- skip sunday, so when you get to sunday just press next day

#Part 2

#First step- Once we are done and stopped at week 2 friday, find the time sheet button and press that
#Second step - find the Previous button so we can back to the previous week
#Third step- review everything and we are finally done. 

#Day 1

MondayPart1Click = web.find_element('xpath', '/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table[1]/tbody/tr[2]/td[8]/div/a')
MondayPart1Click.click()

MondayPart1Box1Time = "9:00"
MondayPart1Box = web.find_element('xpath', '//*[@id="timein_input_id"]')
MondayPart1Box.send_keys(MondayPart1Box1Time)

MondayPart1Box2Time = "11:00"
MondayPart1Box2 = web.find_element('xpath', '//*[@id="timeout_input_id"]')
MondayPart1Box2.send_keys(MondayPart1Box2Time)

NextDayButton1 = web.find_element('xpath', '/html/body/div[3]/form/table[3]/tbody/tr[1]/td/input[3]')
NextDayButton1.click()

#Day 2

TuesdayPart1Box1Time = "9:00"
TuesdayPart1Box = web.find_element('xpath', '//*[@id="timein_input_id"]')
TuesdayPart1Box.send_keys(TuesdayPart1Box1Time)
TuesdayPart1Box2Time = "11:00"
TuesdayPart1Box2 = web.find_element('xpath', '//*[@id="timeout_input_id"]')
TuesdayPart1Box2.send_keys(TuesdayPart1Box2Time)

NextDayButton2 = web.find_element('xpath', '/html/body/div[3]/form/table[3]/tbody/tr[1]/td/input[3]')
NextDayButton2.click()

#Day 3

WednesdayPart1Box1Time = "9:00"
WednesdayPart1Box = web.find_element('xpath', '//*[@id="timein_input_id"]')
WednesdayPart1Box.send_keys(WednesdayPart1Box1Time)
WednesdayPart1Box2Time = "11:00"
WednesdayPart1Box2 = web.find_element('xpath', '//*[@id="timeout_input_id"]')
WednesdayPart1Box2.send_keys(WednesdayPart1Box2Time)

NextDayButton3 = web.find_element('xpath', '/html/body/div[3]/form/table[3]/tbody/tr[1]/td/input[3]')
NextDayButton3.click()

#Day 3

ThursdayPart1Box1Time = "9:00"
ThursdayPart1Box = web.find_element('xpath', '//*[@id="timein_input_id"]')
ThursdayPart1Box.send_keys(ThursdayPart1Box1Time)
ThursdayPart1Box2Time = "11:00"
ThursdayPart1Box2 = web.find_element('xpath', '//*[@id="timeout_input_id"]')
ThursdayPart1Box2.send_keys(ThursdayPart1Box2Time)

NextDayButton4 = web.find_element('xpath', '/html/body/div[3]/form/table[3]/tbody/tr[1]/td/input[3]')
NextDayButton4.click()

#Day 5

FridayPart1Box1Time = "9:00"
FridayPart1Box = web.find_element('xpath', '//*[@id="timein_input_id"]')
FridayPart1Box.send_keys(FridayPart1Box1Time)
FridayPart1Box2Time = "11:00"
FridayPart1Box2 = web.find_element('xpath', '//*[@id="timeout_input_id"]')
FridayPart1Box2.send_keys(FridayPart1Box2Time)

NextDayButton5 = web.find_element('xpath', '/html/body/div[3]/form/table[3]/tbody/tr[1]/td/input[3]')
NextDayButton5.click()

#Weekend Skip

SaturdaySkip = web.find_element('xpath', '/html/body/div[3]/form/table[3]/tbody/tr[1]/td/input[3]')
SaturdaySkip.click()

#Weekend Skip part 2

SundaySkip = web.find_element('xpath', '/html/body/div[3]/form/table[3]/tbody/tr[1]/td/input[3]')
SundaySkip.click()

#Day 6

MondayPart2Box1Time = "9:00"
MondayPart2Box = web.find_element('xpath', '//*[@id="timein_input_id"]')
MondayPart2Box.send_keys(MondayPart2Box1Time)
MondayPart2Box2Time = "11:00"
MondayPart2Box2 = web.find_element('xpath', '//*[@id="timeout_input_id"]')
MondayPart2Box2.send_keys(MondayPart2Box2Time)

NextDayButton6 = web.find_element('xpath', '/html/body/div[3]/form/table[3]/tbody/tr[1]/td/input[3]')
NextDayButton6.click()

#Day 7

TuesdayPart2Box1Time = "9:00"
TuesdayPart2Box = web.find_element('xpath', '//*[@id="timein_input_id"]')
TuesdayPart2Box.send_keys(TuesdayPart2Box1Time)
TuesdayPart2Box2Time = "11:00"
TuesdayPart2Box2 = web.find_element('xpath', '//*[@id="timeout_input_id"]')
TuesdayPart2Box2.send_keys(TuesdayPart2Box2Time)

NextDayButton7 = web.find_element('xpath', '/html/body/div[3]/form/table[3]/tbody/tr[1]/td/input[3]')
NextDayButton7.click()

#Day 8

WednesdayPart2Box1Time = "9:00"
WednesdayPart2Box = web.find_element('xpath', '//*[@id="timein_input_id"]')
WednesdayPart2Box.send_keys(WednesdayPart2Box1Time)
WednesdayPart2Box2Time = "11:00"
WednesdayPart2Box2 = web.find_element('xpath', '//*[@id="timeout_input_id"]')
WednesdayPart2Box2.send_keys(WednesdayPart2Box2Time)

NextDayButton8 = web.find_element('xpath', '/html/body/div[3]/form/table[3]/tbody/tr[1]/td/input[3]')
NextDayButton8.click()

#Day 9

ThursdayPart2Box1Time = "9:00"
ThursdayPart2Box = web.find_element('xpath', '//*[@id="timein_input_id"]')
ThursdayPart2Box.send_keys(ThursdayPart2Box1Time)
ThursdayPart2Box2Time = "11:00"
ThursdayPart2Box2 = web.find_element('xpath', '//*[@id="timeout_input_id"]')
ThursdayPart2Box2.send_keys(ThursdayPart2Box2Time)

NextDayButton9 = web.find_element('xpath', '/html/body/div[3]/form/table[3]/tbody/tr[1]/td/input[3]')
NextDayButton9.click()

#Day 10

FridayPart2Box1Time = "9:00"
FridayPart2Box = web.find_element('xpath', '//*[@id="timein_input_id"]')
FridayPart2Box.send_keys(FridayPart2Box1Time)
FridayPart2Box2Time = "11:00"
FridayPart2Box2 = web.find_element('xpath', '//*[@id="timeout_input_id"]')
FridayPart2Box2.send_keys(FridayPart2Box2Time)

#buttton
BackToTimeSheet = web.find_element('xpath', '/html/body/div[3]/form/table[3]/tbody/tr[1]/td/input[1]')
BackToTimeSheet.click()

#sleep

time.sleep(15)

#Button
PreviousButtom = web.find_element('xpath', '/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table[2]/tbody/tr/td[6]/input')
PreviousButtom.click()

#sleep

time.sleep(15)

#Review Time Sheet for Error(THERE SHOULD BE NONE HAHAHA)