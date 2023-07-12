import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration * 60  # 将分钟转换为秒

    while time.time() < end_time:
        remaining_time = round(end_time - time.time())
        print(f"Remaining time: {remaining_time} seconds", end="\r")
        time.sleep(1)

    print("Focus timer complete!")

# 设置专注时钟的持续时间（以分钟为单位）
duration_minutes = 25

focus_timer(duration_minutes)
