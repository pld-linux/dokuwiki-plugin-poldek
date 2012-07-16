%define		plugin		poldek
Summary:	DokuWiki poldek Plugin
Summary(pl.UTF-8):	Wtyczka Include (dołączania) dla poldek
Name:		dokuwiki-plugin-%{plugin}
Version:	20120716
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/glensc/dokuwiki-plugin-poldek/tarball/%{version}/%{plugin}-%{version}.tgz
# Source0-md5:	ce18635deee1d671f4293fe5d8f4dbda
URL:		https://github.com/glensc/dokuwiki-plugin-poldek
Requires:	dokuwiki >= 20080505
Requires:	poldek
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
Plugin to display package NVR from repository.

{{poldek>PKGNAME}} is the syntax.

%prep
%setup -qc
mv *-%{plugin}-*/* .

version=$(awk '/date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.txt
%{plugindir}/conf
