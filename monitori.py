
from bs4 import BeautifulSoup
import requests
import os, sys 
from openpyxl import Workbook 
from datetime import datetime
from openpyxl.styles import Font

url = requests.get("https://www.links.hr/hr/monitori-1003")


soup = BeautifulSoup(url.content,"html.parser")

body = soup.find(class_="page-body")
item = body.find(class_="item-box")
products = body.find_all(class_="product-item")
#details = products[0].find_all(class_="details")
prices = body.find_all(class_="prices")
pictures = body.find_all(class_="picture")

info = []
for i in range(len(prices)):
	info.append(products[i].find(class_="old-price").get_text())

#info = products.find_all(class_="add-info")

#print(detail)

titles = [product.find(class_="product-title").get_text() for product in products]
actual_prices = [price.find(class_="price actual-price").get_text()[0:-5]  for price in products]
old_prices = [price[0:-5]  for price in info]
pictures = [pic.img["src"] for pic in pictures]
#likes = [like.find(class_="item-like-counter_67997 like-btn item-like-counter") for like in details]

#print(likes)
#print(actual_prices)

"""
for title in titles:
		for prices in actual_prices:
			
			for price in old_prices:

				for pic in pictures:


					pprice = prices.split(".")
					op = price.split(".")
				
					pprice= "".join(pprice)
					op = "".join(op)
					#price = int(price)

					print(f"Title: {title}Actuall price: {pprice} kn \nOld price: {op} kn")
					print(f"Picure(link): {pic}")"""








dt = datetime.now() 

wb = Workbook() 
sheet = wb.active 
sheet.title = 'Monitors'
# Print the titles into Excel Workbook: 
row = 1 
col = 1
ps = 1 
sheet['A'+str(row)] = 'Monitor' 
sheet['B'+str(row)] = 'Old Price' 
sheet['C'+str(row)] = 'Actual Price'
sheet['A1'].font = Font(size=18, italic=True)
sheet['B1'].font = Font(size=18, italic=True)
sheet['C1'].font = Font(size=18, italic=True)
# Populate with data 
for item in titles:
	row += 1    
	sheet.column_dimensions['A'].width = 115
	sheet['A'+str(row)] = item + " kn"
	

for price in old_prices:
	if price == "":
		price = "0"  
	sheet.column_dimensions['B'].width = 16
	col += 1   
	sheet["B"+str(col)]  = price + " kn"

for p in actual_prices:
	sheet.column_dimensions['C'].width = 16

	ps += 1    	
	sheet["C"+str(ps)] =  p + " kn"
	
# Save a file by date: 
filename = 'data_' + dt.strftime("%Y%m%d_%I%M%S") + '.xlsx' 
wb.save(filename)
# Open the file for the user: 
os.chdir(sys.path[0]) 
os.system('start excel.exe "%s\\%s"' % (sys.path[0], filename,))


"""


url2 = requests.get("https://www.links.hr/hr/")


soup2 = BeautifulSoup(url2.content,"html.parser")
body2 = soup2.find(class_="page-body")
print(body2)












prices = [price[0:-6] for price in info]




for title in titles:
		for price in prices:
			print(f"Title: {title}Prices: {price}")
			print()



)
for product in products:
	for title in product.find(class_="product-title").get_text():
		titles.append(title)
	for price in product.find(class_="price actual-price").get_text():
		actual_prices.append(price)


for p in actual_prices:
	#print(prices.index(p))
	if p == " ":
		actual_prices.remove(p)


#print("".join(titles))
#print("".join(actual_prices))
	
	

"""
