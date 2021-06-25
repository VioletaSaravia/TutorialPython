"""
Dia 14 - Debugging
"""

#import pdb

#PDB COMMANDS:
#a -> arg list of function
#b file:linenum, cond -> add break
#b -> list breaks
#c -> continue
#p var -> print
#cl -> clear
#l -> list
#ll -> listlong
#n -> next (skips other func defs)
#s -> step (doesn't)
#u & d -> up and down frames
#h (pdb) & q -> help and quit

def mutate(a_list):
    """ debuggear """
    b_list = []
    for item in a_list:
        new_item = item * 2
        #pdb.set_trace()
        breakpoint()
    b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])
