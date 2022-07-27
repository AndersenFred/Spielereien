from subprocess import call
try:
  import pip
  packages = [dist.project_name for dist in pip.get_installed_distributions()]
except AttributeError:
  import pkg_resources
  packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)

#Additionally on Windows one may add a update.bat file in autostart to update automatically
#pyhton -m pip install --upgrade pip
#python update_all_python_package.py
