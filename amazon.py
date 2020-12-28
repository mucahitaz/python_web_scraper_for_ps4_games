from requests_html import HTMLSession
import csv

csv_columns = ['Title', 'Price']
csv_file = "Games.csv"
my_url = 'https://www.amazon.com/s?k=ps4+games&rh=n%3A6427814011%2Cn%3A6427831011&dc&crid=2YU3H0IADR2RB&qid=1609171242&rnid=2941120011&sprefix=ps%2Caps%2C387&ref=sr_nr_n_2'


def get_price(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    my_list = []
    for i in range(1, 10):
        try:
            product = {
                'Title': r.html.xpath(
                    '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[{x}]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span'.format(
                        x=i), first=True).text,
                'Price': str(r.html.xpath(
                    '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[{x}]/div/span/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/a/span[1]/span[2]/span[2]'.format(
                        x=i), first=True).text) + str(r.html.xpath(
                    '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[{x}]/div/span/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/a/span[1]/span[2]/span[3]'.format(
                        x=i), first=True).text)

            }
            my_list.append(product)
        except:
            print('An error occured, continuing the loop! Wrong Index:{x}'.format(x=i))
    return my_list


try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in get_price(my_url):
            writer.writerow(data)
except IOError:
    print("I/O error")