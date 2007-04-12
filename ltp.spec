%define name ltp
%define srcver 20050707
%define release 1mdk

%define _requires_exceptions perl(.*)
%define _provides_exceptions perl(.*)

Summary: Linux Test Project
Name: %{name}
Version: 0.%srcver
Release: %{release}
Epoch: 1
Source0: http://prdownloads.sourceforge.net/ltp/%{name}-full-%{srcver}.tar.bz2
License: GPL
Group: Development/Kernel
Requires: /usr/bin/ar /usr/bin/objdump gcc cdialog /usr/bin/ld /usr/bin/ldd tar
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: flex rsync
Url: http://ltp.sourceforge.net/

%description
The Linux Test Project is a joint project with SGI, IBM, OSDL, and Bull with a
goal to deliver test suites to the open source community that validate the 
reliability, robustness, and stability of Linux. The Linux Test Project is a 
collection of tools for testing the Linux kernel and related features. Our goal 
is to improve the Linux kernel by bring test automation to the kernel testing 
effort. Interested open source contributors are encouraged to join the project.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %name-full-%srcver

%build
perl -p -i -e 's/@\.\/IDcheck\.sh//' Makefile
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_libdir/ltp/testcases/bin
mkdir -p $RPM_BUILD_ROOT%_libdir/ltp/tools
mkdir -p $RPM_BUILD_ROOT%_libdir/ltp/runtest
mkdir -p $RPM_BUILD_ROOT%_libdir/ltp/testscripts
mkdir -p $RPM_BUILD_ROOT%_libdir/ltp/pan/cgi

mkdir -p $RPM_BUILD_ROOT%_mandir/man1/
mkdir -p $RPM_BUILD_ROOT%_mandir/man3/

mkdir -p $RPM_BUILD_ROOT%_bindir

cp -p runltp *.sh $RPM_BUILD_ROOT%_libdir/ltp
cp -p ltpmenu $RPM_BUILD_ROOT%_libdir/ltp
cp -p ver_linux $RPM_BUILD_ROOT%_libdir/ltp
cp -p pan/{bump,pan,scanner} $RPM_BUILD_ROOT%_libdir/ltp/pan
cp -p pan/cgi/*.cgi $RPM_BUILD_ROOT%_libdir/ltp/pan/cgi
cp -p runtest/[a-z]* $RPM_BUILD_ROOT%_libdir/ltp/runtest
cp -p testscripts/*.sh $RPM_BUILD_ROOT%_libdir/ltp/testscripts

cp -p $RPM_BUILD_DIR/%name-full-%srcver/doc/man1/* $RPM_BUILD_ROOT%_mandir/man1/
cp -p $RPM_BUILD_DIR/%name-full-%srcver/doc/man3/* $RPM_BUILD_ROOT%_mandir/man3/

perl -p -i -e 's/whoami.*/true/' `find . -name \*.sh`
find testcases -type f | xargs perl -p -i -e 's@/usr/local/bin/perl5@/usr/bin/perl@'

%makeinstall

#tar c `find testcases/bin -type f | fgrep -v CVS` | tar x -C $RPM_BUILD_ROOT%_libdir/ltp
rsync -ar --exclude="*.c" --exclude="*.h" --exclude=Makefile tools/ $RPM_BUILD_ROOT%_libdir/ltp/tools
rsync -ar --exclude="*.c" --exclude="*.h" --exclude=Makefile testcases/ $RPM_BUILD_ROOT%_libdir/ltp/testcases

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog CREDITS doc/*.txt
%doc doc/examples doc/*.lyx
%doc doc/testcases
%_bindir/*
%_libdir/ltp
%_mandir/man1/*
%_mandir/man3/*

