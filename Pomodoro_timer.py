import time

# later add match/case and alarm 

def format_time(work_sec):
    minutes = work_sec // 60
    seconds = work_sec % 60
    return f"{minutes:02d}:{seconds:02d}"

def main():
    WORK_MIN = 10
    BREAK_MIN = 10
    work_sec = WORK_MIN * 60
    work_sec = int(work_sec)
   
    print("Pomodoro Timer")
    while work_sec != 0:
        print(f"\r{format_time(work_sec)}", end="")
        time.sleep(1)
        work_sec -= 1
       
if __name__ == "__main__":
    main()
