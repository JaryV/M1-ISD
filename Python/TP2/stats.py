import sys
from collections import Counter



class stat:
    file = sys.argv[1]

    def init(self, filename):
        with open(filename, 'r') as f:
            content = f.read() 
        self.nChars = len(content)
        self.nLines = content.count('\n')
        self.nWords = len(content.split())
        print('nb characters: {0}\nnb lines: {1}\nnb words: {2}'.format(self.nChars, self.nLines, self.nWords))

    def moyenneMotsLigne(self, filename):
        with open(filename, 'r') as f:
            Lines = f.readlines()
            wordCount = 0
            lineCount = 0
            for line in Lines:
                line_word = line.lower().replace(',','').replace('\r','').replace('\n','').replace('.','').split(" ")
                #print(line_word)
                if line_word != ['']:
                    wordCount += len(line_word)
                    lineCount += 1
        print('Mean words / line : {0}'.format(float(wordCount/float(lineCount))))

    
    def longestWord(self, filename):
	    with open(filename,'r+') as f:
                words = f.read().replace(',',' ').replace('.',' ').replace('\r','').replace('\n',' ').split(" ")
                max_len_word = max(words,key=len)
                max_len = len(max(words,key=len))		
                print('maximum lenth word in file : {0} (length = {1})'.format(max_len_word, max_len))


    def mostFrequent(self, filename):
        frequent_word = ""
        frequency = 0  
        words = []
        with open(filename, 'r') as file:
            for line in file:
                line_word = line.lower().replace(',','').replace('.','').replace('\r','').replace('\n','').split(" ");  
                
                for w in line_word:  
                    words.append(w);  
                    
            for i in range(0, len(words)):  
                count = 1;  

                for j in range(i+1, len(words)):  
                    if(words[i] == words[j]):  
                        count = count + 1;  
            
                if(count > frequency):  
                    frequency = count;  
                    frequent_word = words[i];  
            
            print("Most repeated word: {0} ({1} times)".format( frequent_word,str(frequency)))
        return 0

    def LetterCount(self, filename):
        with open(filename) as f:
            c = Counter()
            for line in f:
                line_word = line.lower().replace(',','').replace('.','').replace('\r','').replace(' ','').replace('\n','');  
                c += Counter(line_word)
        print('Most repeated letter : {0} ({1} times)'.format(c.most_common(1)[0][0], c.most_common(1)[0][1]))



st = stat()
print("Text: {}".format(st.file))
st.init(st.file)
st.mostFrequent(st.file)
st.moyenneMotsLigne(st.file)
st.longestWord(st.file)
st.LetterCount(st.file)

#Commande : python stats.py fileName.txt


