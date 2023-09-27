import time
import csv
import board
import digitalio
import adafruit_blinka.board as board
from adafruit_hcsr04 import HCSR04

trig_pin = board.D17
echo_pin = board.D18
sensor = HCSR04(trig_pin, echo_pin)

# Create and open a CSV file for writing
csv_filename = "distance_data.csv"
with open(csv_filename, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Timestamp", "Distance (cm)"])  # Write header row

    try:
        while True:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            distance = sensor.distance
            print(f"Timestamp: {timestamp}, Distance: {distance} cm")
            
            # Write timestamp and distance to the CSV file
            csv_writer.writerow([timestamp, distance])
            
            time.sleep(1)  # Delay between measurements

    except KeyboardInterrupt:
        pass

    finally:
        sensor.deinit()
