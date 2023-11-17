# write a program to find duplicate numbers in a list

def find_duplicate(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                print(f"{l[i]} is a duplicate")

                

        
        