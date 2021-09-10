from distutils.core import setup

setup(
    name='jaml',
    packages=['jaml'],
    version='0.1',
    license='MIT',
    description='Convert json to json using jinja2 and yaml',
    author='Vladimir',
    author_email='vmstarchenko@edu.hse.ru',
    url='https://github.com/vmstarchenko/jaml',
    keywords=['json2json', 'json', 'yaml', 'template'],
    install_requires=[
        'PyYAML',
        'Jinja2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    zip_safe=True,
)
