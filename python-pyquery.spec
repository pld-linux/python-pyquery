%define 	module	pyquery
Summary:	A jquery-like library for Python
Summary(pl.UTF-8):	Podobna do jquery biblioteka dla Pythona
Name:		python-%{module}
Version:	1.2.1
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/p/pyquery/%{module}-%{version}.tar.gz
# Source0-md5:	f4564c372e3905772d0fe094bc00baf6
URL:		http://pypi.python.org/pypi/pyquery
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-cssselect
Requires:	python-lxml
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyquery allows you to make jquery queries on xml documents. The API is
as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

%description -l pl.UTF-8
Pyquery pozwala na wykonywanie zapytań jquery na dokumentach XML.
Interfejs jest jak to tylko możliwe podobny do jquery. Pyquery używa lxml
do szybkiej manipulacji plików XML i HTML.

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir} $RPM_BUILD_ROOT%{_libdir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/pyquery-*.egg-info
%endif
