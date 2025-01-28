#!/usr/bin/env bash
set -oxue pipefail

KVER="$(rpm -q kernel-core --qf '%{version}-%{release}.%{arch}' | head -n1)"
ls -1 --zero /usr/lib/modules | ( grep -vz "^$KVER$" || true ) \
    | sed -z 's/[[:space:]]*$//' \
    | xargs -r -0 -- printf "/usr/lib/modules/%s\0" \
    | xargs -r -0 -- rm -rf

mkdir -p /tmp/dracut
dracut --reproducible -v --add 'ostree' --tmpdir '/tmp/dracut' -f --no-hostonly --kver $KVER "/usr/lib/modules/$KVER/initramfs.img"
