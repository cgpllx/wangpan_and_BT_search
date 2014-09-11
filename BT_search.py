# -*- coding: utf-8 -*-

# BT种子磁力链接搜索脚本
# 使用到的第三方库：requests，BeautifulSoup4
# 本程序使用磁力搜（http://www.cilisou.cn/）的搜索结果
# 经由程序搜索所产生的任何结果皆不代表本人立场
# 本人不对其真实合法性以及版权负责，亦不承担任何法律责任
# 使用方法：终端中输入 “python BT_search.py”运行
# Author：egrcc
# Email：zhaolujun1994@gmail.com
# Version：0.1

import re
import requests
from bs4 import BeautifulSoup

cilisou_url = "http://www.cilisou.cn/s.php"
count = 1

def search(keywords, start_page = 1, end_page = 1):
    global count
    current_page = start_page
    while current_page <= end_page:
        search_url = cilisou_url + "?q=" + '+'.join(keywords) \
        + "&p=" + str((current_page - 1))
        r = requests.get(search_url)
        soup = BeautifulSoup(r.content)

        magnet_and_content_list = []
        magnet_tag_list = soup.find_all('a', title = "magnet链接下载")
        content_tag_list = soup.find_all('td', class_ = "torrent_name")
        if len(magnet_tag_list) == 0:
            if count == 1:
                print "*********************************************"
                print "对不起，这个真没有！"
                print "虽然已经很努力了，但还是没能找到您想要的结果。"
                print "*********************************************", '\n'
            else:
                print "*************"
                print "没有更多了."
                print "*************", '\n'

        i = 0
        while i < len(magnet_tag_list):
            temp = ["", ""]
            temp[0] = re.findall(r'fclck\("(.*)"\)', magnet_tag_list[i]['onclick'])[0]
            temp[1] = str(count) + ". " + content_tag_list[i].get_text().strip()
            magnet_and_content_list.append(temp)
            count = count + 1
            i = i + 1

        for item in magnet_and_content_list:
            print item[1], "\n", item[0]
            print "\n"

        current_page = current_page + 1


print '''#########################################################
# BT种子磁力链接搜索脚本
# 使用到的第三方库：requests，BeautifulSoup4
# 本程序使用磁力搜（http://www.cilisou.cn/）的搜索结果
# 经由程序搜索所产生的任何结果皆不代表本人立场
# 本人不对其真实合法性以及版权负责，亦不承担任何法律责任
# 使用方法：终端中输入 “python BT_search.py”运行
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
