%define upstream_name    Pod-Markdown
%define upstream_version 2.000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Convert POD to Markdown
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/Pod-Markdown-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Pod::Parser)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(parent)
BuildArch:	noarch

%description
This module subclasses the Pod::Parser manpage and converts POD to
Markdown.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml META.json README
%{_bindir}/pod2markdown
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.730-1mdv2011.0
+ Revision: 672859
- update to new version 1.110730

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.103.491-2
+ Revision: 657826
- rebuild for updated spec-helper

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.103491

* Mon Mar 29 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.860-1mdv2011.0
+ Revision: 528818
- import perl-Pod-Markdown


* Mon Mar 29 2010 cpan2dist 1.100860-1mdv
- initial mdv release, generated with cpan2dist



