import pyowm
import json

api_key = '80a89c618fe3f99b1495d14d31ee9c9b'
owm = pyowm.OWM(api_key)

# 使用 weather_manager 來獲取天氣資料
mgr = owm.weather_manager()
observation = mgr.weather_at_coords(lat=23, lon=121)
weather = observation.weather

# 直接將天氣資料轉換為字典並輸出
weather_data = {
    "status": weather.status,
    "detailed_status": weather.detailed_status,
    "temperature": weather.temperature('celsius'),  # 攝氏溫度
    "humidity": weather.humidity,
    "wind": weather.wind(),
    "pressure": weather.pressure
}

# 將字典轉換為 JSON 格式並打印
print(json.dumps(weather_data, indent=4))
