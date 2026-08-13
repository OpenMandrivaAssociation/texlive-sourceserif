%global tl_name sourceserif
%global tl_revision 79618
%global tl_version 2.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Use Source Serif with TeX(-alike) systems
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/sourceserif
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sourceserif.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sourceserif.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides Source Serif for LaTeX. It includes both Type1 and
OpenType fonts and selects the latter when using XeLaTeX or LuaLaTeX.
This package used to be called "sourceserifpro" and contains an alias
package for backwards compatibility.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from sourceserif:
Map SourceSerifFour.map
TL_DROPIN_EOF
