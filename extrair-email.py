from importlib.metadata import files
import eml_parser
import csv
import os, glob
import os.path
import datetime
import json
import pandas as pd
from shutil import copyfile

targetPath = '/home/meulindux/emails/target'
workingPath = '/home/meulindux/emails/working'

def loopPrincipal(filesToOpen):
    listOfFilesToOpen = filesToOpen
    remetentesExtraido = []

    for email in listOfFilesToOpen:
        remetentesExtraido.append(extraiRemetente(email)) #extraiRemetente(email) para remover direto do cabeçalho 
            
    return remetentesExtraido

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
        if "OECustom" in file:
            pass
        else:    
            allEmails.append(file)

    return allEmails

copiaEmails()

emails = getAllTheEmails()

todosOsEmailsExtraidos = loopPrincipal(emails)

print(todosOsEmailsExtraidos)

print(len(todosOsEmailsExtraidos))

df = pd.DataFrame(todosOsEmailsExtraidos)
df.to_csv('Resultado.csv')