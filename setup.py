from setuptools import find_packages, setup


setup(
    name='incuna-internal-social-auth',
    version='0.1',
    url='http://github.com/incuna/incuna-internal-social-auth',
    packages=find_packages(),
    include_package_data=True,
    description='Django Social Auth extras for the Incuna internal apps.',
    long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read(),
    author='Incuna Ltd',
    author_email='admin@incuna.com',
)

