#!/usr/bin/env bash

CCACHE_DIR=${HOME}/.ccache
mkdir -p "${CCACHE_DIR}"

docker run -it --rm -w "${SRC_DIR}" \
  --env=CCACHE_DIR="${CCACHE_DIR}" \
  --env=PX4_ASAN \
  --env=PX4_MSAN \
  --env=PX4_TSAN \
  --env=PX4_UBSAN \
  --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  --volume=${CCACHE_DIR}:${CCACHE_DIR}:rw \
  --volume=$PWD/src:/src:rw \
  px4-dev-custom /bin/bash -c "$@"
