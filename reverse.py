def reverse_bykv(text: str) -> str:
    if not isinstance(text,str):
        raise ValueError('text must be a string')


    s = [x for x in text if x.isalpha()]
    s.reverse()

    result = []
    index = 0

    for i in range(len(text)):
        inx = text[i]
        if inx.isalpha():
            result.append(s[index])
            index += 1
        else:
            result.append(inx)

    return ''.join(result)


if __name__ == '__main__':  # pragma: no cover
    test1 = 'syka12dadasdsgergr4'
    test2 = 'govonzalupapen1s'

    print(reverse_bykv(test1))
    print(reverse_bykv(test2))
