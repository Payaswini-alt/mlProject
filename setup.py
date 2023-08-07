##To build our application as a package itself.Moreover,we can deploy it at PYPI for the use of others.
from setuptools import find_packages,setup
from typing import List
hyphen_dot="-e ."
def get_requirements(file_path:str) ->List[str]:
    '''
    this function will return list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements] ##when it reads from requirements.txt while reading the next line it also reads \n so to replace it with a space.
        if hyphen_dot in requirements:
            requirements.remove(hyphen_dot)
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Payaswini',
author_email='payaswinisinghaj02@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
    


