from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='revivesocialmedia',
    version='0.0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python package to revive blog posts & personal projects to Twitter & LinkedIn',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=required,
    keywords=['carcass', 'blogs', 'oss', 'revive', 'Twitter', 'LinkedIn'],
    url='https://github.com/msadministrator/revivesocialmedia',
    author='MSAdministrator',
    author_email='rickardja@live.com',
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    entry_points={
          'console_scripts': [
              'revivesocialmedia = revivesocialmedia.__main__:main'
          ]
    },
)