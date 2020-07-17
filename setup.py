import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='auto_pip',
    version='0.0.3',
    license='MIT',
    description='Create, version and upload library',
    author='matan h',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='matan.honig2@gmail.com,',
    url='',
    packages=['auto_pip', "auto_pip._cmd_argv", "auto_pip.util", "auto_pip.pypi"],
    scripts=['auto_pip\\cmd\\library.bat'],
    package_data={'auto_pip': ["README_in.md"]},
    install_requires=["Markdown-Editor", "requests", "setuptools", "wheel", "twine"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
