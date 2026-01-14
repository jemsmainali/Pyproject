import time
import random

texts = [
    "The quick brown fox jumps over the lazy dog",
    "Python programming is fun and powerful",
    "Typing speed improves with practice"
]

text = random.choice(texts)
print("\nType the following text:\n")
print(text)
print("\nStart typing...\n")

start = time.time()
typed = input()
end = time.time()

time_taken = end - start
words = len(typed.split())
wpm = round((words / time_taken) * 60)

print(f"\nTime Taken: {round(time_taken, 2)} seconds")
print(f"Your WPM: {wpm}")
