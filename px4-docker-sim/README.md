Clone locally
```
mkdir src
cd src
git clone https://github.com/PX4/PX4-Autopilot.git
```

Then I use podman_run.sh which is a big podman command. If your using docker, you need to replace podman with docker.

Then build with
```
bash podman_run.sh 'cd /src/PX4-Autopilot && make px4_sitl'
```
and run with
```
bash podman_run.sh '/src/PX4-Autopilot/build/px4_sitl_default/bin/px4'
```



