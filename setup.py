from setuptools import setup, find_packages

setup(
    name="bloomberg_analytics",
    version="0.1.0",
    packages=find_packages(),
    install_package_data=True,
    install_requires=[
        "pandas",
        "numpy",
        "yfinance",  # Bloomberg-lite data source
        "scipy",
        "matplotlib",
        "plotly",
        "python-dotenv"
    ],
)
