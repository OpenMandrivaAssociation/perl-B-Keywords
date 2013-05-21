%define	upstream_name	 B-Keywords
%define	upstream_version 1.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Lists of reserved barewords and symbol names
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/B/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor

%check
make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{perl_vendorlib}/B
%{_mandir}/man*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.100.0-4mdv2012.0
+ Revision: 765076
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.100.0-3
+ Revision: 763492
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.100.0-2
+ Revision: 676618
- rebuild

* Tue Oct 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 586764
- new version

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-1mdv2011.0
+ Revision: 402140
- rebuild using %%perl_convert_version
- rebuild using %%perl_convert_version

* Wed Mar 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-1mdv2009.1
+ Revision: 353644
- update to new version 1.09

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.08-3mdv2009.0
+ Revision: 255468
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdv2008.1
+ Revision: 97369
- update to new version 1.08


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2007.0
+ Revision: 133727
- new version

* Tue Feb 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2007.1
+ Revision: 120303
- fix build dependencies

* Mon Feb 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2007.1
- first mdv release

