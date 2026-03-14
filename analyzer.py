def filter_python_repos(repos):

    python_repos = []

    for repo in repos:
        if repo["language"] == "Python":
            python_repos.append(repo)

    return python_repos


def find_top_repo(repos):

    top_repo = None
    max_stars = 0

    for repo in repos:
        if repo["stargazers_count"] > max_stars:
            max_stars = repo["stargazers_count"]
            top_repo = repo

    return top_repo