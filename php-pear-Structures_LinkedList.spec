%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	LinkedList
%define		_status		beta
%define		_pearname	Structures_LinkedList

Summary:	%{_pearname} - Implements singly and doubly-linked lists
Summary(pl.UTF-8):	%{_pearname} - implementacja jedno- i dwukierunkowych list
Name:		php-pear-%{_pearname}
Version:	0.2.2
Release:	2
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e693c54ff0d812e7c91197d1108f3fa4
URL:		http://pear.php.net/package/Structures_LinkedList/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Structures_LinkedList-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A singly-linked list offers the ability to insert or delete nodes at
any point within the list. A doubly-linked list also offers the
ability to request previous nodes in the list.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Lista jednokierunkowych pozwala na wstawienie lub usunięcie elementów
w dowolnym miejscu listy. Lista dwukierunkowa pozwala także na
pobranie elementu poprzedniego.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
sed -i -e 's#Single.php#%{_class}/%{_subclass}/Single.php#' ./%{php_pear_dir}/%{_class}/%{_subclass}/Double.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Structures_LinkedList/{examples,CHANGELOG}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}
