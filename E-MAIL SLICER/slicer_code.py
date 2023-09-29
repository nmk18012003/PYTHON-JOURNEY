'''
IT IS A SIMPLE TOOL THAT WILL TAKE AN EMAIL ADDRESS AS INPUT AND SLICE IT TO PRODUCE THE USER-NAME AND THE DOMAIN ASSOCIATED WITH IT.

THE EMAIL MUST BE DIVIDED INTO TWO STRINGS BY USING '@' AS THE SEPARATOR.
'''

email = input("Enter your email: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1 :]

print(f"Your username is {username} & domain is {domain}")