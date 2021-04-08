#!/usr/bin/python3

from string import Template


build_types=[None, 'debug','release', 'minsizerel', 'relwithdebinfo']

def get_name(profile):
    name = profile['ARCH'] + '-' 
    if profile['OS']:
        name += profile['OS']
    else:
        name += 'none'
    name += '-'
    if profile['ABI_COMPILER']:
        name += profile['ABI_COMPILER']
    else:
        if profile['ABI']:
            name += profile['ABI']
        else:
            name += 'unknown'
        name += '-'
        if profile['COMPILER']:
            name += profile['COMPILER']
        else:
            name += 'unknown'
    if profile['BUILD_TYPE']:
        name += '.' + profile['BUILD_TYPE']
    return name

def get_substitutions(profile):
    if not profile['OS']:
        profile['OS'] = "none"
    if not profile['BUILD_TYPE']:
        profile['BUILD_TYPE'] = "none"
    return profile

def get_arm_none_eabi_gcc_profiles():
    archs=['cortex-m7', 'cortex-m4']
    oses=[None, 'freertos']
    abi_compiler='eabi-gcc'
    compiler='arm-none-eabi-gcc'

    profile_list = list()
    for os in oses:
        for arch in archs:
            for build_type in build_types:
                profile_list.append({
                    'OS': os,
                    'COMPILER': compiler,
                    'ABI_COMPILER': abi_compiler,
                    'ARCH': arch,
                    'BUILD_TYPE': build_type})
    return profile_list

profile_list = get_arm_none_eabi_gcc_profiles()

for profile in profile_list:
    name = get_name(profile)
    substitutions = get_substitutions(profile)
    with open('templates/gcc', 'r') as templateFile:
        src = Template(templateFile.read())
        result = src.safe_substitute(substitutions)
        with open(f'profiles/{name}', 'w') as profileFile:
            profileFile.write(result)


# with open('foo.txt', 'r') as f:
#     src = Template(f.read())
#     result = src.substitute(d)
#     print(result)