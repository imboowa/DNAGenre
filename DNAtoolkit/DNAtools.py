from DNAtoolkit.structures import *
import random


def generate_random_seq(length: int, seq_type: str):
    """
    Parameters:
        length - How long the sequence would be
        seq_type - What is the type of molecule DNA or RNA
    Intuition:
        Receives length and sequence type.
        Uses Random module method 'choice' to pick choice in nucleotide dictionary based on seq type.
        Returns a randomly generated seq_type sequence.
    Return:
        -1 length less than 1 or sequence not in NUCLEOTIDE_BASES
        A String of randomly generated nucleotide bases
    """
    if length <= 0 or seq_type not in NUCLEOTIDE_BASE.keys():
        return -1
    return ''.join([random.choice(NUCLEOTIDE_BASE[seq_type]) for _ in range(length)])

def validate_seq(seq: str, seq_type: str):
    """
    Parameters:
        seq - Sequence to be validated
        seq_type - Type of sequence DNA or RNA
    Intuition:
        Receives seq_type sequence.
        Uses Set method 'issuperset' to check if all in seq are in NUCLEOTIDE_BASE[seq_type].
        Returns True if all true else False.
    Return:
        -1 If seq type is not in NUCLEOTIDE_BASES
        A Boolean value of True or False
    """
    if seq_type not in NUCLEOTIDE_BASE.keys():
        return -1
    return set(NUCLEOTIDE_BASE[seq_type]).issuperset(seq)

def countNucFrequency(seq: str, seq_type: str):
    """
    Parameters:
        seq - Sequence to have its nucleotides counted
        seq_type - Type of sequence DNA or RNA
    Intuition:
        Receives seq_type sequence and its sequence type.
        Returns nucleotide count dictionary for the sequence.
    Return:
        -1 If seq is empty
        -2 If seq type is unavailable
        A Dictionary of nucleotides counted
    """
    if not seq:
        return -1
    if seq_type == "DNA":
        nuc_dict_DNA = {'A':0, 'T':0, 'G':0, 'C':0}
        for nuc in seq:
            if nuc in nuc_dict_DNA.keys(): nuc_dict_DNA[nuc] += 1
        return nuc_dict_DNA
    elif seq_type == "RNA":
        nuc_dict_RNA = {'A':0, 'U':0, 'G':0, 'C':0}
        for nuc in seq:
            if nuc in nuc_dict_RNA.keys(): nuc_dict_RNA[nuc] += 1
        return nuc_dict_RNA
    else:
        return -2

def transcription(seq: str, seq_type: str):
    """
    Parameters:
        seq - Sequence to have its nucleotides counted
        seq_type - Type of sequence DNA or RNA
    Intuition:
        Receives seq_type sequence and sequence type.
        Uses String method 'replace' to put 'U' where 'T' was.
        Returns RNA sequence.
    Return:
        -1 If not DNA
        A String of RNA
    """
    return seq.replace('T','U') if seq_type == 'DNA' else -1

def reverseComplement(seq: str, seq_type: str):
    """
    Parameters:
        seq - Sequence to have its nucleotides counted
        seq_type - Type of sequence DNA or RNA
    Intuition:
        Receives seq_type sequence and sequence type.
        Uses String method 'maketrans' to reverse the nucleotides.
        Use String method 'translate' to bring back the nucleotides instead of the 'maketrans' numbers.
        Reverses the string.
        Returns reversed complementary strand.
    Return:
        -1 If seq type unavailable
        A String of the reversed-complementary strand
    """
    if seq_type == "DNA":
        mapping = str.maketrans('ATGC', 'TACG')
        return seq.translate(mapping)[::-1]
    elif seq_type == "RNA":
        mapping = str.maketrans('AUGC', 'UACG')
        return seq.translate(mapping)[::-1]
    else:
        return -1

