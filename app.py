# GitHub API automation script

from github_api import get_repos
from analyzer import filter_python_repos, find_top_repo


username = input("Enter GitHub username: ")

repos = get_repos(username)

if len(repos) == 0:
    print("No repositories found")

else:
    print("Choose option:")
    print("1 - Show all repositories")
    print("2 - Show Python repositories")
    print("3 - Show top repository by stars")

    option = input("Enter option: ")

    if option == "1":

        for repo in repos:
            print(repo["name"], "⭐", repo["stargazers_count"])

    elif option == "2":

        python_repos = filter_python_repos(repos)

        for repo in python_repos:
            print(repo["name"], "⭐", repo["stargazers_count"])

    elif option == "3":

        top_repo = find_top_repo(repos)

        print("Top repository:")
        print(top_repo["name"], "⭐", top_repo["stargazers_count"])

    else:
        print("Unknown option")

print("Script finished")