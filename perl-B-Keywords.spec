%define upstream_name B-Keywords
%define upstream_version 1.29

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1
Summary:	Lists of reserved barewords and symbol names
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/rurban/b-keywords
Source0:	https://cpan.metacpan.org/authors/id/R/RU/RURBAN/B-Keywords-%{upstream_version}.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildArch:	noarch

%description
B::Keywords supplies seven arrays of keywords: @Scalars, @Arrays,
@Hashes, @Filehandles, @Symbols, @Functions, and @Barewords. The
@Symbols array includes the contents of each of @Scalars, @Arrays,
@Hashes, and @Filehandles. Similarly, @Barewords adds a few
non-function keywords and operators to the @Functions array.

All additions and modifications are welcome.

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor

%check
make test

%install
%make_install

%files
%doc Changes README LICENSE
%{perl_vendorlib}/B
%doc %{_mandir}/man*/*
