avail_chars  = "abcdefghijklmnopqrstuvwxyzåäö"

rawtext = "Elsa. Ja, det gjorde jag visst, ända tills det där med den olagliga värneplikten kom. Då fick jag mina ögon öppnade. Han bestod icke provet, utan lät fegt skrämma sig, och då fick han korgen. Jag vill icke ha en pultron till man, som icke har någon karaktär — och så söp han i smyg. Aldrig skulle jag gifta mig med en man, som begagnade rusdrycker. Min älsta syster gjorde det, och du vet hur det gick. Hon blev nog varnad,men då hon litade på hans löften och på kärleken, att den skulle göra honom till en bättre människa, så gifte hon sig med honom det oaktat. Och inte en glad dag hade hon sedan, tills döden gjorde slut på hennes lidanden. Hennes sista ord till mig voro: Gift dig inte med en drinkare!"

def cleanUp(rawtext):
    rawtext = rawtext.lower()
    cleanedtext = ""
    for index in range(len(rawtext)):
        if rawtext[index] in avail_chars:
            cleanedtext += rawtext[index]
    return cleanedtext

# print(cleanUp(rawtext))