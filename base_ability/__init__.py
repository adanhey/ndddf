import requests


class Base_interface():
    def __init__(self):
        self.userName = "imooc"
        self.password = "12345678"
        self.host = "http://111.231.103.117.8083/"
        self.token = self.login_for_token()

    def login_for_token(self):
        url = "%sloginwithJwt" % self.host
        data = {
            "userName": self.userName,
            "password": self.password
        }
        result = requests.get(url=url, params=data)
        return result.json()['data']

    def get_request(self,url,data=None,param=None,header=None):
        if header:
            pass
        else:
            header={"jwt_token":self.token}
        requests.get(url,param,json=data,headers=header)
    def post_request(self,url,data=None,param=None,header=None):
        if header:
            pass
        else:
            header={"jwt_token":self.token}
        requests.get(url,param,json=data,headers=header)
    def put_request(self,url,data=None,param=None,header=None):
        if header:
            pass
        else:
            header={"jwt_token":self.token}
        requests.get(url,param,json=data,headers=header)
    def delete_request(self,url,data=None,param=None,header=None):
        if header:
            pass
        else:
            header={"jwt_token":self.token}
        requests.get(url,param,json=data,headers=header)

