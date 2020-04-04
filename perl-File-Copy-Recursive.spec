%{?scl:%scl_package perl-File-Copy-Recursive}

Name: 		%{?scl_prefix}perl-File-Copy-Recursive
Version: 	0.45
Release: 	2%{?dist}
Summary: 	Extension for recursively copying files and directories 
License: 	GPL+ or Artistic
URL: 		https://metacpan.org/release/File-Copy-Recursive
Source0: 	https://cpan.metacpan.org/modules/by-module/File/File-Copy-Recursive-%{version}.tar.gz
BuildArch: noarch

Requires:  %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
# rpm's perl dep generators fails to catch this
Requires:  %{?scl_prefix}perl(File::Glob)

BuildRequires:  make

BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Glob)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(Path::Tiny)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
BuildRequires:  %{?scl_prefix}perl(Test::Deep)
BuildRequires:  %{?scl_prefix}perl(Test::Fatal)
BuildRequires:  %{?scl_prefix}perl(Test::File)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(Test::Warnings)

%description
This module copies and moves directories recursively to an optional depth and
attempts to preserve each file or directory's mode.

%prep
%setup -q -n File-Copy-Recursive-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
chmod -R u+w %{buildroot}/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes README
%{perl_vendorlib}/File
%{_mandir}/man3/*

%changelog
* Fri Jan 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-2
- SCL

* Wed Jul 24 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.45-1
- Update to 0.45.

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-2
- Perl 5.28 rebuild

* Mon May 14 2018 Tom Callaway <spot@fedoraproject.org> - 0.44-1
- update to 0.44

* Fri Mar 23 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.40-3
- Remove Path:Iter (RHBZ#1558427).
- Spec file cosmetics.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.40-1
- Update to 0.40.

* Thu Jan 11 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.39-1
- Update to 0.39.
- Modernize *.spec.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-25
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-23
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.38-21
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-19
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-18
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.38-15
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 31 2012 Petr Šabata <contyk@redhat.com> - 0.38-13
- Modernize spec, drop command macros, and fix dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 0.38-11
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.38-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.38-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.38-6
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.38-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.38-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 13 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.38-1
- Upstream update.

* Fri Oct 10 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.37-1
- Upstream update.

* Wed Apr 23 2008 Ralf Corsépius <rc040203@freenet.de> - 0.36-1
- Upstream update.

* Sat Feb  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.35-2
- rebuild for new perl

* Wed Aug 29 2007 Ralf Corsépius <rc040203@freenet.de> - 0.35-1
- Upstream update.

* Mon May 14 2007 Ralf Corsépius <rc040203@freenet.de> - 0.33-2
- BR: perl(Test::More).

* Mon May 14 2007 Ralf Corsépius <rc040203@freenet.de> - 0.33-1
- Upstream update.

* Mon Mar 12 2007 Ralf Corsépius <rc040203@freenet.de> - 0.31-2
- BR: perl(ExtUtils::MakeMaker).

* Fri Mar 02 2007 Ralf Corsépius <rc040203@freenet.de> - 0.31-1
- Upstream update.

* Thu Jan 18 2007 Ralf Corsépius <rc040203@freenet.de> - 0.30-2
- Cosmetics.

* Wed Jan 17 2007 Ralf Corsépius <rc040203@freenet.de> - 0.30-1
- Initial Fedora submission.
