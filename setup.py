from setuptools import setup, find_packages

with open("README.md", "r", encoding = "UTF-8") as file:
    long_desc = file.read()
 
setup(
    name = "aernetworking",
    version = "0.0.1",
    description = "An easy-to-use network interface module.",
    long_description = long_desc,
    long_description_content_type = "text/markdown",
    url = "github.com/Aermoss/AerNetworking_V0.0.1",
    author = "Yusuf Rencber",
    author_email = "yusufrencber546@gmail.com",
    license = "MIT",
    keywords = "networking interface",
    packages = find_packages(),
    install_requires = [""]
)