import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="over-simplified-downloader",
    version="0.0.1",
    author="Liu Zheng",
    author_email="zheng@example.com",
    description=("An over-simplified downloader package to "
                "demonstrate python module and tool packaging."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liuzheng1990/python_packaging_demo",
    project_urls={
        "Bug Tracker": "https://github.com/liuzheng1990/python_packaging_demo/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "download = downloader.cli:main",
        ]
    }
)