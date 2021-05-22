from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os
import mido
import time
from piano import keys,notes
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
 
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://www.onlinepianist.com/virtual-piano")
time.sleep(5)
el = driver.find_element_by_id("keyboardButton")  
ActionChains(driver).move_to_element(el).click().perform()
el = driver.find_element_by_tag_name("body")
pattern = mido.MidiFile(r"E:\nameOfLife.mid")

for msg in pattern.play():
    try:
        if len(notes[msg.note])==3:
           
            el.send_keys(Keys.SHIFT+keys[notes[msg.note]])
            
        else:
            el.send_keys(keys[notes[msg.note]])
    except:
        continue
    
driver.close()