# Copyright (C) 2020 Samuel Baker

DESCRIPTION = "Object approach to common dimensional vectors"
LONG_DESCRIPTION = """
# vectorObjects
#### Object approach to common dimensional vectors 

This project was create by converting and extending a small section of code within the now archived [pymeshio][pymesh], 
relating to Vectors and 3D object rotation matrices which have been extracted and generalised where possible. This was 
due to some of these objects also having the potential to be used outside of this specific use case.
 
vectorObjects also has the ability to allow you to create your own vectors, not pre defined within vectorObjects, 
quickly via inheritance from a master class of methods. All source code is available on the project [github page][pro]

[pymesh]: https://github.com/ousttrue/pymeshio
[docpath]: https://github.com/sbaker-dev/vectorObjects/Examples
[pro]: https://github.com/sbaker-dev/vectorObjects
"""
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"

DISTNAME = 'vectorObjects'
MAINTAINER = 'Samuel Baker'
MAINTAINER_EMAIL = 'samuelbaker.researcher@gmail.com'
LICENSE = 'MIT'
DOWNLOAD_URL = "https://github.com/sbaker-dev/vectorObjects"
VERSION = "0.02.0"
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    "numpy>=1.18.5"

]

PACKAGES = [
    "vectorObjects",
]

CLASSIFIERS = [
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
]

if __name__ == "__main__":

    from setuptools import setup

    import sys

    if sys.version_info[:2] < (3, 7):
        raise RuntimeError("vectorObjects requires python >= 3.7.")

    setup(
        name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
        license=LICENSE,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        packages=PACKAGES,
        classifiers=CLASSIFIERS
    )
