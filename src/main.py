import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from comparison import SectorComparison
from visualiser import Visualiser

def main():
    data_file = os.path.join(os.path.dirname(__file__), '../data/telemetry_data.csv')
    metrics_config = {"speed": "avg_speed", "braking": "brake_pressure"}

    comparator = SectorComparison(data_file, metrics_config)
    comparator.process_data()

    comparison_data = comparator.compare_sectors(1, 2)

    visualiser = Visualiser(comparison_data)
    visualiser.plot_sector_deltas()

if __name__ == "__main__":
    main()
