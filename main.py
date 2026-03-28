from Solar.financialcalculator import*
from Solar.location import* 
from Solar.solarcalculator import*
from Solar.utils import*
from config import*
#----------
"""INPUT HELPER"""
#----------
def get_int_input(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            return ""
        try:
            return int(value)
        except ValueError:
            print("Enter numbers only in digits (no special characters)!")

def get_float_input(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            return ""
        try:
            return float(value)
        except ValueError:
            print("Enter numbers only in digits (no special characters)!")
#---------------
#OBJECT CREATORS
#---------------
def create_consumer_category_obj(consumer):
    if consumer==1:
        consumer_category_obj=ConsumerCategory("Residential")
        return consumer_category_obj
    else:
        consumer_category_obj=ConsumerCategory("Commercial")
        return consumer_category_obj
    
def create_solar_system_obj(panel_wattage,number_of_panels,panel_length,panel_width,roof_length,roof_width,month,start_year,current_year):
    solar_system_obj=SolarSystem(panel_wattage,number_of_panels,panel_length,panel_width,roof_length,roof_width,month,start_year,current_year)
    return solar_system_obj

def create_utils_obj():
    return Utils()
    

def create_location_obj(city,state,solar_system_obj, utils_obj):
    return Location(city,state,solar_system_obj, utils_obj)
     
def create_energy_generation_obj(solar_system_obj, location_obj):
    return EnergyGeneration(solar_system_obj, location_obj)
     

def create_residential_obj(consumer,slab_rate,solar_system_obj,energy_generation_obj,location_obj,utils_obj):
    return Residential(consumer,slab_rate,solar_system_obj,energy_generation_obj,location_obj,utils_obj)
    

def create_residential_finance_obj(residential_obj):
    return ResidentialFinance(residential_obj)
     

def create_commercial_obj(consumer,gst_input_credit,solar_system_obj,energy_generation_obj,location_obj,utils_obj):
    return  Commercial(consumer,gst_input_credit,solar_system_obj,energy_generation_obj,location_obj,utils_obj)
    

def create_commercial_finance_obj(commercial_obj):
    return CommercialFinance(commercial_obj)
     



def residential_finance(choice, rf_obj, u_obj):
    """Print the requested residential finance metric."""
    if choice == '1':
        print("\nGROSS COST OF SYSTEM:")
        print(f'  {u_obj.get_formatted_currency(rf_obj.get_gross_cost())}')

    elif choice == '2':
        print("\nNET INVESTMENT (after subsidy):")
        print(f'  {u_obj.get_formatted_currency(rf_obj.get_net_investment())}')

    elif choice == '3':
        print("\nMONTHLY SAVINGS:")
        print(f'  {u_obj.get_formatted_currency(rf_obj.get_monthly_savings())}')

    elif choice == '4':
        print("\nANNUAL SAVINGS:")
        panel_year=get_int_input("Which year of the system's life do you want to see? (Enter 1-25) : ")
        print(f'  {u_obj.get_formatted_currency(rf_obj.get_annual_savings(panel_year))}')

    elif choice == '5':
        print("\nANNUAL SAVINGS IN EACH MONTH IN A YEAR:")
        panel_year=get_int_input("Which year of the system's life do you want to see? (Enter 1-25) : ")
        savings=rf_obj.get_monthly_savings_in_each_month(panel_year)
        for index in range(12):
            print(f"   {MONTHS[index]} : {u_obj.get_formatted_currency(savings[index])}")

    elif choice == '6':
        print("\nPAYBACK YEAR:")
        print(f'  {u_obj.get_formatted_time_in_years(rf_obj.get_payback_year())}')

    elif choice == '7':
        print("\nTOTAL LIFETIME COST:")
        print(f'  {u_obj.get_formatted_currency(rf_obj.get_total_lifetime_cost())}')

    elif choice == '8':
        print("\nLIFETIME MAINTENANCE COST:")
        maintenance_array=rf_obj.get_lifetime_maintenance_array()
        for index in range(len(maintenance_array)):
            print(f"   Year {index+1} : {u_obj.get_formatted_currency(maintenance_array[index])}")
        print(f'  {u_obj.get_formatted_currency(rf_obj.get_lifetime_maintenance_cost())}')

    elif choice == '9':
        print("\nLEVELIZED COST OF ENERGY (LCOE):")
        print(f'  {u_obj.get_formatted_currency(rf_obj.get_levelized_cost_of_energy())} per kWh')

    elif choice == '10':
        print("\nLIFETIME SAVINGS EACH YEAR:")
        lifetime_savings_each_year=rf_obj.get_lifetime_savings_array()
        for index in range(len(lifetime_savings_each_year)):
            print(f"   Year {index+1} : {u_obj.get_formatted_currency(lifetime_savings_each_year[index])}")
    
    elif choice == '11':
        lifetime_cumulativesum_of_savings=rf_obj.get_cumsum_lifetime_savings()
        print("\nCUMULATIVE LIFETIME SAVINGS:")
        for index in range(len(lifetime_cumulativesum_of_savings)):
            print(f"   Year {index+1} : {u_obj.get_formatted_currency(lifetime_cumulativesum_of_savings[index])}")
    
    elif choice == '12':
        lifetime_savings_per_unit=rf_obj.get_lifetime_savings_per_unit()
        print("\nLIFETIME SAVINGS PER UNIT:")
        for index in range(len(lifetime_savings_per_unit)):
            print(f"   Year {index+1} : {u_obj.get_formatted_currency(lifetime_savings_per_unit[index])}")
    
    elif choice == '13':
        total_roi_array=rf_obj.get_total_roi_array()
        print("\nTOTAL ROI (%):")
        for index in range(len(total_roi_array)):
            print(f"   Year {index+1} : {total_roi_array[index]:.2f} %")

    elif choice == '14':
        print("\nNET PRESENT VALUE:")
        npv=rf_obj.get_net_present_value()
        if npv>0:
            print(f"   {u_obj.get_formatted_currency(npv)} (Profit)")
        else:
            print(f"   {u_obj.get_formatted_currency(npv)} (Loss)")
        

def commercial_finance(choice, cf_obj, u_obj):
    """Print the requested commercial finance metric."""
    if choice == '1':
        print("\nBASE COST OF SOLAR SYSTEM:")
        print(f'  {u_obj.get_formatted_currency(cf_obj.get_base_system_cost())}')

    elif choice == '2':
        print("\nGST AMOUNT:")
        print(f'  {u_obj.get_formatted_currency(cf_obj.get_gst_amount())}')

    elif choice == '3':
        print("\nGROSS CASH OUTFLOW:")
        print(f'  {u_obj.get_formatted_currency(cf_obj.get_gross_cash_outflow())}')

    elif choice == '4':
        print("\nNET INVESTMENT (after tax shield & GST credit):")
        print(f'  {u_obj.get_formatted_currency(cf_obj.get_net_investment())}')

    elif choice == '5':
        print("\nANNUAL SAVINGS (WORKING DAYS):")
        print(f'  {u_obj.get_formatted_currency(cf_obj.get_weekly_work_savings())}')

    elif choice == '6':
        print("\nOFF-DAY EXPORT INCOME:")
        print(f'  {u_obj.get_formatted_currency(cf_obj.get_off_day_export())}')

    elif choice == '7':
        print("\nANNUAL MAINTENANCE COST:")
        print(f'  {u_obj.get_formatted_currency(cf_obj.get_annual_maintenance())}')

    elif choice == '8':
        print("\nNET ANNUAL SAVINGS:")
        print(f'  {u_obj.get_formatted_currency(cf_obj.get_net_annual_savings())}')

    elif choice == '9':
        print("\nPAYBACK PERIOD:")
        print(f'  {u_obj.get_formatted_time_in_years(cf_obj.get_payback_period())}')

def take_object_inputs():
    print("\nWELCOME TO SOLAR POTENTIAL CALCULATOR")

    # --- Consumer type ---
    print("\nTELL ME ABOUT YOU\n")
    while True:
        consumer = get_int_input(
            "What type of user are you?\n"
            "  1. Residential\n"
            "  2. Commercial\n"
            "  (Enter 1 or 2, or press ENTER to stop): "
        )
        if consumer == "":
            return None
        if consumer in (1, 2):
            break
        print("Invalid selection. Please enter 1 or 2.")

    print("---" * 30)

    # --- Location ---
    
    print("\nNOW TELL ME ABOUT YOUR LOCATION\n")
    while True:
        city = input("Enter your city name  : ").strip().title()
        if city in CITY["city_name"]:
            break
        else:
            print("SORRY WE HAVE NO INFORMATION ABOUT THIS CITY!")
            continue
    while True:
        state = input("Enter your state name : ").strip().title()
        if state in STATE["state_name"]:
            break
        else:
            print("SORRY WE HAVE NO INFORMATION ABOUT THIS STATE!")
            continue
   
    print("---" * 30)

    # --- Panel details ---
    print("\nNOW TELL ME ABOUT YOUR SOLAR PANEL!\n")
    panel_wattage = get_int_input(
        "Panel wattage (1=1kW, 2=2kW, 3=3kW, 4=4kW, 5=5kW): "
    )
    if panel_wattage == "":
        return None
    number_of_panels = get_int_input("Number of panels          : ")
    if number_of_panels == "":
        return None
    panel_length = get_float_input("Panel length in metres    : ")
    if panel_length == "":
        return None
    panel_width = get_float_input("Panel width in metres     : ")
    if panel_width == "":
        return None
    print("---" * 30)

    # --- Roof dimensions ---
    print("\nNOW TELL ME ABOUT YOUR ROOF DIMENSIONS\n")
    roof_length = get_float_input("Roof length in metres : ")
    if roof_length == "":
        return None
    roof_width = get_float_input("Roof width in metres  : ")
    if roof_width == "":
        return None

    # --- Date specific inputs-----
    print("\nNOW TELL ME ABOUT THE TIME!\n")
    while True:
        print("""Months:
        1.January
        2.February
        3.March
        4.April
        5.May
        6.June
        7.July
        8.August
        9.September
        10.October
        11.November
        12.December""")
        while True:
            month=get_int_input("Choose only the number of your month : ")
            if month in range(1,13):
                break
            else: 
                print("INVALID INPUT!!!")
                continue
        while True:           
            start_year=get_int_input("Enter the year of installation of panel in digits(e.g., 2024) : ")
            if start_year <= 0:
                print("Cannot be less than/equal to 0")
                print("invalid year entered!!!")
                continue
            else:
                break

        while True:
            current_year=get_int_input("Enter the current year in digits (e.g., 2024) : ")
            if current_year <= 0:
                print("Cannot be less than/equal to 0....")
                print("invalid year entered!!!")
                continue
            elif current_year<start_year:
                print("Current Year cannot be less than Start Year....")
                print("Invalid Input!!!")
                continue
            else:
                break
        break

    # --- Consumer-specific inputs ---
    print("\nNOW LETS TAKE SOME CONSUMER SPECIFIC INPUTS! Almost there....\n")
    slab_rate = 0
    gst_input_credit = False

    if consumer == 1:
        slab_rate_pct = get_float_input("Enter your electricity slab rate in rupees per unit (e.g., 8.2): ")
        if slab_rate_pct == "":
            return None
        slab_rate = slab_rate_pct
    else:
        answer = input("Are you eligible for GST input credit? (y/n): ").strip().lower()
        gst_input_credit = (answer == 'y')

    print("---" * 30)

    # --- Build all objects ---
    utils_obj = create_utils_obj()

    solar_system_obj = create_solar_system_obj(
        panel_wattage, number_of_panels, panel_length, panel_width, roof_length, roof_width,month,start_year,current_year)

    location_obj = create_location_obj(city, state, solar_system_obj, utils_obj)

    energy_generation_obj = create_energy_generation_obj(solar_system_obj, location_obj)

    residential_obj = None
    residential_finance_obj = None
    commercial_obj = None
    commercial_finance_obj = None

    if consumer == 1:
        residential_obj = create_residential_obj(
            "Residential", slab_rate, solar_system_obj,
            energy_generation_obj, location_obj, utils_obj)
        residential_finance_obj = create_residential_finance_obj(residential_obj)
    else:
        commercial_obj = create_commercial_obj(
            "Commercial", solar_system_obj, energy_generation_obj,
            location_obj, utils_obj, gst_input_credit)
        commercial_finance_obj = create_commercial_finance_obj(commercial_obj)

    return {
        "consumer": consumer,
        "solar_system_obj": solar_system_obj,
        "energy_generation_obj": energy_generation_obj,
        "location_obj": location_obj,
        "utils_obj": utils_obj,
        "residential_finance_obj": residential_finance_obj,
        "commercial_finance_obj": commercial_finance_obj,
    }

def main():
    # Collect all inputs and build objects once at startup
    objects = take_object_inputs()
    if objects is None:
        print("\nExiting. Goodbye!")
        return

    consumer = objects["consumer"]
    solar_system_obj = objects["solar_system_obj"]
    energy_generation_obj = objects["energy_generation_obj"]
    utils_obj = objects["utils_obj"]
    rf_obj = objects["residential_finance_obj"]
    cf_obj = objects["commercial_finance_obj"]

    while True:
        print("\n" + "=" * 50)
        print("MAIN MENU — SELECT A CATEGORY")
        print("=" * 50)
        print("  1. SOLAR SYSTEM")
        print("  2. ENERGY GENERATION")
        print("  3. FINANCE")
        print("  (Press ENTER to exit)")
        choice = input("Enter your choice: ").strip()

        if choice == "":
            print("\nExiting. Goodbye!")
            break

        # ── SOLAR SYSTEM ──
        if choice == "1":
            while True:
                print("\nSOLAR SYSTEM OPTIONS:")
                print("  1. Total Panel Area")
                print("  2. Physical Feasibility on Roof")
                print("  (Press ENTER to go back)")
                sub = input("Enter choice: ").strip()
                if sub == "":
                    break
                if sub == "1":
                    print(f"\n  Total Panel Area: {solar_system_obj.calculate_total_panel_area()} m²")
                elif sub == "2":
                    feasible = solar_system_obj.tell_system_setup_feasibility()
                    if feasible:
                        print("\n  ✔ ROOF AREA SUFFICIENT — Installation is possible.")
                    else:
                        print("\n  ✘ ROOF AREA INSUFFICIENT — Installation is not possible.")
                else:
                    print("Invalid selection!")

        # ── ENERGY GENERATION ──
        elif choice == "2":
            while True:
                print("\nENERGY GENERATION OPTIONS:")
                print("  1. System Capacity")
                print("  2. Daily Energy")
                print("  3. Monthly Energy")
                print("  4. Annual Energy")
                print("  5. Annual Energy in months")
                print("  6. Lifetime Energy")
                print("  7. Cumulative Energy Generation In Full Life Cycle")
                print("  (Press ENTER to go back)")
                sub = input("Enter choice: ").strip()
                if sub == "":
                    break
                
                if sub == "1":
                    print(f"\n  System Capacity : {energy_generation_obj.calculate_system_capacity()} kW")
                
                elif sub == "2":
                    print(f"\n  Daily Energy    : {u_obj.get_formatted_number(energy_generation_obj.calculate_daily_energy())} kWh/day")
                
                elif sub == "3":
                    print(f"\n  Monthly Energy  : {u_obj.get_formatted_number(energy_generation_obj.calculate_monthly_energy())} kWh/month")
                
                elif sub == "4":
                    print(f"\n  Annual Energy   : {u_obj.get_formatted_number(energy_generation_obj.calculate_annual_energy())} kWh/year")
                
                elif sub == "5":
                    print("\n Annual Energy In Months In An Year  ")
                    panel_year=get_int_input("Which year of the system's life do you want to see? (Enter 1-25) : ")
                    energy_array=energy_generation_obj.calculate_annual_energy_in_months(panel_year)
                    for index in range(0,12):
                        print(f"\n {MONTHS[index]} : {u_obj.get_formatted_number(energy_array[index])} kWh") 
                    best_month=np.argmax(energy_array)
                    worst_month=np.argmin(energy_array)
                    print(f"🌟 Peak Performance: {MONTHS[best_month]} ({u_obj.get_formatted_number(energy_array[best_month])} kWh)")
                    print(f"☁️ Lowest Generation: {MONTHS[worst_month]} ({u_obj.get_formatted_number(energy_array[worst_month])} kWh)")
                
                elif sub == "6":
                    print("\n Lifetime Energy Considering 0.5% efficiency loss of the Solar Panel:")
                    energy_array=energy_generation_obj.calculate_lifetime_energy()
                    for index in range(0,len(energy_array)):
                        print(f"\n Year {index+1} : {u_obj.get_formatted_number(energy_array[index])} kWh") 
                
                elif sub == "7":
                    print(f"\n  Cumulative Energy Generation In Full Life Cycle Considering 0.5% efficiency loss of the Solar Panel   :\n {u_obj.get_formatted_number(energy_generation_obj.calculate_cumulative_energy_generation())} kWh")
                
                else:
                    print("Invalid selection!")

        # ── FINANCE ──
        elif choice == "3":
            while True:
                print("\nFINANCE OPTIONS:")
                if consumer == 1:
                    print("  1. Gross Cost of Installation")
                    print("  2. Net Investment (after subsidy)")
                    print("  3. Monthly Savings")
                    print("  4. Annual Savings")
                    print("  5. Annual Savings In Each Month In A Year")
                    print("  6. Payback Year")
                    print("  7. Total Lifetime Cost")
                    print("  8. Lifetime Maintenance Cost")
                    print("  9. Levelized Cost of Energy (LCOE)")
                    print("  10. Lifetime Savings Each Year")
                    print("  11. Cumulative Lifetime Savings")
                    print("  12. Lifetime Savings per Unit")
                    print("  13. Total ROI (%) in each year)")
                    print("  14. Net Present Value")
                    print("  (Press ENTER to go back)")
                    sub = get_int_input("Enter choice: ")
                    if sub == "":
                        break
                    if 1 <= sub <= 14:
                        residential_finance(str(sub), rf_obj, utils_obj)
                    else:
                        print("Invalid selection!")
                else:
                    print("  1. Base System Cost")
                    print("  2. GST Amount")
                    print("  3. Gross Cash Outflow")
                    print("  4. Net Investment")
                    print("  5. Annual Working-Day Savings")
                    print("  6. Off-Day Export Income")
                    print("  7. Annual Maintenance Cost")
                    print("  8. Net Annual Savings")
                    print("  9. Payback Period")
                    print("  (Press ENTER to go back)")
                    sub = get_int_input("Enter choice: ")
                    if sub == "":
                        break
                    if 1 <= sub <= 9:
                        commercial_finance(str(sub), cf_obj, utils_obj)
                    else:
                        print("Invalid selection!")
        else:
            print("Invalid selection!")


if __name__ == "__main__":
    main()

