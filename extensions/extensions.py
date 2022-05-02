text = input('The greatest question in the world:  ')
text = text.strip().lower()

if (text[-4:] == '.gif'):
    print('image/gif')
elif (text[-4:] == '.jpg' or text[-5:] == '.jpeg'):
    print('image/jpeg')
elif (text[-4:] == '.png'):
    print('image/png')
elif (text[-4:] == '.pdf'):
    print('application/pdf')
elif (text[-4:] == '.txt'):
    print('text/plain')
elif (text[-4:] == '.zip'):
    print('application/zip')
else:
    print('application/octet-stream')