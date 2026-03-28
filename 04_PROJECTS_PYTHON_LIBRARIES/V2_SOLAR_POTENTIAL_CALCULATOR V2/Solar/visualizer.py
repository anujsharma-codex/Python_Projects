import numpy as np
import matplotlib.pyplot as plt
from config import PANEL

def generate_lifecycle_graph(annual_energy, filename="assets/lifecycle_decay.png"):
    """Generates a professional dark-mode graph for the 25-year lifecycle."""
    
    # --- 1. The NumPy Data Engine ---
    life_years = PANEL["life"][0]
    years = np.arange(life_years)
    decay_rate = PANEL["efficiency_loss"][0]
    
    # Vectorized Lifecycle Array
    decay_vector = decay_rate ** years
    lifecycle_energy = annual_energy * decay_vector
    
    # Static Baseline (The "Lying" Model)
    static_baseline = np.full(life_years, annual_energy)
    
    # --- 2. The Plotting Engine (Styling) ---
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Set background colors to a deep charcoal
    fig.patch.set_facecolor('#121212')
    ax.set_facecolor('#121212')
    
    # Plotting the lines
    ax.plot(years, static_baseline, color='#FFFFFF', linestyle='--', alpha=0.5, label='Static Model (Inaccurate)')
    ax.plot(years, lifecycle_energy, color='#39FF14', linewidth=3, label='NumPy Simulation (0.5% Decay)')
    
    # Highlight the "Modeling Gap"
    ax.fill_between(years, lifecycle_energy, static_baseline, color='#FF4400', alpha=0.1, label='Inaccuracy Gap')
    
    # --- 3. Professional Formatting ---
    ax.set_title("Solar Energy Output: 25-Year Decay Simulation", fontsize=18, fontweight='bold', pad=20, color='#FFFFFF')
    ax.set_xlabel("Years in Operation", fontsize=14, color='#BBBBBB')
    ax.set_ylabel("Annual Energy Generation (kWh)", fontsize=14, color='#BBBBBB')
    
    # Clean up the grid
    ax.grid(color='#333333', linestyle=':', alpha=0.5)
    ax.legend(loc='upper right', fontsize=12, frameon=False)
    
    # Annotations (Callouts for Peak and Year 25)
    peak = lifecycle_energy[0]
    end = lifecycle_energy[-1]
    
    ax.annotate(f"Peak\n{peak:,.0f} kWh", (0, peak), textcoords="offset points", xytext=(10, 10), color='#39FF14', fontweight='bold')
    ax.annotate(f"Year 25\n{end:,.0f} kWh", (24, end), textcoords="offset points", xytext=(-50, -30), color='#FF4400', fontweight='bold')
    
    # Remove top/right borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(filename, facecolor=fig.get_facecolor(), dpi=300)
    print(f"📊 Graph successfully generated and saved to: {filename}")

if __name__ == "__main__":
    # Simulate a standard 5kW system for the graphic
    # (5kW * 0.75 * 6h * 365d = ~8212 kWh)
    dummy_annual = 8212 
    generate_lifecycle_graph(dummy_annual)
