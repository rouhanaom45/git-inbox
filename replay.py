import pyautogui
import random
import time
import string
import math
import subprocess

# Enable fail-safe to prevent runaway scripts
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05  # Small base pause for all actions to avoid overloading

# Initial delay to allow user to prepare
time.sleep(3)

def random_wait(min_time, max_time):
    """Generate a random wait time with a slight bias towards natural human pauses."""
    base_time = random.uniform(min_time, max_time)
    # Occasionally add a longer pause to simulate human hesitation
    if random.random() < 0.1:  # 10% chance for a longer pause
        base_time += random.uniform(0.5, 1.5)
    time.sleep(base_time)

def smooth_mouse_move(target_x, target_y, duration=0.5):
    """Move mouse to target with smooth, human-like path using Bezier-like movement."""
    start_x, start_y = pyautogui.position()
    steps = int(duration * 60)  # Assuming 60 FPS for smooth movement
    for i in range(steps + 1):
        t = i / steps
        # Add slight randomness to simulate natural hand movement
        offset_x = random.uniform(-5, 5) if random.random() < 0.3 else 0
        offset_y = random.uniform(-5, 5) if random.random() < 0.3 else 0
        # Quadratic Bezier curve for smooth movement
        x = (1 - t) * start_x + t * target_x + offset_x
        y = (1 - t) * start_y + t * target_y + offset_y
        pyautogui.moveTo(x, y, duration=0.016, tween=pyautogui.easeInOutQuad)
    # Small overshoot and correction to mimic human imprecision
    if random.random() < 0.2:
        pyautogui.moveTo(target_x + random.randint(-10, 10), target_y + random.randint(-10, 10))
        time.sleep(random.uniform(0.05, 0.15))
        pyautogui.moveTo(target_x, target_y, duration=0.1)

def random_human_typing(text):
    """Simulate human typing with variable delays and occasional mistakes."""
    for i, char in enumerate(text):
        # Occasionally pause to simulate thinking
        if random.random() < 0.05 and i > 0:  # 5% chance to pause mid-typing
            time.sleep(random.uniform(0.3, 0.8))
        # Simulate occasional typos (1% chance per character)
        if random.random() < 0.01:
            wrong_char = random.choice(string.ascii_letters)
            pyautogui.write(wrong_char)
            time.sleep(random.uniform(0.1, 0.3))
            pyautogui.press('backspace')
            time.sleep(random.uniform(0.05, 0.15))
        pyautogui.write(char)
        # Variable typing speed with slight bursts
        if random.random() < 0.3:  # 30% chance for faster typing burst
            time.sleep(random.uniform(0.03, 0.1))
        else:
            time.sleep(random.uniform(0.08, 0.25))

def random_click_within_rect(top_left, bottom_right):
    """Click within a rectangle with human-like mouse movement and hesitation."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    # Add small offset to avoid perfect center clicks
    x += random.randint(-5, 5)
    y += random.randint(-5, 5)
    smooth_mouse_move(x, y, duration=random.uniform(0.3, 0.7))
    # Simulate hesitation before click
    if random.random() < 0.15:  # 15% chance to hesitate
        time.sleep(random.uniform(0.1, 0.4))
    pyautogui.click()
    # Small post-click delay to mimic human reaction
    time.sleep(random.uniform(0.05, 0.2))

def generate_random_name():
    """Generate a random name (unchanged from original logic)."""
    name = ''.join(random.choice(string.ascii_lowercase) + random.choice("aeiou") for _ in range(random.randint(4, 5)))
    return name + str(random.randint(10, 99))

def generate_random_password():
    """Generate a random password (unchanged from original logic)."""
    length = random.randint(9, 11)
    characters = string.ascii_letters + string.digits + ",;!:@."
    return ''.join(random.choice(characters) for _ in range(length))

# Random click within one of two areas
if random.choice([True, False]):
    random_click_within_rect((37, 306), (112, 416))
else:
    random_click_within_rect((1211, 393), (1312, 521))

random_wait(1, 2)
press_count = random.randint(14, 15)

for i in range(press_count):
    pyautogui.press('down')
    time.sleep(random.uniform(0.15, 0.3))  # Slightly adjusted for smoother scrolling

random_wait(1, 2)
random_click_within_rect((238, 151), (569, 161))
random_wait(0.7, 1.2)

# Write a random name
random_human_typing(generate_random_name())
random_wait(0.8, 1.4)

random_click_within_rect((641, 156), (720, 162))
random_wait(1, 1.5)
random_click_within_rect((615, 193), (720, 234))
random_wait(0.8, 1.4)
random_click_within_rect((237, 241), (654, 250))
random_wait(0.5, 1)

# Write a random password
password = generate_random_password()
random_human_typing(password)
random_wait(1, 2)

random_click_within_rect((57, 178), (149, 460))
random_wait(1, 2)
for _ in range(random.randint(2, 3)):
    pyautogui.press("down")
    time.sleep(random.uniform(0.1, 0.3))  # Adjusted for smoother scrolling

random_click_within_rect((243, 271), (662, 278))
random_wait(1, 2)
# Rewrite the same password
random_human_typing(password)
time.sleep(1)

random_click_within_rect((383, 326), (568, 340))
random_wait(6, 7)
random_click_within_rect((859, 147), (868, 154))
random_wait(5, 5.6)
