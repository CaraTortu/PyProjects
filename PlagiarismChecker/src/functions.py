import sys, time, json, requests, jmespath
from termcolor import colored
from os.path import exists
from dotenv import dotenv_values

argError = 'Usage: python3 main.py [path of the text file]'


def readfile(path):

    if exists(path):
        with open(path, 'r') as f:
            print(colored("[+] Valid path", 'green'))
            return f.read()

    print(colored("[+] Invalid path", 'red'))
    sys.exit(0)

def getFileContents():

    if len(sys.argv) < 2:
        print(argError)
        sys.exit(0)

    FilePath = sys.argv[1]
    FileContents = readfile(FilePath)
    return FileContents

def CheckPlagiarism(text):
    str1 = '[~] Looking for plagiarism'

    for letter in str1:
        print(colored(letter, 'blue'), end='')
        sys.stdout.flush()
        time.sleep(0.05)

    url = "https://google-search3.p.rapidapi.com/api/v1/search/q="+str(text).replace(' ', '+').lower().replace('\n', '')+"&num=100"

    headers = {
    'x-rapidapi-key': str(list(dotenv_values("src/.env").values())[0]),
    'x-rapidapi-host': "google-search3.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)


    if response.text != '{"detail":"Not Found"}':
        print(colored("\n[+] Plagiarism found! Printing websites...\n", 'green'))
        time.sleep(1)
        lines = json.loads(response.text)
        lines = jmespath.search("results[*].link", lines)
        total = len(lines)

        for link in lines: print(link)

        print(colored("\nTotal URLs found: "+str(total), 'blue'))
        print("Most likely plagiarised website: "+colored(str(lines[0]), 'green'))

    elif response.text == '{"detail":"Not Found"}':
        print(colored("\n[-] Plagiarism not found!", 'red'))
        print(response.text.replace(',', '\n'))