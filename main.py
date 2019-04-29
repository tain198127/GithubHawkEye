# coding: utf-8
import os.path

from github import Github
from github import RateLimitExceededException

from DataModule import *
from SmartThreshold import *

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Log等级总开关
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.dirname(os.path.realpath(__file__)) + '/log/'
log_name = log_path + rq + '.log'
logfile = log_name
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.ERROR)  # 输出到file的log等级的开关

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
# 需要每次从文本中读出来


cf = configparser.ConfigParser()
cf.read("./conf/application.conf")

auth = cf.get('github', 'github_token')

github = Github(auth)

RepositoriesModel.create_table()
OwnerModel.create_table()
ContributorModel.create_table()
OrgModel.create_table()
Repo_Owner_Rel.create_table()
Repo_Org_Rel.create_table()
Repo_Contributor_Rel.create_table()
Owner_Org_Rel.create_table()
Contributor_Org_Rel.create_table()
LastQueryConfig.create_table()

lastQueryConfig = None
print(auth)




def printRepository(repository):
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


@SmartThreshold.count_keep_rate(github)
def processOwnerOrgs(owner):
    return owner.get_orgs()


@SmartThreshold.count_keep_rate(github)
def processContributors(repo):
    return repo.get_contributors()


@SmartThreshold.count_keep_rate(github)
def processContributorOrgs(contributor):
    return contributor.get_orgs()


@SmartThreshold.count_keep_rate(github)
def processQuery(filterStr, condition, sort):
    repositories = github.search_repositories(filterStr, condition, "desc")
    for r in repositories:
        processRepo(r)

@SmartThreshold.count_keep_rate(github)
def processRepo(repo):
    global github
    printRepository(repo)
    mysql_db.connection()
    # with mysql_db.atomic():
    # 插入repo
    try:
        # 插入repo
        rm = RepositoriesModel().add_repo(repo)
        # 插入owner
        owner = OwnerModel().add_owner(repo.owner)
        # 增加repo和owner的关系
        Repo_Owner_Rel().add_repoownerrel(Repo_Owner_Rel(RepoID=repo.id, OwnerID=repo.owner.id))

        ownerorgs = processOwnerOrgs(repo.owner)
        if ownerorgs is not None:
            for oo in ownerorgs:
                try:
                    o = OrgModel().add_org(oo)
                    Owner_Org_Rel().add_owner_org_rel(Owner_Org_Rel(OrgID=oo.id, OwnerID=repo.owner.id))
                except Exception as e:
                    logger.error(e)

        contributors = processContributors(repo)
        if contributors is not None:
            for c in contributors[:10]:
                try:
                    # 增加贡献者
                    contributor = ContributorModel().add_contributor(c)
                    # 插入贡献者和repo之间的关系
                    Repo_Contributor_Rel().add_repo_contributor_rel(
                        Repo_Contributor_Rel(RepoID=repo.id, ContributorID=c.id))
                    con_orgs = processContributorOrgs(c)
                    if con_orgs is not None:
                        for org in con_orgs:
                            try:
                                o = OrgModel().add_org(org)
                                # 增加贡献者和org之间的关系
                                # 增加项目和org之间的关系
                                Contributor_Org_Rel().add_contributor_org_rel(
                                    Contributor_Org_Rel(OrgID=o.id, ContributorID=c.id))

                                Repo_Org_Rel().add_repo_org_rel(Repo_Org_Rel(RepoID=repo.id, OrgID=o.id))
                            except Exception as oe:
                                logger.error("error:{}".format(oe))
                except Exception as ce:
                    logger.error("error:{}".format(ce))
    except Exception as re:
        logger.error("error :{}".format(re))
    finally:
        mysql_db.commit()
        mysql_db.close()


# 根据一定的条件获取项目分布
# language:java|php|python|JavaScript
# condition:stars|forks|size
# step: per step,must >1
# min: the min range,must >1
# max: step*max = max range,must > 1
# displayAbove:is display the info more than max
def getRepoRangeFreq(language, condition, steps, min, max, displayAbove):
    global github

    if (displayAbove):
        filterStr = "{}:>={} language:{}".format(condition, (max + 1) * steps, language)
    for i in range(min, max + 1):
        filterStr = "{}:{}..{} language:{}".format(condition, (i - 1) * steps - 1, i * steps, language)
        logger.info(filterStr)
        LastQueryConfig().add_config(LastQueryConfig(startIdx=i, endIdx=max, steps=steps))
        try:
            processQuery(filterStr, condition, "desc")
        except RateLimitExceededException as e:
            time.sleep(60)
            logger.error(e)


# 根据fork获取项目分布
def getRepoForkRangeFreq(language):
    steps = 10
    min = 10
    max = 6000
    cfg = LastQueryConfig().get_last_config()
    if cfg is not None:
        min = cfg.startIdx
        max = cfg.endIdx
        steps = cfg.steps
    logger.info("start: steps:{},")
    getRepoRangeFreq(language, "stars", steps, min, max, False)


if __name__ == '__main__':
    getRepoForkRangeFreq("Java")
