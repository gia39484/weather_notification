import logging
import pyowm
from pyowm.utils.config import get_default_config

# 設置logging配置
# 設定日誌的級別為 INFO，這意味著 INFO 級別及以上的日誌（如 WARNING, ERROR）會被記錄，指定日誌的格式，包括時間、日誌級別、訊息
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class WeatherStation:
    def __init__(self, api_key, lat, lon):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon

        # 設置 OWM 的語言選項（可選）
        config_dict = get_default_config()
        config_dict['language'] = 'en'

        try:
            # 初始化 OWM 和 weather manager
            self.owm = pyowm.OWM(api_key, config_dict)  # 創建一個 OWM 物件並配置 API 密鑰和語言
            self.mgr = self.owm.weather_manager()  # 使用 weather_manager 來管理天氣資料
            logger.info("OWM 初始化成功")
        except Exception as e:
            logger.error("無法初始化 OWM: %s", e)
            raise

    @property
    def weather(self):
        """取得當前座標的天氣資訊。"""
        try:
            observation = self.mgr.weather_at_coords(self.lat, self.lon)
            logger.info("成功取得天氣資訊")
            return observation.weather
        except Exception as e:
            logger.error("無法取得天氣資訊: %s", e)
            return None

    @property
    def status(self):
        """返回天氣狀態（如晴天、陰天等）"""
        if self.weather:
            return self.weather.status
        return "無法取得天氣狀態"

    @property
    def detailed_status(self):
        """返回詳細的天氣狀態（如部分多雲、毛毛雨等）"""
        if self.weather:
            return self.weather.detailed_status
        return "無法取得詳細天氣狀態"

    @property
    def temperature(self):
        """以攝氏溫度返回當前溫度"""
        if self.weather:
            return self.weather.temperature('celsius')
        return "無法取得溫度資訊"

    @property
    def humidity(self):
        """返回當前濕度"""
        if self.weather:
            return self.weather.humidity
        return "無法取得濕度資訊"

    @property
    def wind(self):
        """返回風速和風向"""
        if self.weather:
            return self.weather.wind()
        return "無法取得風速資訊"

    @property
    def pressure(self):
        """返回氣壓資訊"""
        if self.weather:
            return self.weather.pressure
        return "無法取得氣壓資訊"
