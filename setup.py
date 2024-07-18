from setuptools import setup

setup(
    name='amazon_scraper',
    version='1.0.0',
    description='Amazon Product Scraper',
    author='LIN Mi',
    author_email='linmi2018@gmail.com',
    url='https://github.com/camillemi/Amazo_Product_Scraper',
    py_modules=['rechercher_resultats', 'gui'],
    include_package_data=True,
    install_requires=[
        'requests',
        'pandas',
        'selectorlib',
    ],
    entry_points={
        'console_scripts': [
            'amazon-scraper-gui=gui:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

