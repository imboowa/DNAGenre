from DNAtools import *


seq_type = 'RNA'
DNAstr = generate_random_seq(50, seq_type)

print(f"\nSequence: {DNAstr}\n")
print(f"[1] Sequence Length: {len(DNAstr)}\n")
print(f"[2] Nucleotide Frequency: {countNucFrequency(DNAstr, seq_type)}\n")
print(f"[3] DNA->RNA: {transcription(DNAstr, seq_type)}\n")
print(f"[4] DNA template + reversed template\n\t5' {DNAstr} 3'")
print(f"\t   {''.join(['|' for _ in range(len(DNAstr))])}")
print(f"\t3' {reverseComplement(DNAstr, seq_type)} 5'\n")
print(f"[5] GC content: {gc_content(DNAstr)}%\n")
print(f"[6] GC content per sub sequences:\n\t{gc_content_per_subseq(DNAstr)}\n")
print(f"[7] Aminoacids from {seq_type}:\n\t{translation_seq(DNAstr, seq_type)}\n")
print(f"[8] Codon Usage:\n\t{codon_usage(DNAstr, seq_type)}\n")
print(f"[9] Reading Frames:")
for i in gen_openReading_frames(DNAstr, seq_type):
    print(f"\t{i}")
print(f"[10] Proteins in DNA Strand:\n")
for protein in protein_generator(DNAstr, seq_type, big_to_small=True):
    print(protein)