import threading
import time
import queue

# lock = threading.Lock()
# shared_resource = 0

my_queue = queue.Queue()

def thread_entry(x):
    for i in range(10000):
        # time.sleep(1)
        my_queue.put(f"entry: {i}") # 发送
        print(f"entry_1 working times: {i}")

def thread_entry_2(x):
    while True:
        msg = my_queue.get() # 接受
        if msg is None:
            break
        print(msg)
        my_queue.task_done() # 表明一个任务已完成

thread1 = threading.Thread(target=thread_entry, args=("thread_1", ))
thread2 = threading.Thread(target=thread_entry_2, args=("thread_2",))

thread1.start()
thread2.start()

thread1.join() # 等待线程1完成
my_queue.put(None) # 在线程1完成之后发送NONE表明不在发送数据
thread2.join() # 等待线程2完成
print("all task done")