from  selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import sys
import time
import dateparser

def path(companyName,a,b):
    startDate=dateparser.parse(a).date()
    endDate=dateparser.parse(b).date()
    url = companyName.replace(" ", "-")
    res={
        "url":url,
        "startDate":startDate,
        "endDate":endDate
    }
    
    return res

def main2(params):
    try:
        
        chrome_options = webdriver.ChromeOptions()
        
        chrome_options.add_argument('proxy-server=203.77.215.45:10000')

        browser = uc.Chrome(options=chrome_options)
        
        browser.get("https://www.g2.com/")

        # to slow the input requests so bot don't get blocked from the fast inputs
        time.sleep(2)

        search_box = browser.find_element(By.XPATH, "//input[@placeholder='Search for software, category']")
        print(search_box," Found")
        time.sleep(1)
        search_box.send_keys("slack")
        time.sleep(1)
        
        company = params['url']  # importing the company name
        search_box.send_keys(company)
        time.sleep(1)
        # Press ENTER to search
        browser.find_element(By.XPATH, "//button[@class='submit-search-btn elv-bg-neutral-10']").click()
        time.sleep(2)
         
        carsoul = browser.find_element(By.XPATH,"//body/div[@class='off-canvas-wrapper']/div[@class='off-canvas-wrapper-inner']/div[@class='off-canvas-content']/div[@class='d-f fd-c min-h-full-screen']/div[@class='f-1 fb-a']/div[@class='page paper-padding']/div[@class='grid-x grid-margin-x']/div[@class='cell large-8 xlarge-9']/div[4]")
        time.sleep(4)
        
        main_Page =carsoul.find_element(By.XPATH, "//img[@class='x-deferred-image-initialized']").click()
        time.sleep(5)
        for i in range(10):
            if(i!=0):
                file=main_Page.find_element(By.XPATH,f"//div[@id='survey-response-10760129']//div[@class='paper__bd'][{i}]").get_attribute('outerHTML')
                read_and_write(file,company)
        
        print("file writtenSuccecfully")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Quit browser properly
        browser.quit()

def read_and_write(webElement,companyName):
    try:
        # Open the source file in read mode
        with open(f"{companyName}.json", 'r', encoding='utf-8') as file:
            content = file.read()  # Read all the content from the input file
        
        # Open the target file in write mode (this will overwrite the file if it exists)
        with open(f"{companyName}.json", 'w', encoding='utf-8') as file:
            toWrite = content.push(webElement)
            file.write(toWrite)  # Write the content to the output file

        print(f"Content successfully written to {toWrite}.")

    except Exception as e:
        print(f"Error: {e}")

if __name__=="__main__":
    args=sys.argv
    params=path(args[1],args[2],args[3])
    print(params['url']," ",params['startDate']," ",params['endDate'])
    main2(params)
