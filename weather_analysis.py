import statistics

# Weather data for Gandhinagar (last 10 days)
temperature = [34, 35, 33, 36, 32, 34, 37, 35, 33, 34]
humidity = [60, 62, 58, 65, 59, 61, 63, 64, 60, 62]

# Calculate average
avg_temp = sum(temperature) / len(temperature)
avg_humidity = sum(humidity) / len(humidity)

# Calculate median
median_temp = statistics.median(temperature)
median_humidity = statistics.median(humidity)

print("Temperature Analysis:")
print("Average:", avg_temp)
print("Median:", median_temp)

print("\nHumidity Analysis:")
print("Average:", avg_humidity)
print("Median:", median_humidity)
