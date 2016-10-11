def is_matched(expression):
    toMatch = []
    pairs = {'}':'{', ']':'[', ')':'('}
    for exp in expression:
        if len(toMatch) == 0:
            toMatch.append(exp)
        elif exp not in pairs.keys():
            toMatch.append(exp)
        else:
            if pairs[exp] == toMatch[-1]:
                toMatch.pop()
        print toMatch

is_matched('{[()]}')
