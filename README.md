# gootkit-crawler
A crawler for Gootkit

# Explanation of what this program will do.
This crawler will use python. 
I will provide an initial search term for a google dork (using duckduckgo); I will provide it by adding it to "search terms" text file list.
The crawler will check the search terms list for the newest search term to use, then it will execute the search, then it will download the search results from DDG.
The crawler will extract the list of results.
The crawler will add the list of results to a text file that will be used to track which specific article still needs to be crawled.

In another python script (script 2) that will be used to download each article in the "article-tracking-list.txt" (please choose the name for me) file.
The python script 2 will search the downloaded article for a regex query that I will provide.
If there is a match, the downloaded article will be put into a "match" (please choose good name) folder, and the article URL will be put into a "match" text file list.
If there was not a match, it would do the same, but it would be in a no-match folder and list.

All python scripts will use a sleep function.
All python scripts will have a debugging flag.
All python scripts will use try/catch before any method that may error.

List of Python files that we will use for this project:
- crawler.py
- downloader.py
- regex_matcher.py
- file_utils.py
- sleep_utils.py

List of folders and text files this project will need:
- search_terms.txt (text file)
- article_tracking_list.txt (text file)
- article_match.txt (text file)
- article_no_match.txt (text file)
- match (folder)
- no_match (folder)
- debug.log

Generate the Linux shell commands to add the folders and text files so that I don't have to do it manually:
mkdir /home/user/Documents/SoftwareDevelopment/GitHubRepos/gootkit-crawler/gootkit-crawler/match
mkdir /home/user/Documents/SoftwareDevelopment/GitHubRepos/gootkit-crawler/gootkit-crawler/no_match
touch /home/user/Documents/SoftwareDevelopment/GitHubRepos/gootkit-crawler/gootkit-crawler/search_terms.txt
touch /home/user/Documents/SoftwareDevelopment/GitHubRepos/gootkit-crawler/gootkit-crawler/article_tracking_list.txt
touch /home/user/Documents/SoftwareDevelopment/GitHubRepos/gootkit-crawler/gootkit-crawler/article_match.txt
touch /home/user/Documents/SoftwareDevelopment/GitHubRepos/gootkit-crawler/gootkit-crawler/article_no_match.txt
touch /home/user/Documents/SoftwareDevelopment/GitHubRepos/gootkit-crawler/gootkit-crawler/debug.log