import os

def StripQuotes(stripme):
    return stripme.rstrip('"').lstrip('"')

def DateCorrect(OldDate):
    #OldDate = r'2020\03\15'
    slash = '\\'
    
    #return '{2}\\{1}\\{0}'.format(*OldDate.rstrip('"').lstrip('"').split('-'))
    return '{2}\\{1}\\{0}'.format(*StripQuotes(OldDate).split('-'))


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

dirfile = open(os.path.join(__location__, 'CSVLocation.txt'))

(OldCSVDir, NewCSVDir) = dirfile.readlines()
OldCSVDir = OldCSVDir.rstrip()
dirfile.close()

if not os.path.exists(NewCSVDir):
    os.mkdir(NewCSVDir)
    print("Created " + NewCSVDir)


iPath = r'C:/Users/DSK1/Desktop/VSCODE_PYTHON/CSV DCC/Unformatted/'
#C:/Users/DSK1/Desktop/VSCODE_PYTHON/CSV DCC/Unformatted/


for (dpath, dnames, filenames) in os.walk(OldCSVDir.rstrip()):
    for filename in filenames:
        OldCSV = open(OldCSVDir+'\\'+filename ,'r')
        NewCSV = open(NewCSVDir + filename , 'w+')
       
        NewCSV.write(OldCSV.readline())

        for line in OldCSV:
            
            terms = line.split(',')
            
            terms[0] = '"' + DateCorrect(''.join(terms[0])) + '"'
            terms[4] = '"' + str(abs(float(''.join((StripQuotes(terms[4])))))) + '"'
            
            for col in terms:
                NewCSV.write(col)
                if not  str(col) == '""\n':
                    NewCSV.write(',')
            
        
        OldCSV.close()
        NewCSV.close()


