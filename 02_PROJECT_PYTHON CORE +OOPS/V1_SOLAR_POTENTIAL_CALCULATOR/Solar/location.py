from Solar.solarcalculator import SolarSystem
from config import CITY_LATITUDE,CITY_LONGITUDE,CITY_PEAK_SUN_HOURS,CENTRAL_STATE_MAX_COMBINED_SUBSIDY,STATE_EXPORT_RATE,STATE_TARIFF
from Solar.utils import Utils 
class Location:
    def __init__(self,city,state,solar_system_obj,utils_obj):
        self.u_obj=utils_obj
        self.ss_obj=solar_system_obj
        self.city=self.u_obj.get_normalized_string(city)
        self.state=self.u_obj.get_normalized_string(state)  
    
    def get_city_latitude(self):
        return CITY_LATITUDE.get(self.city)
    
    def get_city_longitude(self):
        return CITY_LONGITUDE.get(self.city)
    
    def get_city_max_peak_sun_hours(self):
        return CITY_PEAK_SUN_HOURS.get(self.city)
    
    def get_combined_subsidy(self):
        city_subsidies = CENTRAL_STATE_MAX_COMBINED_SUBSIDY.get(self.city, {})
        wattage_key = str(self.ss_obj.panel_wattage) + 'kW'
        return city_subsidies.get(wattage_key, 0)
    
    def get_state_export_rate(self):
        return STATE_EXPORT_RATE.get(self.state)
    
    def get_state_tariff(self):
        return STATE_TARIFF.get(self.state)