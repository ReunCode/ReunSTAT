import time
import sys
import random

choices = ['YA','NA']

print("=== Program ช่วยตัดสินใจถอนรายวิชา ===")
subject = input("\nใส่วิชาที่อยากถอน : ")
input("อยากถอนจิงๆใช่มั้ย(T_T) : ")

result = random.choice(choices)

targets = []
for i in result:
    step = ord(i) - ord('A')
    targets.append(step if step > 0 else 26)

max_step = max(targets)

print()

for step in range(max_step + 1):
    display = ''.join(chr(ord('A') + (min(step, t)%26)) for t in targets)
    delay = 0.05

    sys.stdout.write(f"\rกำลังสุ่มจ้า : {display}")
    sys.stdout.flush()
    time.sleep(delay)

print(f"\n\nผลสรุปสำหรับถอนวิชา : {subject} || ผลลัพธ์ --> {result} <--")

