# coding: utf-8

RESOURCE_MAPPING = {
  "get_pr_comments": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/{id}/comments",
    "methods": [
      "GET"
    ]
  },
  "get_team": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/teams/{teamname}",
    "methods": [
      "GET"
    ]
  },
  "merge_pr": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/{id}/merge",
    "methods": [
      "POST"
    ]
  },
  "get_repository_watchers": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/watchers",
    "methods": [
      "GET"
    ]
  },
  "get_user": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/users/{username}",
    "methods": [
      "GET"
    ]
  },
  "get_forks": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/forks",
    "methods": [
      "GET"
    ]
  },
  "decline_pr": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/{id}/decline",
    "methods": [
      "POST"
    ]
  },
  "get_comment": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/commit/{revision}/comments/{comment_id}",
    "methods": [
      "GET"
    ]
  },
  "get_team_members": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/teams/{teamname}/members",
    "methods": [
      "GET"
    ]
  },
  "get_pr_commentby_id": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/{id}/comments/{comment_id}",
    "methods": [
      "GET"
    ]
  },
  "get_user_repos": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/users/{username}/repositories",
    "methods": [
      "GET"
    ]
  },
  "pull_requests": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests",
    "methods": [
      "POST",
      "GET"
    ]
  },
  "get_repo_by_owner": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}",
    "methods": [
      "GET"
    ]
  },
  "get_pr_diff": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/{id}/diff",
    "methods": [
      "GET"
    ]
  },
  "get_pr_activity": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/activity",
    "methods": [
      "GET"
    ]
  },
  "get_team_repositories": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/teams/{teamname}/repositories",
    "methods": [
      "GET"
    ]
  },
  "get_pull_request_approvals": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/{id}/approvals",
    "methods": [
      "GET"
    ]
  },
  "get_diff": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/diff/{spec}",
    "methods": [
      "GET"
    ]
  },
  "pull_request_changesets": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{accountname}/{repo_slug}/pullrequests/{pull_request_id}/changesets/{approver}",
    "methods": [
      "POST",
      "DELETE",
      "GET"
    ]
  },
  "get_pr_patch": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/{id}/patch",
    "methods": [
      "GET"
    ]
  },
  "commits_revision": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/commits/{revision}",
    "methods": [
      "POST",
      "GET"
    ]
  },
  "branch_restriction": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/branch-restrictions+Resource#branch-restrictionsResource-GETaspecificrestriction",
    "resource": "/repositories/{accountname}/{repo_slug}/branch-restrictions/{id}",
    "methods": [
      "PUT",
      "DELETE",
      "GET"
    ]
  },
  "repository": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}",
    "methods": [
      "POST",
      "DELETE",
      "GET"
    ]
  },
  "get_pull_request_changesets": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{accountname}/{repo_slug}/pullrequests/{pull_request_id}/changesets",
    "methods": [
      "GET"
    ]
  },
  "get_comments": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/commit/{revision}/comments",
    "methods": [
      "GET"
    ]
  },
  "get_repositories": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories",
    "methods": [
      "GET"
    ]
  },
  "get_user_following": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/users/{username}/following",
    "methods": [
      "GET"
    ]
  },
  "branch_restrictions": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/branch-restrictions+Resource#branch-restrictionsResource-GETthebranch-restrictions",
    "resource": "/repositories/{accountname}/{repo_slug}/branch-restrictions",
    "methods": [
      "POST",
      "GET"
    ]
  },
  "get_pr_commits": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/{id}/commits",
    "methods": [
      "GET"
    ]
  },
  "get_patch": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/patch/{spec}",
    "methods": [
      "GET"
    ]
  },
  "get_team_followers": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/teams/{teamname}/followers",
    "methods": [
      "GET"
    ]
  },
  "get_user_followers": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/users/{username}/followers",
    "methods": [
      "GET"
    ]
  },
  "get_team_following": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/teams/{teamname}/following",
    "methods": [
      "GET"
    ]
  },
  "pull_request": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/{id}",
    "methods": [
      "PUT",
      "GET"
    ]
  }
}
