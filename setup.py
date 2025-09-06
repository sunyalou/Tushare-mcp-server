#!/usr/bin/env python3
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="tushare-mcp-server",
    version="0.1.0",
    author="Tushare MCP",
    author_email="noreply@example.com",
    description="MCP Server for Tushare Chinese stock market data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['tushare_mcp_server'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    scripts=["bin/tushare-mcp-server", "bin/tushare-mcp"],
    include_package_data=True,
)