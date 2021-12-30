from distutils.core import setup
setup(
    name='openpython',
    version='0.0.1',
    author='Gavin Newcomer',
    author_email='gjnprivate@gmail.com',
    description='OpenSea Python SDK',
    url='https://github.com/gavinnewcomer/OpenPython',
    download_url='https://github.com/gavinnewcomer/OpenPython/archive/refs/tags/v0.0.1.tar.gz',
    license='MIT',
    packages=['openpython'],
    install_requires=[
        'requests'
    ]
)
