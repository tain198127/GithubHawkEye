# coding: utf-8
# 分析maven依赖网络关系的主程序
import configparser
import os
import re
import time
from html.parser import HTMLParser

import fire
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter

from MavenAnalizeEngine import *

requests.adapters.DEFAULT_RETRIES = 5

p = re.compile('<[^>]+>')

session = requests.Session()
a = HTTPAdapter(max_retries=3)
b = HTTPAdapter(max_retries=3)
# 将重试规则挂载到http和https请求
session.mount('http://', a)
session.mount('https://', b)

logging.basicConfig()
logger = logging.getLogger('MavenDependenceNetworkAnalize')

cf = configparser.ConfigParser()
cf.read("./conf/application.conf")
base_url = cf.get('maven', 'repourl')
base_path = cf.get('maven', 'logpath')
pajek_path = cf.get('maven', 'pajekpath')


# 初始化日志
def initlog():
    global logger
    logger.setLevel(logging.INFO)  # Log等级总开关
    rq = time.strftime('%Y%m%d', time.localtime(time.time()))
    log_path = os.path.dirname(os.path.realpath(__file__)) + '/mdnalog/'
    log_name = log_path + __name__ + rq + '.log'
    logfile = log_name
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.ERROR)  # 输出到file的log等级的开关

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)  # 输出到console的log等级的开关
    # 第三步，定义handler的输出格式
    # formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    formatter = logging.Formatter("%(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 第四步，将logger添加到handler里面
    logger.addHandler(ch)
    logger.addHandler(fh)


htmlparser = HTMLParser()


# 封装了http请求
def req(requrl):
    global session
    # time.sleep(random.randint(3, 5))

    doc = session.get(url=requrl)
    return doc


# 将pom写入文件
def writetoFile(url, content):
    global base_url
    filepath = '' + url.split(base_url)[1:][0]
    readable_file_path = re.sub(r"[^0-9a-zA-Z]", r"_", filepath)
    try:
        readable_content = '' + content.decode('utf-8')
        with open('./mdnalog/' + readable_file_path, 'w+') as f:
            f.write(readable_content)
    except Exception as error:
        logger.error(error)


# 扫描maven reposi
def scan_repo(url):
    document = req(url)
    soup = BeautifulSoup(document.text,  # HTML文档字符串
                         'html.parser',  # HTML解析器
                         from_encoding='utf-8'  # HTML文档编码
                         )
    linkes = soup.find_all('a')

    if linkes is None or len(linkes) <= 0:
        return
    for link in linkes:
        href = link['href']
        currrent_url = None
        if 'http://' in href or 'https://' in href:
            currrent_url = href
        else:
            currrent_url = '{}{}'.format(url, href)
        if currrent_url == None:
            continue
        if href.endswith('.pom'):
            # 记录，并且return
            writetoFile(currrent_url, req(currrent_url).content)
            # print(req(currrent_url).content)
            return
        elif href.endswith('../'):
            continue
        elif href.endswith('/'):
            # 打开
            print(currrent_url)
            try:
                scan_repo(currrent_url)
            except Exception as e:
                logger.error(e)
                raise e


# 下载所有pom
def downpom(url):
    global base_url
    if url is not None:
        base_url = url
    else:
        base_url = 'http://192.168.100.215:8081/nexus/content/repositories/central/'
    try:
        scan_repo(base_url)
        logger.info('finish')
    except Exception as e:
        logger.error(e)
        logger.error('error finish')
    finally:
        session.close()


# 开始分析 path指的是pom文件的目录地址
def analize(path):
    global base_path
    engine = MavenAnalizeEngine()
    real_path = path
    if real_path is None or real_path == '':
        real_path = base_path
    for root, dirs, files in os.walk(real_path):
        for file in files:
            if file.endswith('pom'):
                try:
                    engine.transform(root + file, pajek_path)
                except Exception as ex:
                    logger.error(ex)


if __name__ == '__main__':
    initlog()
    # downpom(None)
    fire.Fire({
        'downpom': downpom,
        'analize': analize
    })
