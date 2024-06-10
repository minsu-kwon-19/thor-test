import time
import traceback

if __name__ == '__main__':
    cnt = 0
    while cnt < 900:
        try:
            print(f"[Version 1.0] Count : {cnt}")
            cnt += 1
            time.sleep(2)
        except KeyboardInterrupt:
            print("Input Ctrl + C !")
            break
        except:
            print(traceback.print_exc())
            break