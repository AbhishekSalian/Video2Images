from setuptools import setup, Extension
from setuptools import find_packages


with open("README.md") as f:
    long_description = f.read()

classifiers = [
               "Programming Language :: Python :: 3",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Development Status :: 4 - Beta",
               "Intended Audience :: Science/Research",
               "Intended Audience :: Financial and Insurance Industry",
               "Intended Audience :: Developers",
               "Topic :: Software Development :: Libraries :: Python Modules",
               "Natural Language :: English"
              ],

SHORT_DESC = "A library for video frames to image converter"

requirements = ["tqdm",
                "imageio",
                "moviepy",
                "imageio-ffmpeg>=0.4.2"]


if __name__ == "__main__":

    setup(
        name="video2images",
        scripts=["scripts/video2images"],
        version="1.3",
        description="Video 2 Image converter",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Abhishek C. Salian",
        author_email="abhishek.c.salian@gmail.com",
        url="https://github.com/AbhishekSalian/Video2Images",
        license="MIT License",
        packages=find_packages(),
        package_data={'': ['LICENSE', 'README.md']},
        include_package_data=True,
        install_requires=requirements,
        package=["video2images"],
        platforms=["windows", "linux", "unix"],
        python_requires=">=3.5"
    )
