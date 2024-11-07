from os import path
import logging
import time

from weather_station import WeatherStation
from weather_notification import LineNotification

logger = logging.getLogger(__name__)
CURRENT_PATH = path.dirname(path.abspath(__file__))
HOUR = 60 * 60

#宣告一個users_data紀錄使用者owm_api_key、line_token、longitude、latitude，這裡用list代表我們假設會有更多使用者。
users_data = [{
    "owm_api_key": "80a89c618fe3f99b1495d14d31ee9c9b",
    "line_token": "ywf72zJDxkzqVxSrMxgkbxVXJZa1QlifEq6WZYlXI7C",
    "longitude": 120.4346272,
    "latitude": 23.6958411
}]


def main():
    while True:
        for user_data in users_data:
            # 初始化 WeatherStation 和 LineNotification
            weather_station = WeatherStation(
                api_key=user_data.get('owm_api_key'),
                lat=user_data.get('latitude', 0),
                lon=user_data.get('longitude', 0)
            )
            notifier = LineNotification(token=user_data.get('line_token'))

            # 獲取天氣資料
            weather_data = {
                "status": weather_station.status,
                "temperature": weather_station.temperature,
                "humidity": weather_station.humidity,
                "wind": weather_station.wind
            }

            # 發送通知
            try:
                status_code = notifier.notify(weather_data)
                logger.info(f"通知已發送，狀態碼: {status_code}")
            except Exception as e:
                logger.error(f"發送通知失敗: {e}")

        # 執行頻率
        time.sleep(HOUR)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )
    main()
