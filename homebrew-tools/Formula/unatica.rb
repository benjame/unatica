class Unatica < Formula
  include Language::Python::Virtualenv

  desc "A Safe and Simple macOS App Uninstaller"
  homepage "https://github.com/yourusername/unatica"
  url "https://github.com/yourusername/unatica/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "YOUR_TARBALL_SHA256"
  license "MIT"

  depends_on "python@3.10"

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
