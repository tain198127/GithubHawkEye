# coding: utf-8
from peewee import *
from playhouse.pool import PooledMySQLDatabase

mysql_db = PooledMySQLDatabase('github_hawk_eye', user='root', password='123456',
                               host='127.0.0.1', port=3306)


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
    print("open_issues_count", repository.open_issues_count)
    print("=========================================================")


class BaseModel(Model):
    class Meta:
        database = mysql_db


# Repo 信息
class RepositoriesModel(BaseModel):
    id = IntegerField(primary_key=True)
    name = FixedCharField(128)
    stargazers_count = IntegerField(null=True)
    subscribers_count = IntegerField(null=True)
    watchers_count = IntegerField(null=True)
    language = FixedCharField(64, null=True)
    full_name = TextField(null=True)
    forks_count = IntegerField(null=True)
    created_at = DateField(null=True)
    description = TextField(null=True)
    # downloads_url = FixedCharField(512)
    # git_url = FixedCharField(512)
    # homepage = FixedCharField(512)
    # html_url = FixedCharField(512)
    network_count = IntegerField()
    open_issues_count = IntegerField()

    def add_repo(self, repository):
        if not self.select(RepositoriesModel.id).where(RepositoriesModel.id == repository.id).exists():
            self.id = repository.id
            self.name = repository.name
            self.stargazers_count = repository.stargazers_count
            self.subscribers_count = repository.subscribers_count
            self.watchers_count = repository.watchers_count
            self.language = repository.language
            self.full_name = repository.full_name
            self.forks_count = repository.forks_count
            self.created_at = repository.created_at
            self.description = repository.description
            self.network_count = repository.network_count
            self.open_issues_count = repository.open_issues_count
            printRepository(self)
            self.save(force_insert=True)
            return self
        else:
            return repository


# owner 信息
class OwnerModel(BaseModel):
    id = IntegerField(primary_key=True)
    login = FixedCharField(128)
    name = FixedCharField(128, null=True)
    collaborators = IntegerField(null=True)
    company = FixedCharField(255, null=True)
    created_at = DateField(null=True)
    email = FixedCharField(128, null=True)
    followers = IntegerField(null=True)
    following = IntegerField(null=True)
    hireable = BooleanField(null=True)
    location = TextField(null=True)
    site_admin = BooleanField(null=True)
    type = FixedCharField(128, null=True)
    private_gists = IntegerField(null=True)
    public_gists = IntegerField(null=True)
    public_repos = IntegerField(null=True)
    total_private_repos = IntegerField(null=True)

    def add_owner(self, owner):
        if not self.select(OwnerModel.id).where(OwnerModel.id == owner.id).exists():
            self.id = owner.id
            self.login = owner.login
            self.name = owner.name
            self.collaborators = owner.collaborators
            self.company = owner.company
            self.created_at = owner.created_at
            self.email = owner.email
            self.followers = owner.followers
            self.following = owner.following
            self.hireable = owner.hireable
            self.location = owner.location
            self.site_admin = owner.site_admin
            self.type = owner.type
            self.private_gists = owner.private_gists
            self.public_gists = owner.public_gists
            self.public_repos = owner.public_repos
            self.total_private_repos = owner.total_private_repos
            self.save(force_insert=True)
            return self
        else:
            return owner


