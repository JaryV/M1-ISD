import sys

def cat():
    tabFile = [sys.argv[i] for i in range(1,len(sys.argv))]
    #print(tabFile)
    for i in range(len(tabFile)):
        try:
            f = open(tabFile[i],'r')
            print('{0}:\n{1}\n'.format(tabFile[i],f.read()))
        except IOError: #IOError pour ma version (python 2.7) et FileNotFoundError pour python 3.
            print('File {0} does not exist \n'.format(tabFile[i]))
            

cat()

# compilation : python cat.py fileName1.txt fileName2.txt ... fileNameN.txt