import pyautogui
import time

x1 = int(input("x1: "))
z1 = int(input("z1: "))
x2 = int(input("x2: "))
z2 = int(input("z2: "))
dist = int(input("dist: "))
y = int(input("y: "))
delay = float(input("time: "))

time.sleep(5)

x = x1
while x <= x2:
    z = z1
    while z <= z2:
        pyautogui.press('t')
        pyautogui.write(f"/tp @p {x} {y} {z}")
        print(f"/tp @p {x} {y} {z}")
        pyautogui.press('enter')

        time.sleep(float(delay))

        z += dist
    x += dist
