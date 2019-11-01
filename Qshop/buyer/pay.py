from alipay import AliPay
def Pay(order_id,money):
    alipay_public_key_string = '''-----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoJlLcBt2z83Dii4vqvbW/P5grTzcskTjRuV4zdbwPGapbxlNtSEMS2KGSauJpdbghAXF6OQBBnEZ33RUjJvMXnCykjeoO03MEsz01G2FwM3n8EICSwnxYxevSQKScW+bVn4ybKuEqFMWNyylhsjIq+2vls5SY4g8gHhqI45GNeHbHjn/+qFP51crTO6sYjOjTMVNe5KcL+qUZYowFTe1dxFDgGMV82xHY7hmRih+xxoIIEPj6OLiFo+wY7TvFm5oAzhg4X39Z4oPR9aDlFYgIkW4ftoxlK2IVV48rWUq0NrCLLccdOV2Zn0ne4Sn/yfskAfii5wd6glWhbPU7nqTEQIDAQAB
    -----END PUBLIC KEY-----'''

    app_private_key_string = '''-----BEGIN RSA PRIVATE KEY-----
        MIIEowIBAAKCAQEAoJlLcBt2z83Dii4vqvbW/P5grTzcskTjRuV4zdbwPGapbxlNtSEMS2KGSauJpdbghAXF6OQBBnEZ33RUjJvMXnCykjeoO03MEsz01G2FwM3n8EICSwnxYxevSQKScW+bVn4ybKuEqFMWNyylhsjIq+2vls5SY4g8gHhqI45GNeHbHjn/+qFP51crTO6sYjOjTMVNe5KcL+qUZYowFTe1dxFDgGMV82xHY7hmRih+xxoIIEPj6OLiFo+wY7TvFm5oAzhg4X39Z4oPR9aDlFYgIkW4ftoxlK2IVV48rWUq0NrCLLccdOV2Zn0ne4Sn/yfskAfii5wd6glWhbPU7nqTEQIDAQABAoIBAC9kjYqL0EgKpMXGU3LUXSVTvBvjdg11nsxxM3ErGMH6Wc3bXb8x/XrRnGdpI7m465CKU5kij9rizYvPvJOx9mF4SHo1yoOVtb9mlGmL2IjJOsT/9cVHLeDcQHH/PFAVa3Xez+qZwxAZVNj7Z+2amv2BquuJ/2436gLPhiLv/XAwuhh1xgxLPsYkJei3uMN2pm+cvodV0qDSXpt8QbqNQv98P8FtkOtDi8vyamJdS3oY7PoTtRfkbQ4Z31A8yytPVGGoNRDmA2abSuSXjc0MfQkxWvldv1zLpm1xQ1hWvDlbeMDfVJQmci7Qd08ZvJOedulST+jFoBMzOen1H8We20ECgYEA4scpMokxAs/dteqwNbAGDjdeOiFBmhXvPUeJN98oWyyROfkha3/ganQ0z8mljYSmO9HIaKextgNkkgJmFzsXSzUKquqDrA5j4+QkAnQXQBeE4XEs7g26rQT7zGmL/osv+GfsuP/6jLCbKEtwwMPalITfh+kn/JVpE5XbuXHjQs0CgYEAtUsMX+u6z23zm3D+pIGUiiWCa8YPOMLRQTm10kOFncn0RDmDLvekwrvBWK/EyNDgCNanVTDdPPwLb/8x/qpv181S1/7F8u9gtZVUVR5qQ6qfUn2LeUmzpeAxgT1qB3j6IM84VzuWsibxbegAsArryBUzkAR93Hz7KDxdnhI8+VUCgYAoWN7PivEZWvpLP3ISWzr4lIlDNl+Blp11/aBAPIflkMxV0ClOAvZeekZbIbk+sHcS9YP+erd3dqsR/zNCttSyIMHBHvBGUFkdVp3Bgf4Q/R47LfOcdvzbg6N4/t5Vb1Ydj//h+kkNdu5kAOgSo8Xj3rAWcjkXC04imer513VjkQKBgH7emTdbOS1GTc9+4MTw5alTnJSdUzOuqk/R+hq+I/iLRwSjltk8drHMQP82aij6e33T8eAdRQYTgFGNLkiAr6o+xvXfFlnvCSep7A1xLn5SHhLVRtDHMhAn95zxBI1cLPbe7Rem3MupkxUN4cVQrzYjGCV17zpowD6lGAKx0rfNAoGBAIzB6Z3toToiM6nJ5Vhgn5hF9Z2ga4PlIUaU/Jj2aldtcjq7Pn3EU2b+5/8A8FycPnmsVgAhfGuwahVYAzj7Vc2MMnhsegnhpCnW63FkrR+53NBHsWk8tWjy3fA7s+SJ1xPpItkrZJ4YZUqYOpXNv0UsVCdCdj9eV0BxArH5OKP2
    -----END RSA PRIVATE KEY-----'''

    alipay = AliPay(
        appid="2016101500695725",  # 支付宝app的id
        app_notify_url="",  # 回调视图
        app_private_key_string=app_private_key_string,  # 私钥字符
        alipay_public_key_string=alipay_public_key_string,  # 公钥字符
        sign_type="RSA2",  # 加密方法
    )
    # 发起支付
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order_id,
        total_amount=str(money),  # 将Decimal类型转换为字符串交给支付宝
        subject="商贸商城",
        return_url=None, #完成之后返回
        notify_url=None  # 可选, 不填则使用默认notify url
    )

    # 让用户进行支付的支付宝页面网址
    return "https://openapi.alipaydev.com/gateway.do?" + order_string

if __name__ == '__main__':
    print(Pay("100000002","1000"))
