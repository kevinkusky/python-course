print('Running my_package/subpackage/module_s1.py as', __name__)

# Will need to set pythonpath variable to run
from another_package import value
print('Value from another package is', value)

value = 'my_package/subpackage/module_s1.py'