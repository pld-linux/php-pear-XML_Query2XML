%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Query2XML
%define		_status		beta
%define		_pearname	XML_Query2XML

Summary:	%{_pearname} - Creates XML data from SQL queries
Summary(pl):	%{_pearname} - Tworzenie danych XML na podstawie zapytañ SQL
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	1
Epoch:		0
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	92e2ce590f9ba3bc832a6bcffe8d5c52
URL:		http://pear.php.net/package/XML_Query2XML/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:5.0.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_Query2XML allows you to transform the records retrieved with one
or more SQL SELECT queries into XML data. Very simple to highly
complex transformations are supported. Is was written with performance
in mind and can handle large amounts of data. No XSLT needed!

Major features:
- XML_Query2XML works with the classes provided by PHP5's DOM XML
  extension
- minimum effort necessary to get the simple jobs done
- highly configurable for more complex tasks
- ISO/IEC 9075-14:2005 support: mapping of SQL identifiers to XML
  names
- works with any database that is supported by PEAR DB or PEAR MDB2
- debugging and logging features
- provides profiling features
- in-depth documentation: tutorials and API documentation
- Eight case studies: from very simple to highly complex scenarios
- 168 unit tests for PHPUnit2

In PEAR status of this package is: %{_status}.

%description -l pl
XML_Query2XML pozwala na przetworzenie rekordów uzyskanych z jednego
lub wiêcej zapytañ SQL SELECT na dane XML. Wspierane s± ró¿ne rodzaje
transformacji - od prostych do bardzo z³o¿onych. Pakiet zosta³
napisany z my¶l± o wydajno¶ci - mo¿e obs³u¿yæ du¿e ilo¶ci danych. XSLT
nie jest potrzebne!

G³ówne cechy:
- XML_Query2XML wspó³pracuje z klasami dostarczonymi przez
  rozszerzenie DOM XML PHP5,
- do prostych zadañ potrzebny jest minimalny nak³ad si³,
- wysoce konfigurowalny dla z³o¿onych zadañ,
- wsparcie dla ISO/IEC 9075-14:2005: mapowanie identyfikatorów SQL do
  nazw XML,
- wspó³pracuje z bazami danych wspieranymi przez PEAR DB lub PEAR
  MDB2,
- mo¿liwo¶æ 'odpluskwiania' i logowania,
- dostarcza mo¿liwo¶æ profilowania,
- rozbudowana dokumentacja: przewodnik oraz opis API,
- osiem studiów przypadku: od prostych do bardzo z³o¿onych
  scenariuszy,
- 168 testów dla PHPUnit2.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/Query2XML.php
%dir %{php_pear_dir}/XML/Query2XML
%{php_pear_dir}/XML/Query2XML/ISO9075Mapper.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/XML_Query2XML