def gc_content(seq: str):
    """
    Parameters:
        seq - Sequence to have its nucleotides counted
    Intuition:
        Receives the sequence.
        Uses String method 'count' to count all 'C' and 'G' occurrences.
        Divides total by sequence length.
        Multiplies result by 100 to get the percentage.
        Rounds it to 6 decimal places.
        Returns GC content percentage.
    Return:
        -1 If Seq is empty
        A Float result for GC percentage
    """
    if not seq:
        return -1
    return round(((seq.count('G') + seq.count('C')) / len(seq)) * 100, 2)

def gc_content_per_subseq(seq: str, k=5):
    """
    Parameters:
        seq - Sequence to have its nucleotides counted
        k - the size of a jump
    Intuition:
        Receives sequence and k-jumps.
        Uses 'gc_content' function to calculate GC content.
        Appends every k-jump's GC content to a List.
        Returns a list of GC content for the k-jumps.
    Return:
        -1 If seq is empty
        A List of GC content for the k-jumps
    """
    if not seq:
        return -1
    temp_seq = list()
    for i in range(0, len(seq) - k + 1, k):
        temp_var = seq[i:i + k]
        gc_result = gc_content(temp_var)
        if gc_result != -1:
            temp_seq.append(gc_result)
        elif gc_result == -1:
            temp_seq.append(0)
    return temp_seq

def at_content(seq: str, seq_type: str):
    """
    Parameters:
        seq - Sequence to have its nucleotides counted
    Intuition:
        Receives the sequence.
        Uses String method 'count' to count all 'A' and 'T' occurrences.
        Divides total by sequence length.
        Multiplies result by 100 to get the percentage.
        Rounds it to 6 decimal places.
        Returns AT content percentage.
    Return:
        -1 If seq is empty
        -2 If seq type is unavailable
        A Float result for AT percentage
    """
    if not seq:
        return -1
    if seq_type == 'DNA':
        return round(((seq.count('A') + seq.count('T')) / len(seq)) * 100, 2)
    elif seq_type == 'RNA':
        return round(((seq.count('A') + seq.count('U')) / len(seq)) * 100, 2)
    else:
        return -2

def translation_seq(seq: str, seq_type: str, initial_pos: int=0):
    """
    Parameters:
        seq - Sequence to have its nucleotides counted
        seq_type - Type of sequence
        initial_pos - the start position for translation (triplet nucleotides to codons)
    Intuition:
        Receives the sequence and initial position to search for codons.
        Respects the seq_type and find codons based on the sequence type.
        Takes in triplet nucleotides and looks for their codon in seq_type codon table.
        Returns a list of codons found from initial positions to end.
    Return:
        -1 If initial position greater than 2 or initial position is less than 0
        -2 If seq is empty
        -3 If seq type unavailable
        A List of codons for the sequence
    """
    if initial_pos > 2 or initial_pos < 0:
        return -1
    if not seq:
        return -2
    if seq_type == 'DNA':
        return [DNA_Codons[seq[pos:pos + 3]] for pos in range(initial_pos, len(seq) - 2, 3)]
    elif seq_type == 'RNA':
        return [RNA_Codons[seq[pos:pos + 3]] for pos in range(initial_pos, len(seq) - 2, 3)]
    return -3

def codon_usage(seq, seq_type, initial_pos=0):
    """
    Parameters:
        seq - Sequence to have its nucleotides counted
        seq_type - Type of sequence
        initial_pos - the start positions for translation (triplet nucleotides into codons)
    Intuition:
        Receives DNA sequence and initial starting position.
        Calls 'translation_seq' function and checks if return result is None.
        Loops through the 'translation_seq' result counting the codons appearing.
        Returns dict of codons and frequency.
    Return:
        -1 If initial pos is greater than 2 or initial pos less than 0
        -2 If seq is empty
        -3 If seq type unavailable
        A Dictionary of codon and number of appearance times
    """
    if initial_pos > 2 or initial_pos < 0:
        return -1
    if not seq:
        return -2
    if seq_type not in NUCLEOTIDE_BASE.keys():
        return -3
    temp = translation_seq(seq, seq_type, initial_pos)
    if temp == -1 or temp == -2 or temp == -3:
        return None
    temp_dict = dict()
    for i in temp:
        if i not in temp_dict.keys(): temp_dict[i] = 1
        else: temp_dict[i] += 1
    return temp_dict

