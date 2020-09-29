def countsubstring(statement):
    sl= len(statement)
    count = 0
    for i in range(sl - 1):
         count += statement[i: i + 4] == 'Emma'
    return count
    
    
counttimes = countsubstring("EmmagEMmahijisEmma")
print ("\"Emma \" appeared ", counttimes, "times")
"""Return the total count of sub-string “Emma” appears in the given string"""
