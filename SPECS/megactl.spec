Summary:	LSI megaraid adapters status tracker
Name:		megactl
Version:	0.4.1
Release:	10%{?dist}
License:	GPL
Group:		Applications/System
URL:		http://sourceforge.net/projects/megactl
Source0:	http://downloads.sourceforge.net/megactl/%{name}-%{version}.tar.gz
Source1:	megactl.sh
Source2:	megasasctl.sh
Source3:	megatrace.sh
Source4:	create-devices-nodes
Source5:	megactl-cron
Source6:	megasasctl-cron
Source7:	megactl.cron
Source8:	megactl-cron.conf
Source9:	megasasctl.cron
Source10:	megasasctl-cron.conf
Source11:	megactl.8
Source12:	megasasctl.8
Source13:	megatrace.8
Source14:	README.Mandriva
Patch0:		megactl-0.4.1.patch
Patch1:		megactl-x86_64.patch
Requires:	mailx
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This project is a small collection of programs for examining configuration and
status of LSI megaraid adapters, especially Dell PERC RAID adapters, and
attached storage devices.

%prep

%setup -q
%patch0 -p1
%patch1 -p1

cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .
cp %{SOURCE5} .
cp %{SOURCE6} .
cp %{SOURCE7} .
cp %{SOURCE8} .
cp %{SOURCE9} .
cp %{SOURCE10} .
cp %{SOURCE11} .
cp %{SOURCE12} .
cp %{SOURCE13} .
cp %{SOURCE14} .

%build
cd src
make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/cron.d
install -d %{buildroot}%{_sysconfdir}/megactl
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_datadir}/megactl
install -d %{buildroot}%{_mandir}/man8

install -m0755 megactl.sh %{buildroot}%{_sbindir}/megactl
install -m0755 megasasctl.sh %{buildroot}%{_sbindir}/megasasctl
install -m0644 create-devices-nodes %{buildroot}%{_datadir}/megactl/
install -m0755 megactl-cron %{buildroot}%{_datadir}/megactl/megactl-cron
install -m0755 megasasctl-cron %{buildroot}%{_datadir}/megactl/megasasctl-cron
install -m0644 megactl.cron %{buildroot}%{_sysconfdir}/cron.d/megactl
install -m0644 megasasctl.cron %{buildroot}%{_sysconfdir}/cron.d/megasasctl
install -m0644 megactl-cron.conf %{buildroot}%{_sysconfdir}/megactl/megactl-cron.conf
install -m0644 megasasctl-cron.conf %{buildroot}%{_sysconfdir}/megactl/megasasctl-cron.conf
install -m0755 src/megactl %{buildroot}%{_sbindir}/megactl.real
install -m0755 src/megasasctl %{buildroot}%{_sbindir}/megasasctl.real
install -m0644 megactl.8 %{buildroot}%{_mandir}/man8/
install -m0644 megasasctl.8 %{buildroot}%{_mandir}/man8/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHOR COPYING README README.Mandriva
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/megactl
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/megasasctl
%dir %{_sysconfdir}/megactl
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/megactl/megactl-cron.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/megactl/megasasctl-cron.conf
%attr(0755,root,root) %{_sbindir}/*
%dir %{_datadir}/megactl
%attr(0644,root,root) %{_datadir}/megactl/create-devices-nodes
%attr(0755,root,root) %{_datadir}/megactl/megactl-cron
%attr(0755,root,root) %{_datadir}/megactl/megasasctl-cron
%attr(0644,root,root) %{_mandir}/man8/*


%changelog
* Sun Nov 06 2016 h0tw1r3 <h0tw1r3@noreply.github.com>
- support 64-bit, remove megatrace (32 bit only)

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-9mdv2011.0
+ Revision: 620317
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.4.1-8mdv2010.0
+ Revision: 430014
- rebuild

* Tue Sep 02 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-7mdv2009.0
+ Revision: 279086
- fix deps (it needs /bin/mail)

* Wed Aug 27 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-6mdv2009.0
+ Revision: 276618
- added a patch from gentoo to make it build
- added lots of changes by acecile@mandriva.com

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Fri Feb 01 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.1-2mdv2008.1
+ Revision: 161130
- install under %%{_sbindir}, not %%{_bindir}

* Thu Jan 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.1-1mdv2008.1
+ Revision: 160750
- import megactl


* Thu Jan 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.1-1mdv2008.1
- first mdv release  
