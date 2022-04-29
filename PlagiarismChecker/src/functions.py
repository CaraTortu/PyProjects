import sys
from termcolor import colored
import os
import time
import threading
import requests
import json
import jmespath

argError = 'Usage: python3 main.py [path]'


def readfile(path):


    path = str(path)
    filePaths = ['./']
    

    try:
        file = open(path, 'r').read()
        print(colored("[+] Valid path", 'green'))
        return file

    except FileNotFoundError:
        try:
            file = open(path+filePaths[0], 'r').read()
            print(colored("[+] Valid path", 'green'))
            return file

        except FileNotFoundError:
            print(colored("[+] Invalid path", 'red'))
            sys.exit(0)

def getFileContents():

    try:
        FilePath = sys.argv[1]
        FileContents = readfile(FilePath)
        return FileContents

    except IndexError:
        print(argError)
        sys.exit(0)

def CheckPlagiarism(text):
    str1 = '[~] Looking for plagiarism'
    str2 = '....'

    for letter in str1:
        print(colored(letter, 'blue'), end='')
        sys.stdout.flush()
        time.sleep(0.05)


    for lett in str2:
        print(colored(lett, 'blue'), end='')
        sys.stdout.flush()
        time.sleep(0.33)


    url = "https://google-search3.p.rapidapi.com/api/v1/search/q="+str(text).replace(' ', '+').lower().replace('\n', '')+"&num=100"

    headers = {
    'x-rapidapi-key': "4fae378d2amsh9960245fc966c5ap1bb293jsnea59414a52d9",
    'x-rapidapi-host': "google-search3.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)


    if response.text != '{"detail":"Not Found"}':
        print('')
        print(colored("[+] Plagiarism found! Printing websites...", 'green'))
        time.sleep(1)
        print('')
        lines = json.loads(response.text)
        lines = jmespath.search("results[*].link", lines)
        total = len(lines)

        for link in lines:
            print(colored(str(link), 'red'))

        print(colored("TOTAL URLS: "+str(total), 'blue'))

    elif response.text == '{"detail":"Not Found"}':
        print('')
        print(colored("[-] Plagiarism not found!", 'red'))
        print(response.text.replace(',', '\n'))


def runCommand(cmd):
    return os.system(cmd)
