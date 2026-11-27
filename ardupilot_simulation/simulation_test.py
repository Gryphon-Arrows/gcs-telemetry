import csv
from datetime import datetime

from pymavlink import mavutil

PORT = "COM4"
BAUD = 57600

CSV_FILE = "simulation_pixhawk_log.csv"

print("Connecting to Pixhawk...")

ser = None

mav = mavutil.mavlink_connection("udpin:0.0.0.0:14550")
hb = mav.wait_heartbeat()

while hb:

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(["time", "name", "sys", "comp", "data"])
        while True:
            msg = mav.recv_match(blocking=True)
            if msg is None or msg.get_type() == "BAD_DATA":
                continue
            writer.writerow([
                datetime.now().isoformat(timespec="milliseconds"),
                msg.get_type(),
                msg.get_srcSystem(),
                msg.get_srcComponent(),
                msg.to_dict(),
            ])
            f.flush()
            print(msg.get_type())