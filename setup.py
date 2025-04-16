from setuptools import setup, find_packages

setup(
    name='aicommiter',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'openai>=1.0.0',
        'questionary',
    ],
    entry_points={
        'console_scripts': [
            'aicommiter=aicommiter.cli:cli',
        ],
    },
    author='Your Name',
    description='AI-powered Git commit and PR automation tool',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
