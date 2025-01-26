from setuptools import setup, find_packages

setup(
    name='topsis',  
    version='1.0.0',
    description='A Python package for implementing TOPSIS.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Tanya Sood',
    author_email='tsood_be22@thapar.edu',
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    python_requires='>=3.6',
)
