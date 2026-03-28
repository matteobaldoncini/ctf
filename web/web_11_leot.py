import requests

BASE_URL = "http://web-11.challs.olicyber.it"

def login(session):
    return session.post(f"{BASE_URL}/login", json={"username":"admin", "password":"admin"})

def flag_piece(session, csrf, index):
    return session.get(f"{BASE_URL}/flag_piece", params={"csrf": csrf, "index": index})




if __name__ == '__main__':
    ses = requests.Session()
    res = login(ses)
    csrf = res.json().get("csrf")
    for i in range(4):
        res = flag_piece(ses, csrf, i)
        csrf = res.json().get("csrf")
        partial_flag = res.json().get("flag_piece")
        print(partial_flag, end='')
        #breakpoint()
