from setuptools import setup

setup(
    name='insight',
    version='0.1',
    py_modules=['insight'],
    install_requires=[
        'Click',
        'nexmo',
    ],
    entry_points='''
        [console_scripts]
        insight=insight:cli
    ''',
)
