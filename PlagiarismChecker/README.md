# Description

The script uses a google search API to search for the content supplied in a file.

# Usage

pip3 install -r requirements.txt

Add your api key to the file .env in src/

python3 main.py [file]

**The text you want to check for plagiarism has to be in a file, that is what the file field is for.**

# Example

The syntax used was **python3 main.py text.txt**, where text.txt's contents are "This is a text"

![PLAGIMG.png](https://github.com/CaraTortu/PyProjects/blob/main/PlagiarismChecker/src/PLAGIMG.png)

As you can see, it has this steps:

  1) Check if the file path is valid
  2) Check if there is plagiarism
  3) Print the urls that contain the text supplied in the command
  4) Say how many urls are there
