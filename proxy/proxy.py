from bs4 import BeautifulSoup
import requests
import random


def get_ip_list(url, headers):
    """
    获取 ip 列表
    """
    session = requests.Session()
    res = session.get(url, headers=headers)
    bs = BeautifulSoup(res.text, 'lxml')
    ips = bs.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list


def get_random_ip(ip_list):
    ip = random.choice(ip_list)
    proxy = 'http://' + ip
    return proxy


def test_ip(ip, headers):
    proxies = {'http': 'http://' + ip}
    try:
        res = requests.get('http://www.ip.cn/',
                           headers=headers, proxies=proxies, timeout=5)
        bs = BeautifulSoup(res.text, 'lxml')
        test_ip = bs.find('code')
        print('success:', test_ip.text)
    except:
        print('error:', ip)


if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nt/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    ip_list = get_ip_list(url, headers)
    ip = get_random_ip(ip_list)

    for ip in ip_list:
        test_ip(ip, headers)
