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

# Create debugging flag
debugging = False

# Function get the search term from search_terms_new.txt
def get_search_terms():
    try:
        search_terms = []
        with open('search_terms_new.txt', 'r') as file:
            for line in file:
                search_terms.append(line.strip())
        return search_terms
    except Exception as e:
        if debugging:
            with open('debug.log', 'a') as file:
                file.write("Error: " + str(e) + "\n")
        else:
            print("Error: ", e)
        return []
    
# Function to move the search term from search_terms_new.txt to search_terms_done.txt; if debugging is true, do nothing.
def move_search_term(search_term):
    try:
        if not debugging:
            with open('search_terms_new.txt', 'r') as file:
                lines = file.readlines()
            with open('search_terms_new.txt', 'w') as file:
                for line in lines:
                    if line.strip() != search_term:
                        file.write(line)
            with open('search_terms_done.txt', 'a') as file:
                file.write(search_term + "\n")
    except Exception as e:
        if debugging:
            with open('debug.log', 'a') as file:
                file.write("Error: " + str(e) + "\n")
        else:
            print("Error: ", e)


# Function to get the links from the web page
def get_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
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
        domain_name = get_domain_name(url)
        base_url = get_base_url(url)
        path = get_path(url)
        query = get_query(url)
        fragment = get_fragment(url)
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
            print("Search Terms: ", search_terms)
        for search_term in search_terms:
            search_term = search_term.replace(" ", "+")
            url = "https://duckduckgo.com/html/?q=" + search_term
            links = get_links_from_web_page(url)
            if debugging:
                print("Links: ", links)
            for link in links:
                print(link)
            move_search_term(search_term)
    except Exception as e:
        if debugging:
            with open('debug.log', 'a') as file:
                file.write("Error: " + str(e) + "\n")
        else:
            print("Error: ", e)
