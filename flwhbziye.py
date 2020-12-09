import requests
import json
import os,time


#https://raw.githubusercontent.com/ziye12/JavaScript/master/flwhbziye.js

#返利网红包


###################################################
# 对应方案1: 下载到本地,需要此处填写  注意cookie以json形式填写
cookies1 = {}
cookies2 = {}

cookiesList = [cookies1,]   # 多账号准备

'''
# 通知服务
BARK = ''                   # bark服务,自行搜索; secrets可填;形如jfjqxDx3xxxxxxxxSaK的字符串
SCKEY = ''                  # Server酱的SCKEY; secrets可填
TG_BOT_TOKEN = ''           # telegram bot token 自行申请
TG_USER_ID = ''             # telegram 用户ID

'''






#账户信息

def flwhbtask(cookies):
    print("\n【账户信息】")
    headers = {
        'Host': 'huodong.fanli.com',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; LM-G710N Build/PKQ1.181105.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Fanli/7.16.7.2 (ID:2-1711358-66699812379993-19-0; WVC:WV; SCR:1440*3120-4.0)',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Referer': 'https://huodong.fanli.com/h5/Fanlishare20201212?spm=page_name.h5.pty-jljhd~id-vxshare~77444&devid=66699812379993&c_aver=1.0&c_src=2&c_v=7.16.7.2&abtest=61747_c-26_d-2036_b-320_a-154_b-316_b-404_b-32_i-124_b-210_c-84_b-22_b-8_c-140_b-22_a-708_b-104_a-12_a-1008_b-146_b-4_b-2_b-28_a-314_b-148_b-90_c-16_a-72_a-32_b-86_b-12_b-6_b-16_b-2_b-20_b-8_a-24_a-2_a-765d&c_nt=wifi&mc=19&ci=%7B%5C%22ud%5C%22%3A%5C%22from%3Ddb%26local%3Dbrick_hp_c_bar%26id%3D917%26id_type%3Dbar%26abtest_group%3D%26abtest_activity%3D%26dpt%3D1%252F5%5C%22%7D',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    try:
        response = requests.get('https://huodong.fanli.com/h5/Fanlishare20201212/ajaxInit', headers=headers, cookies=cookies)
    except:
        print("网络请求异常,直接跳过")
        return
    print(requests.utils.dict_from_cookiejar(response.cookies))

    data = response.json()["data"]

    if response.json()["status"] ==1:
            print('【收益总计】🎉:'+str(data['user_total_money'])+'元'+'\n')
            print('【剩余礼盒】🎉:'+ str(data['remain_num_76728']) + '个' +'\n')
            return (data['remain_num_76728'])
            print('【账户余额】🎉:'+str(data['user_current_money'])+'\n')
    else:
            print('cookie失效'+'\n')




#惊喜礼盒--一天5次
def flwhblh(cookies):
    print("\n【惊喜礼盒】")
    headers = {
        'Host': 'huodong.fanli.com',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; LM-G710N Build/PKQ1.181105.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Fanli/7.16.7.2 (ID:2-1711358-66699812379993-19-0; WVC:WV; SCR:1440*3120-4.0)',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Referer': 'https://huodong.fanli.com/h5/Fanlishare20201212?spm=page_name.h5.pty-jljhd~id-vxshare~77444&devid=66699812379993&c_aver=1.0&c_src=2&c_v=7.16.7.2&abtest=61747_c-26_d-2036_b-320_a-154_b-316_b-404_b-32_i-124_b-210_c-84_b-22_b-8_c-140_b-22_a-708_b-104_a-12_a-1008_b-146_b-4_b-2_b-28_a-314_b-148_b-90_c-16_a-72_a-32_b-86_b-12_b-6_b-16_b-2_b-20_b-8_a-24_a-2_a-765d&c_nt=wifi&mc=19&ci=%7B%5C%22ud%5C%22%3A%5C%22from%3Ddb%26local%3Dbrick_hp_c_bar%26id%3D917%26id_type%3Dbar%26abtest_group%3D%26abtest_activity%3D%26dpt%3D1%252F5%5C%22%7D',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    try:
        response = requests.get('https://huodong.fanli.com/h5/Fanlishare20201212/ajaxDoTask76728', headers=headers, cookies=cookies)
    except:
        print("网络请求异常,直接跳过")
        return
    data = response.json()["data"]


    if (data['remain_num_76728']>0):
        print('【开启礼盒】🎉:'+str(data['remain_num_76728']) +'元'+'\n')
        print('【剩余礼盒】🎉:'+ str(data['remain_num_76728']) + '个' +'\n')

    else:
        print('【开启完毕】✖️:'+'礼盒已全部开启'+'\n') 
        pass



#提现
def flwhbtx(cookies):
    print("\n【微信提现】")
    headers = {
        'Host': 'huodong.fanli.com',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; LM-G710N Build/PKQ1.181105.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Fanli/7.16.7.2 (ID:2-1711358-66699812379993-19-0; WVC:WV; SCR:1440*3120-4.0)',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Referer': 'https://huodong.fanli.com/h5/Fanlishare20201212?spm=page_name.h5.pty-jljhd~id-vxshare~77444&devid=66699812379993&c_aver=1.0&c_src=2&c_v=7.16.7.2&abtest=61747_c-26_d-2036_b-320_a-154_b-316_b-404_b-32_i-124_b-210_c-84_b-22_b-8_c-140_b-22_a-708_b-104_a-12_a-1008_b-146_b-4_b-2_b-28_a-314_b-148_b-90_c-16_a-72_a-32_b-86_b-12_b-6_b-16_b-2_b-20_b-8_a-24_a-2_a-765d&c_nt=wifi&mc=19&ci=%7B%5C%22ud%5C%22%3A%5C%22from%3Ddb%26local%3Dbrick_hp_c_bar%26id%3D917%26id_type%3Dbar%26abtest_group%3D%26abtest_activity%3D%26dpt%3D1%252F5%5C%22%7D',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    try:
        response = requests.get('https://huodong.fanli.com/h5/Fanlishare20201212/ajaxExchangeCash', headers=headers, cookies=cookies)
    except:
        print("网络请求异常,直接跳过")
        return
    data = response.json()["data"]
    print(data)
    '''
    if (data['status'] == 1):
        print('【余额提现】🎉:提现成功,请到公众号领取'+'\n')

    else:
        print('【余额提现】✖️:'+ data['info']+'\n') 
        pass
'''

    



    








def serverJ(title, content):
    print("\n")
    sckey = SCKEY
    if "SCKEY" in os.environ:
        """
        判断是否运行自GitHub action,"SCKEY" 该参数与 repo里的Secrets的名称保持一致
        """
        sckey = os.environ["SCKEY"]

    if not sckey:
        print("server酱服务的SCKEY未设置!!\n取消推送")
        return
    print("serverJ服务启动")
    data = {
        "text": title,
        "desp": content.replace("\n", "\n\n")+"\n\n "  #[打赏作者](https://github.com/pkpkgtr/thanks.md)
    }
    response = requests.post(f"https://sc.ftqq.com/{sckey}.send", data=data)
    print(response.text)


def bark(title, content):
    print("\n")
    bark_token = BARK
    if "BARK" in os.environ:
        bark_token = os.environ["BARK"]
    if not bark_token:
        print("bark服务的bark_token未设置!!\n取消推送")
        return
    print("bark服务启动")
    response = requests.get(
        f"""https://api.day.app/{bark_token}/{title}/{content}""")
    print(response.text)

def telegram_bot(title, content):
    print("\n")
    tg_bot_token = TG_BOT_TOKEN
    tg_user_id = TG_USER_ID
    if "TG_BOT_TOKEN" in os.environ and "TG_USER_ID" in os.environ:
        tg_bot_token = os.environ["TG_BOT_TOKEN"]
        tg_user_id = os.environ["TG_USER_ID"]
    if not tg_bot_token or not tg_user_id:
        print("Telegram推送的tg_bot_token或者tg_user_id未设置!!\n取消推送")
        return
    print("Telegram 推送开始")
    send_data = {"chat_id": tg_user_id, "text": title +
                 '\n\n'+content, "disable_web_page_preview": "true"}
    response = requests.post(
        url='https://api.telegram.org/bot%s/sendMessage' % (tg_bot_token), data=send_data)
    print(response.text)


if __name__ == "__main__":
    for k, v in enumerate(cookiesList):
       cookie = cookiesList[k]

       num = flwhbtask(cookie)
       numbers = iter(range(num))

       for x in numbers:
            flwhblh(cookie)
            time.sleep(5)
    flwhbtx(cookie)
      
'''
 while a < 5 :
            if a == 0 :  
                flwhbtask(cookie)
            flwhblh(cookie)
            time.sleep(10)
'''