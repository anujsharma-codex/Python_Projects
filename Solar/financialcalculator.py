from Solar.solarcalculator import*
from config import RESIDENTIAL_CONFIG,COMMERCIAL_CONFIG,PANEL,DAYS_IN_A_MONTH,ESCALATION_CONFIG
from Solar.location import Location
from Solar.utils import Utils
import numpy as np

class ConsumerCategory:
    def __init__(self,category):
        self.consumer_category=category

class Residential(ConsumerCategory):
    def __init__(self,consumer,slab_rate,solar_system_obj,energy_generation_obj,
                 location_obj,utils_obj): 
        
        super().__init__(consumer)

        self.slab_rate=slab_rate
        self.ss_obj=solar_system_obj
        self.eg_obj=energy_generation_obj 
        self.l_obj=location_obj        
        self.u_obj=utils_obj
        self.life=PANEL["life"][0]
        self.market_rate_per_kW=RESIDENTIAL_CONFIG["market_rate_per_kW"][0]
        self.annual_maintenance_ratio=RESIDENTIAL_CONFIG["annual_maintenance_ratio"][0]

class Commercial(ConsumerCategory):
    def __init__(self,consumer,solar_system_obj,energy_generation_obj,
                 location_obj,utils_obj,gst_input_credit=True):
        
        super().__init__(consumer)

        self.gst_input_credit=gst_input_credit
        self.ss_obj=solar_system_obj
        self.eg_obj=energy_generation_obj
        self.l_obj=location_obj
        self.u_obj=utils_obj
        self.tax_bracket=COMMERCIAL_CONFIG["tax_bracket"][0]
        self.annual_maintenance_ratio=COMMERCIAL_CONFIG["annual_maintenance_ratio"][0]
        self.market_rate_per_kW=COMMERCIAL_CONFIG["market_rate_per_kW"][0] 
        self.working_days_per_week= COMMERCIAL_CONFIG["working_days_per_week"][0]
        self.gst_composite_rate=COMMERCIAL_CONFIG["gst_composite_rate"][0]
        self.accelerated_depreciation_rate= COMMERCIAL_CONFIG["accelerated_depreciation_rate"][0]

class ResidentialFinance():
    """Deals with all financial calculations related to residential user"""
    def __init__(self,residential_obj):
        self.r_obj=residential_obj
        
    def get_gross_cost(self):
        return self.r_obj.eg_obj.calculate_system_capacity() *self.r_obj.market_rate_per_kW
    
    def get_net_investment(self):
        return (self.get_gross_cost() - self.r_obj.l_obj.get_combined_subsidy()).item()
          
    def get_monthly_savings(self):
        return (self.r_obj.eg_obj.calculate_monthly_energy() * self.r_obj.slab_rate).item()

    def get_monthly_savings_in_each_month(self,panel_year):                    # new
        return self.r_obj.eg_obj.calculate_annual_energy_in_months(panel_year) *self.r_obj.slab_rate

    def get_annual_savings(self,panel_year):
        return (np.sum(self.get_monthly_savings_in_each_month(panel_year))).item()
    
    def get_total_lifetime_cost(self):
        return self.get_net_investment() + ((self.get_net_investment()*self.r_obj.annual_maintenance_ratio)*self.r_obj.life)
    
    def get_lifetime_maintenance_array(self):
        escalation_arr=np.arange(25)
        maintenance_escalation=(ESCALATION_CONFIG["maintenance_escalation"]+1)**escalation_arr
        neutral_maintenance_per_year=(self.get_net_investment()*self.r_obj.annual_maintenance_ratio)*np.ones(25)
        return neutral_maintenance_per_year*maintenance_escalation

    def get_lifetime_maintenance_cost(self):
        return (np.sum(self.get_lifetime_maintenance_array())).item()
    
    def get_lifetime_energy_generation(self):
        return (self.r_obj.eg_obj.calculate_cumulative_energy_generation()).item()
    
    def get_levelized_cost_of_energy(self):
        return self.get_total_lifetime_cost() / self.get_lifetime_energy_generation()
 
    def get_lifetime_savings_array(self):
        savings_escalation_arr=np.arange(PANEL["life"][0])
        savings_escalation=(ESCALATION_CONFIG["electricity_price_escalation"][0]+1)**np.arange(25)
        lifetime_energy_arr=self.r_obj.eg_obj.calculate_lifetime_energy()
        return lifetime_energy_arr*savings_escalation*self.r_obj.slab_rate

    def get_cumsum_lifetime_savings(self):
        return np.cumsum(self.get_lifetime_savings_array())
    
    def get_lifetime_savings_per_unit(self):
        return self.get_lifetime_savings_array() / self.get_lifetime_energy_generation()

    def get_total_roi_array(self):
        lifetime_savings_arr=self.get_cumsum_lifetime_savings()
        net_investment=self.get_net_investment()
        return (lifetime_savings_arr/net_investment)*100

    def get_payback_year(self):
        yearly_return=self.get_total_roi_array()
        return (np.where(yearly_return>=100)[0][0]+1)
    
    def get_net_present_value(self):
        lifetime_savings_arr=self.get_lifetime_savings_array()
        time_machine_arr=(1+ESCALATION_CONFIG["discount_rate"][0])**np.arange(25)
        todays_value_of_savings_arr=lifetime_savings_arr/time_machine_arr
        return (np.sum(todays_value_of_savings_arr)-self.get_net_investment()).item()

class CommercialFinance():
    """Deals with all financial calculations related to commercial user"""
    def __init__(self,commercial_obj):
        self.c_obj=commercial_obj
       
    def get_base_system_cost(self):
        return self.c_obj.eg_obj.calculate_system_capacity() *self.c_obj.market_rate_per_kW
    
    def get_gst_amount(self):
        return self.get_base_system_cost() *self.c_obj.gst_composite_rate

    def get_gross_cash_outflow(self):
        return self.get_base_system_cost() + self.get_gst_amount()
    
    def get_net_investment(self):
        gross_cash_outflow=self.get_gross_cash_outflow()
        tax_shield = (self.get_base_system_cost() *self.c_obj.accelerated_depreciation_rate) *self.c_obj.tax_bracket
        gst_amount = self.get_base_system_cost() *0.138
        if self.c_obj.gst_input_credit:
            gst_amount=self.get_gst_amount()
        else:
            gst_amount=0
        return (gross_cash_outflow - gst_amount) - tax_shield
    
    def get_weekly_work_savings(self):
        return self.c_obj.eg_obj.calculate_daily_energy() *self.c_obj.working_days_per_week *52 *self.c_obj.l_obj.get_state_tariff()
    
    def get_off_day_export(self):
        return (self.c_obj.eg_obj.calculate_daily_energy() *(7-self.c_obj.working_days_per_week) *52) *self.c_obj.l_obj.get_state_export_rate()

    def get_annual_maintenance(self):
        return self.get_base_system_cost() *self.c_obj.annual_maintenance_ratio
    
    def get_net_annual_savings(self):
        total_gross_income=self.get_weekly_work_savings() + self.get_off_day_export()
        return total_gross_income - self.get_annual_maintenance()
    
    def get_payback_period(self):
        return self.get_net_investment() / self.get_net_annual_savings()