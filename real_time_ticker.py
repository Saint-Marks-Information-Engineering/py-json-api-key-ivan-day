import requests

ticker = raw_input("What is the ticker: ") #asks user for ticker symbol

url = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol=" + ticker  #api url plus ticker input

r = requests.get(url) #request library magic taking in data from url
j = r.json() #converts the request to readable json
n = j["LastPrice"] #look for value under LastPrice
print(ticker + ": " + str(n)) #prints ticker price
