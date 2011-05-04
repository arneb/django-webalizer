from setuptools import setup, find_packages

setup(
    name='django-webalizer',
    version='0.1',
    description='A Django app for embedding Webalizer reports into the admin',
    long_description=open('README.rst').read(),
    author='Arne Brodowski',
    author_email='info@arnebrodowski.de',
    url='http://github.com/arneb/django-webalizer',
    packages=find_packages(exclude=[]),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
