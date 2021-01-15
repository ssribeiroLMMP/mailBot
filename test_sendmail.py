from mailbot_app import main

emailServer = EmailServer()

recipients = {'To':'sergio@lmmp.mec.puc-rio.br',
              'Cc':'ssribeiro@gmail.com'}

subject = 'New Test Message'
body = 'How about dinner at 6pm this saturday?'

emailServer.sendMessage(recipients,subject,body)