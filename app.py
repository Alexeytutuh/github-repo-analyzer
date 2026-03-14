# GitHub API automation script

from github_api import get_repos
from analyzer import filter_python_repos, find_top_repo
from analyzer import simplify_repos
from analyzer import get_top_repos
from saver import save_to_json
from saver import save_to_csv


username = input("Enter GitHub username: ")

repos = get_repos(username)
repos = simplify_repos(repos)
save_to_json(repos)
save_to_csv(repos)

if not repos:
    print("No repositories found")

else:
    print("Choose option:")
    print("1 - Show all repositories")
    print("2 - Show Python repositories")
    print("3 - Show top repository by stars")
    print("4 - Show top 5 repositories")

    option = input("Enter option: ")

if option == "1":

    for repo in repos:
        print(repo["name"], "⭐", repo["stars"])

elif option == "2":

    python_repos = filter_python_repos(repos)

    for repo in python_repos:
        print(repo["name"], "⭐", repo["stars"])

elif option == "3":

    top_repo = find_top_repo(repos)

    print("Top repository:")
    print(top_repo["name"], "⭐", top_repo["stars"])

elif option == "4":

    top_repos = get_top_repos(repos)

    for repo in top_repos:
        print(repo["name"], "⭐", repo["stars"])

else:
    print("Unknown option")

print("Script finished")