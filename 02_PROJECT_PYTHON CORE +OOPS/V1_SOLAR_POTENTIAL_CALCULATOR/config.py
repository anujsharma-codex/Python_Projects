# all constraints here

RESIDENTIAL_CONFIG = {
"market_rate_per_kW": 58000,
"system_lifetime": 25,
"annual_maintenance_ratio": 0.01,
"performance_ratio": 0.75
}
COMMERCIAL_CONFIG = {
"working_days_per_week":6,
"market_rate_per_kW": 48000,
"gst_composite_rate": 0.089,
"accelerated_depreciation_rate": 0.40,
"annual_maintenance_ratio": 0.02,
"tax_bracket":0.25
}

PANEL= {"life":25,
"performance_factor":0.75
}

CITY_LATITUDE={'Ahmedabad':23.0,
'Dehradun':30.2,
'Delhi':28.6,
'Kolkata':22.5,
'Hyderabad':17.4,
'Chennai':13.0,
'Mumbai':18.9,
'Indore':22.7,
'Jaipur':26.9
}

CITY_LONGITUDE={'Ahmedabad':72.65,
'Dehradun':78.06,
'Delhi':77.52,
'Kolkata':88.38,
'Hyderabad':78.46,
'Chennai':80.3,
'Mumbai':72.85,
'Indore':75.85,
'Jaipur':75.85
}

CITY_PEAK_SUN_HOURS={'Ahmedabad':6.5,
'Dehradun':6,
'Delhi':6.5,
'Kolkata':9.2,
'Hyderabad':6,
'Chennai':6,
'Mumbai':9.9,
'Indore':6.8,
'Jaipur':6.5
}

CENTRAL_STATE_MAX_COMBINED_SUBSIDY={'Ahmedabad':{'1kw':35000,'2kW':67500,'3kW':88000,'4kW':90000,'5kW+':93000},
'Dehradun':{'1kw':53000,'2kW':100000,'3kW':132000,'4kW':132000,'5kW+':132000},
'Delhi':{'1kw':32000,'2kW':64000,'3kW':84000,'4kW':86000,'5kW+':88000},
'Kolkata':{'1kw':30000,'2kW':60000,'3kW':78000,'4kW':78000,'5kW+':78000},
'Hyderabad':{'1kw':30000,'2kW':60000,'3kW':78000,'4kW':78000,'5kW+':78000},
'Chennai':{'1kw':50000,'2kW':80000,'3kW':98000,'4kW':98000,'5kW+':98000},
'Mumbai':{'1kw':45000,'2kW':60000,'3kW':78000,'4kW':78000,'5kW+':78000},
'Indore':{'1kw':44800,'2kW':89600,'3kW':122400,'4kW':133720,'5kW+':141650},
'Jaipur':{'1kw':30000,'2kW':77000,'3kW':95000,'4kW':95000,'5kW+':95000}
}

STATE_EXPORT_RATE={'Gujarat':2.25,
'Uttarakhand':2.00,
'Delhi':4.30,
'West Bengal':2.00,
'Telangana':2.00,
'Tamil Nadu':2.00,
'Maharashtra':2.00,
'Madhya Pradesh':0.50,
'Rajasthan':2.00
}

STATE_TARIFF={'Gujarat':4.50,
'Uttarakhand':4.80,
'Delhi':5.50,
'West Bengal':6.00,
'Telangana':8.50,
'Tamil Nadu':7.50,
'Maharashtra':12.00,
'Madhya Pradesh':6.50,
'Rajasthan':7.00
}

