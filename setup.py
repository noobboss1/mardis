from setuptools import setup
setup(
   name='mardis',
   version='2.0',
   description='A useful module',
   author='kapten-kaizo',
   author_email='cyber2687@gmail.com',
   packages=['mardis'],
   entry_points={"console_scripts": ["mardis=mardis:main"]},
   install_requires=['xdis==5.0.11','uncompyle6==3.7.4']
)