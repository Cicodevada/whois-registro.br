# whois-registro.br

Um simples script em Python para consultar os dados do WHOIS do Registro.br através de uma API Flask.

## 🚀 Descrição

Este projeto fornece uma API para consultar informações de domínios registrados no Registro.br. Ele utiliza web scraping e requisições HTTP para contornar as limitações de acesso direto aos dados do WHOIS.

## ⚙️ Funcionalidades

- Consulta de dados WHOIS para domínios .br
- API RESTful para fácil integração
- Gerenciamento automático de cookies para evitar bloqueios

## 📋 Requisitos

- Python 3.x
- Flask
- Requests
- Selenium
- WebDriver Manager

## 🔧 Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/hugosantoslisboa/whois-registro.br.git
   cd whois-registro.br
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Execute o script:
   ```
   py main.py
   ```

## ⌨️ Uso

Após iniciar o servidor, você pode fazer consultas WHOIS através da seguinte URL:

```
http://localhost:5000/whois?url=exemplo.com.br
```

Substitua `exemplo.com.br` pelo domínio que deseja consultar.

## 🛠️ Como funciona

1. O script utiliza Selenium para obter cookies válidos do site registro.br.
2. Com os cookies obtidos, faz uma requisição à API do Registro.br para obter os dados do WHOIS.
3. Se os cookies expirarem, o processo é repetido automaticamente.

## 🖇️ Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

MIT License

Copyright (c) 2024 Hugo Santos Lisboa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Aviso Legal

Este script é fornecido apenas para fins educacionais e de pesquisa. Certifique-se de cumprir os termos de serviço do Registro.br ao utilizar este software.

## 🎁 Expressões de gratidão
Me pague um café ❤️ Tá ai meu PIX :)<br>
pix@hugosantos.lol<br>
<center><img src="https://i.imgur.com/buWTEb3.png" alt="QR Pix" style="height: 200px; width:200px;"/></center>