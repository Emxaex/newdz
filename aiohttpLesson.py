import aiohttp
import asyncio
from bs4 import BeautifulSoup


url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'


async def main():
    async with aiohttp. ClientSession() as session:
        async with session.get(url) as response:
            web_content = await response.text()
            soup = BeautifulSoup(web_content, 'html.parser')
 #          print(soup.find(alt='image-element').get('src'))
            NameOfBook = soup.find('h1').text
            Price = soup.find('p', {'class': 'price_color'}).text
            Sklad = soup.find('p',{'class':'instock availability'}).text.strip()
            Photo = soup.find(alt='A Light in the Attic').get('src')
            print(f'Название книги - {NameOfBook}\n'
                  f'Цена - {Price}\n'
                  f'Кол-во товара - {Sklad}\n'
                  f'Ссылка на фотографию - {Photo}')
asyncio.run(main())
