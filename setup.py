from setuptools import setup

setup(
    name = 'vc_test_suite',
    version = '0.1.0',
    packages = ['vc_test_suite'],
    entry_points = {
        'console_scripts': [
            'vc_test_suite = vc_test_suite.__main__:main'
        ]
    })