import os
import time


content = input('content: ')
while True:
    # 清理屏幕上的输出
    os.system('clear')  # os.system('clear')
    print(content)
    # 休眠200毫秒
    time.sleep(0.2)
    content = content[1:] + content[0]

