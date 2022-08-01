# 导入模块
from typing import Iterable, Any

import json5
import requests as req
import json
import numpy as np
import time
import csv
import pandas as pd
import os
import re
# import seaborn as sns
# import matplotlib.pyplot as plt
import threading
from queue import Queue
import math


# 时间格式函数
def format_time(format_: str, seconds: int):
    return time.strftime(format_, seconds)


# 文件保存 csv
def save2csv(name: str, content_=None, model=None, encoding=None, newline='', epoch=None, *args,
             **kwargs):
    # if os.path.exists(name) and epoch == 0:
    #     os.remove(name)
    with open(name, mode=model, encoding=encoding, newline=newline) as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(content_)


# # 文件保存 json
def save2json(name: str, content_: Iterable[Iterable[Any]], model=None, encoding=None, newline=None, epoch=None, *args,
              **kwargs):
    with open(name, mode=model, encoding=encoding, newline=newline) as f:
        json.dump(content_, fp=f, ensure_ascii=False)


# 爬虫
def download(method='GET', url='', headers_=None):
    # content_ = json.loads(req.request(method, url=url, headers=headers_).text)
    content_ = req.request(method, url=url, headers=headers_).json()
    return content_


# 多线程 创建 但未启动
def multiply_thread_init(num, target=None, name=None, args=None, daemon=None):
    print('我是args：', args)
    thread_list_ = []
    for i in range(num):
        thread_list_.append(threading.Thread(target=target, name=name, args=args[i], daemon=daemon))
    return thread_list_


# 多线程 启动
def multiply_thread_start(num=1, **kwargs):
    print('准备初始化多线程。。。。。。。。。。。。。。。。。')
    thread_list_ = multiply_thread_init(num=num, **kwargs)  # 注意：安全起见，只可在此处调用初始化线程方法
    for i in range(num):
        print('线程' + threading.currentThread().getName() + '正在启动。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。')
        thread_list_[i].start()
    # # 多线程阻塞：所以子线程结束后 才可 执行主线程（main线程）
    # for i in range(num):
    #     thread_list[i].join()
    return thread_list_


# 测试 线程执行函数
def test():
    print('我被线程：', threading.currentThread().getName(), '调用啦!!!')


# --------------------------上述 通用代码--------------------------

