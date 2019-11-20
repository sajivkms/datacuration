# Importing Modules
import re

# Opening Files
fileA = open('Consumer_Complaints_FileA.xml')
fileB = open('Consumer_Complaints_FileB.xml')
fA = fileA.read()
fB = fileB.read()
# Convert to CRLF
fA = fA.replace('\n', '')
fB = fB.replace('\n', '')

files = [fA, fB]
rang = list(range(0, 2))
# Removing comments and DOCTYPE
for i in rang:
    # Comments
    files[i] = re.sub("(<!--.*?-->)", "", files[i])
    # Doctype
    files[i] = re.sub(r"(<!DOCTYPE.*]>)", "", files[i], 1, re.DOTALL)
    # Removing Whitespaces
    files[i] = files[i].strip()
    files[i] = re.sub(' \s+','', files[i])
    # Useless code
    # match = re.findall(r"(<(.*?)>)", files[i])
    # for j in range(len(match)):
    #     st = match[j][0]
    #     cleared = re.sub('\s+','', st)
    #     print(st, cleared)
    #     files[i] = files[i].replace(st, cleared)
    # files[i] = ''.join(files[i])

# Encoding - do last
for i in rang:
    files[i] = files[i].encode()
# Writing canocilazied files to new files fileCA.xml and fileCB.xml
fileWriteA = open("fileCA.xml", mode="wb")
fileWriteA.write(files[0])
fileWriteB = open("fileCB.xml", mode="wb")
fileWriteB.write(files[1])