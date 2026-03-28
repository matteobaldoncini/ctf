import requests

BASE_URL = "http://web-11.challs.olicyber.it/"

def login(session):
    json = {'username':'admin', 'password':'admin'}
    response = session.post(BASE_URL + "login", json=json)
    return response

def get_piece(session, ses_cookie, csrf_token, index):
    cookies = {'session':ses_cookie}
    params = {'index':index,'csrf':csrf_token}
    response = session.get(BASE_URL + "flag_piece", params=params, cookies=cookies)
    return response

if __name__ == "__main__":
    session = requests.Session()
    response = login(session)
    ses_cookie = response.cookies.get('session')
    csrf_token = response.json().get('csrf')
    
    for index in range(4):
        response = get_piece(session, ses_cookie, csrf_token, index)
        flag_piece = response.json().get('flag_piece')
        print(flag_piece, end="")   
        csrf_token = response.json().get('csrf')
        #print(ses_cookie, csrf_token, index)
