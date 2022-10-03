from Crypto.Cipher import DES

key = b'abcdefgh'  # 密钥 8位或16位,必须为bytes


def pad(text):
    # 如果text不是8的倍数【加密文本text必须为8的倍数！】，补足为8的倍数
    while len(text) % 8 != 0:
        text += ' '
    return text


des = DES.new(key, DES.MODE_ECB)  # 创建DES实例
text = 'Python rocks!'
padded_text = pad(text)

encrypted_text = des.encrypt(padded_text.encode('utf-8'))  # 加密
print(encrypted_text)
# b'>\xfc\x1f\x16x\x87\xb2\x93\x0e\xfcH\x02\xd59VQ'

plain_text = des.decrypt(encrypted_text).decode().rstrip(' ')  # 解密
print(plain_text)
# Python rocks!
# YYYYiJceGQ3Q1JceGI0XHgxMFx4MWJceGU1XHhiMlZceDE1XHgxZEZJXHhkMFx4OTg8XHhlNlx4ZDd4OVx4ZTdceGY2R1x4MTJceGZiXHg4OVx4ZTFceGNiXHg5OC5ceGRjdFx4MDZceGVkdU96XHhkNFx4OTBceDExXHhkMDQnXHhhNFx0TnEkXHhmZXtceDlhXHhjOVx4YjJceDA4XHhjNDYiYYY
