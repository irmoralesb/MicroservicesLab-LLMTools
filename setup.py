from setuptools import setup, find_packages

setup(
    name='llm_tools',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv'
    ],
    description='A package for working with LLM tools',
    author='Raul Morales',
    author_email='irmoralesb@hotmail.com',
    url='https://github.com/irmoralesb/MicroservicesLab-LLMTools',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)