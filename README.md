這個專案是一個自動化的天氣通知系統，旨在定期從 OpenWeatherMap 獲取天氣資訊，並通過 Line Notify 將天氣資訊自動發送給使用者。主要功能包括：

1.天氣資料獲取：使用 OpenWeatherMap API 獲取指定經緯度位置的當前天氣資料，包括溫度、濕度、風速等詳細資訊。

2.資料處理：將原始的天氣資料格式化，並過濾出使用者關注的重點資訊，確保傳遞的資訊簡潔明確。

3.Line 通知發送：利用 Line Notify API，將整理好的天氣資訊自動發送至使用者的 Line，實現即時、無需手動操作的天氣提醒。

4.定時廣播：系統每小時運行一次，保證天氣資訊的即時性，並可支持多個使用者的天氣通知需求。
