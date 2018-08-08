# coding: utf-8
from github import Github


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


def getStart100000Repo():
    g = Github("tain198127@163.com", "bd198127")
    repositories = g.search_repositories("stars:>10000 language:java", "stars", "desc")
    print("count is :", repositories.totalCount)
    for repository in repositories:
        printRepository(repository)
    # for contributor in repository.get_contributors():
    #     print(contributor)


getStart100000Repo()
