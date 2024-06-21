import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classification"
AUTHOR_USER_NAME = "RUPANSHU KAPOOR"
SRC_REPO = "CNNClassifier"
AUTHOR_EMAIL = "rupanshukapoor@outlook.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    Long_description_content = "text/markdown",
    url = "https://github.com/Rupanshu-Kapoor/Chicken-Disease-Classification.git",
    project_urls = {
        "Bug Tracker": "https://github.com/Rupanshu-Kapoor/Chicken-Disease-Classification/issues"
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where="src")
    
)