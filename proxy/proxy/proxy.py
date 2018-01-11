from bs4 import BeautifulSoup
import requests
import json

ip_txt = open('ip.txt', 'a')


class ProxyPool:
    """
    代理池爬虫类
    """
    session = requests.Session()
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        'Accept': "text/html application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }

    def __init__(self, url):
        self.url = url

    def start(self):
        self._get_html()

    def _get_html(self):
        """
        获取页面内容
        """
        res = self.session.get(self.url, headers=self.headers)
        dom = BeautifulSoup(res.text, 'lxml')
        print(dom)


# def get_ip_list(url, headers):
#     """
#     获取 ip 列表
#     """
#     session = requests.Session()
#     res = session.get(url, headers=headers)
#     bs = BeautifulSoup(res.text, 'lxml')
#     ips = bs.find_all('tr')
#     ip_list = []
#     for i in range(1, len(ips)):
#         ip_info = ips[i]
#         tds = ip_info.find_all('td')
#         ip_list.append(tds[1].text + ':' + tds[2].text)
#     return ip_list


# def test_ip(ip, headers):
#     proxies = {'http': 'http://' + ip}
#     try:
#         res = requests.get(
#             'http://www.ip.cn/', headers=headers, proxies=proxies, timeout=5)
#         bs = BeautifulSoup(res.text, 'lxml')
#         test_ip = bs.find('code')
#         ip_txt.write(test_ip + '\n')
#         print('success:', test_ip.text)
#     except:
#         print('error:', ip)


# def test_ip(ip, headers):
#     proxies = {'http': 'http://' + ip}
#     try:
#         res = requests.get(
#             'https://httpbin.org/ip',
#             headers=headers,
#             proxies=proxies,
#             timeout=5)
#         res = json.loads(res.text)
#         print('success:', res['origin'])
#     except:
#         print('error:', ip)


if __name__ == '__main__':
    proxy = ProxyPool('https://www.kuaidaili.com/free/inha/')
    proxy.start()
    # def main():
    #     url = 'http://www.xicidaili.com/nn/'
    #     headers = {
    #     }
    #     ip_list = get_ip_list(url, headers)

    #     for ip in ip_list:
    #         test_ip(ip, headers)

    # main()
