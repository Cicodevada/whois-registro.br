from flask import Flask, request, jsonify
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 
options.add_argument('--no-sandbox')  

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Cookie 0
cookies_dict = None

def pegar_cookies(domain):
    url = f"https://registro.br/tecnologia/ferramentas/whois?search={domain}"
    driver.get(url)
    cookies = driver.get_cookies()
    cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}

    return cookies_dict

def whois(domain, cookies_dict):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.3',
        'x-xsrf-token': cookies_dict.get('XSRF-TOKEN', '')  # Adicione aqui o valor do 'x-xsrf-token', se disponível
    }
    
    cicourl = f"https://registro.br/v2/ajax/whois/?qr={domain}&recaptchaResponse="
    response = requests.get(cicourl, cookies=cookies_dict, headers=headers)

    return response.json()

@app.route('/whois', methods=['GET'])
def consultar_whois():
    global cookies_dict

    domain = request.args.get('url')
    if not domain:
        return jsonify({"error": "O parâmetro 'url' é necessário"}), 400

    if cookies_dict is None:
        print("Obtendo novos cookies...")
        cookies_dict = pegar_cookies(domain)

    while True:
        response_json = whois(domain, cookies_dict)
        if 'messages' in response_json and any(
            msg.get('code') == 'message:invalid-header' for msg in response_json.get('messages', [])
        ):
            print("Cookie expirado. Obtendo novos cookies...")
            cookies_dict = pegar_cookies(domain)
        else:
            break

    return jsonify(response_json)

if __name__ == '__main__':
    app.run(debug=True)
