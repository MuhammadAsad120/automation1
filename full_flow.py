from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import whisper
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
import google.generativeai as genai
import PIL.Image
import requests
from io import BytesIO
op = Options()
op.add_experimental_option("excludeSwitches",["enable-automation"])
# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome(options=op)

# Open the login page
driver.get("https://blsitalypakistan.com/account/login")


# Locate the username and password fields
username_field = driver.find_element(By.XPATH,"""//input[@placeholder="Enter Email"]""")
password_field = driver.find_element(By.NAME, "login_password")

# Enter the username and password
username_field.send_keys("fahadeeeyy@gmail.com")  # Replace with your username
password_field.send_keys("31Octub@r2005") 
# time.sleep(15) # Replace with your password
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
# # Wait for a few seconds to see the result
book_appointment_button = driver.find_element(By.LINK_TEXT, "Book Appointment")
book_appointment_button.click()
time.sleep(2)
popup = driver.find_element(By.CLASS_NAME, "pop-close")
popup.click()

# try:
#     popup = driver.find_element(By.CLASS_NAME, "pop-close")
#     popup.click()
# except:
select = Select(driver.find_element(By.ID, "valCenterLocationId"))
select.select_by_visible_text("Quetta (Pakistan)")
select = Select(driver.find_element(By.ID, "valCenterLocationTypeId"))
select.select_by_visible_text("Legalisation")
select = Select(driver.find_element(By.ID, "valAppointmentForMembers"))
select.select_by_visible_text("Individual")
av=  driver.find_element(By.ID,"valAppointmentDate")
av.click()
calendar_table = driver.find_element(By.CLASS_NAME, "table-condensed")

# Find all the 'td' elements with the class 'new day label-available'
available_dates = calendar_table.find_elements(By.XPATH, ".//td[@title='Available']")

# Loop through available dates and click on each one
for date in available_dates:
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
    # time.sleep(10)
    av.click()
    date.click()
    break
time.sleep(5)
select = Select(driver.find_element(By.ID, "valAppointmentType"))
select.select_by_visible_text("Normal Time")
firstname= driver.find_element(By.NAME,"""valApplicant[1][first_name]""")
firstname.send_keys("Muhammad")
laSTname= driver.find_element(By.NAME,"""valApplicant[1][last_name]""")
laSTname.send_keys("Ali")
# time.sleep(3)
# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))

# # Click on the reCAPTCHA checkbox
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
# driver.switch_to.default_content()
# time.sleep(3)
# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='recaptcha challenge expires in two minutes']")))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "recaptcha-audio-button"))).click()
# time.sleep(1)
# audio_src = driver.find_element(By.ID, "audio-source").get_attribute("src")
# audio_file = requests.get(audio_src)

# # Save the audio file locally
# with open("captcha_audio.mp3", "wb") as f:
#     f.write(audio_file.content)

# # Load the Whisper model
# model = whisper.load_model("base")

# # Transcribe the audio
# result = model.transcribe("captcha_audio.mp3")

# # Enter the transcription into the text box
# driver.find_element(By.ID, "audio-response").send_keys(result["text"])

# # Submit the form
# driver.find_element(By.ID, "recaptcha-verify-button").click()
# # Switch back to the default content
# driver.switch_to.default_content()
# time.sleep(5)
checkbox = driver.find_element(By.ID,"agree")
# time.sleep(5)
checkbox.click()
# time.sleep(5)
booknow = driver.find_element(By.ID,"valBookNow")
# time.sleep(5)
booknow.click()
time.sleep(5)
p1 = driver.find_element(By.ID,"""cardNumber""")
p2 = driver.find_element(By.NAME, "ValidationCode")

# Enter the username and password
p1.send_keys("2222")  # Replace with your username
p2.send_keys("2222") 

# iframe = driver.find_element(By.XPATH, "//iframe")
# driver.switch_to.frame(iframe)

# # Then locate the audio button
# audio_button = driver.find_element(By.ID, "recaptcha-audio-button")
# audio_button.click()
# # # If there's an audio challenge, switch to the audio challenge
# # audio_button = driver.find_element(By.ID, "recaptcha-audio-button")

# # # Click the audio button
# # audio_button.click()

# # Download the audio file from the CAPTCHA challenge


# # WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='g-recaptcha']")))
    
# #     # Now perform actions inside the frame
# # checkbox = WebDriverWait(driver, 10).until(
# #     EC.element_to_be_clickable((By.CLASS_NAME, "recaptcha-checkbox-checkmark"))
# # )
# # checkbox.click()

# # # If there's an audio challenge, switch to the audio challenge
# # audio_button = WebDriverWait(driver, 10).until(
# #     EC.element_to_be_clickable((By.ID, "recaptcha-audio-button"))
# # )
# # audio_button.click()

# # # Download the audio file from the CAPTCHA challenge
# # audio_src = driver.find_element(By.ID, "audio-source").get_attribute("src")
# # audio_file = requests.get(audio_src)

# # # Save the audio file locally
# # with open("captcha_audio.mp3", "wb") as f:
# #     f.write(audio_file.content)

# # # Load the Whisper model
# # model = whisper.load_model("base")

# # # Transcribe the audio
# # result = model.transcribe("captcha_audio.mp3")

# # # Enter the transcription into the text box
# # driver.find_element(By.ID, "audio-response").send_keys(result["text"])

# # # Submit the form
# # driver.find_element(By.ID, "recaptcha-verify-button").click()
