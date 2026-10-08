import io
import os

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
    long_description = f.read()

with io.open(
    os.path.join(HERE, "tutorpathwaysandbox", "__about__.py"), "rt", encoding="utf8"
) as f:
    about = {}
    exec(f.read(), about)

setup(
    name="tutor-contrib-pathway-sandbox",
    version=about["__version__"],
    url="https://github.com/open-craft/tutor-contrib-pathway-sandbox",
    project_urls={
        "Code": "https://github.com/open-craft/tutor-contrib-pathway-sandbox",
        "Issue tracker": "https://github.com/open-craft/tutor-contrib-pathway-sandbox/issues",
    },
    license="AGPLv3",
    author="OpenCraft",
    description="Build the Open edX MFEs from the OpenCraft pathway forks",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=["tutorpathwaysandbox"],
    python_requires=">=3.8",
    install_requires=[
        "tutor>=20.0.0",
        # MFE_APPS/FRONTEND_APPS and the `source` key on frontend apps.
        "tutor-mfe>=22.0.0",
    ],
    entry_points={
        "tutor.plugin.v1": [
            "pathway_sandbox = tutorpathwaysandbox.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
