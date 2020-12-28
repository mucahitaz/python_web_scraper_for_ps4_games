from requests_html import HTMLSession
import csv

csv_columns = ['Oyun Adı', 'Fiyat']
csv_file = "Oyunlar.csv"
url = "https://www.hepsiburada.com/ara?q=ps4+oyun&filtreler=MainCategory.Id:60003893"


# def get_price(url):
#     session = HTMLSession()
#     response = session.get(url)
#     for i in range(1, 10):
#         try:
#             print(i)
#             title = response.html.xpath('//div/div/ul/li[{x}]/div/a/div[2]/h3/div/p/span'.format(x=i), first=True).text
#             price = response.html.xpath('//div/div/ul/li[{x}]/div/a/div[2]/div[3]/div[2]'.format(x=i), first=True).text
#             print(title)
#             print(price)
#         except:
#             print('Hata')


def get_price():
    session = HTMLSession()
    response = session.get(url)
    links = response.html.absolute_links
    yeni = []
    my_list = []
    for link in links:
        if 'ps4-oyun' in link:
            yeni.append(link)
    for x in yeni:
        try:
            r = session.get(x)
            product = {'Oyun Adı': r.html.xpath('//*[@id="detail-container"]/div/header/span', first=True).text,
                       'Fiyat': str(r.html.xpath('//*[@id="offering-price"]/span[1]', first=True).text) + ',' + str(
                           r.html.xpath('//*[@id="offering-price"]/span[2]', first=True).text) + ' ' + str(
                           r.html.xpath('//*[@id="offering-price"]/span[3]', first=True).text)}
            my_list.append(product)
        except:
            print('Hata')
    return my_list

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in get_price():
            writer.writerow(data)
except IOError:
    print("I/O error")