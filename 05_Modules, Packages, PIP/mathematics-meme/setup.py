from setuptools import setup, find_packages

setup(

    name='mathematics-meme',
    version='0.2',
    license='MIT',
    author='Himanshu Ramchandani',
    author_email='himanshuramchandani08@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='mathematics meme',
)