# 业务链接
# url_home = 'https://api5-normal-lf.toutiaoapi.com/api/news/feed/v88/?crypto_info=dGMFEAAAmajkwtUWJYnPIz3kqlqxH%2BNxBg9HNQTmJ4mjWlmE5%2FJ6HH5mMQw3mcNsHrZTui3JlAYQ%0AGc4h1YYzrzxbJ1Yuy2hFCbaf%2FcJcrtEj9knBxkOxZPOo8nsecgMQjiWKpWrLpmKeSFIPdjRFyYyi%0A%2FbP0RWlBVZQZUs1VHsj8O9x12RA%3D%0A&list_count=0&category=news_hotspot&st_time=4679&refer=1&refresh_reason=5&session_refresh_idx=1&count=20&last_refresh_sub_entrance_interval=1657934057&last_ad_show_interval=0&cached_item_num=0&last_response_extra=%7B%22data%22%3A%22eyJoYXNfZm9sbG93aW5nIjpmYWxzZSwib2Zmc2V0IjoxNDIzfQ%22%7D&ad_ui_style=%7B%22is_crowd_generalization_style%22%3A2%2C%22van_package%22%3A11000012%7D&lynx_template_data=%5B%5D&lynx_version=2.4.1-rc.2.5-bugfix&tt_from=enter_auto&client_extra_params=%7B%22last_ad_position%22%3A-1%2C%22har_state%22%3A-1%2C%22hand_state%22%3A0%2C%22playparam%22%3A%22codec_type%3A7%2Ccdn_type%3A1%2Cresolution%3A1080*2400%2Cttm_version%3A884000%2Cenable_dash%3A0%2Cunwatermark%3A1%2Cv1_fitter_info%3A1%2Ctt_net_energy%3A4%2Cis_order_flow%3A-1%2Ctt_device_score%3A8.8%2Ctt_enable_adaptive%3A2%22%2C%22recommend_enable%22%3A1%2C%22immerse_pool_type%22%3A-2%2C%22immerse_candidate_version%22%3A0%2C%22forbid_loc_rec%22%3A2%2C%22forbid_search_history_rec%22%3A0%2C%22forbid_follow_user_rec%22%3A0%2C%22content_diversity_freq%22%3A0%2C%22access_token%22%3A%22act.2.WpbLLAME8UmskGFYJLyIkStzXckLW962MCrP8kzlkpxUT-BooqhfIcp4bK-TRDIYlwj1BqeTD9nMYl6ddaeuztrizyO-DzCinECcvpbqwzLVpqKU1-PPTbRCu9lFaLIRGrIHHNoNAg4hQtGmg2rU5RzcQmOLFBpj7MHJVQ%3D%3D%22%2C%22sec_uid%22%3A%22MS4wLjABAAAAVIyiZZINdDEqnXnecjkeOsEywKWuzEOv9bnvMKNNeZRFNMf0PV5y7i0Ur5NG6UBs%22%2C%22ad_download%22%3A%7B%22su%22%3A155300%2C%22pure_mode%22%3A4%7D%2C%22catower_net_quality%22%3A2%2C%22catower_device_overall_performance%22%3A0%7D&device_platform=android&os=android&ssmix=a&_rticket=1657934057091&cdid=97339bbe-d81e-4d84-a22e-112455297eb5&channel=xiaomi_13_64&aid=13&app_name=news_article&version_code=885&version_name=8.8.5&manifest_version_code=8850&update_version_code=88509&ab_version=668776%2C4303276%2C660830%2C4303284%2C4415414%2C1859936%2C662176%2C4303268%2C668775%2C4137893%2C4303286%2C4374541%2C4381430%2C4407629%2C668779%2C4303281%2C668774%2C4303275%2C4384854%2C662099%2C4303234%2C3540006%2C3596064%2C4235059%2C4246388&ab_feature=94563%2C102749&resolution=1080*2276&dpi=440&device_type=M2012K11AC&device_brand=Redmi&language=zh&os_api=30&os_version=11&ac=wifi&dq_param=0&plugin=0&client_vid=3194524%2C3406951%2C3383553%2C2827920&isTTWebView=0&session_id=bdcea2ce-f9b2-43f5-9ee2-2070725a0a77&host_abi=arm64-v8a&tma_jssdk_version=2.53.0&rom_version=miui_v125_v12.5.19.0.rkhcnxm&iid=1306681848399534&device_id=2313815758479399&cmwz=%2526-%2522%2523ws2K45%25407%2524x%257Bx%257B%2B%25210%252434C%255CEFQH7*3%252FMfOpoCoDBuGDJJKIOKN%253CG%253E-%252F%2525%252F7%2527-%2529G%2560Ia%255D%252F-_4%253CA%2540EFtqwJK63&cp=6f22d52d130e9q1'
url_home = 'https://api5-normal-lf.toutiaoapi.com/api/news/feed/v88/?crypto_info=dGMFEAAAmajkwtUWJYnPIz3kqlqxH%2BNxBg9HNQTmJ4mjWlmE5%2FJ6HH5mMQw3mcNsHrZTui3JlAYQ%0AGc4h1YYzrzxbJ1Yuy2hFCbaf%2FcJcrtEj9knBxkOxZPOo8nsecgMQjiWKpWrLpmKeSFIPdjRFyYyi%0A%2FbP0RWlBVZQZUs1VHsj8O9x12RA%3D%0A&list_count=0&category=news_hotspot&st_time=4679&refer=1&refresh_reason=5&session_refresh_idx=1&count=20&last_refresh_sub_entrance_interval=1657934057&last_ad_show_interval=0&cached_item_num=0&last_response_extra=%7B%22data%22%3A%22eyJoYXNfZm9sbG93aW5nIjpmYWxzZSwib2Zmc2V0IjoxNDIzfQ%22%7D&ad_ui_style=%7B%22is_crowd_generalization_style%22%3A2%2C%22van_package%22%3A11000012%7D&lynx_template_data=%5B%5D&lynx_version=2.4.1-rc.2.5-bugfix&tt_from=enter_auto&client_extra_params=%7B%22last_ad_position%22%3A-1%2C%22har_state%22%3A-1%2C%22hand_state%22%3A0%2C%22playparam%22%3A%22codec_type%3A7%2Ccdn_type%3A1%2Cresolution%3A1080*2400%2Cttm_version%3A884000%2Cenable_dash%3A0%2Cunwatermark%3A1%2Cv1_fitter_info%3A1%2Ctt_net_energy%3A4%2Cis_order_flow%3A-1%2Ctt_device_score%3A8.8%2Ctt_enable_adaptive%3A2%22%2C%22recommend_enable%22%3A1%2C%22immerse_pool_type%22%3A-2%2C%22immerse_candidate_version%22%3A0%2C%22forbid_loc_rec%22%3A2%2C%22forbid_search_history_rec%22%3A0%2C%22forbid_follow_user_rec%22%3A0%2C%22content_diversity_freq%22%3A0%2C%22access_token%22%3A%22act.2.WpbLLAME8UmskGFYJLyIkStzXckLW962MCrP8kzlkpxUT-BooqhfIcp4bK-TRDIYlwj1BqeTD9nMYl6ddaeuztrizyO-DzCinECcvpbqwzLVpqKU1-PPTbRCu9lFaLIRGrIHHNoNAg4hQtGmg2rU5RzcQmOLFBpj7MHJVQ%3D%3D%22%2C%22sec_uid%22%3A%22MS4wLjABAAAAVIyiZZINdDEqnXnecjkeOsEywKWuzEOv9bnvMKNNeZRFNMf0PV5y7i0Ur5NG6UBs%22%2C%22ad_download%22%3A%7B%22su%22%3A155300%2C%22pure_mode%22%3A4%7D%2C%22catower_net_quality%22%3A2%2C%22catower_device_overall_performance%22%3A0%7D&device_platform=android&os=android&ssmix=a&_rticket=1657934057091&cdid=97339bbe-d81e-4d84-a22e-112455297eb5&channel=xiaomi_13_64&app_name=news_article&version_code=885&version_name=8.8.5&manifest_version_code=8850&update_version_code=88509&ab_version=668776%2C4303276%2C660830%2C4303284%2C4415414%2C1859936%2C662176%2C4303268%2C668775%2C4137893%2C4303286%2C4374541%2C4381430%2C4407629%2C668779%2C4303281%2C668774%2C4303275%2C4384854%2C662099%2C4303234%2C3540006%2C3596064%2C4235059%2C4246388&ab_feature=94563%2C102749&resolution=1080*2276&dpi=440&device_type=M2012K11AC&device_brand=Redmi&language=zh&os_api=30&os_version=11&ac=wifi&dq_param=0&plugin=0&client_vid=3194524%2C3406951%2C3383553%2C2827920&isTTWebView=0&session_id=bdcea2ce-f9b2-43f5-9ee2-2070725a0a77&host_abi=arm64-v8a&tma_jssdk_version=2.53.0&rom_version=miui_v125_v12.5.19.0.rkhcnxm&iid=1306681848399534&device_id=2313815758479399&cmwz=%2526-%2522%2523ws2K45%25407%2524x%257Bx%257B%2B%25210%252434C%255CEFQH7*3%252FMfOpoCoDBuGDJJKIOKN%253CG%253E-%252F%2525%252F7%2527-%2529G%2560Ia%255D%252F-_4%253CA%2540EFtqwJK63&cp=6f22d52d130e9q1'
url_home = 'https://api5-normal-lf.toutiaoapi.com/api/news/feed/v88/?category=news_hotspot&device_platform=android&app_name=news_article&version_code=885&version_name=8.8.5&update_version_code=88509'
url_header_comments = 'https://api5-normal-lf.toutiaoapi.com/article/v4/tab_comments/?fold=1&offset=0'
url_footer_comments = '&group_id=%d&count=40&comment_request_from=1&category=topic_hot&device_platform=android&os=android&ssmix=a&_rticket=1657944782433&cdid=97339bbe-d81e-4d84-a22e-112455297eb5&channel=xiaomi_13_64&aid=13&app_name=news_article&version_code=885&version_name=8.8.5&manifest_version_code=8850&update_version_code=88509&ab_version=1859936%2C668779%2C4303281%2C668774%2C4303275%2C4384854%2C662099%2C4303234%2C660830%2C4303284%2C4415414%2C662176%2C4303268%2C668776%2C4303276%2C668775%2C4137893%2C4303286%2C4374541%2C4381430%2C4407629%2C3540006%2C3596064%2C4235059%2C4246388&ab_feature=94563%2C102749&resolution=1080*2276&dpi=440&device_type=M2012K11AC&device_brand=Redmi&language=zh&os_api=30&os_version=11&ac=wifi&dq_param=0&plugin=0&client_vid=3194524%2C3406951%2C3383553%2C2827920&isTTWebView=0&session_id=36f4eaed-5899-4797-8249-30ad4e477d25&host_abi=arm64-v8a&tma_jssdk_version=2.53.0&rom_version=miui_v125_v12.5.19.0.rkhcnxm&iid=1306681848399534&device_id=2313815758479399&openudid=94da3f26488eaf88&oaid=fd7b63e627663835'
# https://api5-normal-lf.toutiaoapi.com/article/v4/tab_comments/?fold=1&offset=0&group_id=%d&comment_request_from=1&category=topic_hot&device_platform=android&os=android&ssmix=a&_rticket=1657944782433&cdid=97339bbe-d81e-4d84-a22e-112455297eb5&channel=xiaomi_13_64&aid=13&app_name=news_article&version_code=885&version_name=8.8.5&manifest_version_code=8850&update_version_code=88509&ab_version=1859936%2C668779%2C4303281%2C668774%2C4303275%2C4384854%2C662099%2C4303234%2C660830%2C4303284%2C4415414%2C662176%2C4303268%2C668776%2C4303276%2C668775%2C4137893%2C4303286%2C4374541%2C4381430%2C4407629%2C3540006%2C3596064%2C4235059%2C4246388&ab_feature=94563%2C102749&resolution=1080*2276&dpi=440&device_type=M2012K11AC&device_brand=Redmi&language=zh&os_api=30&os_version=11&ac=wifi&dq_param=0&plugin=0&client_vid=3194524%2C3406951%2C3383553%2C2827920&isTTWebView=0&session_id=36f4eaed-5899-4797-8249-30ad4e477d25&host_abi=arm64-v8a&tma_jssdk_version=2.53.0&rom_version=miui_v125_v12.5.19.0.rkhcnxm&iid=1306681848399534&device_id=2313815758479399&openudid=94da3f26488eaf88&oaid=fd7b63e627663835
# https://api5-normal-lf.toutiaoapi.com/article/v4/tab_comments/?fold=1&offset=0&group_id=7123110836692303902&count=50&comment_request_from=1&category=topic_hot&device_platform=android&os=android&ssmix=a&_rticket=1657944782433&cdid=97339bbe-d81e-4d84-a22e-112455297eb5&channel=xiaomi_13_64&aid=13&app_name=news_article&version_code=885&version_name=8.8.5&manifest_version_code=8850&update_version_code=88509&ab_version=1859936%2C668779%2C4303281%2C668774%2C4303275%2C4384854%2C662099%2C4303234%2C660830%2C4303284%2C4415414%2C662176%2C4303268%2C668776%2C4303276%2C668775%2C4137893%2C4303286%2C4374541%2C4381430%2C4407629%2C3540006%2C3596064%2C4235059%2C4246388&ab_feature=94563%2C102749&resolution=1080
url_comments = 'https://api5-normal-lf.toutiaoapi.com/article/v4/tab_comments/?fold=1&offset=0&group_id=%d&comment_request_from=1&category=topic_hot&device_platform=android&os=android&ssmix=a&_rticket=1657944782433&cdid=97339bbe-d81e-4d84-a22e-112455297eb5&channel=xiaomi_13_64&aid=13&app_name=news_article&version_code=885&version_name=8.8.5&manifest_version_code=8850&update_version_code=88509&ab_version=1859936%2C668779%2C4303281%2C668774%2C4303275%2C4384854%2C662099%2C4303234%2C660830%2C4303284%2C4415414%2C662176%2C4303268%2C668776%2C4303276%2C668775%2C4137893%2C4303286%2C4374541%2C4381430%2C4407629%2C3540006%2C3596064%2C4235059%2C4246388&ab_feature=94563%2C102749&resolution=1080*2276&dpi=440&device_type=M2012K11AC&device_brand=Redmi&language=zh&os_api=30&os_version=11&ac=wifi&dq_param=0&plugin=0&client_vid=3194524%2C3406951%2C3383553%2C2827920&isTTWebView=0&session_id=36f4eaed-5899-4797-8249-30ad4e477d25&host_abi=arm64-v8a&tma_jssdk_version=2.53.0&rom_version=miui_v125_v12.5.19.0.rkhcnxm&iid=1306681848399534&device_id=2313815758479399&openudid=94da3f26488eaf88&oaid=fd7b63e627663835'
headers = {
    # "cookie": 'd_ticket=d7e74b97e7b97a158c5b18264606a1165f91c; n_mh=C4hSGxZ_bsCaLySaXcdZuCPDId5LzYD-bIeVvfG0gfo; PIXIEL_RATIO=2.75; ssr_tz=Asia/Shanghai; ssr_fs=m; ssr_sbh__=29; FRM=new; s_v_web_id=verify_l2oiw371_wkkHnaEa_dP04_47Nd_9fOr_cYyZGOEDd0A3; MONITOR_WEB_ID=85805291-72db-4dd0-a6e7-311d29f52d7d; odin_tt=fe73066a1eef038e0e7003156a0bbaa8c2d9ffaf6865c26dcd409408b9bd052664db8c3c33eabb67d5569c5542e15f4cd1aa17ccc88670cbdb0462b553049ceb; uid_tt=5b8919768c9ec0d1c1871a8adaa3492b; uid_tt_ss=5b8919768c9ec0d1c1871a8adaa3492b; sid_tt=c571065cf8199d3035063b03973d3ae0; sessionid=c571065cf8199d3035063b03973d3ae0; sessionid_ss=c571065cf8199d3035063b03973d3ae0; WIN_WH=393_857; sid_guard=c571065cf8199d3035063b03973d3ae0%7C1656215143%7C5184000%7CThu%2C+25-Aug-2022+03%3A45%3A43+GMT; install_id=1306681848399534; ttreq=1$c013d61454980958d6b72e457a54440f7bd45832; passport_csrf_token=0f119ba3cd2183f824e37a340edcd852; passport_csrf_token_default=0f119ba3cd2183f824e37a340edcd852; gftoken=YzU3MTA2NWNmOHwxNjU3NDExODAwMjR8fDAGBgYGBgY; msToken=yQHIh_zMD8aBUiRY3df3c-bjd3Vu6D61YYgja_fsWV8jneCimyjRWUehT6IiAT7ihM8BlXZu-_NBXMYzbpHVjCJQwyIhtXgSrbfl6Kw9cGhs8XnuH2AeHFYu3ec6t0c=',
    "user-agent": 'com.ss.android.article.news/8850 (Linux; U; Android 11; zh_CN; M2012K11AC; Build/RKQ1.200826.002; Cronet/TTNetVersion:ff367453 2022-05-16 QuicVersion:b314d107 2021-11-24)'
}


