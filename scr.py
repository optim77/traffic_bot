import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from random import randint
import os

os.system('mode con cols=150 lines=50')

print('                                                                                            ')
print('                                                                                            ')
print('                                              tttt            iiii                          ')
print('                                           ttt:::t           i::::i                         ')
print('                                           t:::::t            iiii                          ')
print('                                           t:::::t                                          ')
print('   ooooooooooo   ppppp   ppppppppp   ttttttt:::::ttttttt    iiiiiii    mmmmmmm    mmmmmmm   ')
print(' oo:::::::::::oo p::::ppp:::::::::p  t:::::::::::::::::t    i:::::i  mm:::::::m  m:::::::mm ')
print('o:::::::::::::::op:::::::::::::::::p t:::::::::::::::::t     i::::i m::::::::::mm::::::::::m')
print('o:::::ooooo:::::opp::::::ppppp::::::ptttttt:::::::tttttt     i::::i m::::::::::::::::::::::m')
print('o::::o     o::::o p:::::p     p:::::p      t:::::t           i::::i m:::::mmm::::::mmm:::::m')
print('o::::o     o::::o p:::::p     p:::::p      t:::::t           i::::i m::::m   m::::m   m::::m')
print('o::::o     o::::o p:::::p     p:::::p      t:::::t           i::::i m::::m   m::::m   m::::m')
print('o::::o     o::::o p:::::p    p::::::p      t:::::t    tttttt i::::i m::::m   m::::m   m::::m')
print('o:::::ooooo:::::o p:::::ppppp:::::::p      t::::::tttt:::::ti::::::im::::m   m::::m   m::::m')
print('o:::::::::::::::o p::::::::::::::::p       tt::::::::::::::ti::::::im::::m   m::::m   m::::m')
print(' oo:::::::::::oo  p::::::::::::::pp          tt:::::::::::tti::::::im::::m   m::::m   m::::m')
print('   ooooooooooo    p::::::pppppppp              ttttttttttt  iiiiiiiimmmmmm   mmmmmm   mmmmmm')
print('                  p:::::p                                                                   ')
print('                  p:::::p                                                                   ')
print('                 p:::::::p                                                                  ')
print('                 p:::::::p                                                                  ')
print('                 p:::::::p                                                                  ')
print('                 ppppppppp                                                                  ')
print('                                                                                            ')
print('Welcome to the script that generates traffic to pages and allows automatically clicking on elements on the page\n\n')
print("Some options to start with")

file = open("p.txt", "a")
file.write("Paste proxies here")
file.close()

# VARIABLES
# ---------------------------------------------------------------------------------------
# Do browser should show up? True or False
headless = True
try:
    headless = input("Program working headless? Default true Y/N:  ")
    if headless == "Y" or headless == "y" or headless == "":
        headless = True
    else:
        headless = False
except Exception as e:
    print("Wrong answer \n " + e)
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# Website to use
website = 'https://www.google.com/'
try:
    website = input("Input website do action: example: https://www.google.com/:  ")
except Exception as e:
    print("Insert right website adress \n" + e)

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# The xpath element should be clicked
try:
    xpath_element_to_click = input('Insert xpath element to localize on website (example(//*[@id="footer-container"]): ')
except Exception as e:
    print("Insert right xpath \n" + str(e))
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------


# Do script click any element? False or True
try:
    click_element = input("Is this element is clickable? Y/N:")
    if click_element == "y" or click_element == "Y":
        click_element = True
    else:
        click_element = False
except Exception as e:
    print("Insert yes or not \n" + str(e))

# xpath_element_to_click = '//*[@id="footer-container"]/div[2]/div/div[1]/div[1]/ul/li[2]/a'
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# Use proxy? False or True
# And set the amount of repeat if there is no proxies
proxy = False
amount = 50
save_working_proxy = False
try:
    d = input("Paste proxy to p.txt file if you want to use them.You want to use proxy?(Default No) Y/N: ")
    if d == "y" or d == "Y":
        print("Using proxy")
        proxy = True

        # Save proxies which working? False or True
        try:
            save_working_proxy = input("Save working proxy? (default: false) Y/N: ")
            if save_working_proxy == "Y" or save_working_proxy == "y":
                save_working_proxy = True
            else:
                save_working_proxy = False
        except Exception as e:
            print("Input right value \n" + str(e))
    else:
        proxy = False
        try:
            amount = int(input("Input the amount of repeat (default 50): ") or 50)
        except Exception as e:
            print("Insert integer value \n" + str(e))
except Exception as e:
    print("Wrong input \n" + str(e))
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# Time in second to timeout after bad connections
try:
    timeout = int(input("Insert timeout in seconds(default 7s):") or 7)
    print()
except Exception as e:
    print("Insert integer value \n" + str(e))





try:
    # create file to save working ip
    if save_working_proxy is True:
        try:
            s = open("working.txt", "w")
        except Exception as sexe:
            print("Cannot create file for working proxies ------" + str(sexe))

    if proxy is False:
        x = 0
        while x <= amount:
            x += 1
            try:
                s = Service(ChromeDriverManager().install())
                # decide to headless or not
                if headless is True:
                    options = ChromeOptions()
                    options.add_argument('--headless')
                    options.add_argument('--disable-gpu')
                    driver = webdriver.Chrome(service=s, chrome_options=options)
                else:
                    driver = webdriver.Chrome(service=s)

                driver.get(website)
                driver.set_page_load_timeout(timeout)
                # Generate human behavior
                driver.execute_script("window.scrollTo(0, {})".format(randint(100, 500)))

                # execute website action
                if click_element is True:
                    element = driver.find_element(By.XPATH, xpath_element_to_click)
                    driver.execute_script("arguments[0].click();", element)

            except Exception as nope:
                print("No proxy method not working" + nope)
                time.sleep(5)


    else:

        with open("p.txt") as f:
            l = list(f)

            for x in l:
                http_proxy = "http://" + x
                https_proxy = "https://" + x
                ftp_proxy = "ftp://" + x
                proxyDict = {
                    "http": http_proxy,
                    "https": https_proxy,
                    "ftp": ftp_proxy
                }
                try:
                    # set chrome to working
                    s = Service(ChromeDriverManager().install())

                    # decide to headless or not
                    if headless is True:
                        options = ChromeOptions()
                        options.add_argument('--headless')
                        options.add_argument('--disable-gpu')
                        driver = webdriver.Chrome(service=s, chrome_options=options)
                    else:
                        driver = webdriver.Chrome(service=s)
                    # set proxy
                    proxy = Proxy()
                    proxy.proxyType = ProxyType.MANUAL
                    proxy.http_proxy = x
                    # proxy.socksProxy = x
                    proxy.ssl_proxy = x
                    cap = webdriver.DesiredCapabilities.CHROME
                    proxy.add_to_capabilities(cap)
                    driver.set_page_load_timeout(timeout)
                    # set website to working
                    driver.get(website)


                    # Generate human behavior
                    driver.execute_script("window.scrollTo(0, {})".format(randint(100, 500)))

                    # execute website action
                    if click_element is True:
                        element = driver.find_element(By.XPATH, xpath_element_to_click)
                        driver.execute_script("arguments[0].click();", element)

                    # with open("working.txt", "a") as w:
                    #	w.write(x)

                    print("PROXY {} WORKING".format(x))
                except Exception as ereq:
                    print("PROXY {} NOT WORKING".format(x))
                    print(ereq)


except Exception as exz:
    print(exz)
    time.sleep(5)
