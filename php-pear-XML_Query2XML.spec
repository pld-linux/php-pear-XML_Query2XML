%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	XML_Query2XML
Summary:	%{_pearname} - Creates XML data from SQL queries
Summary(pl.UTF-8):	%{_pearname} - Tworzenie danych XML na podstawie zapytań SQL
Name:		php-pear-%{_pearname}
Version:	1.7.1
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0d669e5326401bcd257b3954500fd79d
URL:		http://pear.php.net/package/XML_Query2XML/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:5.0.0
Requires:	php-pear
Suggests:	php-pear-I18N_UnicodeString
Suggests:	php-pear-MDB2
Suggests:	php-pear-Net_LDAP2
Obsoletes:	php-pear-XML_Query2XML-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(DB.*)' 'pear(MDB2.*)' 'pear(I18N/UnicodeString.*)' pear(Net/LDAP2.*)

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

%description -l pl.UTF-8
XML_Query2XML pozwala na przetworzenie rekordów uzyskanych z jednego
lub więcej zapytań SQL SELECT na dane XML. Wspierane są różne rodzaje
transformacji - od prostych do bardzo złożonych. Pakiet został
napisany z myślą o wydajności - może obsłużyć duże ilości danych. XSLT
nie jest potrzebne!

Główne cechy:
- XML_Query2XML współpracuje z klasami dostarczonymi przez
  rozszerzenie DOM XML PHP5,
- do prostych zadań potrzebny jest minimalny nakład sił,
- wysoce konfigurowalny dla złożonych zadań,
- wsparcie dla ISO/IEC 9075-14:2005: mapowanie identyfikatorów SQL do
  nazw XML,
- współpracuje z bazami danych wspieranymi przez PEAR DB lub PEAR
  MDB2,
- możliwość 'odpluskwiania' i logowania,
- dostarcza możliwość profilowania,
- rozbudowana dokumentacja: przewodnik oraz opis API,
- osiem studiów przypadku: od prostych do bardzo złożonych
  scenariuszy,
- 168 testów dla PHPUnit2.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/XML/Query2XML
