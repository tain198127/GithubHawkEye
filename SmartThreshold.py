# coding: utf-8
# 限流器
import Queue
import datetime
import logging
import threading
import time

import schedule

# 最开始的时间
BeginCallTime = datetime.datetime.now()
# 最后一次时间
EndCallTime = None
InvokeTimes = 0
Threshold = [(1000, 0.1), (2000, 0.2), (3000, 0.4), (4000, 0.8), (5000, 1.8)]
AllInvokeCount = 0
q = Queue.LifoQueue(maxsize=100)
logger = logging.getLogger()


class SmartThreshold:
    # 计时器,同时阻塞调用，保证在1小时以内调用次数低于5000次
    @staticmethod
    def count_keep_rate(fn):
        def run(*args, **kwargs):
            global Threshold, InvokeTimes, EndCallTime, AllInvokeCount, BeginCallTime
            sleeptime = 0
            start_ts = datetime.datetime.now()
            for t in Threshold:
                if InvokeTimes >= t[0]:
                    sleeptime = t[1]
                else:
                    break
            logger.info("调用次数{}- 休眠时间{}".format(InvokeTimes, sleeptime))
            if sleeptime > 0:
                time.sleep(sleeptime)

            end_ts = datetime.datetime.now()
            EndCallTime = datetime.datetime.now()
            InvokeTimes = InvokeTimes + 1
            AllInvokeCount = AllInvokeCount + 1

            span = (EndCallTime - BeginCallTime).seconds
            # 每60秒插入一次
            if span > 60:
                if q.full():
                    q.queue.pop()
                q.put((BeginCallTime, EndCallTime, AllInvokeCount))
                AllInvokeCount = 0
                BeginCallTime = datetime.datetime.now()
            result = fn(*args, **kwargs)
            return result

        return run

    @staticmethod
    def dcreaseThreshold():
        global InvokeTimes
        if InvokeTimes > 0:
            InvokeTimes = InvokeTimes - 1
        logger.info("调用次数{}".format(InvokeTimes))

    @staticmethod
    def threadInovker(job_func):
        job_thread = threading.Thread(target=job_func)
        job_thread.start()

    @staticmethod
    def show_freq():
        if not q.empty():
            for f in q.queue[:10]:
                print("开始时间:{},结束时间:{},间隔时间:{}秒,调用次数:{}".format(f[0], f[1], (f[1] - f[0]).seconds, f[2]))


schedule.every(1).seconds.do(SmartThreshold.threadInovker, SmartThreshold.dcreaseThreshold)
# 每60秒打印一次
schedule.every(60).seconds.do(SmartThreshold.threadInovker, SmartThreshold.show_freq)


# 守护进程
def deamonInvoker():
    while True:
        schedule.run_pending()
        time.sleep(1)


deamonThread = threading.Thread(target=deamonInvoker)
deamonThread.start()
