text = input('The greatest question in the world:  ')
text = text.strip().lower()

if (text[:5] == 'hello'):
    print('$0')
elif (text[0] == 'h'):
    print('$20')
else:
    print('$100')