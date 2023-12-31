from requests_html import HTMLSession
import sys
import requests
import re
import random
import subprocess

try: 
    l = sys.argv[1]
    ref = "108462"
    entra = f'https://camelbtc.com/index.php?bitcoinwallet={l}&ref={ref}'
    response = requests.get(entra)
    cookie = response.cookies.get_dict()

    if re.search("I'm Not Bot", response.text):
        try:
            session = HTMLSession()
            r = session.get(entra)
            r.html.render(sleep=7, keep_page=True, scrolldown=1, timeout=100)
            page_content = r.html.html
            # recaptcha = r.html.find('textarea[name="g-recaptcha-response"]', first=True).text
            recaptcha = page_content.split('g-recaptcha-response" value="')[1].split('">')[0]
            data = {"g-recaptcha-response" : recaptcha, "action" : "validate_captcha"}
            requests.post('https://camelbtc.com/index.php', data=data, cookies=cookie)
        except:
            subprocess.run("pip install --upgrade pip", shell=True).stdout
            subprocess.run("pip install --upgrade requests-html pyppeteer websockets", shell=True).stdout
            subprocess.run("pip install --upgrade pip", shell=True).stdout
            subprocess.run("playwright install-deps", shell=True).stdout
            pass

    animais = 'https://camelbtc.com/barn.php'
    response = requests.get(animais, cookies=cookie)
    food = re.findall(r'action=feed&aid=(\d+)"', response.text)
    feed = f'https://camelbtc.com/grass.php?action=feed{random.choice([2,2,"",""])}&aid={food[0]}'
    requests.get(feed, cookies=cookie)

    requests.get("https://camelbtc.com/animmarket.php?purchase=8&confirm=1", cookies=cookie)
    # animmarket = f'https://camelbtc.com/animmarket.php?purchase={random.randint(1, 11)}&confirm=1'
    # requests.get(animmarket, cookies=cookie)
    
    requests.get("https://camelbtc.com/market.php?action=collect", cookies=cookie)
    requests.get("https://camelbtc.com/market.php?action=deliver", cookies=cookie)

    # trade = f'https://camelbtc.com/dailyoffers.php?action=trade{random.randint(1, 3)}&confirm=1'
    # requests.get(trade, cookies=cookie)
    attack = f'https://camelbtc.com/attack.php?type={random.choice(["gold","wood","rock","steel"])}'
    requests.get(attack, cookies=cookie)
    sell = f'https://camelbtc.com/bulkmarket.php?action=sell{random.randint(1, 3)}'
    requests.get(sell, cookies=cookie)
    # requests.get("https://camelbtc.com/mysterybox.php?action=buy", cookies=cookie)
    #https://camelbtc.com/grass.php?action=claimdall
    
    print('Ok')
        
except KeyboardInterrupt:
    print('exit')
except:
    print('Erro')
    pass
