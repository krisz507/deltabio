def main3(s: str):

    s.strip()

    complements = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
    reverse = ''.join([complements[c] for c in reversed(s)])

    return (f'{reverse}')

if __name__ == '__main__':
    print(main3("AACCTAGTTACCATCCACTACAAGGTGGCGAGCTCTCTACATCTCCTCGTCCTCGAAGGGGGTGGTTGAATAGCAGCCAGCTCCGTACCGTTTTGAGGGCGGTATAGCGCCGCGTCTAATCACCCGTCCGGTCATGGTGCCGGACAGTAAATCGCGGCGCACCTACCGGCTCTAAGCGCCTTACGAACAATGCACGCATAAACACTAACCACCTACAGCGGACTTTGGTACGAGAGGCGGGCCCATTATTACTACCCTCCAACTAGACCTTGGTAGCACCCACTCATCGCAAGCCTCTGCATCTGGTTAGATGGTACGGTGATTTGACCGTCACGAGCCCGAGAGGCCATCGACAGACTTGGCCTACGTGCCGGGATTCCGACGCTACAGTCCGCTTCCATATTTTCCGGGTCTGGTTGTGACTCATATATGACGAACATGCCAGCAGCCGTTCCCAAGGGTGCTATTCAAGTCTCATCCCCATCATCATCGATAGCTGGGTAGAGGCGTCTGTATGTGCCAACAAAGGGCGGTTCGCTGCTGGGAGGGTACCGGCGCTCCGAGGGCGTTAGCCATGTTGCAGAACGACCCTGCGCGCCGAACTCTTGAGCCGTGATCTTACGGAGCTTCGCCTGTCACAGAATTCCATAATTCAATGCAGCCTAGTAAAATCAGGTGTGCGGCCTTATCTCCGAATTGGACAGTTCGAAATAGGTTCGTTTCCCTGGCAAGGCTTGAAATTCGTCGGTAAGCGGCCTTCTATAGCACAACCGAGCCCGGGGAGGACTCTAATTAGATATTGGCTAGTATGGGGAAAGTGTGGCTCCGATATCCTCAGACGAGTAATTAACAACGTTGAATGTGGTCTTGCTCTCTTGGTTGTGCCCTCTCTATACCGCATTCAACCATTAACGCTAATGGTCCGATGAGGAACCGACTCCTCATGCTCCTAT"))