import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='openpython',
    version='0.0.11',
    author='Gavin Newcomer',
    author_email='gjnprivate@gmail.com',
    description='OpenSea Python SDK',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/gavinnewcomer/OpenPython',
    project_urls = {
        "Open Python": "https://github.com/gavinnewcomer/OpenPython/issues"
    },
    license='MIT',
    packages=['openpython'],
    install_requires=['requests'],
)
