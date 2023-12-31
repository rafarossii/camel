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
            
    type = re.findall(r'([a-zA-Z]+) Available : (\d+)', response.text)
    result_list = [{'type': 'wood' if tipo[0] == 'Log' else tipo[0], 'Available': int(tipo[1])} for tipo in type]

    for t in result_list:
        if int(t["Available"]) > random.randint(149, 999):
            gold = f'https://camelbtc.com/index.php?claim=1&type={t["type"].lower()}'
            response = requests.get(gold, cookies=cookie)
            hash = response.text.split('hash=')[1].split('&')[0]
            hash2 = f'https://camelbtc.com/reward.php?hash={hash}&user={l}&type={t["type"].lower()}'
            response = requests.get(hash2, cookies=cookie)
            claim = response.text.split('index.php?confirm1=')[1].split('"')[0]
            claim2 = f'https://camelbtc.com/index.php?confirm1={claim}'
            requests.get(claim2, cookies=cookie)

    for i in range(3):
        x = i + 1
        requests.get(f'https://camelbtc.com/grass.php?action=claim{x}', cookies=cookie)
        requests.get(f'https://camelbtc.com/grass.php?action=grass{x}', cookies=cookie)

    requests.get('https://camelbtc.com/farm.php?action=claim', cookies=cookie)
    requests.get('https://camelbtc.com/index.php?action=claimref', cookies=cookie)
    requests.get('https://camelbtc.com/dailygift.php?claim=1', cookies=cookie)
    requests.get('https://camelbtc.com/hunt.php', cookies=cookie)
    requests.get('https://camelbtc.com/hunt.php?action=hunt1', cookies=cookie)
    requests.get('https://camelbtc.com/index.php?action=hide', cookies=cookie)

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
    
    print('Ok')
        
except KeyboardInterrupt:
    print('exit')
except:
    print('Erro')
    pass
