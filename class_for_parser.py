from bs4 import BeautifulSoup
import urllib.request


class Parser:

    raw_html = ''
    html = ''
    results = []

    def __init__(self,url,path):
        self.url = url
        self.path = path
    
    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html,'html.parser')

    def parsing(self):
        news = self.html.find_all('li',class_="liga-news-item")

        for item in news:
            title = item.find('span',class_='d-block').get_text(strip=True)
            desc = item.find('span',class_='name-dop').get_text(strip=True)
            href = item.a.get('href')
            self.results.append({
                'title':title,
                'desc':desc,
                'href':href,
                }
            )

    def save(self):
        with open(self.path,'w',encoding='utf-8') as f:
            i=0
            for item in self.results:
                i+=1
                f.write(f'Новость № {i} \n\nНазвание: {item["title"]}\nОписание: \
                 {item["desc"]}\n\nСсылка: {item["href"]}\n\n**************************\n')
                 
    def success(self):
        if len(self.results) > 0:
            print(' OK! ')
        else:
            raise Exception('something wrong')

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
        self.success()

