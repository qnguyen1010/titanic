from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
    name='titanic',
    version='0.1',
    description='Analysis of the Titanic dataset',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    # Substitute <github_account> with the name of your GitHub account
    url='https://github.com/qnguyen1010/titanic_datascience',
    author='JackNguyen',  # Substitute your name
    author_email='qnguyen1010@gmail.com',  # Substitute your email
    license='MIT',
    packages=['titanic'],
    install_requires = ['pypandoc>=1.4']
)
