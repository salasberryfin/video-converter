from setuptools import setup

setup(
        name="app",
        packages=["flaskapplication"],
        include_package_data=True,
        install_requires=[
            "flask",
            ]
        )
