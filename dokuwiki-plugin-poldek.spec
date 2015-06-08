%define		plugin		poldek
Summary:	DokuWiki poldek Plugin
Summary(pl.UTF-8):	Wtyczka Include (dołączania) dla poldek
Name:		dokuwiki-plugin-%{plugin}
Version:	20130610
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/glensc/dokuwiki-plugin-poldek/archive/%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	82625a9f8fdcc6c2baaa8391847e0b04
URL:		https://github.com/glensc/dokuwiki-plugin-poldek
Requires:	dokuwiki >= 20080505
Requires:	poldek
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		_sysconfdir	/etc/webapps/dokuwiki
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
Plugin to display package NVR from repository.

{{poldek>PKGNAME}} is the syntax.

%prep
%setup -q

version=$(awk '/date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{plugindir},%{_sysconfdir}}
cp -a . $RPM_BUILD_ROOT%{plugindir}
mv $RPM_BUILD_ROOT{%{plugindir},%{_sysconfdir}}/poldek.conf

%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/poldek.conf
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.txt
%{plugindir}/conf
