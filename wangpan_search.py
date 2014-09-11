# -*- coding: utf-8 -*-

# 网盘搜索脚本，可搜索国内各大网盘资源
# 使用到的第三方库：requests，BeautifulSoup4
# 本程序使用网盘搜（http://www.wangpansou.cn/）的搜索结果
# 经由程序搜索所产生的任何结果皆不代表本人立场
# 本人不对其真实合法性以及版权负责，亦不承担任何法律责任
# 使用方法：终端中输入 “python wangpan_search.py”运行
# Author：egrcc
# Email：zhaolujun1994@gmail.com
# Version：0.1

import re
import WangPan
import requests
from bs4 import BeautifulSoup

wangpansou_url = "http://www.wangpansou.cn/s.php"
count = 1

def search(keywords, start_page = 1, end_page = 1, wangpan = WangPan.All):
    global count
    current_page = start_page
    while current_page <= end_page:
        search_url = wangpansou_url + "?q=" + '+'.join(keywords) \
        + "&wp=" + str(wangpan) + "&start=" + str((current_page - 1) * 10)
        r = requests.get(search_url)
        soup = BeautifulSoup(r.content)
        result_list = soup.find_all('a', class_ = "cse-search-result_content_item_top_a")

        if len(result_list) == 0:
            print "*********************************************"
            print "对不起，这个真没有！"
            print "虽然已经很努力了，但还是没能找到您想要的结果。"
            print "*********************************************", '\n'

        url_and_content_list = []
        for result in result_list:
            if not re.match('http', result['href']):
                hint = result.parent.get_text().replace('\n', '').replace('\t', '')
                print "*" * len(hint) * 2
                print hint
                print "*" * len(hint) * 2, '\n'
                continue
            temp = ["", ""]
            temp[0] = result['href']
            temp[1] = str(count) + ". " + result.get_text().strip()
            count = count + 1
            url_and_content_list.append(temp)
        for item in url_and_content_list:
            print item[1], "\n", item[0]
            print "\n"

        current_page = current_page + 1


print '''#########################################################
# 网盘搜索脚本，可搜索国内各大网盘资源
# 使用到的第三方库：requests，BeautifulSoup4
# 本程序使用网盘搜（http://www.wangpansou.cn/）的搜索结果
# 经由程序搜索所产生的任何结果皆不代表本人立场
# 本人不对其真实合法性以及版权负责，亦不承担任何法律责任
# 使用方法：终端中输入 “python wangpan_search.py”运行
# Author：egrcc
# Email：zhaolujun1994@gmail.com
# Version：0.1
#########################################################'''
kw = raw_input("请输入关键字（多个关键字请以空格隔开）:")
keywords = kw.split()
while True:
    try:
        page = int(raw_input("请输入搜索结果的显示页数（每页10条结果）:"))
    except Exception:
        print "输入有误，必须输入一个大于0的整数."
        continue
    else:
        if page <= 0:
            print "输入有误，必须输入一个大于0的整数."
            continue
    break

print ''
search(keywords, end_page = page)
