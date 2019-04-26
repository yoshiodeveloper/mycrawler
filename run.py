# -*- encoding: utf-8 -*-

from mycrawler import MyCrawler


if __name__ == '__main__':
    initial_link = input('Informe o link inicial: ')
    initial_link = initial_link.strip()
    slow = input('Deseja coletar lentamente (s/n): ')
    slow = slow.strip() in ('s', 'S', 'y', 'Y', 'sim', 'yes')
    c = MyCrawler([initial_link], slow)
    c.start()