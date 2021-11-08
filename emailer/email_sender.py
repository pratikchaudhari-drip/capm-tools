import yagmail


def send_email(to='brian@dripcapital.com'
               ,cc=None 
               ,subject='This is an automated email'
               ,body='This email was sent using yagmail'
               ,attachments=None):

        yag = yagmail.SMTP('brian@dripcapital.com')

        yag.send(to=to
                ,cc=cc
                ,subject=subject
                ,contents=body
                ,attachments=attachments        
        )

