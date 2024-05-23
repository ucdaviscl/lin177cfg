from setuptools import setup

setup(
    name='my_pip_package',
    version='0.5',

    url='https://github.com/ucdaviscl/lin177cfg',
    author='Kenji Sagae',
    
    install_requires=['pcfg'],
    py_modules=['cfg'],
)
