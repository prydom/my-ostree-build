#!/usr/bin/env bash
set -oue pipefail

KVER="$(ls /usr/lib/modules)"
mkdir -p /tmp/dracut

dracut --reproducible -v --add 'ostree' --tmpdir '/tmp/dracut' -f --no-hostonly --kver $KVER "/usr/lib/modules/$KVER/initramfs.img"
