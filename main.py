# coding: utf-8
import logging
import os.path
import time

from github import Github

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

    g = Github("tain198127@163.com", "bd198127")
    repositories = g.search_repositories("stars:>=800000 language:{}".format(language), "stars", "desc")
    for repo in repositories:
        logger.info("stargazers_count is {}".format(repo.stargazers_count))
    for i in reversed(range(50, 55)):
        filterStr = "stars:{}..{} language:{}".format((i - 1) * 1000 + 1, i * 1000, language)
        time.sleep(1)
        repositories = g.search_repositories(filterStr, "stars", "desc")
        logger.info("{},{},{}".format((i - 1) * 1000 + 1, i * 1000, repositories.totalCount))
    time.sleep(1)
    lessrepo = g.search_repositories("stars:1..1000 language:{}".format(language), "stars", "desc")
    logger.info("{},{},{}".format(1, 1000, lessrepo.totalCount))


# getJavaRepoStartRangeFreq("python")
getRepoStartRangeFreq("JavaScript")

# g = Github("tain198127@163.com", "bd198127")
# lessrepo = g.search_repositories("stars:1..1000 language:php", "stars", "desc")
# logger.info("{},{},{}".format(1, 1000, lessrepo.totalCount))
