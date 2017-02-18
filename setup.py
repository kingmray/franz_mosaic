from distutils.core import setup

setup(
    name='franz_mosaic',
    packages=['my_python_package'],
    version='version number',  # Ideally should be same as your GitHub release tag varsion
    description='reduces pictures and creates new image based on reduced information',
    author='raymond schmidt',
    author_email='raymond.schmidt@googlemail.com',
    url='github package source url',
    download_url='download link you saved',
    keywords=['image', 'processing'],
    classifiers=[],
    entry_points={
        'console_scripts': ['franz-mosaic=franz_mosaic.app:main'],
    },
    install_requires=[
        'instagram-scraper==1.1.0',
        'Pillow==4.0.0',
        'pkg-resources==0.0.0',
        'pyparsing==2.1.10',
    ]
)
