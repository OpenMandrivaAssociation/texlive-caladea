%global tl_name caladea
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for the Caladea family of fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/caladea
License:	apache2 lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/caladea.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/caladea.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Caladea family of fonts, designed by Carolina Giovagnoli and Andres
Torresi of the Huerta Tipografica foundry and adopted by Google for
ChromeOS as a font-metric compatible replacement for Cambria.

