import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name='college-costs',
    version_format='{tag}.dev{commitcount}+{gitsha}',
    author='CFPB',
    author_email='tech@cfpb.gov',
    maintainer='cfpb',
    maintainer_email='tech@cfpb.gov',
    packages=find_packages(),
    package_data={'paying_for_college':
                  ['data_sources/ipeds/*cleaned.csv',
                   'data_sources/ipeds/test.txt.zip',
                   'fixtures/*.json',
                   'templates/*.txt',
                   'templates/*.html',
                   'static/paying_for_college/feedback/css/*.css',
                   'static/paying_for_college/feedback/js/*.js',
                   'static/paying_for_college/feedback/images/*.png',
                   'static/paying_for_college/disclosures/static/css/*.css',
                   'static/paying_for_college/disclosures/static/css/*.map',
                   'static/paying_for_college/disclosures/static/fonts/*.eot',
                   'static/paying_for_college/disclosures/static/fonts/*.svg',
                   'static/paying_for_college/disclosures/static/fonts/*.woff',
                   'static/paying_for_college/disclosures/static/fonts/*.ttf',
                   'static/paying_for_college/disclosures/static/js/*.htc',
                   'static/paying_for_college/disclosures/static/js/*.js',
                   'static/paying_for_college/disclosures/static/js/*.map',
                   'static/paying_for_college/disclosures/static/img/*.png',
                   'static/vendor/box-sizing-polyfill/boxsizing.htc'
                   ],
                  },
    include_package_data=True,
    description=u'College cost tools',
    classifiers=[
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=read_file('README.md'),
    zip_safe=False,
    setup_requires=['cfgov_setup==1.2', 'setuptools-git-version'],
    frontend_build_script='setup.sh'
)
