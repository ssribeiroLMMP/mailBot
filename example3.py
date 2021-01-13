from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
from time import mktime

conn = sqlite3.connect('./database/Orders.db')

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

with open('output1.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup.prettify())
# Get all order info together
match = soup.title

# Get Order Number
orderNumberText =match.text
for word in orderNumberText.split():
    if word.isdigit():
        orderNumber = int(word)

# Get Order Date
match = soup.find_all('td',style = "border-bottom: 1px solid #ddd; padding: 6px;")

# Client Name
orderClientName =match[1].text

# Client CPF
orderClientEmail =match[3].text

# Client Address
orderClientMobile =match[5].text

# Client CPF
orderClientCPF =match[7].text

# Client Address
orderClientAddress = match[9].text.replace('\n        ',' - ').replace('\n',' - ')

# Client Data Dictionary
orderClientData = {'CPF': orderClientCPF,
                   'Name': orderClientName,
                   'Email': orderClientEmail,
                   'Mobile': orderClientMobile,
                   'Address': orderClientAddress}
# Order Shipment Type
orderChipment = 

# Order Items Initialization
orderItems = [{}]

# Match Data
matchDiv = soup.find('div',style="color: #475C7A; padding: 5px 20px 10px; border: 5px solid #EFF8FF;")
matchTable = matchDiv.find_all('table',border="0")
tableLines = matchTable[2].find_all('tr')

orderItems = []
orderSubtotal = 0

# Append Column Values
for line in tableLines[1:]:
    columns = line.find_all('td')
    ItemId = columns[1].text[columns[1].text.find('SKU:')+5:-2]
    ItemDescrition = columns[1].text.replace('  ','').replace('\n',' ')
    ItemQty = int(columns[2].text)
    ItemPrice = float(columns[3].text.replace('R$ ',''))
    orderItems.append({'Id':ItemId ,
                       'Description':ItemDescrition,
                       'Quantity':ItemQty,
                       'Price':ItemPrice})
    orderSubtotal = orderSubtotal+ItemPrice

# Order Shipment Type
tableLinesNew = matchTable[3].find_all('tr')
OrderShipment = tableLinesNew[1].find_all('td').text


# Order Complete Data
orderData = {'Number': orderNumber,
             'DateTime': mktime(datetime.now().timetuple()),
             'Client': orderClientData['CPF'],
             'Shipment': OrderShipment,
             'Subtotal': orderSubtotal
             'Items': orderItems}


with conn:
    c = conn.cursor()
    # Insert or Update Clients data
    try:
        c.execute("INSERT INTO clients VALUES (:CPF, :Name, :Email, :Mobile, :Address)", orderClientData)
    except:
        c.execute("""UPDATE clients SET name = :Name, 
                                        email = :Email,
                                        mobile = :Mobile,
                                        address = :Address 
                    WHERE cpf = :CPF""", orderClientData)
    
    # Insert or Update Order data
    try:
        c.execute("INSERT INTO orders VALUES (:Number, :DateTime, :Client)", orderData)
    except:
        c.execute("""UPDATE orders SET dateTime = :DateTime,
                                        client = :Client 
                    WHERE number = :Number""", orderData)
    
    # Insert or Update Order Items
    try:
        for item in orderItems:
            c.execute("""INSERT INTO orderItems VALUES (orderData['Number'],
                                                        item['id'],
                                                        item['Description'],
                                                        item['Quantity'],
                                                        item['Price'])""")


    except:
        c.execute("""UPDATE clients SET name = :Name, 
                                        email = :Email,
                                        quantity = :Quantity,
                                        price = :Price 
                    WHERE orderNumber = :Number""", orderItems)
pretty(order)

# TODO: Save in Database