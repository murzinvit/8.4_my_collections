#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import os

from ansible.module_utils.basic import AnsibleModule

module_args = dict(
        name=dict(type='str', required=True),
        new=dict(type='bool', required=False, default=False),
        path=dict(type='str', required=False, default=False),
        content=dict(type='str', required=False, default=False)
    )

module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

def run_module():

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    if module.check_mode:
        module.exit_json(**result)

    result['original_message'] = module.params['name']
    result['message'] = 'goodbye'

    if module.params['new']:
        result['changed'] = True

    if module.params['name'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    module.exit_json(**result)

def mk_file():
    p = os.path.join(module.params['path'])
    os.chdir(p)
    f_set = open('My_File.txt', 'w+')
    f_set.write(module.params['content'])
    f_set.close()

mk_file()

def main():
    run_module()

if __name__ == '__main__':
    main()
