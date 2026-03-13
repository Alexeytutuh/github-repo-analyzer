# GitHub API automation script

import requests

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)

repos = response.json()

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
        for repo in repos:
            if repo["language"] == "Python":
                print(repo["name"], "⭐", repo["stargazers_count"])

    elif option == "3":
        top_repo = None
        max_stars = 0

        for repo in repos:
            if repo["stargazers_count"] > max_stars:
                max_stars = repo["stargazers_count"]
                top_repo = repo

        print("Top repository:")
        print(top_repo["name"], "⭐", max_stars)

    else:
        print("Unknown option")
        print("Script finished")