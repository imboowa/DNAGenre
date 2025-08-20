from collections import defaultdict
# Is Done

def validate_file(filepath):
    """
    Receives a file path and reads its content
    Return 0 when ATGC numbers are high in the file
    """
    letters = defaultdict(int)
    try:
        with open(filepath, 'r') as file:
            # Set 'File Pointer' To Start At Zero
            file.seek(0)
            for i in file.read():
                letters[i] += 1
        nucs = letters['G'] + letters['C'] + letters['A'] + letters['T'] + letters['U']
        # Is Our Nucleotide Total Greater Than The Other Characters In the File
        return 0 if nucs > (sum(letters.values()) - nucs) else -1
    # Any Exception Is An Error
    except Exception:
        return -1


def clean_data(filepath, label_char):
    """
    Receives a file path and separates strand labels from DNA
    Returns a dict of {strand labels: DNA}
    """
    DNAdict = dict()
    # Temporary Storage For Read Indexes
    label = '?'
    try:
        with open(filepath, 'r') as file:
            # Set 'File Pointer' To Start At Zero
            file.seek(0)
            for i in file.readlines():
                i = i.strip()
                if label_char in str(i):
                    label = i
                    DNAdict[label] = ''
                else:
                    if label not in DNAdict.keys():
                        DNAdict[label] = ''
                    DNAdict[label] += i
        return DNAdict
    # Any Exception Is An Error
    except Exception:
        return None