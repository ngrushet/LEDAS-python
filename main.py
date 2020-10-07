import os
from funcs import scanforsum, Layout

#catalog adress input

#as comfortable - input in IDLE or with stdin - comment what is needed
directory = 'statistics-from-logs\\example-logs\\today'
print("input adress: ")
directory = input()
while not (os.path.isdir(directory)):
    print("Incorrect adress. Try again.")
    print("input adress: ")
    directory = input()


#big one List with all collecting data
allCases = []

try: 
    for catalog in os.listdir(directory): 
        
        #scanning catalogs for .log files 
        try: 
            for file in os.listdir(directory+"\\"+catalog): 

                if file.endswith(".log"):

                    log = open(directory+"\\"+catalog+"\\"+file, 'r')
                    case = [catalog]
                    case.append(scanforsum(log))
                    allCases.append(case)
                    log.close()

        except NotADirectoryError: 
            print("It seems the directory doesn't contain test-cases folders")
except FileNotFoundError :  
    print("Incorrect directory name. Folder not found")
except NotADirectoryError:  
    print("Incorrect directory name: It's maybe a file, not folder")
else: 
    #output table
    
    if allCases != []:
        allCases.sort(key=lambda i: i[1][0],reverse=True)
        Layout(allCases) 
    else: print("No data")

input("Press Enter to close...")