# inputs for everything
class Utils:
    def get_normalized_string(self,value):
        return value.strip().title()
    
    def get_formatted_currency(self,amount):
        return f'Rs. {amount:,.2f}'
    
    def get_formatted_number(self,amount):
        return f'{amount:,.2f}'
    
    def get_formatted_time_in_years(self,time):
        return f'{time} years'
    
    def get_formatted_energy_in_kW(self,energy):
        return f'{energy} kWh'  
    
    def percentage_conversion(self, value):
        return value/100
    
    def safe_divide(self,a, b):
        if b == 0:
            return 0
        return a / b