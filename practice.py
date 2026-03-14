repos = [
    {"name": "repo1", "stars": 10},
    {"name": "repo2", "stars": 25},
    {"name": "repo3", "stars": 5}
]

top_repo = None
max_stars = 0

for repo in repos:
    if repo["stars"] > max_stars:
        max_stars = repo["stars"]
        top_repo = repo

print("Top repo:")
print(top_repo["name"], max_stars)