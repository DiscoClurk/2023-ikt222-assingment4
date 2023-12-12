
import requests

def send_login_request(url, username, password):
    payload = {
        'username': username,
        'password': password
    }
    response = requests.post(url, json=payload)
    return response



def main():
    
    targetWebsite = "http://10.13.13.254/login"
    username = "jonas.dahle" * 1337  
    password = "1337" * 1337 

    #Calling post function and printing the result
    result = send_login_request(targetWebsite, username, password)
    print(result.text)

if __name__ == "__main__":
    main()
