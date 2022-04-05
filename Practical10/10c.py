from nltk.parse import malt
#mp = malt.MaltParser('C:\\Users\\User\\AppData\\Roaming\\Python\\Python310\\maltparser-1.7.2', 'C:\\Users\\User\\AppData\\Roaming\\Python\\Python310\\engmalt.linear-1.7.mco')#file
mp = malt.MaltParser('F:\\BhagyasriMSC-IT\\MSC-IT-IV\\NLP\\uni\\maltparser-1.7.2', 'F:\\BhagyasriMSC-IT\\MSC-IT-IV\\NLP\\uni\\engmalt.linear-1.7.mco')#file
t = mp.parse_one('I saw a bird from my window.'.split()).tree()
print(t)
t.draw()
