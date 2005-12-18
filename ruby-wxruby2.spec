#
%define	_pnam	wxruby2
%define	_rel	0.1
%define _cvs	20051218	
#
Summary:	Ruby bindings for wxWidgets
Name:		ruby-%{_pnam}
Version:	0.3.0
Release:	0.%{_cvs}.%{_rel}
License:	distributable
Group:		X11/Libraries
Source0:	http://twittner.host.sk/files/wxruby2/%{_pnam}-%{version}-cvs-%{_cvs}.tar.gz
# Source0-md5:	a994011d0da5c684891c61664068df56
#Patch0:	%{name}-DESTDIR.patch # not used for now
Patch1:		%{name}-wx-config.patch
Patch2:		%{name}-FLAGS.patch
URL:		http://wxruby.rubyforge.org/
BuildRequires:	rake
BuildRequires:	ruby
BuildRequires:	wxWidgets-devel >= 2.6.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby bindings for wxWidgets.

%package examples
Summary:	Ruby bindings for wxWidgets examples
Group:		X11/Libraries

%description examples
Ruby bindings for wxWidgets examples.

%prep
%setup -q -n %{_pnam}
#patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CXXFLAGS="%{rpmcxxflags}" rake

%install
rm -rf $RPM_BUILD_ROOT

# `rake install' is broken - puts both wx.rb and wxruby2.so in ruby_sitearchdir
install -d $RPM_BUILD_ROOT/%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT{%{ruby_sitelibdir},%{ruby_sitearchdir}}

install lib/wx.rb $RPM_BUILD_ROOT%{ruby_sitelibdir}
install lib/wxruby2.so $RPM_BUILD_ROOT%{ruby_sitearchdir}

cp -R samples/* $RPM_BUILD_ROOT/%{_examplesdir}/%{name}-%{version} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog LICENSE README TODO
%{ruby_sitelibdir}/*
%{ruby_sitearchdir}/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
