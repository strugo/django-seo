from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='django-seo',
      version=version,
      description="Simple SEO for Django projects",

      classifiers=[
        'Development Status :: 1 - Initial',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
      ],
      keywords='django seo',
      author='Arcady Chumachenko',
      author_email='arcady.chumachenko@gmail.com',
      url='http://github.com/ilvar/django-seo',
      license='BSD',
      packages = find_packages('.'),
      package_dir = {'': '.'},
      include_package_data=True,
      install_requires=[
          'setuptools',
      ],
      zip_safe=False,
)
