def calculate_average(values):
    return sum(values) / len(values)
data = [72, 55, 90, 91]
average = calculate_average(data)
print("Average:", average)

stations = [
 ['A1', 62],
 ['B9', 97],
 ['C3', 135]
]
for station in stations:
 print(station[0], "=", station[1])

def report_status(stations, threshold):
 for id, pm25 in stations:
 if pm25 <= threshold:
 print(f"{id} - {pm25} µg/m³ (safe)")
 else:
 print(f"{id} - {pm25} µg/m³ (danger!)")
