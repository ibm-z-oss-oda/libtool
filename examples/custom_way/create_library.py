from libtool.libtool_class import Library

l = Library(
    test_file="test.py",
    email="your.email@your_mail.com",
    description="only for test",
    url = "http://your.url.com",
    pylicense="mit",
    author="author",
    install_requires=["mhyt","mhmovie"],
    #and the additional options:
    folder="foldername",
    start_version="2.7.3",
    scripts=["script1.bat",]
)
#to create __init__.py
l.c_init()
#to create licence.txt
l.c_licence()
#to create setup.py
l.c_setup()
#to create readme.md
l.c_md()
#to edit readme.md
l.edit_md()