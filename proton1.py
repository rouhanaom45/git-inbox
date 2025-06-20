import pyautogui
import random
import time
import string
import subprocess

time.sleep(1)

def random_wait(min_time, max_time):
    time.sleep(random.uniform(min_time, max_time))

def random_human_typing(text):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(0.05, 0.2))  # Simulate human typing delay

def random_click_within_rect(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x, y)
    time.sleep(random.uniform(0.1, 0.3))  # Simulate human-like click

def generate_random_name():
    name = ''.join(random.choice(string.ascii_lowercase) + random.choice("aeiou") for _ in range(random.randint(4, 5)))
    return name + str(random.randint(10, 99))

def generate_random_password():
    length = random.randint(9, 11)
    characters = string.ascii_letters + string.digits + ",;!:@."
    return ''.join(random.choice(characters) for _ in range(length))

# Step-by-step script
time.sleep(1.5)
subprocess.run(["bash", "profile1.sh"])
time.sleep(4.5)
pyautogui.click(478, 44)
time.sleep(1)
pyautogui.click(502, 83)
time.sleep(1)
pyautogui.write("https://account.proton.me/mail/signup?plan=free&ref=mail_plus_intro-mailpricing-2")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(12)

# Random click within one of two areas
if random.choice([True, False]):
    random_click_within_rect((30, 322), (163, 558))
else:
    random_click_within_rect((1173, 279), (1296, 556))

random_wait(1, 2)
press_count = random.randint(10, 12)

for i in range(press_count):
    pyautogui.press('down')
    time.sleep(random.uniform(0.3, 0.4))

random_wait(1, 2)
random_click_within_rect((255, 160), (587, 166))
random_wait(0.5, 1.2)

# Write a random name
random_human_typing(generate_random_name())
random_wait(0.8, 1.4)

random_click_within_rect((615, 159), (689, 169))
random_wait(1, 1.5)
random_click_within_rect((625, 199), (724, 238))
random_wait(0.8, 1.4)
random_click_within_rect((252, 244), (574, 255))
random_wait(0.5, 1)

# Write a random password
password = generate_random_password()
random_human_typing(password)
random_wait(1, 2)

random_click_within_rect((35, 286), (140, 461))
random_wait(1, 2)
for _ in range(random.randint(5, 6)):
    pyautogui.press("down")
    time.sleep(random.uniform(0.1, 0.3))

random_click_within_rect((247, 271), (589, 280))
random_wait(1, 2)
# Rewrite the same password
random_human_typing(password)
time.sleep(1)

random_click_within_rect((395, 327), (586, 339))
random_wait(5, 6.5)
pyautogui.click(648, 293)
time.sleep(1)
random_click_within_rect((862, 211), (868, 219))
random_wait(5, 5.6)

subprocess.run(["python3", "bad-traffic.py"])
time.sleep(1)

random_click_within_rect((722, 224), (960, 237))
random_wait(1.5, 2.4)
random_click_within_rect((368, 394), (767, 407))
random_wait(1.5, 2.0)

subprocess.run(["python3", "get-email-adress.py"])
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(random.uniform(0.5, 1))
# Perform a random click within the specified area
random_click_within_rect((435, 483), (808, 502))
random_wait(6.5, 7.5)
pyautogui.click(1079, 628)
time.sleep(1)
pyautogui.click(537, 629)
time.sleep(1)
pyautogui.click(96, 62)
time.sleep(2)
