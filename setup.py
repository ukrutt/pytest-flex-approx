"""pytest-flex-approx -- Flexible approx for pytest
"""

import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))

# Get version from VERSION and long description from the README files
with open(os.path.join(HERE, "VERSION")) as version_file:
    VERSION = version_file.read().strip()

with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()


setup(
    name="pytest-flex-approx",
    version=VERSION,
    description="Flexible approx for pytest",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/ukrutt/pytest-flex-approx",
    author="Henrik Holm",
    author_email="henrik@forestglenresearch.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires=">=3.6, <4",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pytest>=5.3",
    ],
    entry_points={
        # If this isn't a runnable program, you can delete this entry point.
        "console_scripts": ["hello_world=pytest_flex_approx.main:hello_world"]
    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
