warning-#you can delete this line if you want to run but please read whats below first
#if you want to try to automate email login , I won't recommend it as most email operators will consider it as a security threat and may block your account.
# Try on website that allows automation like Raddit. thanks for your interest.

from selenium import webdriver #imprting libraries
import time as t
from selenium.webdriver.chrome.options import Options
op=Options()
op.add_argument("--disable-notifications") #removes the page notifications

#openning trending page in raddit
driver = webdriver.Chrome('C:\webdrivers/chromedriver',options=op) #path to webdriver folder, you must download it
driver.get('https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2Fsettings')#going to the raddit page
driver.maximize_window()#opening window in maximum
t.sleep(2) #wait 5 seconds

username= driver.find_element_by_xpath("/html/body/div/main/div[1]/div/div[2]/form/fieldset[1]/input")#xpath for username field
username.send_keys("put your reddit username")# putting the username
t.sleep(2)


password=driver.find_element_by_xpath("/html/body/div/main/div[1]/div/div[2]/form/fieldset[2]/input")#xpath for the password field
password.send_keys("put the raddit passsword")

login_button=driver.find_element_by_xpath("/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button")#xpath for login button
login_button.click()#clicking on the button

t.sleep(3)

sett=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/header/div/div[1]/div[1]/button")
sett.click()
t.sleep(3)
popular=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/header/div/div[1]/div[1]/div/a[8]/span")
popular.click()
t.sleep(1)




