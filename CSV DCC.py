import os
def DateCorrect(OldDate):
    #OldDate = r'2020\03\15'
    slash = '\\'
    #print('{2}\\{1}\\{0}'.format(*OldDate.split('-').rstrip('"').lstrip('"')))
    return '{2}\\{1}\\{0}'.format(*OldDate.rstrip('\n').rstrip('"').lstrip('"').split('-'))

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
        print(filename)

for (dpath, dnames, filenames) in os.walk(OldCSVDir.rstrip()):
    for filename in filenames:
        OldCSV = open(OldCSVDir+'\\'+filename ,'r')
        NewCSV = open(NewCSVDir + filename , 'w+')
       
        NewCSV.write(OldCSV.readline())

        for line in OldCSV:
            
            terms = line.split(',')
            
            terms[0] = '"' + DateCorrect(''.join(terms[0])) + '"'
            terms[4] = '"' + str(abs(float(''.join((terms[4].rstrip('"').lstrip('"')))))) + '"'
            
            for col in terms:
                NewCSV.write(col)
                if not  str(col) == '""\n':
                    NewCSV.write(',')
            
        
        OldCSV.close()
        NewCSV.close()


