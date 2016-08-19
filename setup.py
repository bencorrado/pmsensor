from setuptools import setup, find_packages

setup(name='pmsensor',
      version='0.3',
      description='Library to read data from environment ensors',
      url='https://github.com/open-homeautomation/pmsensor',
      author='Daniel Matuschek',
      author_email='daniel@matuschek.net',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: System :: Hardware :: Hardware Drivers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5'
      ],
      packages=find_packages(),
      install_requires=['pyserial>=3'],
      keywords='serial pm2.5 pm1.0 pm10 co2',
      zip_safe=False)
