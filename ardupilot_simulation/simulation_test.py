import csv
from datetime import datetime

from pymavlink import mavutil

CSV_FILE = "ardupilot_simulation/simulation_pixhawk_log.csv"

print("Connecting to Pixhawk...")
mav = mavutil.mavlink_connection("udpin:0.0.0.0:14550")
hb = mav.wait_heartbeat()

while hb:

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(["time", "message", "field", "value"])

        while True:
            msg = mav.recv_match(blocking=True)
            if msg is None or msg.get_type() == "BAD_DATA":
                continue

            time_now = datetime.now().isoformat(timespec="milliseconds")
            data = msg.to_dict()

            data.pop("mavpackettype")

            for field, value in data.items():
                print("Program Running")
                writer.writerow([time_now, msg.get_type(), field, value])
            f.flush()
