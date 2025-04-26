import setuptools
import distutils.core

setuptools.setup(
    name='pypi-stats-timeline',
    version="1.0.1",
    author='Author',
    long_description_content_type='text/markdown',
    author_email='Email',
    description='',
    license='BSD3',
    keywords='',
    url='',
    packages=["pypi_stats_timeline"],
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': ['pypi-stats-timeline=pypi_stats_timeline.main:main']
    },
    classifiers=[
    ],
    test_suite='nose.collector'
)
