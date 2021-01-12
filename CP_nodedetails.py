        'client_secret': secret
    }
    r = requests.post(uri, data=payload, headers=headers)
    data = r.json()
    print(data)
    base64Token = base64.b64encode(
        data['access_token'].encode('ascii')).decode("utf-8")
    return base64Token


def makeRequest(tokenb64):
    uri = "https://io.catchpoint.com/ui/api/v1/nodes"
    headers = {
        'Accept': "application/json",
        'Host': "io.catchpoint.com",
        'Authorization': "Bearer " + tokenb64
    }
    r = requests.get(uri, headers=headers)
    # print(r.content)
    data = r.json()
    return data


# Replace the client key and secret
token = generateToken('Key','Secret')
print(token)

CatchpointData = makeRequest(token)
print (CatchpointData)
