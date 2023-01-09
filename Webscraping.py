# Here are the essentials to download for the report

import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur
from urllib.request import Request, urlopen
import lxml
import csv

# Enter a Stock Symbol
index = 'MAR'

# URL Link
url_is = 'https://finance.yahoo.com/quote/' + index + '/financials?p=' + index
url_bs ='https://finance.yahoo.com/quote/' + index +'/balance-sheet?p=' + index
url_cf = 'https://finance.yahoo.com/quote/' + index + '/cash-flow?p='+ index





# Read URL
print(url_is)

#read_data = ur.urlopen(url_is).read()

   
req = Request(url_is, headers={'User-Agent': 'Mozilla/5.0'})    
html_is = urlopen(req)

#for line in html_is:
#    print(line)

soup_is = BeautifulSoup(html_is, 'lxml')

# Data Manipulation

ls= [] # Create empty list
for l in soup_is.find_all('div'): 
  #Find all data structure that is ‘div’
  ls.append(l.string) # add each element one by one to the list
 
#ls = [e for e in ls if e not in ('Operating Expenses','Non-recurring Events')] # Exclude those columns

new_ls = list(filter(None,ls))

new_ls

is_data = list(zip(*[iter(new_ls)]*5))
#print(is_data)


Income_st = pd.DataFrame(is_data[0:])
##print(Income_st)


Income_st.columns = Income_st.iloc[0] # Name columns to first row of dataframe
Income_st = Income_st.iloc[1:,] # start to read 1st row
Income_st = Income_st.T # transpose dataframe
Income_st.columns = Income_st.iloc[0] #Name columns to first row of dataframe
Income_st.drop(Income_st.index[0],inplace=True) #Drop first index row
Income_st.index.name = '' # Remove the index name
Income_st.rename(index={'ttm': '12/31/2022'},inplace=True) #Rename ttm in index columns to end of the year
Income_st = Income_st[Income_st.columns[:-5]] # remove last 5 irrelevant columns


Income_st.to_csv(r'D:\Coding\VSC\WebScraping/export_dataframe.csv', index=False, header=True) # How do you make it so the name  of the csv is concatenated with the stock index?

print(Income_st)


# Issues / Things to add

# Currently, any part of the table that can be expanded is not included, see Total Revenue, Operating Expense, ect. How can we either add those after the fact, or how to just clean it to include initially?
# How do you make it so the name  of the csv is concatenated with the stock index?