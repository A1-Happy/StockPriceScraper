from requests_html import HTMLSession
s = HTMLSession()
query = input("Enter a Company name: ")
url = f'https://www.google.com/search?q=stock+price+{query}'
try:
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'})
except:
    print("Network Error. Please try again later.")
    exit()
try:
    temp = r.html.find('div.PZPZlf span.IsqQVc.NprOob.wT3VGc', first = True).text
except:
    print("Company not found.")
    exit()
name = r.html.find('div.oPhL2e span.aMEhee.PZPZlf', first = True).text
desc = r.html.find('span.knFDje', first = True).text
print(f'{name}        {temp} {desc}')