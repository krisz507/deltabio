def main7(k: int, m: int, n: int):

    osszesen = k + m + n
    kedvezo = 0.0

    kedvezo += (k / osszesen) * ((k - 1) / (osszesen - 1))  
    kedvezo += (k / osszesen) * (m / (osszesen - 1)) * 2 
    kedvezo += (k / osszesen) * (n / (osszesen - 1)) * 2    
    kedvezo += (m / osszesen) * ((m - 1) / (osszesen - 1)) * 0.75  
    kedvezo += (m / osszesen) * (n / (osszesen - 1)) * 0.5 * 2  
    
    return round(kedvezo, 5)

if __name__ == '__main__':
    print(main7(19, 30, 17))