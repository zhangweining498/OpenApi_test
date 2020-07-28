import hashlib,json,uuid,requests
import base64
import hmac
def md5value(data):
    md5 = hashlib.md5()
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()


#
# appsecret = 'e9943b6b167554fe555e39c1428c1d86'

def getSignature(orderData,appsecret):
    data = ''
    secret = md5value(appsecret)
    for key in orderData:
        if key != 'sign' and key != 'opreturn':
            if data:
                data += '&' + key + '=' + str(orderData[key])
            else:
                data = key + '=' + str(orderData[key])

    data += '&secret=' + secret
    data = data.upper()
    HMAC = hmac.new(secret.encode('utf-8'),data.encode('utf-8'),digestmod="sha256").hexdigest()
    return HMAC

def get_order_sign(url):
    appsecret = "e9943b6b167554fe555e39c1428c1d86"
    order_data = {"nonce_str": "1595558549178",
                  "merchant_order_sn": "",
                  "order_amount": 600, "sign": "",
                  "notice_uri": "http://localhost.com:8002",
                  "item_name": "商品名称:一个苹果",
                  "check_order_uri": "http://localhost.com:8003",
                  "opreturn": "这是一笔普了一个苹果",
                  "redirect_uri": "http://localhost.com:8001",
                  "app_id": "0d158bc3605fffe30f7046f0c9c7e4bf",
                  "receive_address": "[{\"address\":\"19ncrjsYsF2L2QNLViLQmbySXpMcafgm5N\",\"amount\":600}]"}
    order_data['merchant_order_sn'] = str(uuid.uuid1())
    sign = getSignature(order_data,appsecret)
    order_data['sign'] = sign
    res = requests.post(url,json=order_data)
    order_sn = json.loads(res.text)['data']['order_sn']

    return order_sn
if __name__ == '__main__':

    url = 'https://www.ddpurse.com/platform/openapi/create_order'
    print(get_order_sign(url))











