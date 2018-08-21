# coding: utf-8
import logging
import os.path
import time

from github import Github

# db=MySQLDatabase()

logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.dirname(os.path.realpath(__file__)) + '/log/'
log_name = log_path + rq + '.log'
logfile = log_name
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.INFO)  # 输出到file的log等级的开关

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)  # 输出到console的log等级的开关
# 第三步，定义handler的输出格式
# formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
formatter = logging.Formatter("%(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第四步，将logger添加到handler里面
logger.addHandler(ch)
logger.addHandler(fh)
# 日志
logger.debug('this is a logger debug message')

# 思路如下：
# 1.根据stars和folk的数量进行筛选
# 2.

auth = "36827d66490ddbbd09ba07b25fb32144132709e2"


def printRepository(repository):
    print("project owner:", repository.owner)
    print("organization:", repository.organization)
    print("name:", repository.name)
    print("start count:", repository.stargazers_count)
    print("subscribers count:", repository.subscribers_count)
    print("watchers count:", repository.watchers_count)
    print("language:", repository.language)
    print("id:", repository.id)
    print("full name:", repository.full_name)
    print("forks count:", repository.forks_count)
    print("created at:", repository.created_at)
    print("description", repository.description)
    print("=========================================================")


# 获取前3万赞的java项目的数量分布
def getRepoStartRangeFreq(language):
    g = Github(auth)
    repositories = g.search_repositories("stars:>=800000 language:{}".format(language), "stars", "desc")
    for repo in repositories:
        logger.info("stargazers_count is {}".format(repo.stargazers_count))
    for i in reversed(range(1, 101)):
        filterStr = "stars:{}..{} language:{}".format((i - 1) * 1000 + 1, i * 1000, language)
        time.sleep(2)
        repositories = g.search_repositories(filterStr, "stars", "desc")
        logger.info("{},{},{}".format((i - 1) * 1000 + 1, i * 1000, repositories.totalCount))
    time.sleep(2)
    lessrepo = g.search_repositories("stars:1..1000 language:{}".format(language), "stars", "desc")
    logger.info("{},{},{}".format(1, 1000, lessrepo.totalCount))


# 根据一定的条件获取项目分布
# language:java|php|python|JavaScript
# condition:stars|forks|size
# step: per step,must >1
# max: step*max = max range,must > 1
def getRepoRangeFreq(language, condition, steps, max):
    g = Github(auth)
    repositories = g.search_repositories("{}:>={} language:{}".format(condition, (max + 1) * steps, language),
                                         condition, "desc")
    for repo in repositories:
        logger.info("{}_count is {}".format(condition, repo.stargazers_count))
    for i in reversed(range(1, max + 1)):
        filterStr = "{}:{}..{} language:{}".format(condition, (i - 1) * steps + 1, i * steps, language)
        time.sleep(2)
        repositories = g.search_repositories(filterStr, condition, "desc")
        logger.info("{},{},{}".format((i - 1) * steps + 1, i * steps, repositories.totalCount))
    time.sleep(2)
    lessrepo = g.search_repositories("{}:1..{} language:{}".format(condition, steps, language), condition, "desc")
    logger.info("{},{},{}".format(1, steps, lessrepo.totalCount))


# 根据fork获取项目分布
def getRepoForkRangeFreq(language):
    getRepoRangeFreq(language, "forks", 50, 200)


# 获取1000以内的赞的分布
def getRepoStartLess1000RangeFreq(language):
    g = Github("36827d66490ddbbd09ba07b25fb32144132709e2")
    for i in reversed(range(1, 101)):
        filterStr = "stars:{}..{} language:{}".format((i - 1) * 10 + 1, i * 10, language)
        time.sleep(2)
        repositories = g.search_repositories(filterStr, "stars", "desc")
        logger.info("{},{},{}".format((i - 1) * 10 + 1, i * 10, repositories.totalCount))
    time.sleep(2)
    lessrepo = g.search_repositories("stars:1..10 language:{}".format(language), "stars", "desc")
    logger.info("{},{},{}".format(1, 1000, lessrepo.totalCount))


# getRepoStartRangeFreq("java")


# getRepoStartLess1000RangeFreq("JavaScript")

getRepoForkRangeFreq("Java")
