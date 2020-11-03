from bs4 import BeautifulSoup as bs
import requests

URLS = ['https://danielfooddiary.com/2020/10/10/japanesecafessg/',
        'https://danielfooddiary.com/2020/10/11/maxicoffeebarsg/',
        'https://danielfooddiary.com/2020/10/12/82bunsik/',
        'https://danielfooddiary.com/2020/10/10/forthepeople/',
        'https://danielfooddiary.com/2014/09/01/chargrillbar/',
        'https://danielfooddiary.com/2019/03/27/spaceout/',
        'https://danielfooddiary.com/2020/10/04/nikuking/',
        'https://danielfooddiary.com/2020/10/09/september/',
        'https://danielfooddiary.com/2020/04/21/sinhoisai/',
        'https://danielfooddiary.com/2020/09/11/dimsumhouse/',

        'https://danielfooddiary.com/2020/03/12/kingoffriedrice/',
        'http://ieatishootipost.sg/yishun-park-hawker-centre-food-trail/',
        'http://ieatishootipost.sg/shrimp-pot-seafood-steelpot-woon-sen/',
        'http://ieatishootipost.sg/sohgood-bak-chang-good-grandma/',
        'http://ieatishootipost.sg/lukes-lobster-singapore-review/',
        'http://ieatishootipost.sg/58-prawn-mee-old-school-prawn-mee/',
        'http://ieatishootipost.sg/house-kueh-thin-chewy-slippery-soon-kueh/',
        'http://ieatishootipost.sg/bedok-bak-chor-mee-bak-chor-mee-soup-city/',
        'http://ieatishootipost.sg/big-fish-small-fish-fish-chips-menu-makeover/',
        'http://ieatishootipost.sg/ashes-burnnit-rise-hawker-burgers/'
        ]

for i in range(len(URLS)):
    page = requests.get(URLS[i])

    soup = bs(page.content, 'html.parser')

    results = soup.find_all('p')
    text = ""
    for result in results:
        text += result.text
    print(text)
    with open('./../food_reviews_scraping//document'+str(i)+'.txt', 'w') as f:
        f.write(text)
