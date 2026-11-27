podman run -it --rm \
    --device /dev/dri:/dev/dri \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /home/jon/dev/pixhawk-sim/src/PX4-Autopilot:/src/PX4-Autopilot \
    -w /src/PX4-Autopilot \
    -p 14550:14550/udp \
    docker.io/px4io/px4-sitl-gazebo:latest
