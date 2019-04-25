# coding: utf-8
# 限流器
import logging
import threading
import time

import schedule

# 5000开始的时间
FirstCallTime = time.time()
EndCall = None
InvokeTimes = 0
Threshold = [(1000, 0.1), (2000, 0.2), (3000, 0.4), (4000, 0.8), (5000, 1.8)]

logger = logging.getLogger()


class SmartThreshold:
    # 计时器,同时阻塞调用，保证在1小时以内调用次数低于5000次
    @staticmethod
    def count_keep_rate(fn):
        def run(*args, **kwargs):
            global Threshold, InvokeTimes, EndCall
            sleeptime = 0
            for t in Threshold:
                if InvokeTimes >= t[0]:
                    sleeptime = t[1]
                else:
                    break
            logger.info("调用次数{}- 休眠时间{}".format(InvokeTimes, sleeptime))
            if sleeptime > 0:
                time.sleep(sleeptime)
            start_ts = time.time()
            end_ts = time.time()
            EndCall = time.time()
            InvokeTimes = InvokeTimes + 1
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


schedule.every(1).seconds.do(SmartThreshold.threadInovker, SmartThreshold.dcreaseThreshold)


# 守护进程
def deamonInvoker():
    while True:
        schedule.run_pending()
        time.sleep(1)


deamonThread = threading.Thread(target=deamonInvoker)
deamonThread.start()
