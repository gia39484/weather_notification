import requests

LINE_URL = 'https://notify-api.line.me/api/notify'

def send_message(token, msg):
    headers = {'Authorization': 'Bearer ' + token}
    payload = {'message': msg}
    response = requests.post(LINE_URL, headers=headers, params=payload)
    return response.status_code

def main():
    line_token = 'ywf72zJDxkzqVxSrMxgkbxVXJZa1QlifEq6WZYlXI7C'
    status_code = send_message(line_token, 'hi Shang-Zhe,Cheng , it is a test.')
    print(status_code)

if __name__ == '__main__':
    main()
