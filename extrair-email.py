from importlib.metadata import files
import eml_parser
import csv
import os, glob
import os.path
import datetime
import json
from shutil import copyfile


def loopPrincipal(filesToOpen):
    listOfFilesToOpen = filesToOpen
    remetentesExtraido = []

    for email in listOfFilesToOpen:
        remetentesExtraido.append(extraiRemetente(email))
            
    return remetentesExtraido

# def writeEmailsToCSV(toExtracted):
#     emailsExtraidos = toExtracted
#     with open('emails-bounced-extraidos.csv', 'a') as f:
#         f.write(',\n'.join(emailsExtraidos))



# filesToOpen = getAllTheNames()
# print("*************************")
# print("ARQUIVOS QUE SERÃO USADOS:")
# print(f"Total: {len(filesToOpen)}")
# print("*************************")
# print(filesToOpen)
# toExtracted =  toExtractor(filesToOpen)


# print("*************************")
# print("EMAILS SENDO SALVOS EM ARQUIVO:")
# print("*************************")
# print(toExtracted)

# writeEmailsToCSV(toExtracted)
# print("*************************")
# print(f"ARQUIVO SALVO COMO: emails-bounced-extraidos.csv")
# print("*************************")

targetPath = '/home/meulindux/emails/target'
workingPath = '/home/meulindux/emails/working'

def copiaEmails():
    index = 1
    for file in os.listdir(targetPath):    
        copyfile(f'{targetPath}/{file}', f'{workingPath}/{index}.eml')
        index = index + 1

def extraiRemetente(eml):
    def json_serial(obj):
        if isinstance(obj, datetime.datetime):
            serial = obj.isoformat()
            return serial

    with open(f'working/{eml}', 'rb') as fhdl:
        raw_email = fhdl.read()

    ep = eml_parser.EmlParser()
    parsed_eml = ep.decode_email_bytes(raw_email)

    try:
        return parsed_eml['header']['from']

    except:
        print('*********************')
        print('Não achei o remetente')
        print('*********************')

def getAllTheEmails ():
    allEmails = []

    for file in os.listdir(workingPath):
        allEmails.append(file)

    return allEmails

copiaEmails()

emails = getAllTheEmails()

todosOsEmailsExtraidos = loopPrincipal(emails)

print(todosOsEmailsExtraidos)

print(len(todosOsEmailsExtraidos))