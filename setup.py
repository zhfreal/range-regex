import os
from setuptools import find_packages, setup

root = os.path.dirname(os.path.realpath(__file__))
long_description = open(os.path.join(root, 'README.rst')).read()

setup(
    name='range-regex',
    version='1.0.4',
    description='Python numeric range regular expression generator',
    long_description=long_description,
    url='http://github.com/zhfreal/range-regex',
    author='Dmitry Voronin',
    author_email='zhfreal@gmail.com',
    license='BSD',
    # packages=['range_regex'],
    packages=find_packages(),
    include_package_data=True,
    keywords='numeric range regex regular expression generator',
)
