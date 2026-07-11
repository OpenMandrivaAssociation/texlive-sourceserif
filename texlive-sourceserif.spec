%global tl_name sourceserif
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Use Source Serif with TeX(-alike) systems
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/sourceserif
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sourceserif.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sourceserif.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides Source Serif for LaTeX. It includes both Type1 and
OpenType fonts and selects the latter when using XeLaTeX or LuaLaTeX.
This package used to be called "sourceserifpro" and contains an alias
package for backwards compatibility.

