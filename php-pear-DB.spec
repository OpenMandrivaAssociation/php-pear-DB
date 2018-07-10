%define _class	DB
%define	modname	%{_class}

Summary:	Database Abstraction Layer
Name:		php-pear-%{modname}
Version:	1.8.2
Release:	3
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/%{modname}
Source0:	http://download.pear.php.net/package/DB-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun): php-pear
Requires:	php-pear

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
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/doc/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{modname}.xml
