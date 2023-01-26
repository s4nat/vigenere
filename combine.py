from sys import path as sp
from os import path
from pathlib import Path

sp.append(path.join((Path.cwd())))
from cleanup import cleanUp
from vig_encrypt import vig_encrypt

text = "Tillbaka i nutiden fortsätter Ove med sina självmordsförsök. En dag försöker Ove ta livet av sig genom kolmonoxidförgiftning, men han blir avbruten av Parvaneh. Hon frågar honom om hon kan få skjuts till sjukhuset och om han kan vara barnvakt till hennes båda döttrar, efter att Patrick råkat ramla från en stege. När Ove motvilligt fullgjort detta går han till en tågstation och planerar att hoppa framför ett tåg. När en man på perrongen plötsligt svimmar och faller ner på spåret, hoppar Ove ner och räddar honom. På vägen hem tar Ove in en herrelös katt som han tidigare skrämt bort. En dag frågar Parvaneh om Ove kan lära henne att köra bil. Efter en tids reflektion hjälper Ove henne att ta sitt körkort. Ove reparerar en cykel som han först konfiskerat och senare lämnar tillbaka till tonåringen Adrian, en gammal elev till Sonja. Ove försöker senare begå självmord med ett hagelgevär, men han avbryts av att Adrian och hans kompis Mirsad ringer på hans dörr. De frågar om Mirsad kan få bo hos Ove eftersom Mirsad hade blivit utslängd från sitt hem efter att ha kommit ut som homosexuell inför sin familj. Då Adrian påpekar att Sonja alltid hjälpt andra, bjuder Ove in Mirsad i sitt hus."
key = "blåsöneähs"

clean_text = cleanUp(text)

encrypted_text = vig_encrypt(clean_text, key)

print(encrypted_text)
