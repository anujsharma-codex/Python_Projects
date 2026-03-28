"""ALL CALCULATIONS RELATED TO SOLAR PANEL"""
from config import PANEL, DAYS_IN_A_MONTH
import numpy as np

class SolarSystem:
    def __init__(self,panel_wattage,number_of_panels,panel_length,panel_width,roof_length,roof_width,month,year):
        self.panel_wattage=panel_wattage              #int numbers e.g. 1,2,3,4.... in kW
        self.number_of_panels= number_of_panels       #int - e.g. 2,3,300,1000.....
        self.length=panel_length                      #float length of one panel
        self.width=panel_width                        #float width of one panel
        self.roof_length=roof_length
        self.roof_width=roof_width 
        self.performance_factor = PANEL["performance_factor"]  
        self.month=month                             # int number
        self.year=year                               # int number

    def calculate_total_panel_area(self):
        return self.length*self.width*self.number_of_panels

    def tell_system_setup_feasibility(self):
        return self.calculate_total_panel_area() <= self.roof_length*self.roof_width

class EnergyGeneration:
    def __init__(self,solar_system_obj,location_obj):
        self.ss_obj=solar_system_obj                 #object_assignment
        self.l_obj=location_obj                      #object_assignment
        
    def calculate_system_capacity(self):
        return self.ss_obj.panel_wattage*self.ss_obj.number_of_panels
    
    def calculate_daily_energy(self):
        return (self.ss_obj.panel_wattage            #object accession
                *self.ss_obj.performance_factor      #object accession
                *self.l_obj.get_city_max_peak_sun_hours()
                *self.ss_obj.number_of_panels)       #object accession
    
    def calculate_monthly_energy(self):
        days=DAYS_IN_A_MONTH[DAYS_IN_A_MONTH["month"]==self.ss_obj.month]["no_of_days"][0]
        return self.calculate_daily_energy()*days
    
    def calculate_annual_energy_in_months(self,panel_year):      # new
        annual_peak_energy_in_months=DAYS_IN_A_MONTH["no_of_days"]*self.calculate_daily_energy()
        decay_factor=self.ss_obj.PANEL["efficiency_loss"][0]**(panel_year-1)
        return annual_peak_energy_in_months*decay_factor

    def calculate_annual_energy(self):
        if self.ss_obj.year%4==0:
            no_of_days_in_year=366
        else:
            no_of_days_in_year=365
        return self.calculate_daily_energy()*no_of_days_in_year
    
    def calculate_lifetime_energy(self):
        years=np.arange(self.ss_obj.PANEL["life"][0])
        decay_arr=(self.ss_obj.PANEL["efficiency_loss"][0])**years
        return decay_arr*self.calculate_annual_energy()

    def calculate_cumulative_energy_generation(self):
        return np.sum(self.calculate_lifetime_energy())



























'''
class Panels:
    def __init__(self,panel_wattage,panel_weight,panel_length,panel_width,peak_sun_hours):
        self.panel_wattage=panel_wattage
        self.panel_weight=panel_weight
        self.panel_length=panel_length
        self.panel_width=panel_width
        self.peak_sun_hours=peak_sun_hours
        self.performance_factor=0.75
        
    def tell_physical_feasibility_on_roof(self,roof_area):
        panel_area=(self.panel_length)*(self.panel_width)
        return if panel_area <= roof_area:
                
class EnergyGeneration(Panels):
    def __init__(self,panel_wattage,panel_weight,panel_length,panel_width,peak_sun_hours):
        super().__init__(panel_wattage,panel_weight,panel_length,panel_width,peak_sun_hours)
        self.daily_energy=self.panel_wattage*self.peak_sun_hours*self.performance_factor
    
    def daily_energy(self):
        return self.daily_energy
    
    def monthly_energy(self):
        return self.daily_energy*30
    
    def annual_energy(self):
        return self.monthly_energy()*12

'''