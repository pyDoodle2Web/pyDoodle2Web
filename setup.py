import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyDoodle2Web",
    version="0.0.7",
    author="pyDoodle2Web",
    author_email="renerjake@gmail.com",
    description="",
    long_description=long_description,
    url="https://github.com/pyDoodle2Web/pyDoodle2Web",
    packages=setuptools.find_packages(),
    install_requires=[
        'beautifulsoup4',
        'pytesseract',
    ],
    keywords=['bootstrap', 'ocr', 'website', 'genertion'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
