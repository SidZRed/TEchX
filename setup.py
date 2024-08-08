from setuptools import setup, find_packages

setup(
    name='techx',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'techx=techx.main:main',
        ],
    },
    install_requires=[
        'reportlab',
    ],
    author='Siddharth Reddy',
    author_email='siddharthrr@iisc.ac.in',
    description='A typesetting system for quick and easy technical documentation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SidZRed/TEchX',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)