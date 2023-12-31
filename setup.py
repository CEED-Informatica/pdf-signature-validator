import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pdf_signature_validator',
    author='Álvaro Maceda',
    author_email='alvaro@alvaromaceda.es',
    description='Module for validating pdf signatures using pdfsig ',
    keywords='pdfsig, pdf, certificate, signature, validation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tomchen/example_pypi_package',
    project_urls={
        'Documentation': 'https://github.com/CEED-Informatica/pdf-signature-validator',
        'Bug Reports':
        'https://github.com/CEED-Informatica/pdf-signature-validator/issues',
        'Source Code': 'https://github.com/CEED-Informatica/pdf-signature-validator',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: GPL-3.0',
        'Operating System :: Linux',
    ],
    python_requires='>=3.8',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=examplepy:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
    #     ],
    # },
)
