emails=['hello@gmail.com','hello@yahoo.com','hello@hotmail.com','contact@gmail.com','contact@outlook.com']


domains=set([email.split('@')[1] for email in emails])
print(domains)
    


''