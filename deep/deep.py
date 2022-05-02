text = input('The greatest question in the world:  ')
text = text.strip().lower()

if (text == '42' or text == 'forty-two' or text == 'forty two'):
    print('Yes')
else:
    print('No')