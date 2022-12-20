# -*- coding:utf-8 -*-
import random
import time
import requests
import json


def random_ua():
    ua_list = [
        "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.1; PAR-AL00 Build/HUAWEIPAR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/WIFI Language/zh_CN Process/tools",
        "Mozilla/5.0 (Linux; Android 8.1.0; ALP-AL00 Build/HUAWEIALP-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.1.0)",
        "Mozilla/5.0 (Linux; Android 8.1; EML-AL00 Build/HUAWEIEML-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.143 Crosswalk/24.53.595.0 XWEB/358 MMWEBSDK/23 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/4G Language/zh_CN",
        "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/NON_NETWORK Language/zh_CN Process/tools",
        "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 UWS/2.11.1.50 Mobile Safari/537.36 AliApp(DingTalk/4.5.8) com.alibaba.android.rimet/10380049 Channel/227200 language/zh-CN",
        "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-AL00 Build/HUAWEIEML-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.4.974 UWS/2.13.1.48 Mobile Safari/537.36 AliApp(DingTalk/4.5.11) com.alibaba.android.rimet/10487439 Channel/227200 language/zh-CN",
        "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-TL00 Build/HUAWEIEML-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.4.974 UWS/2.14.0.13 Mobile Safari/537.36 AliApp(TB/7.10.4) UCBS/2.11.1.1 TTID/227200@taobao_android_7.10.4 WindVane/8.3.0 1080X2244",
        "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; HUAWEI MT1-U06 Build/HuaweiMT1-U06) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/042_2.7.3_diordna_8021_027/IEWAUH_61_2.1.4_60U-1TM+IEWAUH/7300001a/91E050E40679F078E51FD06CD5BF0A43%7C544176010472968/1",
        "Mozilla/5.0 (Linux; Android 8.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/4G Language/zh_CN Process/tools",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/6.7.3(0x16070321) NetType/WIFI Language/zh_CN",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/6.7.3(0x16070321) NetType/WIFI Language/zh_HK",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.8.2 Mobile/15B87 Safari/604.1 MttCustomUA/2 QBWebViewType/1 WKType/1",
        "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.3.0 Mobile/15B87 Safari/604.1 MttCustomUA/2 QBWebViewType/1 WKType/1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.8.2 Mobile/14B72c Safari/602.1 MttCustomUA/2 QBWebViewType/1 WKType/1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_2 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A421 wxwork/2.5.8 MicroMessenger/6.3.22 Language/zh",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 wxwork/2.5.1 MicroMessenger/6.3.22 Language/zh",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.8.2 Mobile/14B100 Safari/602.1 MttCustomUA/2 QBWebViewType/1 WKType/1",
        "Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.18.21.0 (Baidu; P1 6.0.1)",
        "Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.10 (Baidu; P1 6.0.1)",
        "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; vivo Y85 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.6.976 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R9 Plustm A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.12 baiduboxapp/10.12.0.12 (Baidu; P1 5.1.1)",
        "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 7.1.1)",
        "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044207 Mobile Safari/537.36 MicroMessenger/6.7.3.1340(0x26070332) NetType/4G Language/zh_CN Process/tools",
        "Mozilla/5.0 (Linux; Android 8.1.0; PACM00 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.1.0)",
        "Mozilla/5.0 (Linux; Android 7.1.1; vivo X20A Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/WIFI Language/zh_CN",
        "Mozilla/5.0 (Linux; Android 8.1.0; vivo Y71A Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.1.0)",
        "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; Mi Note 2 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.1",
        "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.2.2",
        "Mozilla/5.0 (Linux; Android 8.0.0; MI 6 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.0.0)",
        "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MI 5 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.9.969 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; MI 6 Build/OPR1.170623.027) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 Maxthon/3235",
        "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; Mi Note 3 Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.0.2",
        "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; SM-J3109 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.0.960 UWS/2.12.1.18 Mobile Safari/537.36 AliApp(TB/7.5.4) UCBS/2.11.1.1 WindVane/8.3.0 720X1280",
        "Mozilla/5.0 (Linux; Android 8.0.0; SM-G9650 Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.0.0)",
        "Mozilla/5.0 (Linux; Android 8.0.0; SM-N9500 Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.0.0)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.31(0x18001f2d) NetType/WIFI Language/zh_CN",
    ]
    ua = random.choice(ua_list)
    return ua

