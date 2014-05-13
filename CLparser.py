from csv import writer
import os

def extractContent(inString):

    outArray = []
    temp = ''
    ignore = False
    getOneMore = False
    for i in range(len(inString)):
        #print(i, inString[i])
        if (inString[i] == '<'):
            ignore = True
            temp = temp.strip()
            if (len(temp) > 0) :
                if (('UTC' in temp or 'EST' in temp or 'CET' in temp) and len(outArray)>0):
                    #print(temp)
                    if('(' in outArray[-1]):
                        getOneMore = True
                    outArray[-1]+=(' '+temp)
            
                elif 'aet' in temp or 'a.e.t.' in temp:
                    outArray[-1]+=temp
                    getOneMore = True
                elif getOneMore:
                    outArray[-1]+=temp
                    getOneMore = False
                elif 'orfeited' in temp:
                    pass
                else:   
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
            if tokenCount < 5:
                newTokens = extractContent(line)
                tokens.extend(newTokens)
                tokenCount += len(newTokens)
            else:
                mywriter.writerow(tokens)
                getTokens = False
                
        else:
            continue
            
            
def driver(directory):

    

    os.chdir(directory)
    fnames = os.listdir('.')
    
    outfile = open('CLHistory.log', 'w', newline='', encoding='utf-8')
    mywriter = writer(outfile, delimiter = ',')
    
    for fname in fnames:
        if fname != 'CLHistory.log':
            readFile(fname,mywriter)
        
    outfile.close()
        
    
    
    
    
    
