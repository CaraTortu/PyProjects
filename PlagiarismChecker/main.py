import src.functions as functions
import time

if __name__ == '__main__':

    print(str(functions.runCommand('figlet PlagiarismCheck')).replace('0', ''))
    print('')
    time.sleep(1)

    contents = functions.getFileContents() #Reads the file set in arguments

    time.sleep(1)
    functions.CheckPlagiarism(contents) #checks plagiarism
