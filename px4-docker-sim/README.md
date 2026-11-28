Clone locally
```
mkdir src
cd src
git clone https://github.com/PX4/PX4-Autopilot.git
```

Then I use docker_run.sh which is a big docker command.

Then build with
```
bash docker_run.sh 'cd /src/PX4-Autopilot && make px4_sitl'
```
and run with
```
bash docker_run.sh '/src/PX4-Autopilot/build/px4_sitl_default/bin/px4'
```

