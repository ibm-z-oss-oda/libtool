from piptool.piptools_class import Library
u = Library(
    test_file="test_file.py",
    author="test author",
    email="test.author@@",
    description = "test description",
    url="http://test.author.com",
    install_requires=["numpy"],
    start_version="0.2",
    scripts=['libtool\\library.bat'],
)
u.c_setup()
u.c_init()
u.c_md()
u.c_licence()
