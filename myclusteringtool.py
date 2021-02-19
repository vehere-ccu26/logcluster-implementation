import sys

#ele = int(sys.argv[2]) - 1
#print("Value of ele : " + str(ele) + '\n')
file_name = sys.argv[1]

candidates = {}
all_data = []

flines = open(file_name,'r').read().split('\n')

for ele in range(0,len(flines[0].split(','))):
    for line in flines:
        elements = line.split(",")
        #print("Elements Array : " + str(elements) + '\n')
        #print("Value of ele : " + str(ele) + "   Element : "  +  elements[ele])
        if elements[ele] in candidates:
            candidates[elements[ele]] = candidates[elements[ele]] + 1
        else:
            candidates[elements[ele]] = 1
    all_data.append(candidates)
    print(candidates)
    print("\n\n")
    candidates.clear()


#print(all_data)