def output_xls(choiceList_X):           #写入已有的EXCEL文件-在文件根目录的result.xls
    #print(type(datalist))  # <class 'list'>　
    import xlwt
    import xlrd
    import xlutils
    from xlutils.copy import copy
    filename = 'result.xls'
    f = xlrd.open_workbook(filename) # 打开Excel为xlrd对象
    old_sheet = f.sheet_by_index(0) # 取到第一个旧表
    old_sheet_rows = old_sheet.nrows # 第一个旧表的行数，下面追加就得在这个后面写入数据
    copy_read = copy(f) # 把xlrd对象转为xlwt对象
    exist_sheet = copy_read.get_sheet(0) # 取旧表
    for len in range(20):
        if choiceList_X[len][0]==2 or choiceList_X[len][0]==3:
            if choiceList_X[len][0]==2:
                 choiceC="单选题"
            else:
                if choiceList_X[len][0]==3:
                    choiceC="多选题"
            exist_sheet.write(old_sheet_rows,0,choiceC)
            choiceList_Y=choiceList_X[len][1].replace("</p>","",1)
            choiceList_Y=choiceList_Y.replace("<p>","",1)
            exist_sheet.write(old_sheet_rows,1,choiceList_Y)
            exist_sheet.write(old_sheet_rows,2,choiceList_X[len][2])
            exist_sheet.write(old_sheet_rows,4,choiceList_X[len][4])
            exist_sheet.write(old_sheet_rows,5,choiceList_X[len][6])
            exist_sheet.write(old_sheet_rows,6,choiceList_X[len][8])
            exist_sheet.write(old_sheet_rows,7,choiceList_X[len][10])
            old_sheet_rows += 1
        else:
            choiceC="判断题"
            exist_sheet.write(old_sheet_rows,0,choiceC)
            choiceList_Y=choiceList_X[len][1].replace("</p>","",1)
            choiceList_Y=choiceList_Y.replace("<p>","",1)
            exist_sheet.write(old_sheet_rows,1,choiceList_Y)
            exist_sheet.write(old_sheet_rows,1,choiceList_X[len][1])
            exist_sheet.write(old_sheet_rows,2,choiceList_X[len][2])
            exist_sheet.write(old_sheet_rows,4,choiceList_X[len][4])
            exist_sheet.write(old_sheet_rows,5,choiceList_X[len][6])
            old_sheet_rows += 1
    copy_read.save(filename)


