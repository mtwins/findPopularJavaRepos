## Instructions to run Get Repositories scripts
1) Make sure to have the BeautifulSoup and requests python libraries installed
```
pip install requests
pip install beautifulsoup4
```
2) Run get_top_repos.py to get the top Java repositories in a csv file (sorted by stars currently, but can be updated to be sorted by something else)
3) Run get_trending_repos.py to get the trending Java repositories in a csv file 

#### Commands to run scripts from root directory in terminal
```
python scripts/getRepositories/get_top_repos.py
python scripts/getRepositories/get_trending_repos.py
```

## Instructions to run Get Repo Size script
1) Make sure to have the requests python library installed
```
pip install requests
```
2) As the endpoint has rate limiting for unauthorized users, create a GitHub Personal Access token(with full repo permission): [instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
3) Replace the following text in get_repo_size.py with your token: {replace with personal access token}
4) Run the get_repo_size.py script to get the size of the repos according to the GitHub Api in a csv file and identify the largest repo

#### Commands to run scripts from root directory in terminal
```
python scripts/getRepositories/get_repo_size.py
```
