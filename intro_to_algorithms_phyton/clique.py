#
# How many edges in a complete graph on n nodes? 
# 

def clique(n):
    # Return the number of edges
    # Try to use a mathematical formula...
    answer = 0
    for x in range(n) :
    	answer = answer + x
   
    return answer


print clique(5)