# ☀️ Solar Potential Calculator (V2)
### *From Pure Python to the High-Performance NumPy Engine*

![Solar Calculator Banner](assets/banner.png)

> [!NOTE]
> **The V2 Transformation**: This project transitions from basic scalar OOP to a **vectorized NumPy engine**, enabling high-speed calculation of solar generation across 12 months and 25-year lifecycles in a single operation.

## 🚀 Key Features

| Feature | Description | Why it Matters? |
| :--- | :--- | :--- |
| **Data Structure** | **NumPy Structured Arrays** | Row-based record filtering & efficient memory mapping |
| **Time Analysis** | **12-Month Array (Vectorized)** | Seasonal variations handled in one operation (no loops!) |
| **Life Cycle** | **25-Year Degradation Array** | Models real-world efficiency loss (0.5% yearly decay) |
| **Indexing** | **Boolean Search & Masking** | Professional data-science method for location retrieval |

---

## 🏗 Architecture: The "NumPy Core"
The core engine has been "supercharged" to handle complex data modeling:

1.  **`config.py`**: Centralized configuration using `np.array` with custom `dtypes` for Cities, States, and Subsidies.
2.  **`Solar/Location`**: Implements **Boolean Masking** (`np.where`) to retrieve solar irradiation data instantly.
3.  **`Solar/EnergyGeneration`**: Calculates energy yield for all 12 months simultaneously—**zero Python loops**.
4.  **`Solar/Finance`**: Models a 25-year financial horizon considering cumulative performance degradation using `np.cumprod`.

---

## 📊 Technical Highlights

### **1. Vectorized Month Analytics**
Instead of calculating one day and multiplying by 30, V2 uses a "Days-Per-Month" array:
```python
# Calculates monthly specific energy in one vectorized line
monthly_gen = daily_energy * np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
```

### **2. Lifecycle Performance Decay**
We model 25 years of investment by creating a degradation curve:
```python
# Each year is 0.5% less efficient than the last
degradation = 0.995 ** np.arange(25)
total_lifetime_energy = np.sum(annual_energy * degradation)
```

---

## 🛣 Learning Roadmap
- [x] **V1: Core Python & OOP** (The Foundation)
- [x] **V2: NumPy Integration** (The Engine - *Current*)
- [ ] **V3: Pandas DataFrames** (Enhanced Analysis)
- [ ] **V4: Matplotlib & Seaborn** (Visual Dashboard)
- [ ] **V5: NSRDB/NASA APIs** (Real-World Data Integration)

---

## 💻 Installation & Usage

1.  **Clone the Repository**:
    ```bash
    git clone <your-repo-link>
    cd V2_SOLAR_POTENTIAL_CALCULATOR
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Calculator**:
    ```bash
    python main.py
    ```

---

## ✍️ Author
**Built for Climate Physical Risk Intelligence** — demonstrating the transition from standard algorithmic logic to high-performance data modeling.
