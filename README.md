Weather Broadcaster 是一個自動化的天氣通知系統，通過整合 OpenWeatherMap API 和 Line Notify API，實現每小時自動獲取天氣資訊並將其發送給使用者。此專案特別適合於需要定期掌握當前天氣狀況的使用者，無論是日常生活、戶外活動還是需要監控特定地點天氣的應用場景。

功能特色

天氣資料獲取：基於 OpenWeatherMap API，根據指定的經緯度獲取即時的天氣資訊，包括天氣狀態、溫度、濕度、風速等。

資料處理與格式化：過濾並格式化原始天氣數據，僅保留使用者需要的重點資訊，以簡明清晰的方式展示。

Line 通知推送：透過 Line Notify API，將處理好的天氣資訊自動發送至使用者的 Line，隨時掌握天氣變化。

定時廣播：每小時自動運行一次，保證天氣資訊的即時性並支持多個使用者的天氣通知需求。

weather_broadcaster_project/
├── check_api.py                  # 測試 OpenWeatherMap API，檢查天氣資料獲取是否正常
├── line_token.py                 # Line Notify 權杖的管理與配置
├── utils.py                      # 通用工具函數，如單位轉換（若有需要）
├── weather_broadcaster_broker.py # 主控腳本，負責整合各模組並控制天氣廣播流程
├── weather_notification.py       # LineNotification 類別，用於處理通知的發送
├── weather_station.py            # WeatherStation 類別，用於從 OpenWeatherMap 獲取天氣資料
