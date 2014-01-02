%define	upstream_name	 B-Keywords
%define upstream_version 1.13

Summary:	Lists of reserved barewords and symbol names
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/B/B-Keywords-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
B::Keywords supplies seven arrays of keywords:	@Scalars, @Arrays,
@Hashes, @Filehandles, @Symbols, @Functions, and @Barewords. The
@Symbols array includes the contents of each of @Scalars, @Arrays,
@Hashes, and @Filehandles. Similarly, @Barewords adds a few
non-function keywords and operators to the @Functions array.

All additions and modifications are welcome.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%check
make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{perl_vendorlib}/B
%{_mandir}/man3/*


