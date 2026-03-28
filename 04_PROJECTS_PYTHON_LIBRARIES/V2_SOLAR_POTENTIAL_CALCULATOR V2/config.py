# all constraints here
import numpy as np
RESIDENTIAL_CONFIG=np.array(
    [(58000,25,0.01,0.75)],
    dtype=[("market_rate_per_kW",int),
           ("system_lifetime",int),
           ("annual_maintenance_ratio",float),
           ("performance_ratio",float)])


COMMERCIAL_CONFIG=np.array(
    [(6,48000,0.089,0.40,0.02,0.25)],
    dtype=[
        ("working_days_per_week",int),
        ("market_rate_per_kW",float),
        ("gst_composite_rate",float),
        ("accelerated_depreciation_rate",float),
        ("annual_maintenance_ratio",float),
        ("tax_bracket",float)
        ])

PANEL=np.array(
    [(25,0.75,0.995)],
    dtype= [("life",int),
            ("performance_factor",float),
            ("efficiency_loss",float)
            ])

CITY = np.array([
    ("Ahmedabad", 23.0, 72.65, 6.5),
    ("Dehradun", 30.2, 78.06, 6.0),
    ("Delhi", 28.6, 77.52, 6.5),
    ("Kolkata", 22.5, 88.38, 9.2),
    ("Hyderabad", 17.4, 78.46, 6.0),
    ("Chennai", 13.0, 80.3, 6.0),
    ("Mumbai", 18.9, 72.85, 9.9),
    ("Indore", 22.7, 75.85, 6.8),
    ("Jaipur", 26.9, 75.85, 6.5)
], dtype=[
    ("city_name", "U20"),      # Unicode string, max 20 chars
    ("latitude", "f8"),        # 64-bit float
    ("longitude", "f8"),       # 64-bit float  
    ("peak_sun_hours", "f8")   # 64-bit float
])


STATE = np.array([
    ("Gujarat", 2.25, 4.50),
    ("Uttarakhand", 2.00, 4.80),
    ("Delhi", 4.30, 5.50),
    ("West Bengal", 2.00, 6.00),
    ("Telangana", 2.00, 8.50),
    ("Tamil Nadu", 2.00, 7.50),
    ("Maharashtra", 2.00, 12.00),
    ("Madhya Pradesh", 0.50, 6.50),
    ("Rajasthan", 2.00, 7.00)
], dtype=[
    ("state_name", "U20"),
    ("export_rate", "f8"),
    ("tariff", "f8")
])

SUBSIDIES=np.array([
    [35000, 67500, 88000, 90000, 93000],  # Ahmedabad
    [53000, 100000, 132000, 132000, 132000],  # Dehradun
    [32000, 64000, 84000, 86000, 88000],  # Delhi
    [30000, 60000, 78000, 78000, 78000],  # Kolkata
    [30000, 60000, 78000, 78000, 78000],  # Hyderabad
    [50000, 80000, 98000, 98000, 98000],  # Chennai
    [45000, 60000, 78000, 78000, 78000],  # Mumbai
    [44800, 89600, 122400, 133720, 141650],  # Indore
    [30000, 77000, 95000, 95000, 95000]   # Jaipur
    ])

KW_BRACKETS = np.array(["1kW", "2kW", "3kW", "4kW", "5kW"])

DAYS_IN_A_MONTH=np.array([
    (1,31),
    (2,28),
    (3,31),
    (4,30),
    (5,31),
    (6,30),
    (7,31),
    (8,31),
    (9,30),
    (10,31),
    (11,30),
    (12,31)],
    dtype=[("month",int),("no_of_days",int)]
)

MONTHS=np.array(["January","February","March","April","May","June","July","August","September","October","November","December"])
'''
# v1 without numpy configs

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
'''
