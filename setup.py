from setuptools import setup, find_packages

setup(
    name="langtimezone",
    version="0.1",
    author="Amir Bargahi",
    author_email="lightdevs666@gmail.com",
    description="A Python library for extracting language and timezone based on country code.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/langtimezone",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pytz",
        "lxml",
        "phonenumbers",
    ],
)
