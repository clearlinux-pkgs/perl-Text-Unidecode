#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Unidecode
Version  : 1.30
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/S/SB/SBURKE/Text-Unidecode-1.30.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SB/SBURKE/Text-Unidecode-1.30.tar.gz
Summary  : 'Provide plain ASCII transliterations of Unicode text'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-Unidecode-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
# Time-stamp: "2016-07-24 03:12:31 MDT"
# (This page is in UTF-8!) |Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·Â·|

%package dev
Summary: dev components for the perl-Text-Unidecode package.
Group: Development
Provides: perl-Text-Unidecode-devel = %{version}-%{release}

%description dev
dev components for the perl-Text-Unidecode package.


%package license
Summary: license components for the perl-Text-Unidecode package.
Group: Default

%description license
license components for the perl-Text-Unidecode package.


%prep
%setup -q -n Text-Unidecode-1.30

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Unidecode
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-Unidecode/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x00.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x01.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x02.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x03.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x04.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x05.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x06.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x07.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x08.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x09.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x0a.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x0b.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x0c.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x0d.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x0e.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x0f.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x10.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x11.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x12.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x13.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x14.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x15.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x16.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x17.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x18.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x19.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x1a.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x1b.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x1c.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x1d.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x1e.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x1f.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x20.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x21.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x22.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x23.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x24.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x25.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x26.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x27.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x28.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x29.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x2a.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x2b.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x2c.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x2d.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x2e.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x2f.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x30.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x31.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x32.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x33.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x34.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x35.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x36.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x37.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x38.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x39.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x3a.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x3b.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x3c.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x3d.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x3e.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x3f.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x40.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x41.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x42.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x43.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x44.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x45.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x46.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x47.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x48.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x49.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x4a.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x4b.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x4c.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x4d.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x4e.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x4f.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x50.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x51.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x52.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x53.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x54.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x55.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x56.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x57.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x58.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x59.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x5a.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x5b.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x5c.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x5d.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x5e.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x5f.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x60.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x61.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x62.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x63.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x64.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x65.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x66.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x67.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x68.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x69.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x6a.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x6b.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x6c.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x6d.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x6e.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x6f.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x70.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x71.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x72.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x73.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x74.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x75.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x76.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x77.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x78.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x79.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x7a.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x7b.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x7c.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x7d.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x7e.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x7f.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x80.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x81.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x82.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x83.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x84.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x85.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x86.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x87.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x88.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x89.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x8a.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x8b.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x8c.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x8d.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x8e.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x8f.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x90.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x91.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x92.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x93.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x94.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x95.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x96.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x97.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x98.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x99.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x9a.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x9b.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x9c.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x9d.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x9e.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/x9f.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xa0.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xa1.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xa2.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xa3.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xa4.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xa5.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xa6.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xa7.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xa8.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xa9.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xaa.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xab.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xac.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xad.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xae.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xaf.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xb0.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xb1.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xb2.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xb3.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xb4.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xb5.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xb6.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xb7.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xb8.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xb9.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xba.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xbb.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xbc.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xbd.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xbe.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xbf.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xc0.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xc1.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xc2.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xc3.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xc4.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xc5.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xc6.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xc7.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xc8.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xc9.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xca.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xcb.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xcc.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xcd.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xce.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xcf.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xd0.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xd1.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xd2.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xd3.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xd4.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xd5.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xd6.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xd7.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xd8.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xd9.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xda.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xdb.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xdc.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xdd.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xde.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xdf.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xe0.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xe1.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xe2.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xe3.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xe4.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xe5.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xe6.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xe7.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xe8.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xe9.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xea.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xeb.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xec.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xed.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xee.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xef.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xf0.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xf1.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xf2.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xf3.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xf4.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xf5.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xf6.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xf7.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xf8.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xf9.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xfa.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xfb.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xfc.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xfd.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xfe.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Unidecode/xff.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Unidecode.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Unidecode/LICENSE
