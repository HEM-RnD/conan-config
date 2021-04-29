import os
import time
import shutil

def pre_export(output, conanfile, conanfile_path, reference, **kwargs):
    # Check basic meta-data
    for field in ["url", "license", "description"]:
        field_value = getattr(conanfile, field, None)
        if not field_value:
            output.warn("Conanfile doesn't have '%s'. It is recommended to add it as attribute"
                        % field)

def pre_build(output, conanfile, **kwargs):
    assert conanfile
    if conanfile.in_local_cache:
        output.info("reference={}".format(kwargs["reference"].full_str()))
        output.info("package_id={}".format(kwargs["package_id"]))
    else:
        output.info("conanfile_path={}".format(kwargs["conanfile_path"]))

        destPath = kwargs["conanfile_path"]
        for x in range(2):
            destPath = destPath[:destPath.rfind('/')]

        try:
            os.system("git clone https://adziwinski@bitbucket.org/hemrnd/clangtidy.git")
            shutil.copyfile("clangtidy/.clang-tidy", destPath + "/.clang-tidy")
            output.info(".clang-tidy file copied to: "+ destPath)
        except:
            output.warn(".clang-tidy file can not be copied")

        try:
            os.system("git clone https://adziwinski@bitbucket.org/hemrnd/clangformat.git")
            shutil.copyfile("clangformat/.clang-format", destPath + "/.clang-format")
            output.info(".clang-format file copied to: "+ destPath)
        except:
            output.warn(".clang-format file can not be copied")
