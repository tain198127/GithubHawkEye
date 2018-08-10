# coding: utf-8
import logging

from github import Github

from DataModule import repositories


def listAllTop100Repo(baseNumStars, language):
    g = Github("36827d66490ddbbd09ba07b25fb32144132709e2")
    repos = g.search_repositories("stars:>={} language:{}".format(baseNumStars, language), "stars", "desc")
    if (repos.totalCount < 100):
        logging.error(
            'The param baseNumStars[{}] is too small, the repos count is {} '.format(baseNumStars, repos.totalCount))
        return
    else:
        top100 = repos[:100]
        for repo in top100:
            print(repo)
            repodb = repositories(repo)
            repodb.owner = repo.owner.name
            repodb.owner_email = repo.owner.email
            repodb.save()


listAllTop100Repo(7000, 'java')
