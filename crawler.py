#crawler.py is a web crawler that crawls the web and extracts the links from the web pages.
# Create the bash command to run the crawler.py
# python3 crawler.py

import requests
from bs4 import BeautifulSoup
import re
import time
import os
import sys
import json
import urllib.parse
from urllib.parse import urljoin
import datetime

# Create debugging flag
debugging = True

# Function get the search term from search_terms_new.txt
def get_search_terms():
    try:
        search_terms = []
        with open('search_terms_new.txt', 'r') as file:
            for line in file:
                # url encode the search term, and save it as search_terms_url_encoded
                search_terms_url_encoded = urllib.parse.quote(line.strip())
                # replace the %20 with +, and save it as search_terms_plus
                search_terms_plus = search_terms_url_encoded.replace("%20", "+")
                # append the search_terms_plus to search_terms
                search_terms.append(search_terms_plus)
        return search_terms
    except Exception as e:
        if debugging:
            with open('debug.log', 'a') as file:
                file.write("Error: " + str(e) + "\n")
        else:
            print("Error: ", e)
        return []
    
# Function to move the search term from search_terms_new.txt to search_terms_complete.txt; if debugging is true, do nothing.
def move_search_term(search_term):
    try:
        if not debugging:
            with open('search_terms_new.txt', 'r') as file:
                lines = file.readlines()
            with open('search_terms_new.txt', 'w') as file:
                for line in lines:
                    if line.strip() != search_term:
                        file.write(line)
            with open('search_terms_complete.txt', 'a') as file:
                file.write(search_term + "\n")
    except Exception as e:
        if debugging:
            with open('debug.log', 'a') as file:
                file.write("Error: " + str(e) + "\n")
        else:
            print("Error: ", e)


# Function to get the links from the web page
def get_links(url):
    # if debugging is true, write the url to the debug.log file
    if debugging:
        with open('debug.log', 'a') as file:
            file.write(str(datetime.datetime.now()) + " get_links_url: " + url + "\n")
    try:
        # Set the headers to appear as a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        # Get the response from the url

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        # if debugging is true, write the response, the soup, and the links to the debug.log file
        if debugging:
            with open('debug.log', 'a') as file:
                file.write(str(datetime.datetime.now()) + " response: " + str(response) + "\n")
                file.write(str(datetime.datetime.now()) + " soup: " + str(soup) + "\n")
                file.write(str(datetime.datetime.now()) + " links: " + str(links) + "\n")
        return links
    except Exception as e:
        if debugging:
            with open('debug.log', 'a') as file:
                file.write("Error: " + str(e) + "\n")
        else:
            print("Error: ", e)
        return []
    
# Function to get the domain name from the url
def get_domain_name(url):
    try:
        domain_name = urllib.parse.urlparse(url).netloc
        return domain_name
    except Exception as e:
        if debugging:
            with open('debug.log', 'a') as file:
                file.write("Error: " + str(e) + "\n")
        else:
            print("Error: ", e)
        return ""
    
# Function to get the base url from the url
def get_base_url(url):
    try:
        base_url = urllib.parse.urlparse(url).scheme + "://" + urllib.parse.urlparse(url).netloc
        return base_url
    except Exception as e:
        if debugging:
            with open('debug.log', 'a') as file:
                file.write("Error: " + str(e) + "\n")
        else:
            print("Error: ", e)
        return ""
    
# Function to get the path from the url
def get_path(url):
    try:
        path = urllib.parse.urlparse(url).path
        return path
    except Exception as e:
        if debugging:
            with open('debug.log', 'a') as file:
                file.write("Error: " + str(e) + "\n")
        else:
            print("Error: ", e)
        return ""
    
# Function to get the query from the url
def get_query(url):
    try:
        query = urllib.parse.urlparse(url).query
        return query
    except Exception as e:
        if debugging:
            with open('debug.log', 'a') as file:
                file.write("Error: " + str(e) + "\n")
        else:
            print("Error: ", e)
        return ""
    
# Function to get the fragment from the url
def get_fragment(url):
    try:
        fragment = urllib.parse.urlparse(url).fragment
        return fragment
    except Exception as e:
        if debugging:
            with open('debug.log', 'a') as file:
                file.write("Error: " + str(e) + "\n")
        else:
            print("Error: ", e)
        return ""
    
# Function to get the links from the web page
def get_links_from_web_page(url):
    try:
        links = get_links(url)
        if debugging:
            with open('debug.log', 'a') as file:
                file.write(str(datetime.datetime.now()) + " links: " + str(links) + "\n")
        domain_name = get_domain_name(url)
        if debugging:
            with open('debug.log', 'a') as file:
                file.write(str(datetime.datetime.now()) + " domain_name: " + domain_name + "\n")
        base_url = get_base_url(url)
        if debugging:
            with open('debug.log', 'a') as file:
                file.write(str(datetime.datetime.now()) + " base_url: " + base_url + "\n")
        path = get_path(url)
        if debugging:
            with open('debug.log', 'a') as file:
                file.write(str(datetime.datetime.now()) + " path: " + path + "\n")
        query = get_query(url)
        if debugging:
            with open('debug.log', 'a') as file:
                file.write(str(datetime.datetime.now()) + " query: " + query + "\n")
        fragment = get_fragment(url)
        if debugging:
            with open('debug.log', 'a') as file:
                file.write(str(datetime.datetime.now()) + " fragment: " + fragment + "\n")
        links_list = []
        for link in links:
            link = link['href']
            link = urljoin(base_url, link)
            if link not in links_list:
                links_list.append(link)
        return links_list
    except Exception as e:
        if debugging:
            with open('debug.log', 'a') as file:
                file.write("Error: " + str(e) + "\n")
        else:
            print("Error: ", e)
        return []
    
# main function
def main():
    try:
        search_terms = get_search_terms()
        if debugging:
            print(str(datetime.datetime.now()) + " Search Terms: ", search_terms)
        for search_term in search_terms:
            search_term = search_term.replace(" ", "+")
            url = "https://www.google.com/search?q=" + search_term
            links = get_links_from_web_page(url)
            if debugging:
                print(datetime.datetime.now(), "Links: ", links)
            for link in links:
                print(link)
            move_search_term(search_term)
    except Exception as e:
        if debugging:
            with open('debug.log', 'a') as file:
                file.write("Error: " + str(e) + "\n")
        else:
            print("Error: ", e)

if __name__ == "__main__":
    if debugging:
        print(datetime.datetime.now(), "Starting main...")
        with open('debug.log', 'a') as file:
            file.write(str(datetime.datetime.now()) + " Starting main...\n")
        # Set the log file path
        log_file = 'debug.log'
        # Redirect stdout to the log file
        sys.stdout = open(log_file, 'a')
        
    main()

# End of crawler.py