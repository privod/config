from setuptools import setup, find_packages
from os.path import join, dirname

import config

setup(
    name='config',
    version=config.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),

    # install_requires=[
    #     'bokeh',
    #     'flask',
    #     'pandas',
    # ],
    # entry_points={
        # 'console_scripts': [
            # 'actual_ncr = config.main:start',
        # ]
    # },
    # include_package_data=True,
    test_suite='tests',
)