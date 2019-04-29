# coding: utf-8
# 限流器
import datetime
import logging
import sys
import threading
import time
from queue import LifoQueue

from apscheduler.schedulers.background import BackgroundScheduler
from github import GithubException

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)

logging.getLogger('apscheduler.scheduler').setLevel(logging.WARNING)

# 最开始的时间
BeginCallTime = datetime.datetime.now()
# 最后一次时间
EndCallTime = datetime.datetime.now()
InvokeTimes = 0
Threshold = [(0, 0), (1.2, 1), (2, 2), (3, 4), (4, 8), (5, 18)]
AllInvokeCount = 0
sleeptime = 0
RATE_LIMIT = 1.4  # 按照1小时5000次计算，每秒钟1.4次计算。
github = None

StatisticBeginTime = datetime.datetime.now()
StatisticEndTime = datetime.datetime.now()

q = LifoQueue(maxsize=100)

scheduler = BackgroundScheduler()


class SmartThreshold:
    # 计时器,同时阻塞调用，保证在1小时以内调用次数低于5000次
    @staticmethod
    def count_keep_rate(*out_args, **out_kwargs):
        global github
        if github is None:
            github = out_args[0]

        def inner_proxy(fn):
            def run(*args, **kwargs):
                global Threshold, InvokeTimes, EndCallTime, AllInvokeCount, BeginCallTime, sleeptime, github

                if sleeptime > 0:
                    logger.info("休眠:{}".format(sleeptime))
                    time.sleep(sleeptime)

                EndCallTime = datetime.datetime.now()
                InvokeTimes = InvokeTimes + 1
                AllInvokeCount = AllInvokeCount + 1
                try:
                    result = fn(*args, **kwargs)
                    return result
                except GithubException.RateLimitExceededException as e:
                    time.sleep(60)
                    logger.error(e)
                # return result

            return run

        return inner_proxy

    # 统计访问速率，如果速率查过一定值，将自动调整等待时间,每10秒统计一次
    @staticmethod
    def dcreaseThreshold():
        global InvokeTimes, sleeptime, BeginCallTime, EndCallTime, github
        # 计算出频率
        if (EndCallTime - BeginCallTime).seconds > 0:
            freq = float(InvokeTimes / (EndCallTime - BeginCallTime).seconds)
        else:
            freq = 0
        # 计算出休眠时间
        sleeptime = round(freq / RATE_LIMIT)
        if github is not None:
            limit = github.get_rate_limit()
            logger.info("limit.core:limit:{},remaining:{},reset:{}".format(limit.core.limit, limit.core.remaining,
                                                                           limit.core.reset))
            logger.info("limit.search:imit:{},remaining:{},reset:{}".format(limit.search.limit, limit.search.remaining,
                                                                            limit.search.reset))
            if limit.core.remaining < 10:
                nowtime = datetime.datetime.utcnow()
                toTime = limit.core.reset
                sleeptime = (toTime - nowtime).seconds
                logger.warning(
                    "limit.core.remaining less than:{} ; will sleep :{} seconds".format(limit.core.remaining,
                                                                                        sleeptime))
            if limit.search.remaining < 3:
                nowtime = datetime.datetime.utcnow()
                toTime = limit.search.reset
                sleeptime = (toTime - nowtime).seconds
                logger.warning(
                    "limit.search.remaining less than:{} ; will sleep :{} seconds".format(limit.search.remaining,
                                                                                          sleeptime))

        # 重置调用次数和时间
        InvokeTimes = 0
        BeginCallTime = datetime.datetime.now()
        print("当前调用速率:{}, 将每次休眠时间调整为:{} 秒".format(freq, sleeptime))

    # 打印统计信息
    @staticmethod
    def show_freq():
        global StatisticBeginTime, StatisticEndTime, AllInvokeCount

        StatisticEndTime = datetime.datetime.now()
        if q.full():
            q.queue.pop()
        q.put((StatisticBeginTime, StatisticEndTime, AllInvokeCount))
        AllInvokeCount = 0
        StatisticBeginTime = datetime.datetime.now()
        if not q.empty():
            for f in q.queue[:10]:
                print("开始时间:{},结束时间:{},间隔时间:{}秒,调用次数:{}".format(f[0], f[1], (f[1] - f[0]).seconds, f[2]))

    @staticmethod
    def threadInovker(job_func):
        print("active count:{}".format(threading.active_count()))
        job_thread = threading.Thread(target=job_func)
        # job_thread.setDaemon(True)
        job_thread.start()

    @staticmethod
    def finalize():
        scheduler.shutdown()
        sys.exit(0)


scheduler.add_job(SmartThreshold.show_freq, 'interval', seconds=60)
scheduler.add_job(SmartThreshold.dcreaseThreshold, 'interval', seconds=10)
scheduler.start()
