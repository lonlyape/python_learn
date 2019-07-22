from bs4 import BeautifulSoup
import re


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"^/item/\s*"))
        for link in links:
            new_url = link['href']
            new_full_url = 'https://baike.baidu.com' + new_url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title')
        if title_node:
        	title_node=title_node.find('h1')
        	if title_node and title_node.get_text:
        		res_data['title'] = title_node.get_text()
        summary_node = soup.find('div', class_='lemma-summary')
        if summary_node:
        	summary_node=summary_node.find('div', class_='para')
	        if summary_node and summary_node.get_text:
	        	res_data['summary'] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):

        if page_url is None or html_cont is None:
            return None ,None

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data