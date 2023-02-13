avail_chars  = "abcdefghijklmnopqrstuvwxyzåäö"

rawtext = "tänka fritt är stort men tänkarätt är större"

def cleanUp(rawtext):
    rawtext = rawtext.lower()
    cleanedtext = ""
    for index in range(len(rawtext)):
        if rawtext[index] in avail_chars:
            cleanedtext += rawtext[index]
    return cleanedtext

# print(cleanUp(rawtext))