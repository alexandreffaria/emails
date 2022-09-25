import os
import pandas as pd

targetPath = '/home/meulindux/emails/target'
workingPath = '/home/meulindux/emails/working'


def extraiRemetenteCorpo(eml):   
    with open(f"working/{eml}", "r") as email:
        teste = "To: "
        remove = "carlos@diadoarauto.com.br"
        for line in email:
            if teste in line:
                if remove in line:
                    pass
                else:
                    remetente = line.split(teste)[1]
                    # print(remetente)
                    return remetente

email = open("working/1.eml", "r")

# extraiRemetenteCorpo("working/1.eml")


def getAllTheEmails ():
    allEmails = []

    for file in os.listdir(workingPath):
        allEmails.append(file)
    # print(allEmails)
    return allEmails

emails = getAllTheEmails()
emails_extraidos = []
for email in emails:
    
    quickfix = ":OECustomProperty"
    if quickfix in email:
        pass
    else:
        # print(email)
        try:
            emails_extraidos.append(extraiRemetenteCorpo(email))
        except:
            pass

# print(emails_extraidos[859])

for email_extraido in emails_extraidos:
    nosso_email = "@diadoarauto"
    # print(email_extraido)  
    if nosso_email in str(email_extraido):
        emails_extraidos.remove(email_extraido)

print(emails_extraidos)

df = pd.DataFrame(emails_extraidos)
df.to_csv('Resultado.csv')