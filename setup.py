from setuptools import setup, find_packages

version = __import__('iBanners').get_version()

setup(
    name = 'iBanners',
    version = version,
    description = "Banner rotation and managment system for Django Framework",
    keywords='django banners advertising',
    long_description = """This is application help you to manage advertising 
        place on your site, manage advertising companies and baner settings.""",
    author = 'Nikita Shultais',
    author_email = 'nikita@shultais.ru',
    url = 'git://github.com/shultais/iBanners.git',
    platforms = ['any'],
    classifiers = ['Development Status :: 0 - Alfa',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
    packages=find_packages(),
        package_data = {
        'ibanners': [
            'templates/*/*.*',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
