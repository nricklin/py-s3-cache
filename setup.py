import sys
from setuptools import setup, find_packages

open_kwds = {}
if sys.version_info > (3,):
    open_kwds['encoding'] = 'utf-8'

setup(name='py-s3-cache',
      version='1.0.0',
      description='Super minimal python S3 cache',
      classifiers=[],
      keywords='',
      author='Nate Ricklin',
      author_email='nate.ricklin@gmail.com',
      url='https://github.com/nricklin/py-s3-cache',
      license='MIT',
      packages=find_packages(exclude=['docs','tests','examples']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['boto3', 'arrow'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest','vcrpy']
)
