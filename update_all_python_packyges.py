from subprocess import call
try:
  import pip
  packages = [dist.project_name for dist in pip.get_installed_distributions()]
except AttributeError:
  import pkg_resources
  packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)
