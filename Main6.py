def main6(s: str, t:str):

    tavolsag = 0

    for i in range(len(s)):
        if s[i] != t[i]:
            tavolsag += 1

    return tavolsag

if __name__ == '__main__':
    print(main6("",
                 ""))