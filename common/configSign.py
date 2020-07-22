import hashlib,json
import base64
import hmac
def md5value(data):
    md5 = hashlib.md5()
    md5.update(data.encode())
    return md5.hexdigest()


order_data =  {
    "nonce_str": "1593312690806",
    "merchant_order_sn": "b023e54b-cfbe-4bc3-9444-5b7728e973a3",
    "order_amount": 10000,
    "sign": "",
    "notice_uri": "http://localhost.com:8002",
    "item_name": "A red apple",
    "check_order_uri": "http://localhost.com:8003",
    "opreturn": "This is a lovely apple",
    "redirect_uri": "http://localhost.com:8001",
    "app_id": "5a192d599b0be66bdb2ef72784acb0f8",
    "receive_address":[{"address":"1","amount":444},{"address":"2","amount":555},{"address":"3","amount":666}]
  }
def getSignature(orderData):
    data = ''
    secret = md5value('b71557823ce2b25d07fb186368999181')
    for key in orderData:
        if key != 'sign' and key != 'opreturn':
            if data != '':
                data += '&' + key + '=' + str(orderData[key])
            else:
                data += key + '=' + str(orderData[key])

    data += '&secret=' + secret
    data.upper()

    hash256 = hashlib.sha256()
    hash256.update(data.encode('utf-8'))
    print(hash256.hexdigest())

getSignature(order_data)