def gen_openReading_frames(seq, seq_type):
    """
    Parameters:
        seq - Sequence to have its nucleotides counted
        seq_type - Type of sequence
    Intuition:
        Receives sequence and seq_type.
        Appends to 'frames' List the template strand's open reading frames form read position 0, 1, 2.
        Appends to 'frames' List the reversed templated strand's open reading frames from read 0, 1, 2.
        Returns reading frames: normal and reversed strand.
    Return:
        -1 If empty seq
        -2 If seq type not in NUCLEOTIDE_BASES
        A 2D List of all open reading frames
    """
    if not seq:
        return -1
    if seq_type not in NUCLEOTIDE_BASE.keys():
        return -2
    frames = list()
    frames.append(translation_seq(seq, seq_type, 0))
    frames.append(translation_seq(seq, seq_type, 1))
    frames.append(translation_seq(seq, seq_type, 2))
    frames.append(translation_seq(reverseComplement(seq, seq_type), seq_type, 0))
    frames.append(translation_seq(reverseComplement(seq, seq_type), seq_type, 1))
    frames.append(translation_seq(reverseComplement(seq, seq_type), seq_type, 2))
    return frames

def proteins_from_reference(seq: str):
    """
    Parameters:
        seq - Sequence to have its nucleotides counted
    Intuition:
        Receives sequence.
        Creates two lists (one stores protein(s) when stop codon is found) (one stores protein(s) found after start codon).
        If start codon is found, the 'current_protein' list creates an entry with codon(s) including start codon, then all that comes is put into that entry.
        Else stop codon is found, checks if there are protein(s) in the 'current_protein' list then appends all to the 'protein' list and sets the 'current_protein' list to empty.
        Returns all proteins in sequence.
    Return:
        -1 If seq is empty
        A List of all proteins in the sequence
    """
    if not seq:
        return -1
    proteins = list()
    current_protein = list()
    for nuc in seq:
        if nuc == '_':
            if current_protein:
                for protein in current_protein:
                    proteins.append(protein)
                current_protein = list()
        else:
            if nuc == 'M':
                current_protein.append('')
            for i in range(len(current_protein)):
                current_protein[i] += nuc
    return proteins

def protein_generator(seq: str, seq_type: str, start_pos=0, stop_pos=0, big_to_small=True):
    """
    Parameters:
        seq - Sequence to have its nucleotides counted
        seq_type - Type of sequence DNA or RNA
        start_pos - where to start when generating proteins in string
        stop_pos - where to stop when generating proteins
        big_to_small - if True, descending order else ascending order
    Intuition:
        Receives a sequence, seq_type, start_pos, stop_pos, big_to_small.
        Creates 'protein_list' List and loops through frames in 'frame_seq'.
        Passes down that frame to 'proteins_from_reference' function to get protein(s) in that frame.
        Loops through that returned list of protein(s) for frame and appends that to the 'protein_list'.
        A huge list of protein(s) is got and returned in either ascending or descending order.
        Returns all protein(s).
    Return:
        -1 If seq is empty
        -2 If seq type unavailable
        A List of proteins()
    """
    if not seq:
        return -1
    if seq_type not in NUCLEOTIDE_BASE.keys():
        return -2
    if start_pos < stop_pos:
        frame_seq = gen_openReading_frames(seq[start_pos:stop_pos], seq_type)
    elif start_pos > stop_pos:
        frame_seq = gen_openReading_frames(seq[stop_pos:start_pos], seq_type)
    else:
        frame_seq = gen_openReading_frames(seq, seq_type)
    protein_list = list()
    for frame in frame_seq:
        temp_protein_list = proteins_from_reference(frame)
        for protein in temp_protein_list:
            protein_list.append(protein)
    if big_to_small:
        return sorted(protein_list, key=len, reverse=True)
    else:
        return protein_list

