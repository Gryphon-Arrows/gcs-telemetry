# ArduPilot simulation

ArduPlane software-in-the-loop, run in Docker. Telemetry is MAVLink over UDP on port 14550. `simulation_test.py` writes each message to `simulation_pixhawk_log.csv`.

## Setup

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and leave it running.
2. From the repo root, install the Python packages:

```powershell
pip install -r requirements.txt
```

## Run the simulator

From `ardupilot_simulation`:

```powershell
docker run --rm -it orthuk/ardupilot-sitl ./Tools/autotest/sim_vehicle.py -v ArduPlane --out=udp:host.docker.internal:14550
```

The same command is in `simulation.sh`. The first start downloads the image. When the `MAV>` prompt appears, the plane is sending heartbeats.

Type those two lines in the Docker window, at the MAV> prompt, when you want it to leave the ground:

```text
mode takeoff
arm throttle
```

## Log the stream

In a second terminal, from `ardupilot_simulation`:

```powershell
python simulation_test.py
```

Leave the Docker container running. Ctrl+C stops the logger. Rows go to `simulation_pixhawk_log.csv`. A `HEARTBEAT` row has `type` 1 (fixed wing) and `autopilot` 3 (ArduPilot) inside `data`.

Only one program can listen on port 14550. Stop any other listener before starting the script.