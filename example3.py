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
match = soup.find_all('td padding:="" solid="" style='3D"border-bottom:' valign='3D"middle=')