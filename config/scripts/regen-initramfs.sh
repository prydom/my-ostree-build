#!/usr/bin/env bash
set -oue pipefail

KVER="$(rpm -q kernel | sed -rn 's/^kernel-(.*)$/\1/p')"
ls -1 --zero /usr/lib/modules | grep -vz "^$KVER$" \
    | sed -z 's/[[:space:]]*$//' \
    | xargs -r -0 -- printf "/usr/lib/modules/%s\0" \
    | xargs -r -0 -- rm -rf

mkdir -p /tmp/dracut
dracut --reproducible -v --add 'ostree' --tmpdir '/tmp/dracut' -f --no-hostonly --kver $KVER "/usr/lib/modules/$KVER/initramfs.img"
