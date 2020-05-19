"""
author:Sanchit Monga
Lang: Python
Purpose: This program performs various operations on the nodes
"""
from linked_code import LinkNode as Node
import linked_code
def convert_to_nodes(dna_string):
    """
This function takes the string as the input and convert it into the node data structure

"""
    if(dna_string==""):
        return None
    else:
        return Node(dna_string[0],convert_to_nodes(dna_string[1:]))

def is_match(dna_seq1, dna_seq2):
    """
This function takes the input of 2 DNA sequences and matches whether the two sequences are true or not
"""
    if dna_seq1==None and dna_seq2==None:
        return True
    elif dna_seq1==None or dna_seq2==None:
        return False
    elif dna_seq1.value!=dna_seq2.value:
        return False
    else:
        return is_match(dna_seq1.rest, dna_seq2.rest)
        
def insertion(dna_seq1,dna_seq2,index):
    """
This function takes the input of 2 DNA sequences and an index and insert the second DNA sequence in the first sequence at the specified index
"""
    if index==0:
        return linked_code.concatenate(dna_seq2,dna_seq1)
    elif dna_seq1==None:
        raise IndexError ("Invalid Insertion Index")
    else:
        return (Node(dna_seq1.value,insertion(dna_seq1.rest,dna_seq2, index-1)))
    
def is_palindrome(dna_seq):
    """
This function takes the DNA sequence in the form of Node data structure and checks whether it is palindrome or not
"""
    if(dna_seq==None):
        return True
    elif(linked_code.length_rec(dna_seq)==1):
        return True
    elif(dna_seq.value==linked_code.value_at(dna_seq,(linked_code.length_tail_rec(dna_seq)-1))):
        return is_palindrome(linked_code.remove_at(linked_code.length_rec(dna_seq.rest)-1,dna_seq.rest))
    else:
        return False

    
def substitution(dna_seq,index,base):
    """
This function takes the input of the DNA sequence, index at which the base has to be replaced and the base by which the original sequence will be replaced
"""
    if linked_code.length_rec(dna_seq)<index:
        raise IndexError ("Invalid Insertion Index")    
    else:
        return linked_code.insert_at(index,base,linked_code.remove_at(index,dna_seq))

def convert_to_string(dna_seq):
    """
This function converts the DNA sequence which is a node datta structure into the string data type
"""
    if(dna_seq==None):
        return ""
    else:
        return(str(dna_seq.value)+convert_to_string(dna_seq.rest))

def is_pairing(dna_seq1,dna_seq2):
    """
This function takes 2 DNA sequences in the form of Node data structure and check whether the corrersponding elements are matching or not
"""
    if(dna_seq1==None and dna_seq2== None):
        return True
    elif(dna_seq1==None or dna_seq2==None):
        return False
    elif(dna_seq1.value=='A' and dna_seq2.value=='T'):
        return is_pairing(dna_seq1.rest,dna_seq2.rest)
    elif(dna_seq1.value=='G' and dna_seq2.value=='C'):
        return is_pairing(dna_seq1.rest,dna_seq2.rest)
    elif(dna_seq1.value=='T' and dna_seq2.value=='A'):
        return is_pairing(dna_seq1.rest,dna_seq2.rest)
    elif(dna_seq1.value=='C' and dna_seq2.value=='G'):
        return is_pairing(dna_seq1.rest,dna_seq2.rest)
    else:
        return False

def deletion(dna_seq, idx, segment_size):
    """
This function takes the DNA sequence , index at which the element has to deleted and the segment size that has to be deleted
"""
    if(segment_size==0):
        return dna_seq
    elif(segment_size+idx>linked_code.length_rec(dna_seq)):
        raise IndexError("Sequence out of range")
    else:
        return deletion(linked_code.remove_at(idx,dna_seq), idx,segment_size-1)

def duplication(dna_seq, idx, segment_size):
    """
This function takes the dna_seq, index  a and the segment size that has to be copied and added after that
"""
    
    if segment_size!=0:
        a=segment_size
        while(segment_size>0):
            v=linked_code.value_at(dna_seq,idx)
            dna_seq=linked_code.insert_at(idx+a,v,dna_seq)
            idx+=1
            segment_size-=1
        return dna_seq
    else:
        return dna_seq
    
