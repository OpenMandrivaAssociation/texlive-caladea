Name:		texlive-caladea
Version:	64549
Release:	2
Summary:	Support for the Caladea family of fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/caladea
License:	apache2 lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/caladea.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/caladea.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Caladea family of fonts, designed by Carolina
Giovagnoli and Andres Torresi of the Huerta Tipografica foundry
and adopted by Google for ChromeOS as a font-metric compatible
replacement for Cambria.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/caladea
%{_texmfdistdir}/fonts/vf/huerta/caladea
%{_texmfdistdir}/fonts/type1/huerta/caladea
%{_texmfdistdir}/fonts/truetype/huerta/caladea
%{_texmfdistdir}/fonts/tfm/huerta/caladea
%{_texmfdistdir}/fonts/map/dvips/caladea
%{_texmfdistdir}/fonts/enc/dvips/caladea
%doc %{_texmfdistdir}/doc/fonts/caladea

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
