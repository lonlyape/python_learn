class DataHandle(object):
    def outData(self, data):
        if data is None:
            return '无数据'

        if 'title' in data:
            return data['title']
        else:
            return '无标题'