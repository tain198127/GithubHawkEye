SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS  `repo_contributor_rel`;
CREATE TABLE `repo_contributor_rel` (
  `RepoID` int(11) NOT NULL,
  `ContributorID` int(11) NOT NULL,
  PRIMARY KEY (`RepoID`,`ContributorID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS  `contributormodel`;
CREATE TABLE `contributormodel` (
  `id` int(11) NOT NULL,
  `login` char(128) NOT NULL,
  `name` char(128) DEFAULT NULL,
  `collaborators` int(11) DEFAULT NULL,
  `company` char(255) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `email` char(128) DEFAULT NULL,
  `followers` int(11) DEFAULT NULL,
  `following` int(11) DEFAULT NULL,
  `hireable` tinyint(1) DEFAULT NULL,
  `location` mediumtext,
  `site_admin` tinyint(1) DEFAULT NULL,
  `type` char(128) DEFAULT NULL,
  `private_gists` int(11) DEFAULT NULL,
  `public_gists` int(11) DEFAULT NULL,
  `public_repos` int(11) DEFAULT NULL,
  `total_private_repos` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS  `repo_org_rel`;
CREATE TABLE `repo_org_rel` (
  `RepoID` int(11) NOT NULL,
  `OrgID` int(11) NOT NULL,
  PRIMARY KEY (`RepoID`,`OrgID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS  `repositoriesmodel`;
CREATE TABLE `repositoriesmodel` (
  `id` int(11) NOT NULL,
  `name` char(128) NOT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `subscribers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `language` char(64) DEFAULT NULL,
  `full_name` mediumtext,
  `forks_count` int(11) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `description` mediumtext,
  `network_count` int(11) DEFAULT NULL,
  `open_issues_count` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS  `orgmodel`;
CREATE TABLE `orgmodel` (
  `id` int(11) NOT NULL,
  `login` char(128) NOT NULL,
  `name` char(128) DEFAULT NULL,
  `company` char(255) DEFAULT NULL,
  `email` char(128) DEFAULT NULL,
  `billing_email` char(128) DEFAULT NULL,
  `type` char(128) DEFAULT NULL,
  `location` mediumtext,
  `blog` mediumtext,
  `collaborators` int(11) DEFAULT NULL,
  `disk_usage` int(11) DEFAULT NULL,
  `followers` int(11) DEFAULT NULL,
  `following` int(11) DEFAULT NULL,
  `private_gists` int(11) DEFAULT NULL,
  `public_gists` int(11) DEFAULT NULL,
  `public_repos` int(11) DEFAULT NULL,
  `total_private_repos` int(11) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `updated_at` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS  `repo_owner_rel`;
CREATE TABLE `repo_owner_rel` (
  `RepoID` int(11) NOT NULL,
  `OwnerID` int(11) NOT NULL,
  PRIMARY KEY (`RepoID`,`OwnerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS  `lastqueryconfig`;
CREATE TABLE `lastqueryconfig` (
  `id` int(11) NOT NULL,
  `startIdx` int(11) NOT NULL,
  `steps` int(11) NOT NULL,
  `endIdx` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS  `ownermodel`;
CREATE TABLE `ownermodel` (
  `id` int(11) NOT NULL,
  `login` char(128) NOT NULL,
  `name` char(128) DEFAULT NULL,
  `collaborators` int(11) DEFAULT NULL,
  `company` char(255) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `email` char(128) DEFAULT NULL,
  `followers` int(11) DEFAULT NULL,
  `following` int(11) DEFAULT NULL,
  `hireable` tinyint(1) DEFAULT NULL,
  `location` mediumtext,
  `site_admin` tinyint(1) DEFAULT NULL,
  `type` char(128) DEFAULT NULL,
  `private_gists` int(11) DEFAULT NULL,
  `public_gists` int(11) DEFAULT NULL,
  `public_repos` int(11) DEFAULT NULL,
  `total_private_repos` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS  `contributor_org_rel`;
CREATE TABLE `contributor_org_rel` (
  `ContributorID` int(11) NOT NULL,
  `OrgID` int(11) NOT NULL,
  PRIMARY KEY (`ContributorID`,`OrgID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS  `owner_org_rel`;
CREATE TABLE `owner_org_rel` (
  `OwnerID` int(11) NOT NULL,
  `OrgID` int(11) NOT NULL,
  PRIMARY KEY (`OwnerID`,`OrgID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

SET FOREIGN_KEY_CHECKS = 1;

