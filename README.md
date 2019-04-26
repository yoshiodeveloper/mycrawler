# mycrawler

Trabalho sobre crawling para demonstrar o conceito de coleta de links e páginas da web.

O script solicita uma URL inicial e a partir dela são coletados os links existentes no HTML. O crawler continua coletando os "links dos links" indefinidamente.

## Instalação no Linux

* `É necessário ter o Python 3 e virtualenv instalados.`

Crie um virtualenv.

```shell
$ virtualenv -p python3 venv
```

Ative o ambiente.

```shell
$ source venv/bin/activate
```

Instale as libs do Python no ambiente utilizando o arquivo "requirements.txt".

```shell
$ pip install -r requirements.txt
```

Rode o crawler.


```shell
$ python run.py
```

Qualquer dúvida entre em contato: yoshiodeveloper@gmail.com