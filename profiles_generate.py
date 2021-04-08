#!/usr/bin/python3

from string import Template


build_types=[None, 'debug','release']
cpus=['cortex-m7', 'cortex-m4']
oses=[None, 'freertos']
compilers=['arm-none-eabi-gcc']

def get_name(profile):
    name = ""
    if profile['OS']:
        os = profile['OS']
        name += f'{os}-'
    name += profile['CPU']
    if profile['BUILD_TYPE']:
        build_Type = profile['BUILD_TYPE']
        name += f'.{build_Type}'
    return name

def get_substitutions(profile):
    if not profile['OS']:
        profile['OS'] = "none"
    if not profile['BUILD_TYPE']:
        profile['BUILD_TYPE'] = "release"
    return profile

profile_list = list()
for compiler in compilers:
    for os in oses:
        for cpu in cpus:
            for build_type in build_types:
                profile_list.append({
                    'OS': os,
                    'COMPILER': compiler,
                    'CPU': cpu,
                    'BUILD_TYPE': build_type})

for profile in profile_list:
    name = get_name(profile)
    substitutions = get_substitutions(profile)
    with open('templates/gcc_cpu', 'r') as templateFile:
        src = Template(templateFile.read())
        result = src.safe_substitute(substitutions)
        with open(f'profiles/{name}', 'w') as profileFile:
            profileFile.write(result)


# with open('foo.txt', 'r') as f:
#     src = Template(f.read())
#     result = src.substitute(d)
#     print(result)