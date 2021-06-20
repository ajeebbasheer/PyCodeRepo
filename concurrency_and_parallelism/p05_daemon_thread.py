import threading
import time

def kitchen_cleaner():
    while True:
        print("Olivia Cleaned the kitchen.")
        time.sleep(1)

if __name__ == "__main__":
    olivia = threading.Thread(target=kitchen_cleaner)
    olivia.daemon = True
    olivia.start()

    print("Barron is cooking")
    time.sleep(0.6)

    print("Barron is cooking")
    time.sleep(0.6)

    print("Barron is cooking")
    time.sleep(0.6)

    print("Barron is done!")
