from bs4 import BeautifulSoup
from datetime import datetime

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

# TODO: Order Details
matchDiv = soup.find('div',style="color: #475C7A; padding: 5px 20px 10px; border: 5px solid #EFF8FF;")
matchTable = matchDiv.find_all('table',border="0")


