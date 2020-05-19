"""
author: Sanchit Monga
language: python3
function:  compare two different files in Python and the comparison is
line by line and character by character on each line of a file.
"""
def char_by_char(filename1, filename2):
    """
    This function takes in two inputs of text files and compares them charecter by charecter and
    prints out the the index of the characters which are different and the line which they are present in.
    It also prints out the number of charecters in both the files. It also prints the number of unmatched lines.
    """
    f1 = open(filename1)
    f2 = open(filename2)
    line_count = 0    #line number
    unm_char = 0   #No. of unmatched characters
    unm_line = 0   #No. of unmatched lines
    st = ""        # empty string to print out the unmatched charecters
    ch_count_line = 0    #count of the number of charecters in f1
    ch_count_line1 = 0  #count of the number of charecters in f2
    while True:
        line_count += 1
        line = f1.readline()
        line = line.strip()
        line1 = f2.readline()
        line1 = line1.strip()
        if len(line1) == len(line):
            for i in range(len(line)):
                if line[i] != line1[i]:
                    unm_char += 1
                    st += str(line_count) + ":" + str(i + 1) + ", "
                        
        elif len(line1)!= len(line) or len(line) == 0 or len(line1) == 0:
            unm_line += 1
            st += str(line_count) + ", "
        for i in range(len(line1)):
            ch_count_line1 += 1
        for i in range (len(line)):
            ch_count_line += 1
        if not line:
            print("Character by character: ")
            print("Unmatched Charecters: ", st)
            print("There are", ch_count_line, "charecters in", filename1)
            print("There are", ch_count_line1, "charecters in", filename2)
            print("There were", unm_char, "unmatched charecters in the files")
            print("There were", unm_line, "lines of different length." )
            f1.close()
            f2.close()
            break                    

def main():
    """
    main function prompts the user for input and after taking the input from the user it calls char_by_char function
    """
    filename1 = input("Enter the first filename: ")
    filename2 = input("Enter the second filename: ")
    char_by_char(filename1, filename2)
#calling the main function
main()
