%define		_class		    DB
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.7.13
Release:	7
Summary:	Database Abstraction Layer
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/%{upstream_name}
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch

%description
DB is a database abstraction layer providing:
* an OO-style query API
* portability features that make programs written for one DBMS work with other
  DBMS's
* a DSN (data source name) format for specifying database servers
* prepare/execute (bind) emulation for databases that don't support it natively
* a result object for each query response
* portable error codes
* sequence emulation
* sequential and non-sequential row fetching as well as bulk fetching
* formats fetched rows as associative arrays, ordered arrays or objects
* row limit support
* transactions support
* table information interface
* DocBook and phpDocumentor API documentation

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/doc/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7.13-4mdv2011.0
+ Revision: 667491
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7.13-3mdv2011.0
+ Revision: 607094
- rebuild

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.13-2mdv2010.1
+ Revision: 479284
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Sep 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.13-1mdv2010.0
+ Revision: 450205
- import php-pear-DB


* Fri Sep 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.13-1mdv2010.0
- split out from php-pear package
