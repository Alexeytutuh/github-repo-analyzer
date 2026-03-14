import requests

def get_repos(username):

    url = f"https://api.github.com/users/{username}/repos?per_page=100"

    headers = {
        "User-Agent": "Python API Client"
    }

    try:

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            return response.json()

        else:
            print("API error:", response.status_code)
            return []

    except:
        print("Connection error")
        return []