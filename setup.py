from setuptools import setup

setup(name='Personal Assistant',
      version='0.0.1',
      description='Personal assistant with a command line interface',
      author='Code Geeks',
      url='https://github.com/Veslo7601/Team_Project_1',
      license='MIT',
      packages=['Personal_Assistant'],
      install_requires=['python-dateutil==2.8.2'],
      entry_points={'console_scripts': ['Code_Geeks=Personal_Assistant.main:main']})
