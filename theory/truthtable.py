for a in range(2):
    for b in range(2):
        for c in range(2):
            result = (not (a or b) or (a or c) and not(b or not c))
            print(f'A: {a} B: {b} C: {c}, {result}')
