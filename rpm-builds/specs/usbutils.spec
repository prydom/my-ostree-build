Name:    usbutils
Version: 017
Release: 2_jxpryde
Summary: Linux USB utilities
URL:     http://www.linux-usb.org/
License: GPL-2.0-or-later

Source0: https://www.kernel.org/pub/linux/utils/usb/usbutils/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: libusb1-devel
BuildRequires: systemd-devel
Requires: hwdata

%description
This package contains utilities for inspecting devices connected to a
USB bus.

%prep
%autosetup -p1

%build
%configure --sbindir=%{_sbindir} --datadir=%{_datadir}/hwdata --disable-usbids
%make_build

%install
%make_install
install -vDm 755 usbreset -t "%{buildroot}/%{_bindir}"
rm -rf %{buildroot}/%{_libdir}/pkgconfig/usbutils.pc

%files
%license LICENSES/GPL*
%doc NEWS
%{_mandir}/*/*
%{_bindir}/*

%changelog
## START: Generated by rpmautospec
* Thu May 02 2024 Jordan Pryde <jordan@pryde.me> - 017-3
- Add usbreset to package

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jan Macku <jamacku@redhat.com> - 017-1
- Update to 017

* Sun Oct 29 2023 Peter Robinson <pbrobinson@gmail.com> - 016-1
- Update to 016

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 11 2023 Lukáš Zaoral <lzaoral@redhat.com> - 015-3
- migrate to SPDX license format

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Jan Macku <jamacku@redhat.com> - 015-1
- Update to usbutils-015

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 014-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 014-1
- Update to 014
- Cleanup spec, licenses now shipped upstream

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 013-1
- Update to 013

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 012-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 012-2
- New 012 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jun 08 2018 Lukas Nykryn <lnykryn@redhat.com> - 010-2
- add upstream fixes

* Wed May 16 2018 Lukas Nykryn <lnykryn@redhat.com> - 010-1
- New 010 release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec  4 2017 Peter Robinson <pbrobinson@fedoraproject.org> 009-1
- New 009 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 008-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 Peter Robinson <pbrobinson@fedoraproject.org> 008-6
- Don't ship usbutils pkgconfig file

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 008-4
- Fix FTBFS, cleanup and modernise spec, use %%license

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 008-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Wed Oct 22 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 008-1
- new release

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 007-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 Lukáš Nykrýn <lnykryn@redhat.com> - 007-1
- new upstream release

* Tue Feb 26 2013 Lukáš Nykrýn <lnykryn@redhat.com> - 006-4
- lsusb-t: make sure that interfaces are added to lists only once (#914929)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Lukáš Nykrýn <lnykryn@redhat.com> - 006-1
- new upstream release

* Thu Apr 19 2012 Lukas Nykryn <lnykryn@redhat.com> 005-1
- new upstream release

* Thu Apr 19 2012 Lukas Nykryn <lnykryn@redhat.com> 004-4
- Ignore missing driver symlink (#808934)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

## END: Generated by rpmautospec
