from setuptools import setup, find_packages

setup(
    name='mcqgenderator',
    version='0.0.1',
    author='Pruthviraj Rathod',
    author_email='prithvirathod29884@gmail.com',
    install_requires=[
        'openai',
        'langchain',
        'streamlit',
        'python-dotenv',
        'PyPDF2'
    ],
    packages=find_packages()
)
