from csv import writer
import os

def extractContent(inString):

    inString = inString.replace('&#160;',' ')
    outArray = []
    temp = ''
    ignore = False
    for i in range(len(inString)):
        #print(i, inString[i])
        if (inString[i] == '<'):
            ignore = True
            temp = temp.strip()
            if (len(temp) > 0) :
                if ('UTC' in temp or 'EST' in temp or 'CET' in temp):
                    pass
                elif (('2001-08-' in temp) or ('2001-07-' in temp) or ('2001-09-' in temp)):
                    pass
                elif ((':' in temp) or (')' in temp)):
                    pass
                elif ( '(' in temp):
                    temp = temp.replace('(','')
                    if (len(temp)>0):
                        outArray.append(temp)
                elif 'aet' in temp or 'a.e.t.' in temp:
                    if (len(outArray)>0):
                        outArray[-1]+=temp
                    else:
                        outArray.append('special'+temp+'special')
                elif 'orfeited' in temp:
                    pass
                elif not temp.isspace():   
                    outArray.append(temp)
                temp = ''
                
        elif (inString[i] == '>'):
            ignore = False
        else:
            if (ignore == False):
                temp+=inString[i]
             
    temp = temp.strip()
    if (len(temp) > 0 and not temp.isspace()):
        outArray.append(temp)
        
    return outArray
    
def readFile(fname, mywriter):
 
    infile = open(fname,  encoding='utf8')
    #outfile = open(fname[:-5]+'.out', 'w', newline='', encoding='utf-8')
    
    #mywriter = writer(outfile, delimiter = ',')
    
    matchInfo = []
    getTokens = False
    for line in infile:
        #print(line)
        line.rstrip()
        if 'class="summary"' in line:
            getTokens = True
            tokenCount = 0
            tokens = []
        if getTokens == True:
            #print(line)
            if tokenCount < 4:
                newTokens = extractContent(line)
                tokens.extend(newTokens)
                tokenCount += len(newTokens)
            else:
                mywriter.writerow(tokens)
                getTokens = False
                
        else:
            continue
            
       
createSortedFile():

    monthLookup = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12,
    }

       
def driver(directory):

    

    os.chdir(directory)
    fnames = os.listdir('.')
    
    outfile = open('CLHistory.log', 'w', newline='', encoding='utf-8')
    mywriter = writer(outfile, delimiter = ',')
    
    for fname in fnames:
        if CLHistory not in fname:
            readFile(fname,mywriter)
        
    outfile.close()
        
    
    
    
    
    
