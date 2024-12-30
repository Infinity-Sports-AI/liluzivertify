from setuptools import find_packages, setup

setup(
    name="liluzivertify",
    py_modules=["liluzivertify"],
    version="0.0.1",
    description=(
        "Lil Uzi Vertify is based on a fork of Lil Uzi Vertify but solely looks to "
        "meaningfully convert horizontal videos to vertical using AI"
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Alexander Fayad",
    author_email="dev@infinitystud.io",
    url="https://infinitystud.io/",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "av",
        "facenet-pytorch",
        "matplotlib",
        "mediapipe",
        "nltk",
        "numpy",
        "opencv-python",
        "pandas",
        "psutil",
        "pyannote.audio",
        "pyannote.core",
        "pynvml",
        "pytest",
        "python-magic",
        "scenedetect",
        "scikit-learn",
        "sentence-transformers",
        "scipy",
        "torch",
    ],
    zip_safe=False,
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Repository": "https://github.com/Infinity-Sports-AI/liluzivertify",
        "Issues": "https://github.com/Infinity-Sports-AI/liluzivertify/issues",
    },
    include_package_data=True,
    extras_require={
        "dev": [
            "black",
            "black[jupyter]",
            "build",
            "flake8",
            "ipykernel",
            "pytest",
            "twine",
        ],
    },
)
