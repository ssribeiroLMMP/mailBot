from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
from time import mktime
import os
from mail.utils import EmailServer


def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

# Check mail specifically for purchases
def checkForPurchases():
   emailServer = EmailServer()

   # Compose filterQuery
   # Example: 'UNSEEN (OR (FROM "nao-responder@avisoautomatico.com" TEXT "Pedido de venda") (FROM "suporte@paghiper.com"))'
   searchFilter = 'UNSEEN FROM "nao-responder@avisoautomatico.com" TEXT "Pedido de venda"'
   _, mailIDs, lenMailIDs = emailServer.checkForMails(mailbox='INBOX',filterQuery=searchFilter)

   return mailIDs, lenMailIDs

# Read purchases into Temp HTML Files
def logRecentPurchasesHTML():
   emailServer = EmailServer()

   # Compose filterQuery
   # Example: 'UNSEEN (OR (FROM "nao-responder@avisoautomatico.com" TEXT "Pedido de venda") (FROM "suporte@paghiper.com"))'
   searchFilter = 'UNSEEN FROM "nao-responder@avisoautomatico.com" TEXT "Pedido de venda"'
   recentPurchasesList = emailServer.readMessages(mailbox='INBOX',filterQuery=searchFilter,htmlFile='temp/purchaseMails')

   return recentPurchasesList

# Check mail specifically for purchases
def checkForPayments():
   emailServer = EmailServer()

   # Compose filterQuery
   # Example: 'UNSEEN (OR (FROM "nao-responder@avisoautomatico.com" TEXT "Pedido de venda") (FROM "suporte@paghiper.com"))'
   searchFilter = 'UNSEEN FROM "suporte@paghiper.com" TEXT "Pagamento" TEXT "foi aprovado"'
   _, mailIDs, lenMailIDs = emailServer.checkForMails(mailbox='INBOX',filterQuery=searchFilter)

   return mailIDs, lenMailIDs