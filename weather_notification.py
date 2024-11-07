import requests
LINE_URL = 'https://notify-api.line.me/api/notify'

class LineNotification:
    def __init__(self, token):
        self.token = token
    def _enrich_message(self, weather_data):
        """
        從天氣資料中提取需要的訊息。
        假設天氣資料是一個 dictionary 格式，並包含需要的資訊。
        """
        status = weather_data.get('status', '無法取得天氣狀態')
        temperature = weather_data.get('temperature', {}).get('temp', '無法取得溫度')  # 直接使用攝氏溫度
        humidity = weather_data.get('humidity', '無法取得濕度')
        wind_speed = weather_data.get('wind', {}).get('speed', '無法取得風速')

        # 組合訊息
        message = f"天氣狀態: {status}\n溫度: {temperature:.2f}°C\n濕度: {humidity}%\n風速: {wind_speed} m/s"
        return message

    def notify(self, weather_data):
        """
        發送天氣訊息到 Line Notify。
        """
        message = self._enrich_message(weather_data)
        headers = {'Authorization': 'Bearer ' + self.token}
        payload = {'message': message}

        try:
            response = requests.post(LINE_URL, headers=headers, params=payload)
            response.raise_for_status()  # 檢查請求是否成功
            return response.status_code
        except requests.exceptions.RequestException as e:
            print("發送 Line Notify 訊息失敗:", e)
            return None
