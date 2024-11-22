class Unatica < Formula
  include Language::Python::Virtualenv

  desc "A Safe and Simple macOS App Uninstaller"
  homepage "https://github.com/benjame/unatica"
  url "https://github.com/benjame/unatica/archive/refs/tags/v0.0.1.tar.gz"
  sha256 "YOUR_TARBALL_SHA256"
  license "Apache-2.0"

  depends_on "python@3.12"

  resource "rich" do
    url "https://files.pythonhosted.org/packages/source/r/rich/rich-13.7.0.tar.gz"
    sha256 "5cb5123b5cf9ee70584244246816e9114227e0b98ad9176eede6ad54bf5403fa"
  end

  def install
    virtualenv_create(libexec, "python3")
    virtualenv_install_with_resources
  end

  test do
    system bin/"unatica", "--help"
  end
end
