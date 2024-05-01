from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--headless')  
# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)


wait = WebDriverWait(driver, 30)

# Function to log in

driver.get("https://webapp4.asu.edu/myasu/")

# Wait until the email input box is available
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

# Find and fill the email input box
email_input = driver.find_element(By.ID, "username")
email_input.send_keys('')

# Find and fill the password input box
password_input = driver.find_element(By.ID, "password")
password_input.send_keys('')

sign_in_button = driver.find_element(By.NAME, "submit")
sign_in_button.click()


WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='duo_iframe']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Send Me a Push']"))).click()

driver.switch_to.default_content()
# time.sleep(30)

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH , "(//a[@title='Spring 2024 Registration'])[1]"))).click()
# registration_button.click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH ,"(//a[@title= 'Swap classes'])[3]"))).click()

try:
    time.sleep(10)
    print('trying to click the old dropdown')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"(//span[contains(text(),'Select from your schedule')]//following::select)[1]"))).click()
    # old_dropdown.click()
    print('clicked')

    # Interact with the old dropdown
    time.sleep(20)
    print('trying to select value in old dropdown')
  
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"(//span[contains(text(),'Select from your schedule')]//following::div)[1]//option[@value = '29797']"))).click()
    # SVVT_cartermc.click()
    print('done')
    time.sleep(5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='DERIVED_REGFRM1_CLASS_NBR']"))).click()
    # Iterate through the new dropdown options
    course_list = ['11088','26559','19657','24342']
    while True :
        for course in course_list:
            print("sending key for class number field")
            print(course)
            time.sleep(5)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='DERIVED_REGFRM1_CLASS_NBR']"))).send_keys(course)

            time.sleep(5)
            #click the 'Next' Button on swap page for first time
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "SSR_SWAP_FL_WRK_SSR_PB_SRCH"))).click()
            print('entered class number moving to next page')

            time.sleep(15)
            
            status = driver.find_element(By.XPATH,"//span[@id = 'DERIVED_SSR_FL_SSR_DESCR50$0']").text
            print(status)

            if status in "Closed" :
                #click on previous
                print('Decreasing time by coming previous on closed seats')
                time.sleep(30)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID,'ASU_SS_GEN_WRK_ASU_PM_PB_RETURN'))).click()
                print('done')

            else :    
                print("seats seem open!\nLet's go!")
                time.sleep(15)
                # Click the 'Next' button
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "PT_NEXT"))).click()

                if course!="19657" :
                    time.sleep(5)
                    # Click the 'Accept' button
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "DERIVED_SSR_FL_SSR_SELECT"))).click()
                
                time.sleep(5)
                # Click the 'Submit' button
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID,"SSR_ENRL_FL_WRK_SUBMIT_PB"))).click()

                time.sleep(5)
                # Click the 'Yes' button
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "#ICYes"))).click()

                # 
                # Click on the 'Swap Classes' div
                print('clicking the swap classes after completing the process')
                time.sleep(20)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@title = 'Swap Classes']"))).click()
                print('done')
                driver.switch_to.default_content()

            #Continuing
            # Recheck the old dropdown
            time.sleep(10)
            print('clicking on the old dropdown again')
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"(//span[contains(text(),'Select from your schedule')]//following::div)[1]"))).click()
            print('done')
            print('value in dd')
            time.sleep(5)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"(//span[contains(text(),'Select from your schedule')]//following::div)[1]//option[@value = '29797']"))).click()
            print('Selected value from DD')

except Exception:
    print("The required element was not found on the page.")

