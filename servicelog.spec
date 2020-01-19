Name:           servicelog
Version:        1.1.11
Release:        1%{?dist}
Summary:        Servicelog Tools

Group:          System Environment/Base
License:        GPLv2
URL:            http://linux-diag.sourceforge.net/servicelog
Source0:        http://downloads.sourceforge.net/linux-diag/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#Requires(pre):       shadow-utils

BuildRequires:  libservicelog-devel >= 1.1.9-2
BuildRequires:  autoconf libtool librtas-devel help2man

# because of librtas-devel in libservicelog
ExclusiveArch: ppc ppc64

%description
Command-line interfaces for viewing and manipulating the contents of
the servicelog database. Contains entries that are useful
for performing system service operations, and for providing a history
of service operations that have been performed on the system.

%prep
%setup -q

%build
autoreconf -fiv
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
help2man -s 8 -N $RPM_BUILD_ROOT/%{_sbindir}/slog_common_event > $RPM_BUILD_ROOT/%{_mandir}/man8/slog_common_event.8

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/servicelog
%{_bindir}/v1_servicelog
%{_bindir}/v29_servicelog
%{_bindir}/servicelog_notify
%{_bindir}/log_repair_action
%{_sbindir}/slog_common_event
%{_bindir}/servicelog_manage
%{_mandir}/man[18]/*.[18]*

%changelog
* Tue May 21 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.1.11
- Update to latest upstream 1.1.11

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 08 2012 Karsten Hopp <karsten@redhat.com> 1.1.10-1
- update to servicelog-1.1.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 09 2011 Jiri Skala <jskala@redhat.com> - 1.1.9-1
- update to latest upstream 1.1.9

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 16 2010 Roman Rakus <rrakus@redhat.com> - 1.1.7-2
- Generate missing man page from help (help2man)

* Tue May 18 2010 Roman Rakus <rrakus@redhat.com> - 1.1.7-1
- Initial packaging

