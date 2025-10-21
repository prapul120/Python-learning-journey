import time

for hour in range(0,61):
    for minut in range(0,61):
        for sec in range(1,61):
            print(f"{hour:02}:{minut:02}:{sec:02}")
            time.sleep(1)
print("\n timer finished")
