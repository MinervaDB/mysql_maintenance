Name: mysql_maintenance
Version: 0.2
Release: 2%{?dist}
Summary: mySQL maintenance tools.
Group: Applications/System
License: GNU v3
URL: https://github.com/Oneiroi/mysql_maintenance
Source0: https://github.com/downloads/Oneiroi/mysql_maintenance/%{name}-%{version}-%{release}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

Requires: python,MySQL-python
BuildRequires: python-sphinx
Provides: myisam_defrag

%description

Provides tools to aid in the maintenance of MySQL servers.

%prep

%setup -q

%build

cd $RPM_BUILD_DIR/%{name}-%{version}/docs/


%install
[[ -d "$RPM_BUILD_ROOT" ]] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man7
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8

install -D $RPM_BUILD_DIR/%{name}-%{version}/myisam_defrag.py $RPM_BUILD_ROOT%{_bindir}/myisam_defrag
install -D $RPM_BUILD_DIR/%{name}-%{version}/myisam_defrag.conf.7 $RPM_BUILD_ROOT%{_mandir}/man7/myisam_defrag.conf.7
install -D $RPM_BUILD_DIR/%{name}-%{version}/myisam_defrag.8 $RPM_BUILD_ROOT%{_mandir}/man8/myisam_defrag.8
install -D $RPM_BUILD_DIR/%{name}-%{version}/myisam_defrag.conf $RPM_BUILD_ROOT%{_sysconfdir}/myisam_defrag.conf

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%attr(700, root, root) %{_bindir}/myisam_defrag.py
%doc %{_mandir}/man7/myisam_defrag.conf.7.gz
%doc %{_mandir}/man8/myisam_defrag.8.gz
%config %{_sysconfdir}/myisam_defrag.conf

%changelog

* Fri Jan 27 2012 David Busby <oneiroi@fedoraprohect.org> - 0.2-2
- bugfix #6f4b41b - small tables would be missed due to DATA_LENGTH >= (1024*1024) in initial SQL
  since changed to (DATA_LENGTH > 0 OR DATA_FREE > 0) to catch recently truncated tables aswell as generally small ones.

* Thu Sep 28 2010 David Busby <d.busby@saiweb.co.uk> - 0.2-1
- Initial verison for packaging, 0.1 was never officialy tagged


