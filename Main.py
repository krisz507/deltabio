def main(s: str):

    s.strip()

    a = s.count('A')
    c = s.count('C')
    g = s.count('G')
    t = s.count('T')

    return(f'{a} {c} {g} {t}')

if __name__ == "__main__":
    print(main(""))