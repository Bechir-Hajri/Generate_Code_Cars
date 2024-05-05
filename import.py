import json
import random
from datetime import datetime, timedelta

def generate_vehicle_data():
    now = datetime.now()
    start_time = now - timedelta(hours=random.randint(1, 24))
    end_time = now
    
    return {
        "CBOX": str(random.randint(100000000000000, 999999999999999)),
        "date": now.strftime("%Y-%m-%d"),
        "DailyDistance": round(random.uniform(10, 100), 2),
        "dailyFuel": round(random.uniform(0, 10), 1),
        "litersFilled": round(random.uniform(0, 50), 1),
        "startTime": start_time.strftime("%Y-%m-%d %H:%M:%S+00:00"),
        "endTime": end_time.strftime("%Y-%m-%d %H:%M:%S+00:00"),
        "travelHours": round((end_time - start_time).seconds / 3600, 4),
        "maxTravelHours": round(random.uniform(0, 1), 10),
        "NombreFatime": random.randint(0, 5),
        "CarbUsedMaxTravelHours": round(random.uniform(0, 10), 1),
        "nbHardBraking": random.randint(0, 10),
        "nbHardAcceleration": random.randint(0, 10),
        "temperatureLiquide": random.randint(20, 100),
        "IdleHours": round(random.uniform(0, 10), 10),
        "maxSpeed": random.randint(40, 120),
        "averageSpeed": round(random.uniform(10, 100), 2),
        "score": round(random.uniform(0, 100), 2)
    }

def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    try:
        num_vehicles = int(input("Enter the number of vehicles to generate data for: "))
        if num_vehicles < 1:
            raise ValueError("Number of vehicles must be at least 1.")
        
        for _ in range(num_vehicles):
            vehicle_data = generate_vehicle_data()
            filename = f"{vehicle_data['CBOX']}-{vehicle_data['date']}.json"
            save_data_to_file(vehicle_data, filename)
            print(f"Data for vehicle {vehicle_data['CBOX']} saved to {filename}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