# 提取 首页相关热点 字段
def extract_home_fields(data):
    # 报错，疑似网络波动
    # titles_fixed = data['raw_data']['board'][0]['fixed_items'][0]['title']# TypeError: 'NoneType' object is not subscriptable
    hot_ranking = [(
        item['id'], item['title'], item['title_label_desc'], item['title_label_type']
    )
        for item in data['raw_data']['board'][0]['hot_board_items']
    ]
    #     return titles_fixed, hot_ranking
    return '待补充置顶新闻模块', hot_ranking


# 通过 前50个热点 各字段 构建 各评论链接
def generate_comment_urls(url_root=None, home_top50_contents_=None):
    url_splits = url_root.split('%d')
    home_top50_urls_ = []
    for fields in home_top50_contents_:
        home_top50_urls_.append(url_splits[0] + str(fields[0]) + url_splits[1])
    return home_top50_urls_


# 抓取 评论
def get_comments(*home_choice10_urls):
    for _, (url, title) in enumerate(home_choice10_urls):
        epoch = 0
        url_splits = url.split('offset=0')

        comment_fields = []
        while True:
            offset = 'offset=%d' % epoch
            comments = download('GET', url_splits[0] + offset + url_splits[1], headers)
            comments_data = comments['data']
            if len(comments_data) > 0:
                comment_fields += [(
                    item['comment']['id'], item['comment']['text'],
                    item['comment']['reply_count'], item['comment']['digg_count'],
                    item['comment']['bury_count'],
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item['comment']['create_time'])),
                    item['comment']['publish_loc_info'], item['comment']['user_id'], item['comment']['user_name']
                )
                    for item in comments_data
                ]
                # 注意：添加字段时要修改形状大小
                # save_comments(, np.array(comment_fields).reshape((-1, 9)), epoch)
                # save2csv(os.path.join('hot_news', title + '.csv'), comment_fields, model='a+', encoding='utf-8')
                epoch += 40
            else:
                print('====》跳出：' + url_splits[0] + offset + url_splits[1])
                break
        save2csv(os.path.join(file_path, ''.join(re.compile(r'[^/:*?"<>|\\]', ).findall(title)) + '.csv'),
                 comment_fields, model='w+', encoding='utf-8')


