# ========== PSEUDO CODE ==========
# - Def function
def counting_lines_in_a_text():
    file = open("story.txt","r")
    count= 0
    
# - Using for loop
    for i in file:
        count+= 1
    file.close()
    
# - Printing the conclusion
    print("The number of lines in the 'story.txt' file is", count) 
    
# - Caller of the def function
counting_lines_in_a_text()