def n_distance(seq_1: str, seq_2: str):
    """
    Parameters:
        seq_1 - sequence one to be compared to sequence two
        seq_2 - sequence two
    Intuition:
        Receives 2 sequences and checks each index on both (i=0 at seq_1 also i=0 at seq_2).
        Returns a tuple (index, seq_1[i], seq_2[i]).
    Return:
        A List of tuples containing (index, seq_1[i], seq_2[i])
        -1 If seq 1 or seq 2 is empty
        -2 If seq 1's length is not equal to seq 2's length
    """
    if not seq_1 or not seq_2:
        return -1
    if len(seq_1) != len(seq_2):
        return -2
    n_distance_list = list()
    for index, (nuc_1, nuc_2) in enumerate(zip(seq_1, seq_2)):
        n_distance_list.append((index, nuc_1, nuc_2))
    return n_distance_list

def k_mer_indexes(seq: str, seq_type: str, k_mer: str):
    """
    Parameters:
        seq - Sequence to have its nucleotides counted
        seq_type - Type of k_mer
        k_mer - the small segment we are looking for
    Intuition:
        Receives a seq and checks if the both are compatible.
        Searches for k_mer in received sequence.
        If an index has the desired 'k_mer', we keep that index.
        Returns a list of indexes where k_mer appeared (length of that list could be the k_mers in sequence).
    Return:
        -1 if K_mer and seq_type are incompatible
        -2 if seq is empty or k_mer is empty
        A List of indexes where k_mer appeared
    """
    if not validate_seq(k_mer, seq_type):
        return -1
    if not seq or not k_mer:
        return -2
    k_mer_list = list()
    for i in range(len(seq) - len(k_mer) + 1):
        if seq[i:i+len(k_mer)] == k_mer:
            k_mer_list.append(i)
    return k_mer_list

def highest_k_mer_len(seq: str, k_mer_len: str):
    """
    Parameters:
        seq - Sequence to have its nucleotides counted
        k_mer_len - the length of k_mer we want to find
    Intuition:
        Receives a sequence
        Creates a 'k_mers' Dictionary.
        Loops through sequence getting segments of length of the k_mer's length.
        Adds those segments to Dictionary {'segment':appearances}.
        Returns a Dictionary of {'segment':appearances:int}.
    Return:
        -1 If seq is empty
        -2 if k_mer_len is not int
        -3 If k_mer_len is below 0 or above the length of seq
        A Dictionary of {'segment':appearance}
    """
    if not seq:
        return -1
    if not k_mer_len.isdigit():
        return -2
    k_mer_len = int(k_mer_len)
    if k_mer_len <= 0 or k_mer_len > len(seq):
        return -3
    k_mers = dict()
    for i in range(len(seq) - k_mer_len + 1):
        if seq[i:i + k_mer_len] not in k_mers.keys():
            k_mers[seq[i:i + k_mer_len]] = 1
        else:
            k_mers[seq[i:i + k_mer_len]] += 1
    return k_mers

def DNA_fib_list(stop_fibonacci: int):
    """
    Parameters:
        stop_fibonacci - this is the number that we stop on
    Intuition:
        Receives top number for the list.
        Uses 'while' loop to check the highest produced fibonacci on the stop fibonacci.
        Returns list of fibonacci numbers till the stop fibonacci.
    Return:
        A List of fibonacci numbers till the stop fibonacci
    """
    if stop_fibonacci < 3:
        return "Bad Stop Fibonacci Number"
    fib_list = list()
    a, b = 0, 1
    while (a + 3) <= stop_fibonacci:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list