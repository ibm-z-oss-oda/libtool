import setuptools

setuptools.setup(
    name='auto_pip',
    version='1.1',
    license='MIT',
    description='create library',
    author='matan h',
    author_email='matan.honig2@gmail.com,',
    url='',
    packages=['auto_pip', "auto_pip._cmd_argv", "auto_pip.util", "auto_pip.pypi"],
    scripts=['auto_pip\\cmd\\library.bat'],
    package_data={'auto_pip': ["README_in.md"]},
    install_requires=["Markdown-Editor", "requests", "setuptools", "wheel", "twine"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
