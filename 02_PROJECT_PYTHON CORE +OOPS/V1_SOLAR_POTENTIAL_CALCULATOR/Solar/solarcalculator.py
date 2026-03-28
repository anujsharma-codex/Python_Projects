"""ALL CALCULATIONS RELATED TO SOLAR PANEL"""
from config import PANEL

class SolarSystem:
    def __init__(self,panel_wattage,number_of_panels,length,width,roof_length,roof_width):
        self.panel_wattage=panel_wattage              #int numbers e.g. 1,2,3,4.... in kW
        self.number_of_panels= number_of_panels     #int - e.g. 2,3,300,1000.....
        self.length=length     #float length of one panel
        self.width=width        #float width of one panel
        self.roof_length=roof_length
        self.roof_width=roof_width 
        self.performance_factor = PANEL.get("performance_factor")   

    def calculate_total_panel_area(self):
        return self.length*self.width*self.number_of_panels

    def tell_system_setup_feasibility(self):
        return self.calculate_total_panel_area() <= self.roof_length*self.roof_width

class EnergyGeneration:
    def __init__(self,solar_system_obj,location_obj):
        self.ss_obj=solar_system_obj    #object_assignment
        self.l_obj=location_obj         #object_assignment
        
    def calculate_system_capacity(self):
        return self.ss_obj.panel_wattage*self.ss_obj.number_of_panels
    
    def calculate_daily_energy(self):
        return (self.ss_obj.panel_wattage              #object accession
                *self.ss_obj.performance_factor  #object accession
                *self.l_obj.get_city_max_peak_sun_hours()
                *self.ss_obj.number_of_panels)   #object accession
    
    def calculate_monthly_energy(self):
        return self.calculate_daily_energy()*30
    
    def calculate_annual_energy(self):
        return self.calculate_monthly_energy()*12





























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