import pyautogui
import time
import random
import subprocess
import string

time.sleep(3)
def human_type(text, interval_range=(0.05, 0.15)):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(*interval_range))

def random_click(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(x + random.uniform(-2, 2), y + random.uniform(-2, 2), duration=random.uniform(0.1, 0.4))
    pyautogui.click()

def generate_patterned_name(length=6, with_digits=False):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    name = ''
    for _ in range(length // 2):
        name += random.choice(consonants) + random.choice(vowels)
    if len(name) < length:
        name += random.choice(vowels)
    if with_digits:
        name += f"{random.randint(10, 99)}"
    return name[:length] + (name[length:] if with_digits else '')

def generate_password(length=10):
    chars = string.ascii_letters + string.digits + ",;!:@."
    return ''.join(random.choice(chars) for _ in range(length))

# Start the automation
pyautogui.write("https://kolabnow.com/login")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(9)

random_click((71, 180), (295, 444))
time.sleep(random.uniform(0.5, 1.0))

for _ in range(random.randint(4, 6)):
    pyautogui.press("down")
    time.sleep(0.35)

time.sleep(1)
# 1st Click
random_click((485, 221), (773, 229))
time.sleep(random.uniform(0.5, 1.0))
human_type("kouki@kolabnow.com")  # Fixed email string quotes
time.sleep(random.uniform(0.5, 1.0))
random_click((481, 272), (781, 278))
time.sleep(random.uniform(0.5, 1.0))
human_type("s.iR2fH5ca9FXp2")
time.sleep(random.uniform(0.5, 1.0))
random_click((642, 409), (701, 424))
time.sleep(8)
pyautogui.click(1228, 370)
time.sleep(1.5)
random_click((249, 394), (887, 478))
time.sleep(random.uniform(0.5, 1.0))
pyautogui.hotkey('ctrl', 't')
time.sleep(1)
pyautogui.write("https://kolabnow.com/settings")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(8)
random_click((1171, 472), (1190, 487))
time.sleep(random.uniform(2.5, 3.0))
random_click((531, 440), (891, 448))
time.sleep(random.uniform(0.5, 1.0))
try:
    with open('domain.txt', 'r') as file:
        domains = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print("Error: domain.txt not found")
    exit(1)  # Exit the script if file not found

if not domains:
    print("Error: No domains found in domain.txt")
    exit(1)  # Exit the script if no domains

# Generate name and select random domain
name = generate_patterned_name(length=6, with_digits=True)
domain = random.choice(domains)
email = f"{name}@{domain}"
human_type(email)
time.sleep(1)
with open("email1.txt", "w", encoding="utf-8") as f:
    f.write(email)
time.sleep(1)
random_click((1170, 436), (1190, 452))
time.sleep(random.uniform(2.5, 3.0))

random_click((529, 527), (973, 531))
time.sleep(random.uniform(0.5, 1.0))
human_type("s.iR2fH5ca9FXp2")
time.sleep(random.uniform(0.5, 1.0))
random_click((528, 571), (934, 577))
time.sleep(random.uniform(0.5, 1.0))
human_type("s.iR2fH5ca9FXp2")
time.sleep(random.uniform(0.5, 1.0))
random_click((32, 221), (97, 539))
time.sleep(random.uniform(0.5, 1.0))
for _ in range(random.randint(14, 15)):
    pyautogui.press("down")
    time.sleep(0.35)

time.sleep(1)
random_click((164, 426), (222, 442))
time.sleep(random.uniform(8.5, 9.0))
pyautogui.hotkey('ctrl', 'w')
time.sleep(1.5)
pyautogui.click(96, 63)
time.sleep(7)
random_click((1104, 241), (1203, 339))
time.sleep(random.uniform(5.5, 6.0))
random_click((571, 410), (780, 423))
time.sleep(random.uniform(5.5, 6.0))
time.sleep(1)
subprocess.run(["python", "pret.py"])
time.sleep(2.5)
