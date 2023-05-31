def matching_parentheses(string):
    opening = []
    pairs = []
    for o, c in enumerate(string):
        if c == ')':
            if len(opening) == 0:
                return False
            else:
                temp = []
                temp.append(opening.pop())
                temp.append(o)
                pairs.append(tuple(temp))
                return pairs
        elif c == '(':
            opening.append(o)
def calculate(arr:list):
    steps = []
    text = ''
    for element in arr:
        text += element
    steps .append(text +'\n')
    m = matching_parentheses(text)
    while(m):
        num = m[0][0]
        num2 = m[0][1]
        if not text[num-1].isdigit():
            new_str = text[0:num] + str(eval(text[num+1:num2])) + text[num2+1:]
        else:
            new_str = text[0:num] + '* ' + str(eval(text[num + 1:num2])) + text[num2 + 1:]
        text = new_str
        steps.append( text + '\n')
        m = matching_parentheses(text)
    return (steps)
    