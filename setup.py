from setuptools import setup
def readme():
    with open('README.rst') as f:
        return f.read()
    
setup(name='processlog',
      version='0.0.1',
      description='Process Logging in Redshift with python',
      long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='Redshift,Logging, SFTP, Pandas, CSV, JSON',        
      url='https://github.com/KaranSinghMalhotra/processlog',
      author='Karan Malhotra/ Swati Srivastava',
      author_email='karan.ashwa@gmail.com/ ',
      license='MIT',
      packages=['processlog'],
      install_requires=['pandas', 'psycopg2', 'dsconnect'],
      include_package_data=True,      
      zip_safe=False)