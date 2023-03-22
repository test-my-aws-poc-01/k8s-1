from setuptools import setup, find_packages


setup(
    name='Simloud Flask Demo Project',
    version='0.1.0',
    long_description=__doc__,
    packages=find_packages(exclude=['*.egg']),
    include_package_data=True,
    zip_safe=False,
    python_requires='~=3.7',
    install_requires=[
        'Flask>=1.1.0,<1.2.0',
        'gunicorn>=19.9.0,<19.10.0',
    ],
)
