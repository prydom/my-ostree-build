Name:           1password-ostree-workaround
Version:        0.0.0_main
Release:        1%{?dist}
Summary:        HACK: patch 1Password to avoid quit on rpm-ostree invocation

License: MIT
URL: https://github.com/prydom/1password-ldpreload-inotify
Source0: https://github.com/prydom/1password-ldpreload-inotify/archive/refs/heads/main.tar.gz

BuildRequires: gcc
BuildRequires: make

Requires: 1password
Requires: patchelf


%description
Changes to file attributes — particularly the link count — is triggering an inotify event which quits 1Password.
The workaround is to remove the `IN_ATTRIB` bit from the `mask` provided to `inotify_add_watch()` when the `filepath` ends with `/1password`.

We do this by creating a shared object file which when loaded into the binary with `LD_PRELOAD` or `patchelf` will hook `inotify_add_watch()`.


%prep
%setup -n 1password-ldpreload-inotify-main


%build
%make_build


%install
%make_install


%post
patchelf --add-needed 1p-ldpreload.so /opt/1Password/1password


%files
/opt/1Password/1p-ldpreload.so
%license LICENSE
%doc README.md


%changelog
* Fri Mar 01 2024 Jordan Pryde <jordan@pryde.me>
- Created package
