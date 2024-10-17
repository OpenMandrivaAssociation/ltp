%define srcver 20120903

Summary: Linux Test Project
Name:    ltp
Version: 0.%{srcver}
Release: 2
source0: http://downloads.sourceforge.net/project/%{name}/LTP%20Source/%{name}-%{srcver}/%{name}-full-%{srcver}.bz2
patch0:  ltp-full-20120903.printf.patch
License: GPL
Group: Development/Kernel
Requires: /usr/bin/ar /usr/bin/objdump gcc cdialog /usr/bin/ld /usr/bin/ldd tar
BuildRequires: flex glibc-static-devel rsync
BuildRequires: zip
Url: https://ltp.sourceforge.net/

%description
The Linux Test Project is a joint project with SGI, IBM, OSDL, and Bull with a
goal to deliver test suites to the open source community that validate the 
reliability, robustness, and stability of Linux. The Linux Test Project is a 
collection of tools for testing the Linux kernel and related features. Our goal
is to improve the Linux kernel by bring test automation to the kernel testing 
effort. Interested open source contributors are encouraged to join the project.

%prep
%setup -q -n %{name}-full-%{srcver}
%patch0 -p1 -b .printf

%build
make autotools
%configure2_5x
%make

%install
%makeinstall

mkdir -p %{buildroot}%{_libdir}/%{name}/
mv %{buildroot}%{_prefix}/{runtest,testcases,testscripts,scenario_groups,Version} %{buildroot}%{_libdir}/%{name}/
mv %{buildroot}%{_prefix}/{IDcheck.sh,runalltests.sh,runltp,runltplite.sh,ver_linux} %{buildroot}%{_bindir}/
find %{buildroot} -type f -perm 775 -exec chmod 755 \{\} \;
strip %{buildroot}%{_libdir}/%{name}/testcases/bin/*.obj

%files
%defattr(-,root,root)
%doc README CREDITS doc/*.txt
%doc doc/examples doc/*.lyx
%doc doc/testcases
%_libdir/%{name}
%_libdir/libkerntest.a
%_libdir/libmem.a
%_mandir/man1/*
%_mandir/man3/*
%{_bindir}/*


%changelog
* Wed Dec 23 2009 Frederik Himpe <fhimpe@mandriva.org> 1:0.20091031-1mdv2010.1
+ Revision: 481840
- update to new version 0.20091031

* Sun Sep 27 2009 trem <trem@mandriva.org> 1:0.20090831-1mdv2010.0
+ Revision: 449941
- update to 20090831

* Wed Jul 01 2009 trem <trem@mandriva.org> 1:0.20090630-1mdv2010.0
+ Revision: 391374
- update to 20090630

* Tue May 26 2009 trem <trem@mandriva.org> 1:0.20090430-1mdv2010.0
+ Revision: 380028
- update to 20090430

* Wed Feb 04 2009 trem <trem@mandriva.org> 1:0.20090131-1mdv2009.1
+ Revision: 337606
- add zip as BuildRequires
- update to 20090131

* Thu Nov 13 2008 trem <trem@mandriva.org> 1:0.20081031-1mdv2009.1
+ Revision: 302823
- update to 20081031

* Mon Sep 08 2008 trem <trem@mandriva.org> 1:0.20080831-1mdv2009.0
+ Revision: 282825
- add patch fix_dirent_h.patch that change #include <linux/dirent.h> to #include <dirent.h>
- update to 20080831

* Thu Jul 31 2008 trem <trem@mandriva.org> 1:0.20080731-1mdv2009.0
+ Revision: 258519
- update to 20080731

* Thu Jul 10 2008 trem <trem@mandriva.org> 1:0.20080630-1mdv2009.0
+ Revision: 233602
- add patch to fix the compilation of hackbench
- update to 20080630
- update to 20080331

* Sat Mar 01 2008 trem <trem@mandriva.org> 1:0.20080229-1mdv2008.1
+ Revision: 177033
- update to 20080229

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix description-line-too-long

* Sat Feb 09 2008 trem <trem@mandriva.org> 1:0.20080131-1mdv2008.1
+ Revision: 164602
- update to 20080131

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 29 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:0.20070731-1mdv2008.0
+ Revision: 74607
- Updated to 20070731.
- Added needed BuildRequires for glibc-static-devel.
- Move ChangeLog to _libdir/ltp, it's required by runltp.

* Thu May 03 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:0.20070430-1mdv2008.0
+ Revision: 22040
- Updated to release 20070430.


* Thu Jul 14 2005 Frederic Lepied <flepied@mandriva.com> 20050707-1mdk
- New release 20050707

* Wed Mar 09 2005 Frederic Lepied <flepied@mandrakesoft.com> 20050307-1mdk
- New release 20050307

* Fri Feb 11 2005 Frederic Lepied <flepied@mandrakesoft.com> 20050207-1mdk
- New release 20050207

* Thu Jan 13 2005 Frederic Lepied <flepied@mandrakesoft.com> 20050107-1mdk
- New release 20050107

* Thu Dec 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.20041203-3mdk
- Remove all perl requires as well, since it comes with all required modules
  bundled in a private directory.

* Thu Dec 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.20041203-2mdk
- Do not provide any perl module, since they're not installed in the standard
  location (@INC)

* Thu Dec 16 2004 Mandrakelinux Team <http://www.mandrakeexpert.com> 20041203-1mdk
- New release 20041203

* Sun Feb 15 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.20040206-1mdk
- 2004/02/06 version

* Sun Nov 09 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.20031002-1mdk
- 20031002
- Add test scripts directory in the rpm package
- Add the full testcases directory because some needed files were missing
- Remove execution of IDcheck.sh from the Makefile

* Tue May 06 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.20030404-2mdk
- rebuild

* Mon May 05 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.20030404-1mdk
- 20030404

* Mon May 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.20030206-2mdk
- buildrequires

* Fri Feb 07 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.20030206-1mdk
- 20030206

* Wed Jan 15 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.20030110-1mdk
- 20030110

* Mon Oct 14 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.20021008-1mdk
- 20021008

* Mon Oct 14 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 20021008-1mdk
- fix version

* Wed Oct 09 2002 Lenny Cartier <lenny@mandrakesoft.com> 10.08.02-1mdk
- 10.08.02

* Wed Sep 11 2002 Lenny Cartier <lenny@mandrakesoft.com> 9.10.02-1mdk
- 9.10.02

* Thu Jul 11 2002 Lenny Cartier <lenny@mandrakesoft.com> 7.9.02-1mdk
- 7.9.02

* Tue Jun 11 2002 Lenny Cartier <lenny@mandrakesoft.com> 0-0.20020607.1mdk
- 20020607

* Fri Jan 11 2002 Lenny Cartier <lenny@mandrakesoft.com> 0-0.20020108.1mdk
- 20020108

* Fri Dec 07 2001 Lenny Cartier <lenny@mandrakesoft.com> 0-0.20011206.1mdk
- updated to 20011206
- move manpages

* Wed Sep 26 2001 Frederic Lepied <flepied@mandrakesoft.com> 0-0.20010925.1mdk
- first Mandrake Linux version

