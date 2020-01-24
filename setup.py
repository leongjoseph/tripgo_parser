from setuptools import setup

setup(
    name='tripgo_parser',
    version='0.1.1',
    description='Parser for use with the TripGo API',
    url='https://github.com/leongjoseph/tripgo-parser',
    author='Joseph Leong',
    author_email='leong.joseph@me.com',
    license='MIT',
    packages=['tripgo_parser'],
    install_requires=['numpy','pandas','requests']
)
