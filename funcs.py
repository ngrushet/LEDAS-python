def scanforsum(f):  
# scans .log file for "key" and read digits
#returning sum of all found number lists

    total = [0, 0, 0, 0, 0]  
    key = "Statistics: "
    key_len = len(key)

    #scan lines to find key
    for Line in f.readlines():
        s = Line.find(key)
        if (s == -1): continue
        #scan digits as strings
        nums = Line[ (s + key_len) :].rstrip().split(' ')
        #converting into @int@
        nums = [int(num) for num in nums]
        total=[sum(n) for n in zip(total,nums)]
    return(total)

def Layout(Cases):
    # ::: param :::: List of lists with sum of scanned digits and label of testcase
    # 
    # prints a table with "Label", "Stat 1"..."Stat 5".
    #
    # ::: returns::: 0 if all is ok 
    tableline = "-"*55
    
    print(
        tableline +
          "\n| Name   | Stat 0 | Stat 1 | Stat 2 | Stat 3 | Stat 4 |\n" +
        tableline, 
          end = ''
          )

    for i in Cases:
        print("\n| "+ '{:<6}'.format(i[0]), end = " |")

        for j in range(len(i[1])):
            print( '{:>7}'.format(i[1][j]), end = " |")
    print("\n"+tableline)    
    return 0   