while True:
    datetime_current = time.strftime('%Y-%m-%d', time.localtime())
    file_path = os.path.join('./hot_news', datetime_current)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    try:
        home_content = download('GET', url_home, headers)
        data = home_content['data']
    except Exception as err:
        print('有异常：\n', err)
    thread_list = None
    print('进入。。。。。。。。。。。。。。。。。。。。循环体', len(data))
    for i, data_ in enumerate(data):
        print('遍历主页。。。。。。。。。。。。。。。。。。。。。。')
        data_content = data_['content']  # data_content在json中为str类型
        data_content = json.loads(data_content)
        data_content = extract_home_fields(data_content)  # 提取字段
        home_top50_contents = data_content[1]  # 除去首页置顶新闻，留前50个热点新闻

        home_top50_urls = generate_comment_urls(url_comments, home_top50_contents)  # 50个评论链接
        home_top50_titles = [items[1] for items in home_top50_contents]

        # thread_list = multiply_thread_start(5, target=get_comments,
        #                                     args=[list(zip(home_top50_urls[i:i + 10], home_top50_titles[i:i + 10])) for i in
        #                                           range(0, 50, 10)])
        # thread_list = multiply_thread_start(10, target=get_comments,
        #                                     args=[list(zip(home_top50_urls[i:i + 5], home_top50_titles[i:i + 5])) for i in
        #                                           range(0, 50, 5)])
        thread_list = multiply_thread_start(25, target=get_comments,
                                            args=[list(zip(home_top50_urls[i:i + 2], home_top50_titles[i:i + 2])) for i
                                                  in
                                                  range(0, 50, 2)])
        break

        # thread_list = multiply_thread_start(10, target=test)
    if len(data) > 0:
        print('子线程将被阻塞。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。')
        # 阻塞主线程：即所有子线程执行完毕 才可执行主线程此处的后续代码块
        for thread in thread_list:
            thread.join()
        print('正在睡眠中。。。')
        time.sleep(540)
    else:
        time.sleep(1)
        print('data长度：', home_content)
