# Solar Potential Calculator

A command-line tool to evaluate solar panel installation viability for residential and commercial properties in India. Built using **pure Python and OOP** — no external libraries.

This is Phase 1 of my learning roadmap toward climate physical risk intelligence. The goal was to translate real-world domain logic (solar insolation, Indian subsidy structures, commercial tax incentives) into clean, object-oriented Python.

---

## What It Does

Takes user inputs about their location, panel specs, and roof dimensions, then calculates:

**For residential users:**
- Gross installation cost and net investment after government subsidy
- Monthly and annual savings based on electricity slab rate
- Payback period, total lifetime cost, LCOE, and lifetime savings per unit

**For commercial users:**
- Base system cost, GST amount, and gross cash outflow
- Net investment after accelerated depreciation tax shield and GST input credit
- Annual savings from working-day consumption and off-day grid export
- Net annual savings and payback period

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/anujsharma-codex/01_SOLAR_POTENTIAL_CALCULATOR.git
cd 01_SOLAR_POTENTIAL_CALCULATOR

# No dependencies to install — pure Python 3
python main.py
```

The program will walk you through inputs interactively. Press **Enter** at any prompt to exit.

---

## Sample Session

```
WELCOME TO SOLAR POTENTIAL CALCULATOR

TELL ME ABOUT YOU

What type of user are you?
  1. Residential
  2. Commercial
  (Enter 1 or 2, or press ENTER to stop): 1

NOW TELL ME ABOUT YOUR LOCATION

Enter your city name  : Mumbai
Enter your state name : Maharashtra

NOW TELL ME ABOUT YOUR SOLAR PANEL!

Panel wattage (1=1kW, 2=2kW, 3=3kW, 4=4kW, 5=5kW): 3
Number of panels          : 10
Panel length in metres    : 2
Panel width in metres     : 1

NOW TELL ME ABOUT YOUR ROOF DIMENSIONS

Roof length in metres : 10
Roof width in metres  : 8
Enter your electricity slab rate (just the % number): 6

==================================================
MAIN MENU — SELECT A CATEGORY
==================================================
  1. SOLAR SYSTEM
  2. ENERGY GENERATION
  3. FINANCE

FINANCE OPTIONS:
  2. Net Investment (after subsidy)

NET INVESTMENT (after subsidy):
  Rs. 12,000.00

  5. Payback Period

PAYBACK PERIOD:
  3.8 years
```

---

## Project Structure

```
solar-potential-calculator/
│
├── main.py                     # CLI entry point, menu logic, factory functions
├── config.py                   # All constants: tariffs, subsidies, panel specs, city data
│
└── Solar/
    ├── solarcalculator.py      # SolarSystem and EnergyGeneration classes
    ├── location.py             # Location class — city/state lookup for tariffs and subsidies
    ├── financialcalculator.py  # ConsumerCategory, Residential, Commercial,
    │                           # ResidentialFinance, CommercialFinance classes
    └── utils.py                # Utils class — formatting, safe division, normalisation
```

---

## OOP Design

The class hierarchy is deliberately split by responsibility:

| Class | Responsibility |
|---|---|
| `SolarSystem` | Physical properties — panel area, feasibility check |
| `EnergyGeneration` | Energy calculations — daily, monthly, annual output |
| `Location` | Location-specific lookups — peak sun hours, tariffs, subsidies |
| `ConsumerCategory` → `Residential` / `Commercial` | User profile and config values per consumer type |
| `ResidentialFinance` / `CommercialFinance` | Financial calculations per consumer type |
| `Utils` | Shared helpers — string normalisation, currency formatting, safe divide |

`Residential` and `Commercial` both inherit from `ConsumerCategory`. The finance classes are intentionally separate rather than sharing a base class — residential finance is subsidy-driven while commercial finance is structured around GST and accelerated depreciation, which are fundamentally different cost models.

---

## Data Coverage

Currently supports **9 Indian cities**:

| City | State |
|---|---|
| Ahmedabad | Gujarat |
| Dehradun | Uttarakhand |
| Delhi | Delhi |
| Kolkata | West Bengal |
| Hyderabad | Telangana |
| Chennai | Tamil Nadu |
| Mumbai | Maharashtra |
| Indore | Madhya Pradesh |
| Jaipur | Rajasthan |

Subsidy data is based on PM Surya Ghar Yojana combined central + state figures. Tariff data reflects 2024 state electricity board rates. Peak sun hours are sourced from MNRE solar radiation data.

---

## Known Limitations

These are genuine constraints I'm aware of — not omissions:

**Data scope:** Only 9 cities are supported. Any city not in the dictionary returns `None` silently rather than raising a clear error. A production version would either fetch live data from an API or surface the failure explicitly to the user.

**Static data:** Electricity tariffs, subsidies, and market rates are hardcoded in `config.py`. These change regularly at state and central level. Ideally they'd be loaded from a regularly updated source.

**Energy model is simplified:** `calculate_daily_energy()` uses a single peak-sun-hours constant per city. It doesn't account for seasonality, shading, dust losses beyond the performance factor, panel degradation over time, or inverter efficiency. A more accurate model would use hourly irradiance data (e.g., ERA5 or NSRDB).

**No input validation on city/state:** If a user types "Bombay" instead of "Mumbai", lookups silently return `None` and calculations break downstream. String normalisation is applied, but there's no fuzzy matching or user warning.

**Slab rate is a single flat figure:** Real residential electricity billing in India is tiered — the marginal unit cost depends on total consumption. This calculator assumes a single average slab rate entered by the user.

**Commercial working-day savings formula:** Assumes 100% of daily energy generation is consumed on working days. In reality, self-consumption varies with business load profile and time of generation.

---

## Reflection

**What I assumed:** That a single performance factor (0.75) and one peak-sun-hours value per city is sufficient for a first approximation. For a calculator making investment decisions over 25 years, this is a significant simplification.

**Where this approach fails:** On the finance side, the payback period calculation doesn't discount future savings to present value. An NPV or IRR calculation would be more financially rigorous. A solar installation that pays back in 4 years at 0% discount rate looks different at a 10% discount rate.

**If I had external libraries available:** I'd replace the static city data with an API call to PVGIS or the NSRDB for real hourly irradiance data, use pandas for data cleaning and aggregation, and add a visualisation of monthly savings vs. loan repayment over the panel lifetime. That's the direction this project evolves in Phase 2.

---

## What's Next

This project will be extended in later phases of my roadmap:

- **Phase 2:** Replace static peak-sun-hours with real ERA5 reanalysis data; add seasonal and inter-annual variability analysis using pandas and xarray
- **Phase 4:** Add statistical uncertainty to savings projections — bootstrapped confidence intervals on payback period estimates
- **Phase 5:** Build a generation forecasting model that predicts daily output from atmospheric variables

---

## Author

Built as Phase 1 of a climate physical risk intelligence learning roadmap — demonstrating algorithmic thinking and OOP design in a domain-relevant context before introducing any external libraries.
