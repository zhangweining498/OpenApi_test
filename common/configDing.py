import requests,json
# from dingtalkchatbot.chatbot import DingtalkChatbot
import time


# 接口正常断言
def dingmsg(url,return_json,code):
    import time
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=1069b1c9bb790fb8f46154904eac9cf53152e4216b5175b654dbb9ec81244d3e'
    header = {"Content-Type": "application/json",
                "Charset": "UTF-8"}
    time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    # 请求状态码
    status_code = return_json.status_code

    # 响应正文
    info = json.loads(return_json.text)

    # 错误码
    re_code = info['code']


    text =  "【标题】: 开放平台接口自动化测试 \n" \
            "【报警时间】: {} \n" \
            "【url】 : {} \n" \
            "【status_code】: {} \n" \
            "【报警信息】: 错误码  {},与预期结果  {}  不符 \n" \
            "【响应正文】: {}".format(time,url,status_code,re_code,code,info)
    msg = {"msgtype":"text",
           "text":{
               "content":text
           }
           }


    msg_json = json.dumps(msg)
    requests.post(url=webhook,data=msg_json,headers = header)
if __name__ == '__main__':

    # print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    url = '/platform/openapi/svdb/BSV/block/transaction'
    code = 500
    info = "1001"
    dingmsg(url,code,info)