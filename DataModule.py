# coding: utf-8
from peewee import *

mysql_db = MySQLDatabase('github_hawk_eye', user='root', password='123456',
                         host='127.0.0.1', port=3306, charset='utf8')


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


class BaseModel(Model):
    class Meta:
        database = mysql_db


class repositories(BaseModel):
    id = IntegerField(primary_key=True)
    owner = FixedCharField(64)
    owner_email = FixedCharField(64)
    organization = FixedCharField(128)
    name = FixedCharField(128)
    stargazers_count = IntegerField()
    subscribers_count = IntegerField()
    watchers_count = IntegerField()
    language = FixedCharField(64)
    full_name = FixedCharField(64)
    forks_count = IntegerField()
    created_at = DateTimeField()
    description = FixedCharField(512)
    downloads_url = FixedCharField(512)
    git_url = FixedCharField(512)
    homepage = FixedCharField(512)
    html_url = FixedCharField(512)
    network_count = IntegerField()
    open_issues_count = IntegerField()
    size = IntegerField()
