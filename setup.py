from setuptools import setup, find_packages
import os

version = '0.3.1'

setup(name='zopyx.tinymceplugins.imgmap',
      version=version,
      description="Imgmap editor plugin for TinyMCE",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='Plone Zope TinyMCE editor',
      author='Andreas Jung',
      author_email='info@zopyx.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['zopyx', 'zopyx.tinymceplugins'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'BeautifulSoup',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
