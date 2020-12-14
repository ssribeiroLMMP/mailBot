from bs4 import BeautifulSoup
from datetime import datetime

with open('Message.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup.prettify())
# Get all order info together
match = soup.find_all('td')

# Get Order Number
orderNumberText =match[0].text
for word in orderNumberText.split():
    if word.isdigit():
        orderNumber = int(word)

# Get Order Date
orderDateText = match[1].text
orderDate = datetime.strptime(orderDateText,'%d/%m/%Y %H:%M')


# Get all order info together
match = soup.find_all('s')

# Client Name
orderClientName =match[1].text

# Client CPF
orderClientCPF =match[3].text

# Client Address
orderClientAddress =match[4].text

# Get all order info together
match = soup.find_all('span')

# Order Origin
orderOrigin = match[2].text[18:]

# Client Email
orderClientEmail = match[5].text.replace('=\n    ','')

# Client Phone
orderClientPhone = match[7].text.replace('=\n    ','')

# Client Mobile
orderClientMobile = match[9].text.replace('=\n    ','')

# TODO: Order Details