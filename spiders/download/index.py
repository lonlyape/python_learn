import urllib.request
import http.cookiejar

urllib=urllib.request
cookiejar=http.cookiejar

class HtmlDownloader(object):
	def download(self,url):
		if url is None:
			return None
		try:
			response = urllib.urlopen(url)
			if response.getcode() !=200:
				return None
			return response.read()
		except:
			print('加载失败')
			return None