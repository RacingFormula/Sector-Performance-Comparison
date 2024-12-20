import matplotlib.pyplot as plt

class Visualiser:
    def __init__(self, comparison_data):
        self.comparison_data = comparison_data

    def plot_sector_deltas(self):
        plt.figure(figsize=(10, 6))
        plt.bar(self.comparison_data['Sector'], self.comparison_data['SectorDelta'], alpha=0.75)
        plt.title("Sector Time Deltas")
        plt.xlabel("Sector")
        plt.ylabel("Time Delta (s)")
        plt.grid()
        plt.show()

if __name__ == "__main__":
    import pandas as pd
    # Example use
    comparison_data = pd.DataFrame({
        "Sector": [1, 2, 3],
        "SectorDelta": [-0.1, 0.05, -0.07]
    })
    visualiser = Visualiser(comparison_data)
    visualiser.plot_sector_deltas()