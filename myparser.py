# -*- encoding: utf-8 -*-

"""

Módulo com funções úteis para tratar HTML.

"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin


def extract_links(html, base_url):
    """ Retorna uma lista com todas os links encontrados nas tags "<a>" do HTML informado.
    O parâmetro `html` é a string contendo o html de onde os links devem ser extraído.
    O parâmetro `base_url` é a URL base para ser utilizado nos links que forem relativos.
    """
    soup = BeautifulSoup(html, 'lxml')
    a_tags = soup.find_all('a', href=True)  # Encontra todas as tags "a" dentro do HTML.
    links = []
    for a in a_tags:
        href = a.get('href', '')  # Extrai o valor do atributo "href" da tag. O href contém o link.
        href = href.strip()
        if not href:
            continue
        # É possível que o link seja relativo. Ex: "/parte1/meulink.html".
        # Neste caso o base_url será utilizado para montar a versão absoluta do link.
        # Por exemplo se o base_url for "http://meusite.com/aaa/bb/cc.html" será utilizado a primeira parte "http://meusite.com".
        # O link final será http://meusite.com/parte1/meulink.html".
        link = urljoin(base_url, href)
        links.append(link)
    return links
