import src.functions as functions
import time, os

if __name__ == '__main__':

    os.system('figlet PlagiarismCheck && echo')
    time.sleep(1)

    contents = functions.getFileContents() #Reads the file set in arguments

    time.sleep(1)
    functions.CheckPlagiarism(contents) #checks plagiarism
