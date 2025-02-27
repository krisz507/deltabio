def gc_tartalom(a: str, b: str, c: str): #Computing GC Content (nincs kesz kozelt sem)

    A = a.count('C') + a.count('G')
    B = b.count('C') + b.count('G')
    C = c.count('C') + c.count('G')

    Aszaz = ( A / (len(a) / 100))
    Bszaz = (B / (len(b) / 100))
    Cszaz = (C / (len(c) / 100))

    if (Aszaz > Bszaz) and (Aszaz > Cszaz):
        return (f'valami1 {round(Aszaz, 6)}')
    
    elif (Bszaz > Aszaz) and (Bszaz > Cszaz):
        return (f'valami2 {round(Bszaz, 6)}')
    
    elif (Cszaz > Bszaz) and (Cszaz > Aszaz):
        return (f'valami3 {round(Cszaz, 6)}')

if __name__ == '__main__':
    print(gc_tartalom("CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG",
                       "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC",
                         "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"))

