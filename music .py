import time
import sys

def lyrics():
    lyrics = [
        'Haathon ko sambhale mere haathon mein',
        'Kaise haathon ko sambhale mere haathon mein',
        'Jab tak neend na aaye, inn lakeeron mein baatein ho, haaye',
        'Baatein ho.........',
        'Hayeee'
    ]

    delays = [1.0, 0.1, 1.12, 0.9, 0.8]

    print("Arz kya hai?...........\n")
    time.sleep(1.4)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.08)   # typing effect
        print()               # move to next line AFTER sentence
        time.sleep(delays[i])

lyrics()
