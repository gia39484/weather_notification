import requests
from utils import kelvin_to_celsius  # 導入轉換絕對溫度到攝氏的函數
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
        temp_k = weather_data.get('temperature', {}).get('temp', 273.15)  # 絕對溫度預設為 273.15K
        temp_c = kelvin_to_celsius(temp_k)  # 使用 utils 的轉換函數
        humidity = weather_data.get('humidity', '無法取得濕度')
        wind_speed = weather_data.get('wind', {}).get('speed', '無法取得風速')

        # 組合訊息
        message = f"天氣狀態: {status}\n溫度: {temp_c:.2f}°C\n濕度: {humidity}%\n風速: {wind_speed} m/s"
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