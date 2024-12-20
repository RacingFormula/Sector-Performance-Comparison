import pandas as pd

class SectorComparison:
    def __init__(self, data_file, metrics_config):
        self.data = pd.read_csv(data_file)
        self.metrics = metrics_config

    def process_data(self):
        self.data['Delta'] = self.data['LapTime'].diff().fillna(0)
        self.data['SectorTime'] = self.data['SectorEnd'] - self.data['SectorStart']
        print("Telemetry data processed.")

    def compare_sectors(self, lap1, lap2):
        lap1_data = self.data[self.data['Lap'] == lap1]
        lap2_data = self.data[self.data['Lap'] == lap2]

        comparison = lap1_data.merge(lap2_data, on="Sector", suffixes=('_Lap1', '_Lap2'))
        comparison['SectorDelta'] = comparison['SectorTime_Lap2'] - comparison['SectorTime_Lap1']
        return comparison[['Sector', 'SectorTime_Lap1', 'SectorTime_Lap2', 'SectorDelta']]

if __name__ == "__main__":
    metrics_config = {"speed": "avg_speed", "braking": "brake_pressure"}
    comparator = SectorComparison("data/telemetry_data.csv", metrics_config)
    comparator.process_data()
    result = comparator.compare_sectors(1, 2)
    print(result)