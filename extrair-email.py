from importlib.metadata import files
import eml_parser
import csv
import os, glob

def toExtractor(filesToOpen):
    listOfFilesToOpen = filesToOpen
    todos_os_emails = []

    for email in listOfFilesToOpen:
        with open(email, 'r') as openedFile:
            raw_email = openedFile.read()
            raw_email_n = raw_email.split('\n')
        
            sub = 'To: '
            res_cheio = [i for i in raw_email_n if sub in i]
            res_final = res_cheio[-1]
            # print(res_final.split(': ')[1])
            todos_os_emails.append(res_final.split(': ')[1])
    return todos_os_emails

def writeEmailsToCSV(toExtracted):
    emailsExtraidos = toExtracted
    with open('emails-bounced-extraidos.csv', 'a') as f:
        f.write(',\n'.join(emailsExtraidos))

def getAllTheNames ():
    allFiles = []

    for file in glob.glob("*.eml"):
        allFiles.append(file)

    return allFiles



filesToOpen = getAllTheNames()
print("*************************")
print("ARQUIVOS QUE SERÃO USADOS:")
print(f"Total: {len(filesToOpen)}")
print("*************************")
print(filesToOpen)
toExtracted =  toExtractor(filesToOpen)


print("*************************")
print("EMAILS SENDO SALVOS EM ARQUIVO:")
print("*************************")
print(toExtracted)

writeEmailsToCSV(toExtracted)
print("*************************")
print(f"ARQUIVO SALVO COMO: emails-bounced-extraidos.csv")
print("*************************")