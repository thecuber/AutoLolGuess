import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import loader
from PIL import Image
import io
import numpy as np

loader.local_load()

driver = webdriver.Chrome('./driver/chromedriver')

driver.get('https://lolguess.com')
driver.maximize_window()
time.sleep(2)
#We set the name
driver.find_element(By.ID, 'random').click()
time.sleep(0.5)
driver.find_element(By.CLASS_NAME, 'Bt2').click()
time.sleep(2)
start = driver.find_element(By.ID, 'btnplay')
img = driver.find_element(By.ID, 'bild')
btns = [driver.find_element(By.ID, 'spell' + str(i)) for i in range(2, 6)]
input = driver.find_element(By.ID, 'champ')
start.click()
while True:
    bytes = img.screenshot_as_png
    i = np.array(Image.open(io.BytesIO(bytes)).resize((64, 64)))
    name, index = loader.compare(i).replace('.npy', '').split('---')
    input.send_keys(name)
    btns[int(index)].click()
    time.sleep(0.1)


    
    