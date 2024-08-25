from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import google.generativeai as genai
import PIL.Image
import requests
from io import BytesIO

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open the login page
driver.get("https://blsitalypakistan.com/account/login")
time.sleep(4)

# Locate the username and password fields
username_field = driver.find_element(By.XPATH,"""//input[@placeholder="Enter Email"]""")
password_field = driver.find_element(By.NAME, "login_password")

# Enter the username and password
username_field.send_keys("fahadeeeyy@gmail.com")  # Replace with your username
password_field.send_keys("31Octub@r2005")  # Replace with your password

# Locate the CAPTCHA image and download it
captcha_image = driver.find_element(By.ID, "Imageid")
captcha_src = captcha_image.get_attribute("src")
captcha_response = requests.get(captcha_src)
captcha_image = PIL.Image.open(BytesIO(captcha_response.content))

# Save the captcha image to a file (optional, for debugging)
captcha_image.save("captcha.png")

# Use Google's generative AI to solve the CAPTCHA
api_key = "AIzaSyCPv2tYR0g_o5DksfLhTyh_ooX7jOjtG4o"
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-pro')
promot = "Read the CAPTCHA and return only the text or number found in the image."
response = model.generate_content([promot, captcha_image])
captcha_text = response.text.strip()

# Locate the CAPTCHA input field and enter the solved CAPTCHA
captcha_field = driver.find_element(By.NAME, "captcha_code")
captcha_field.send_keys(captcha_text)

# Submit the form
captcha_field.send_keys(Keys.RETURN)

# Wait for a few seconds to see the result
time.sleep(5)

# Optionally, close the browser
