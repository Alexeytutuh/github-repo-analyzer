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
        if repo["stars"] > max_stars:
            max_stars = repo["stars"]
            top_repo = repo

    return top_repo

def simplify_repos(repos):

    clean_repos = []

    for repo in repos:

        clean_repo = {
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "language": repo["language"]
        }

        clean_repos.append(clean_repo)

    return clean_repos

def get_top_repos(repos):

    sorted_repos = sorted(repos, key=lambda repo: repo["stars"], reverse=True)

    return sorted_repos[:5]