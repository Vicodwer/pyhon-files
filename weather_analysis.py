import statistics

# Weather data for Gandhinagar (last 10 days)
temperature = [34, 35, 33, 36, 32, 34, 37, 35, 33, 34]
humidity = [60, 62, 58, 65, 59, 61, 63, 64, 60, 62]
aqi = [110, 120, 105, 130, 115, 118, 125, 140, 112, 119]

# Temperature calculations
avg_temp = sum(temperature) / len(temperature)
median_temp = statistics.median(temperature)

# Humidity calculations
avg_humidity = sum(humidity) / len(humidity)
median_humidity = statistics.median(humidity)

# AQI calculations
avg_aqi = sum(aqi) / len(aqi)
median_aqi = statistics.median(aqi)

print("Temperature Analysis:")
print("Average:", avg_temp)
print("Median:", median_temp)

print("\nHumidity Analysis:")
print("Average:", avg_humidity)
print("Median:", median_humidity)

print("\nAQI Analysis:")
print("Average:", avg_aqi)
print("Median:", median_aqi)

# Store results in file
with open("results.txt", "w") as file:
    file.write("Weather Analysis Results\n")
    file.write("------------------------\n")
    file.write(f"Temperature Average: {avg_temp}\n")
    file.write(f"Temperature Median: {median_temp}\n")
    file.write(f"Humidity Average: {avg_humidity}\n")
    file.write(f"Humidity Median: {median_humidity}\n")
    file.write(f"AQI Average: {avg_aqi}\n")
    file.write(f"AQI Median: {median_aqi}\n")
