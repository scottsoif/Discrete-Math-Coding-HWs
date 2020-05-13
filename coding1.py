#COMS3203 DISCRETE MATHEMATICS
#CODING ASSIGNMENT 1

# Scott Soifer
# sas2412

def format_prop(prop):
    '''
    format a string from a proposition formula represented by lists
    '''

    infixStr = ""
    infixStr = str(fpHelper(prop))

    return infixStr


def fpHelper(prop):
    if type(prop) is list:
        for i in range( len(prop) ):
            if( len(prop) == 1 ):
                return prop[0]
            if(prop[i] == "if"):
                return "(" + str(fpHelper(prop[i+1]) ) + " -> " + str(fpHelper(prop[i+2])) + ")" 
            elif(prop[i] == "iff"):
                return "(" + str(fpHelper(prop[i+1]) ) + " <-> " + str(fpHelper(prop[i+2])) + ")" 
            elif(prop[i] == "and"):
                return "(" + str(fpHelper(prop[i+1])) + " and " + str(fpHelper(prop[i+2])) + ")" 
            elif(prop[i] == "or"):
                return "(" + str(fpHelper(prop[i+1])) + " or " + str(fpHelper(prop[i+2])) + ")"    
            elif(prop[i] == "xor"):
                return "(" + str(fpHelper(prop[i+1])) + " xor " + str(fpHelper(prop[i+2])) + ")"    
            elif(prop[i] == "not"):
                return "(not " + str(fpHelper(prop[i+1])) + ")"
    else:
        return prop


def eval_prop(prop, values):
    '''
    evaluate a proposition formula over atomic propositions p1, p2, ... ,pn
    '''
    # fill here
    idx  =  0
    vals = {}
    for i in range(1,10):   # converts the values to a dictionary
        if ('p'+str(i) ) in  format_prop(prop):
            vals['p'+str(i)] = values[idx] 
            idx +=1
    prop = EpHelper(prop, vals)
    
    return prop

def EpHelper(prop,values):

    if type(prop) is list:
        for i in range( len(prop) ):
            if( len(prop) == 1 ):
                return EpHelper(prop[0], values)
            elif(prop[i] == "if"):
                return (not EpHelper(prop[i+1], values)) or EpHelper(prop[i+2], values)
            elif(prop[i] == "iff"):
                return ( (not EpHelper(prop[i+1], values)) or EpHelper(prop[i+2], values) ) and (  EpHelper(prop[i+1], values) or (not EpHelper(prop[i+2], values)) )
            elif(prop[i] == "and"):
                return EpHelper(prop[i+1], values)  and  EpHelper(prop[i+2], values)
            elif(prop[i] == "or"):
                return EpHelper(prop[i+1], values) or EpHelper(prop[i+2], values)   
            elif(prop[i] == "xor"):
                return (not EpHelper(prop[i+1], values) and EpHelper(prop[i+2], values ) ) or (EpHelper(prop[i+1], values) and not EpHelper(prop[i+2], values) )
            elif(prop[i] == "not"):
                return not EpHelper(prop[i+1], values)   
    else:     
        if prop == "true":
            return True    
        if prop == "false":
            return False 
        return True if values[ prop ] else False


def print_table(prop, n_var):
    '''
    print truth table
    '''
    vals = []
    for i in range(2**(n_var)):
        tmp = []  # used to store each row
        binNum = (bin(i)[2:]) # converts a number to binary
                              # there are 2**n rows, each
                              # bin # row can be used as
                              # a row for truth tab
        binNum = [int(i) for i in binNum]
        for j in range(n_var):
            tmp.append(0)
        for j in range( len(binNum)):
            tmp[j + (n_var-len(binNum))] = binNum[j]
        vals.append(tmp)
    vals.reverse()

    tableHeader = []
    infixProp = format_prop(prop)
    for i in range(1,10):
        if ('p'+str(i) ) in  infixProp:
            tableHeader.append('p'+str(i))
    tableHeader.append(" " +infixProp)
    frmat = '|'.join(['{:^12}'] * len(tableHeader))
    print(frmat.format(*tableHeader))
    print("_"*len(tableHeader)*15)
    for i in vals:
        tabVals = []
        for j in i: tabVals.append(j)
        tabVals.append(eval_prop(prop, i))
        frmat = '|'.join(['{:^12}'] * len(tabVals))
        print(frmat.format(*tabVals))

    n_var = 3


    pass


if __name__ == '__main__':
    print("---------------------------------------")
    print("Welcome to Propositional Logic!")
    print("---------------------------------------")
    values = [1, 1, 0]
    prop = ["if", ["and", "p1", ["not", "p2"]], "p3"]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    prop_str = format_prop(prop)
    print("Evaluating proposition p =", prop_str)
    prop_val = eval_prop(prop, values)
    print("over", ps_str, ":", prop_val)

    print()
    values = [1, 0, 1]
    prop = ["iff", "p1", ["or", "p2", ["not", "p3"]]]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    print("Evaluating proposition p =", format_prop(prop))
    prop_val = eval_prop(prop, values)
    print("over", ps_str, ":", prop_val)

    print("---------------------------------------------------")
    print("Table:")
    # print("\n\n")
    # print_table(["if", "p1", "p2"], 2)
    # print("\n\n")
    # print_table(["or", "true", ["and","p1","p2"]], 2)
    # print("\n\n")
    # print_table(["and", "p1", "p2"], 2)
    # print("\n\n")
    # print_table(["or", "p1", "p2"], 2)
    # print("\n\n")
    # print_table(["if", ["not","p1"], "p2"], 2)
    # print("\n\n")
    # print_table(["or", ["or","p1","p2"], ["or",["not","p1"],"p2"]], 2)
    # print("\n\n")
    # print_table(["iff", ["not",["not","p1"]], "p1"], 1)
    # print("\n\n")
    # print_table(["if", ["and", ["if", "p1", "p2"],["if", "p2", "p3"]], ["if", "p1", "p3"]], 3)
    # print("\n\n")
    # print_table(["and", ["or","p1","p2"], ["and",["not","p1"],["not","p2"]]], 2)
    # print("\n\n")
    # print_table(["not",["if", ["if","p1","false"], ["not","p1"]]  ], 2)
    print_table(["xor", ["xor","p1","p2"],  ["xor","p3","p4"]] ,4) 