#
# Conditional build:
%bcond_without  doc             # don't build doc
%bcond_without  tests   # do not perform "make test"
%bcond_without  python2 # CPython 2.x module
%bcond_without  python3 # CPython 3.x module

%define 	module	pyquery
Summary:	A jquery-like library for Python
Summary(pl.UTF-8):	Podobna do jquery biblioteka dla Pythona
Name:		python-%{module}
Version:	1.2.9
Release:	5
License:	BSD
Group:		Development/Languages/Python
# Source0:	http://pypi.python.org/packages/source/p/pyquery/%{module}-%{version}.tar.gz
Source0:	https://github.com/gawel/pyquery/archive/%{version}.tar.gz
# Source0-md5:	902e2ded38899c7c3f66cba6d4a464fb
URL:		http://pypi.python.org/pypi/pyquery
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-WebOb
BuildRequires:	python-cssselect
BuildRequires:	python-webtest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-WebOb
BuildRequires:	python3-cssselect
BuildRequires:	python3-webtest
%endif
%endif
Requires:	python-cssselect
Requires:	python-lxml
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyquery allows you to make jquery queries on xml documents. The API is
as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

%description -l pl.UTF-8
Pyquery pozwala na wykonywanie zapytań jquery na dokumentach XML.
Interfejs jest jak to tylko możliwe podobny do jquery. Pyquery używa
lxml do szybkiej manipulacji plików XML i HTML.

%package -n python3-%{module}
Summary:	A jquery-like library for Python
Summary(pl.UTF-8):	Podobna do jquery biblioteka dla Pythona
Group:		Libraries/Python
Requires:	python3-cssselect
Requires:	python3-lxml
Requires:	python3-modules

%description -n python3-%{module}
Pyquery allows you to make jquery queries on xml documents. The API is
as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

%description -n python3-%{module} -l pl.UTF-8
Pyquery pozwala na wykonywanie zapytań jquery na dokumentach XML.
Interfejs jest jak to tylko możliwe podobny do jquery. Pyquery używa
lxml do szybkiej manipulacji plików XML i HTML.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/pyquery-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
