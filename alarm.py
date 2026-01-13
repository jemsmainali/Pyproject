import time
import winsound
import os

def alarm(total_seconds):
    while total_seconds > 0:
        minutes = total_seconds // 60
        seconds = total_seconds % 60

        print(f"\rTime Left: {minutes:02d}:{seconds:02d}", end="")
        time.sleep(1)
        total_seconds -= 1

    print("\n⏰ TIME UP!")

    # Play alarm sound
    for _ in range(5):
        winsound.Beep(1000, 700)
        time.sleep(0.3)


# -------- INPUT --------
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds = minutes * 60 + seconds
alarm(total_seconds)
