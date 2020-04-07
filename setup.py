import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='acme-client-nick-hess',
    version='0.0.1',
    author='Nick Hess',
    author_email='hessproject@gmail.com',
    description='Client for SURE Acme API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hessproject/acme-volcano-insurance',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8'
)