# 贡献者
class ContributorModel(BaseModel):
    id = IntegerField(primary_key=True)
    login = FixedCharField(128)
    name = FixedCharField(128, null=True)
    collaborators = IntegerField(null=True)
    company = FixedCharField(255, null=True)
    created_at = DateField(null=True)
    email = FixedCharField(128, null=True)
    followers = IntegerField(null=True)
    following = IntegerField(null=True)
    hireable = BooleanField(null=True)
    location = TextField(null=True)
    site_admin = BooleanField(null=True)
    type = FixedCharField(128, null=True)
    private_gists = IntegerField(null=True)
    public_gists = IntegerField(null=True)
    public_repos = IntegerField(null=True)
    total_private_repos = IntegerField(null=True)

    def add_contributor(self, contributor):
        if not self.select(ContributorModel.id).where(ContributorModel.id == contributor.id).exists():
            self.id = contributor.id
            self.login = contributor.login
            self.name = contributor.name
            self.collaborators = contributor.collaborators
            self.company = contributor.company
            self.created_at = contributor.created_at
            self.email = contributor.email
            self.followers = contributor.followers
            self.following = contributor.following
            self.hireable = contributor.hireable
            self.location = contributor.location
            self.site_admin = contributor.site_admin
            self.type = contributor.type
            self.private_gists = contributor.private_gists
            self.public_gists = contributor.public_gists
            self.public_repos = contributor.public_repos
            self.total_private_repos = contributor.total_private_repos
            self.save(force_insert=True)
            return self
        else:
            return contributor


# 组织模型
class OrgModel(BaseModel):
    id = IntegerField(primary_key=True)
    login = FixedCharField(128)
    name = FixedCharField(128, null=True)
    company = FixedCharField(255, null=True)
    email = FixedCharField(128, null=True)
    billing_email = FixedCharField(128, null=True)
    type = FixedCharField(128, null=True)
    location = TextField(null=True)
    blog = TextField(null=True)
    collaborators = IntegerField(null=True)
    disk_usage = IntegerField(null=True)
    followers = IntegerField(null=True)
    following = IntegerField(null=True)
    private_gists = IntegerField(null=True)
    public_gists = IntegerField(null=True)
    public_repos = IntegerField(null=True)
    total_private_repos = IntegerField(null=True)
    created_at = DateField(null=True)
    updated_at = DateField(null=True)

    def add_org(self, org):
        if not self.select(OrgModel.id).where(OrgModel.id == org.id).exists():
            self.id = org.id
            self.login = org.login
            self.name = org.name
            self.company = org.company
            self.email = org.email
            self.billing_email = org.billing_email
            self.type = org.type
            self.location = org.location
            self.blog = org.blog
            self.collaborators = org.collaborators
            self.disk_usage = org.disk_usage
            self.followers = org.followers
            self.following = org.following
            self.private_gists = org.private_gists
            self.public_gists = org.public_gists
            self.public_repos = org.public_repos
            self.total_private_repos = org.total_private_repos
            self.created_at = org.created_at
            self.updated_at = org.updated_at
            self.save(force_insert=True)
            return self
        else:
            return org


# repo与owner的关系表
class Repo_Owner_Rel(BaseModel):
    RepoID = IntegerField()
    OwnerID = IntegerField()

    class Meta:
        primary_key = CompositeKey('RepoID', 'OwnerID')

    def add_repoownerrel(self, rel):
        self._meta.auto_increment = False
        if not self.select(Repo_Owner_Rel.id).where(
                (Repo_Owner_Rel.RepoID == rel.RepoID) & (
                        Repo_Owner_Rel.OwnerID == rel.OwnerID)
        ).exists():
            self.RepoID = rel.RepoID
            self.OwnerID = rel.OwnerID
            self.save(force_insert=True)


# repo与组织的关系表
class Repo_Org_Rel(BaseModel):
    RepoID = IntegerField()
    OrgID = IntegerField()

    class Meta:
        primary_key = CompositeKey('RepoID', 'OrgID')


# repo与贡献者的关系表
class Repo_Contributor_Rel(BaseModel):
    RepoID = IntegerField()
    ContributorID = IntegerField()

    class Meta:
        primary_key = CompositeKey('RepoID', 'ContributorID')


# owner与贡献者的关系表
class Owner_Org_Rel(BaseModel):
    OwnerID = IntegerField()
    OrgID = IntegerField()

    class Meta:
        primary_key = CompositeKey('OwnerID', 'OrgID')


# 贡献者与组织的关系表
class Contributor_Org_Rel(BaseModel):
    ContributorID = IntegerField()
    OrgID = IntegerField()

    class Meta:
        primary_key = CompositeKey('ContributorID', 'OrgID')
