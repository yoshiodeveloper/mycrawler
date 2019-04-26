# -*- encoding: utf-8 -*-

from datetime import datetime
from time import sleep
from yrequests import YRequests

from myparser import extract_links


class MyCrawler(object):

    def __init__(self, initial_links, slow=False):
        """
        :param initial_links: Lista com os links iniciais. É por onde o crawler começará as coletas.
        :param slow: Indica que deve realizar uma coleta lenta para poder visualizar os dados na tela.
        """
        self.initial_links = initial_links
        self.collected_links = set() # "DB" em memória com os links que já foram coletados.
        self.links_to_collect = self.initial_links[:]  # "DB" em memória com os links que devem ser coletados.
        self.slow = slow
    
    def start(self):
        """ Inicia o crawler. """

        while self.links_to_collect:  # "Enquanto houve links em links_to_collect...".
            link = self.links_to_collect.pop(0)  # Retorna o primeiro link e remove ele da lista links_to_collect.
            self.collected_links.add(link)  # Adiciona o link em collected_links para sabermo
            html = self.get_link_content(link)
            if html is None:
                continue
            
            # <- Aqui pode-se armazenar o HTML em algum lugar. Ex. em memória ou em um DB. ->
            
            new_links = extract_links(html, link)
            new_links_count = 0
            for new_link in new_links:
                if new_link in self.collected_links:
                    # Se o link já foi colectado ele não deve ser coletado novamente.
                    continue
                new_links_count += 1
                self.links_to_collect.append(new_link)
            
            total = len(self.collected_links) + len(self.links_to_collect)
            # Acada link coletado é exibido um pequeno relatório.
            report_msg = 'Relatório:\n    Novos links: %d\n    Links já coletados: %d\n    Links para coletar: %d\n    Total de links: %d' % (
                new_links_count, len(self.collected_links), len(self.links_to_collect), total
            )
            self.print(report_msg)
            if self.slow:
                sleep(3)  # Uma pausa para podermos acompanhar. Mas pode ser removido para tornar mais o script mais rápido.

    def get_link_content(self, link):
        """ Coleta o conteúdo do link e retorna. """
        self.print('Coletando %s...', link)
        req = YRequests()
        result = req.get(link)
        if not result['ok']:
            self.print('    ERRO: %s', result['error'])
            return None
        html = result['text']
        return html
    
    def print(self, msg, *args, **kwargs):
        """ Exibe mensagens no terminal com uma data prefixada. """
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            msg = msg % args
        except:
            pass
        msg = '[%s] %s' % (dt, msg)
        print(msg)
