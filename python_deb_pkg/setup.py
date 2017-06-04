import setuptools

setuptools.setup(
    name="python-deb-pkg",
    version='0.1.0',

    author="Krzysztof Zuraw",
    author_email="krzysztof.zuraw@gmail.com",

    description="Python Debian PKG example",

    packages=setuptools.find_packages('src', exclude=('tests',)),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        'requests',
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'python-deb-pkg = python_deb_pkg.main:main',
        ],
    }
)
