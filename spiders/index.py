from manager import index as url_manager
from download import index as html_downloader
from parse import index as html_parser
from output import index as data_outputer

from multiprocessing import Process, Value, Pipe

import threading


class myThread (threading.Thread):
    def __init__(self, fun, url):
        threading.Thread.__init__(self)
        self.fun = fun
        self.url = url

    def run(self):
        self.fun(self.url)


class SpiderMain(object):
    def __init__(self):
        self.count = Value('i', 1)
        self.process_set = set()
        self.threading_count = 0
        self.threadLock = threading.Lock()
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = data_outputer.DataHandle()

    def _add_count(self):
        self.count.value += 1

    def _get_html(self, url, pipe=None):
        html_cont = self.downloader.download(url)
        new_urls, new_data = self.parser.parse(url, html_cont)

        self.threadLock.acquire()
        self.threading_count -= 1
        if pipe is None:
            self.urls.add_new_urls(new_urls)
        else:
            pipe.send(new_urls)

        title = self.outputer.outData(new_data)
        print(self.count.value, title, url)
        self._add_count()
        self.threadLock.release()

    def _create_process(self, url):
        if url is None:
            return None

        new_urls_parent, new_urls_child = Pipe()
        p = Process(target=self._get_html, args=(url, new_urls_parent,))
        p.start()
        self.process_set.add(p.pid)
        p.join()
        while True:
            if not p.is_alive():
                self.process_set.remove(p.pid)
                self.urls.add_new_urls(new_urls_child.recv())
                new_urls_child.close()
                new_urls_parent.close()
                p.close()
                break

    def _create_threading(self, url):
        if url is None:
            return None

        thread = myThread(self._get_html, url)
        thread.start()
        self.threading_count += 1

    def craw_threading(self, url):
        if url is None:
            return None

        threading_num = 10
        self.urls.add_new_url(root_url)

        while self.count.value < threading_num or self.urls.has_new_url():
            if not self.urls.has_new_url():
                continue

            while self.threading_count < threading_num:
                if self.urls.has_new_url():
                    self._create_threading(self.urls.get_new_url())
                else:
                    break

            if self.count.value > 100:
                break

    def craw_process(self, root_url):
        process_num = 10
        self.urls.add_new_url(root_url)

        while self.count.value < process_num or self.urls.has_new_url():
            if not self.urls.has_new_url():
                continue

            while len(self.process_set) < process_num:
                if self.urls.has_new_url():
                    self._create_process(self.urls.get_new_url())
                else:
                    break

            if self.count.value > 100:
                break

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            self._get_html(new_url)
            if self.count.value > 100:
                break


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()
    obj_spider.craw_threading(root_url)
