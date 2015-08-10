from distutils.core import setup

setup(
    name="pybase",
    version="1.0.0",
    author="Andrew Emmons",
    author_email="andrewcemmons@gmail.com",
    packages=["namespace", "namespace.pybase"],
    namespace_packages = ["namespace"],
    url="http://example.com/",
    license="LICENSE",
    description="A quick starting point for namespaced python packages",
    long_description=open("README.md").read(),
    install_requires=[
        "pymysql==0.5",
    ]
)
