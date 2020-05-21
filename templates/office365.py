from O365 import Account
from requests import request

# Microsoft client secret: t1-K7l~NMF.NZ-_29xPD-m5p-X3.8ex8KR

CLIENT_ID = "d5cefbb8-8f72-40e4-91c3-ca3f900c1363"
CLIENT_SECRET = "t1-K7l~NMF.NZ-_29xPD-m5p-X3.8ex8KR"
AUTHORITY = "https://login.microsoftonline.com/d6bf299f-57f6-4534-9c77-168f5c6df4b0"

credentials = ('samuel.dd@gmail.com', 'Azure8888816119')
scopes = ['https://graph.microsoft.com/Mail.ReadWrite', 'https://graph.microsoft.com/Mail.Send']

account = Account(credentials, scopes=scopes)

if account.authenticate():
   print('Authenticated!')

else:
    print('Error')

# Check for user in the session

# m = account.new_message()
# m.to.add('shamuel.dandwate@gmail.com')
# m.subject = 'Testing!'
# m.body = "George Best quote: I've stopped drinking, but only while I'm asleep."
# m.send()