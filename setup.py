from setuptools import find_packages, setup

setup(
    name='toolbox',
    version='0.0.1',
    author='BlackBeard',
    description=('A toolbox for cybersecurity'),
    packages=find_packages(),
    install_requires=[
        'typer'
    ],
    # entry_points='''
    # [console_scripts]
    # toolbox=main:app
    # '''
    entry_points={'console_scripts': ['toolbox=main:toolbox']}
)
