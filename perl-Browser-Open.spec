#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Browser
%define		pnam	Open
Summary:	Browser::Open - open a browser in a given URL
Summary(pl.UTF-8):	Browser::Open - otwieranie przeglądarki z podanym URL-em
Name:		perl-Browser-Open
Version:	0.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CF/CFRANKS/Browser-Open-%{version}.tar.gz
# Source0-md5:	4cb43edda495ca86869778246da89dd8
URL:		http://search.cpan.org/dist/Browser-Open/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.92
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The functions optionaly exported by this module allows you to open
URLs in the user browser.

A set of known commands per OS-name is tested for presence, and the
first one found is executed.

%description -l pl.UTF-8
Funkcje opcjonalnie udostępniane przez ten moduł pozwalają na
otwieranie URL-i w przeglądarce użytkownika.

Zbiór znanych poleceń dla poszczególnych systemów operacyjnych jest
sprawdzany pog kątem istnienia i wykonywane jest pierwsze znalezione
polecenie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Browser
%{perl_vendorlib}/Browser/Open.pm
%{_mandir}/man3/Browser::Open.3pm*