def Onceanswer(name_idX):
    base_url1="https://ehsfront.crc.com.cn/gw/edu/mobile/getToken?"
    authCode1="&authCode=AAB204653960435D98F5604F5E9CCC6B"
    userId1="&userId="
    userId2=str(random.randint(1111111111,9999999999))
    businessId1="&businessId=f23521a34a27456682b99baf8590a950"
    businessId2="f23521a34a27456682b99baf8590a950"
    url1=''.join([base_url1, authCode1,userId1,userId2,businessId1])
    #print(url1)
    ua_ = random_ua()
    header1 = {
        "Content-Type": "application/json;charset=utf-8",
        "origin": "https://ehsfront.crc.com.cn",
        "accept-language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "accept": "application/json, text/plain, */*",
        "User-Agent": "%s" % ua_,
        "Token": "MB85D33211601A06D3711D6816871EE2A5D98C4BCFD91E73AF3C291607B8A33CA5",
    }
    result1 = requests.get(url1, headers=header1)
    dict1 = json.loads(result1.text)
    #print(dict1)
    msg1 = dict1.get("msg")
    #print(msg1)
    if msg1 == "操作成功":
        data1=dict1.get("data")
        #print(data1)
        base_Url2="https://ehsfront.crc.com.cn/gw/edu/mobile/getQuizInfoAndConfig?quizId="
        url2 = ''.join([base_Url2,businessId2])
        header2 = {
        "Content-Type": "application/json;charset=utf-8",
        "origin": "https://ehsfront.crc.com.cn",
        "accept-language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "accept": "application/json, text/plain, */*",
        "User-Agent": "%s" % ua_,
        "Token": "%s" % data1,
        }
        #print(url2)
        result2 = requests.get(url2, headers=header2)
        dict2 = json.loads(result2.text)
        #print(dict2)
        msg2 = dict2.get("msg")
        if msg2 == "操作成功":
            quiz_Id=dict2.get("data").get("quizId")
            paper_Id=dict2.get("data").get("paperId")
            #print(quiz_Id)
            #print(paper_Id)
            startQuiz_url = "https://ehsfront.crc.com.cn/gw/edu/mobile/startQuiz"
            token_header = {
                "Host": "ehsfront.crc.com.cn",
                "Content-Type": "application/json;charset=utf-8",
                "origin": "https://ehsfront.crc.com.cn",
                "accept-language": "zh-CN,zh-Hans;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "Keep-Alive",
                "accept": "application/json, text/plain, */*",
                "User-Agent": "%s" % ua_,
                "Token": "%s" % data1,
                }
            token_data1={
                "userStep": "0",
                "userCode": "renbaocheng1",
                "userName": "任宝城",
                "userTel": "",
                "userOrgName": "",
                "userType": "1",
                "userLdap": "renbaocheng1",
                "paperId": "%s" % paper_Id,
                "quizId": "%s" % quiz_Id,
            }
            token_data2={
                "userStep": "0",
                "userCode": "",
                "userName": "%s" % name_idX,
                "userTel": "13123456780",
                "userOrgName": "测试",
                "userType": "3",
                "paperId": "%s" % paper_Id,
                "quizId": "%s" % quiz_Id,
            }
            token_result = requests.post(startQuiz_url, headers=token_header, json=token_data2)
            token_dict = json.loads(token_result.text)
            #print(token_dict)
            msg = token_dict.get("msg")
            Quest_header = {
                "Host": "ehsfront.crc.com.cn",
                "accept-language": "zh-CN,zh-Hans;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "Keep-Alive",
                "accept": "application/json, text/plain, */*",
                "User-Agent": "%s" % ua_,
                "Token": "%s" % data1,
            }
            if msg == "操作成功":
                user_AnswerId=token_dict.get("data").get("userAnswerId")
                #print(user_AnswerId)
                base_Url="https://ehsfront.crc.com.cn/gw/edu/mobile/previewEduPaper?paperId=a26ec4cd9cd3490ba17d6cf20a221021&userAnswerId="
                Question_url = ''.join([base_Url, user_AnswerId])
                #print(Question_url)
                Quest_result = requests.get(Question_url, headers=Quest_header)
                quest_dict = json.loads(Quest_result.text)
                #print(quest_dict)
                msg = quest_dict.get("msg")
                if msg == "操作成功":     #把题目和选项写入choiceList数组
                    #print(msg)
                    choiceList=[]
                    for ID_ in range(20):
                        quest_type=quest_dict.get("data").get("itemBankInfoList")[ID_].get("type")
                        #print(quest_type)    #2  单选题、3  多选题、4  判断题
                        #print(answer_content_len)   #1  单选  5 3个选项  7  
                        choiceList_1=[]
                        choiceList_1.append(quest_type)
                        quest_Id=quest_dict.get("data").get("itemBankInfoList")[ID_].get("detail").get("id")
                        #print(ID_+1)
                        quest_content=quest_dict.get("data").get("itemBankInfoList")[ID_].get("detail").get("content")
                        #print(quest_content)
                        choiceList_1.append(quest_content)
                        answer_content=quest_dict.get("data").get("itemBankInfoList")[ID_].get("detail").get("answer")
                        answer_content_len=len(answer_content)
                        choiceList_1.append(answer_content)
                        #print(answer_content)
                        answer_versionId=quest_dict.get("data").get("itemBankInfoList")[ID_].get("detail").get("versionId")
                        if quest_type==2 or quest_type==3:
                            for choiceList_ID in range(4):
                                choice_ID=[]
                                choice_Value=[]
                                choice_ID=quest_dict.get("data").get("itemBankInfoList")[ID_].get("choiceList")[choiceList_ID].get("id")
                                choice_Value=quest_dict.get("data").get("itemBankInfoList")[ID_].get("choiceList")[choiceList_ID].get("choiceValue")
                                #print(choice_ID)
                                choiceList_1.append(choice_ID)
                                choiceList_1.append(choice_Value)
                            choiceList.append(choiceList_1)
                        else:
                            for choiceList_ID in range(2):
                                choice_ID=[]
                                choice_Value=[]
                                choice_ID=quest_dict.get("data").get("itemBankInfoList")[ID_].get("choiceList")[choiceList_ID].get("id")
                                choice_Value=quest_dict.get("data").get("itemBankInfoList")[ID_].get("choiceList")[choiceList_ID].get("choiceValue")
                                #print(choice_ID)
                                choiceList_1.append(choice_ID)
                                choiceList_1.append(choice_Value)
                            choiceList.append(choiceList_1)
                    #print(choiceList) 
                    #print(choiceList[11][1]) 
                    output_xls(choiceList)

for i in range(100):
    base_name_id1=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    base_name_id2=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    base_name_id3=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    base_name_id4=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    base_name_id5=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    name_id = ''.join([base_name_id1, base_name_id2,base_name_id3,base_name_id4,base_name_id5])
    Onceanswer(name_id)
    print(i)
    time.sleep(random.randint(1, 2))
