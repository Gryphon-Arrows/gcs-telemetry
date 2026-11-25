
from pymavlink import mavutil
import serial
import csv
from datetime import datetime

PORT = "COM4"
BAUD = 57600

CSV_FILE = "pixhawk_log.csv"

print("Connecting to Pixhawk...")
print(f"Port: {PORT} | Baud: {BAUD}")

ser = None

try:
    ser = serial.Serial(PORT, BAUD, timeout=0.1)

    mav = mavutil.mavlink.MAVLink(None)

    with open(CSV_FILE, "a", newline="") as csvfile:

        writer = csv.writer(csvfile)

        if csvfile.tell() == 0:
            writer.writerow([
                "Timestamp",
                "MAVLink Version",
                "Message ID",
                "Message Name",
                "System ID",
                "Component ID",
                "Decoded Data"
            ])

        print("Listening to Pixhawk traffic...")
        print("Press CTRL+C to stop.\n")

        while True:
            data = ser.read(ser.in_waiting or 1)

            if not data:
                continue

            timestamp = datetime.now().isoformat(
                timespec="milliseconds"
            )

            # Parse MAVLink packets
            for byte in data:
                try:
                    msg = mav.parse_char(bytes([byte]))

                    if msg is None:
                        continue

                    version = (
                        "MAVLink 2"
                        if msg.get_msgbuf()[0] == 0xFD   # FD for mavlink 2 and FE for mavlink 1 packets.
                        else "MAVLink 1"
                    )

                    msg_id = msg.get_msgId()
                    msg_name = msg.get_type()
                    sysid = msg.get_srcSystem()
                    compid = msg.get_srcComponent()

                    decoded = str(msg.to_dict())

                    writer.writerow([
                        timestamp,
                        version,
                        msg_id,
                        msg_name,
                        sysid,
                        compid,
                        decoded
                    ])

                    csvfile.flush()

                    print(
                        f"[{timestamp}] "
                        f"{version} | "
                        f"{msg_name} | "
                        f"SYS={sysid} | "
                        f"COMP={compid}"
                    )

                except Exception as e:
                    print("Parser error:", e)

except KeyboardInterrupt:
    print("\nTELEM1 logging stopped.")

except Exception as e:
    print("Connection error:", repr(e))

finally:
    if ser and ser.is_open:
        ser.close()

    print("Serial port closed.")
    print("CSV log:", CSV_FILE)
