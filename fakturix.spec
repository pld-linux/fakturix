Summary:	fakturiX - software for invoicing
Summary(pl.UTF-8):   fakturiX - program do wystawiania faktur
Name:		fakturix
Version:	0.0.3
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/fakturix/%{name}-%{version}.tar.bz2
# Source0-md5:	1f4e0e5520f8c07faf68e0ace0424900
URL:		http://fakturix.sourceforge.net/
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fakturiX is software for issuing invoices.
 
%description -l pl.UTF-8
fakturiX jest programem do wystawiania faktur.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README sql/create.sql
%attr(755,root,root) %{_bindir}/%{name}
%{_pixmapsdir}/%{name}
