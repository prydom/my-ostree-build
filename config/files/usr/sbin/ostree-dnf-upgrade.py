#!/usr/bin/env python3

import argparse
import glob
import libdnf5
import subprocess
import sys
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument('--distrosync', default=False, action='store_true')
parser.add_argument('--fail-if-no-upgrades', default=False, action='store_true')
args = parser.parse_args()

base = libdnf5.base.Base()
base.load_config()
config = base.get_config()

with tempfile.TemporaryDirectory(prefix='rpms_') as td:
    config.destdir = td
    config.excludepkgs = ['kernel*']
    # HACK: remove systemd and shadow-utils from this list
    #       once https://github.com/coreos/rpm-ostree/issues/4938 is resolved
    config.excludepkgs += ['systemd*', 'shadow-utils*']
    base.setup()

    repo_sack = base.get_repo_sack()
    repo_sack.create_repos_from_system_configuration()
    repo_sack.update_and_load_enabled_repos(True)

    goal = libdnf5.base.Goal(base)
    if args.distrosync:
        goal.add_rpm_distro_sync()
    else:
        goal.add_upgrade("*")

    transaction = goal.resolve()
    count = transaction.get_transaction_packages_count()
    print(f"Number of package changes in transaction: {count}")
    if count == 0:
        sys.exit(0 if not args.fail_if_no_upgrades else 1)

    transaction.download()
    packages = glob.glob(td + '/*.rpm')

    cmd = ["rpm-ostree", "override", "replace"] + packages
    print(cmd)
    completed_process = subprocess.run(cmd)
    completed_process.check_returncode()
