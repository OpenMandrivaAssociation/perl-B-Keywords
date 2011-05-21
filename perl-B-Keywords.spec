%define	upstream_name	 B-Keywords
%define	upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	Lists of reserved barewords and symbol names
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/B/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
B::Keywords supplies seven arrays of keywords: @Scalars, @Arrays,
@Hashes, @Filehandles, @Symbols, @Functions, and @Barewords. The
@Symbols array includes the contents of each of @Scalars, @Arrays,
@Hashes, and @Filehandles. Similarly, @Barewords adds a few
non-function keywords and operators to the @Functions array.

All additions and modifications are welcome.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{perl_vendorlib}/B
%{_mandir}/man*/*
