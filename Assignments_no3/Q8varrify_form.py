import random
id=input('UserID :')
p=input('Password :')

if(id=='admin' and p=='2222'):
    captcha= random.randint(1000,9999)
    print(f'Your captcha : {captcha}')
    entered=int(input('Enter the above Number:'))
    if(captcha==entered):
        print('Login Successful')
    else:
        print('Verification Failed')
else:
     print('Invalid UserId and Password')
