# coding: utf-8

RESOURCE_MAPPING = {
  "pr_comments": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/{id}/comments",
    "methods": [
      "GET"
    ]
  },
  "team": {
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
  "repository_watchers": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/watchers",
    "methods": [
      "GET"
    ]
  },
  "user": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/users/{username}",
    "methods": [
      "GET"
    ]
  },
  "forks": {
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
  "comment": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/commit/{revision}/comments/{comment_id}",
    "methods": [
      "GET"
    ]
  },
  "team_members": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/teams/{teamname}/members",
    "methods": [
      "GET"
    ]
  },
  "pr_commentby_id": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/{id}/comments/{comment_id}",
    "methods": [
      "GET"
    ]
  },
  "user_repos": {
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
  "repo_by_owner": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}",
    "methods": [
      "GET"
    ]
  },
  "pr_diff": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/{id}/diff",
    "methods": [
      "GET"
    ]
  },
  "pr_activity": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/activity",
    "methods": [
      "GET"
    ]
  },
  "team_repositories": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/teams/{teamname}/repositories",
    "methods": [
      "GET"
    ]
  },
  "pull_request_approvals": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/{id}/approvals",
    "methods": [
      "GET"
    ]
  },
  "diff": {
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
  "pr_patch": {
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
  "pull_request_changesets": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{accountname}/{repo_slug}/pullrequests/{pull_request_id}/changesets",
    "methods": [
      "GET"
    ]
  },
  "comments": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/commit/{revision}/comments",
    "methods": [
      "GET"
    ]
  },
  "repositories": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/repositories+Endpoint",
    "resource": "/repositories",
    "methods": [
      "GET"
    ]
  },
  "user_following": {
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
  "pr_commits": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/pullrequests/{id}/commits",
    "methods": [
      "GET"
    ]
  },
  "patch": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/repositories/{owner}/{repo_slug}/patch/{spec}",
    "methods": [
      "GET"
    ]
  },
  "team_followers": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/teams/{teamname}/followers",
    "methods": [
      "GET"
    ]
  },
  "user_followers": {
    "docs": "https://confluence.atlassian.com/display/BITBUCKET/Version+2",
    "resource": "/users/{username}/followers",
    "methods": [
      "GET"
    ]
  },
  "team_following": {
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
