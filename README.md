# 8.4_my_collections
====================================</br>
В шаблон модуля добавил функцию - `def mk_file()`, которая берёт значения из `dict module_args` </br>
`dict module_args и module = AnsibleModule`, вынес из функции `def run_module()` для общего доступа </br>
Значения параметров модуля по умолчанию заданы в роли в папке `defaults/main.yml - name, new, path, content` </br>
Сам модуль поместил в папку `library` в папке роли `mk_file` </br>
После выполнения роль по умолчанию создаёт файл `My_File.txt` в папке /home, с текстом Hi,there! </br>
Установка collection в папке с playbook: `ansible-galaxy collection install devops6-own_modules-1.0.0.tar.gz -p .` </br>
Далее, либо добавить путь к роли в `ansible.cfg`, либо скопировть папку с roles в корень папки с playbook, чтобы Ansible смог найти роль</br>


Модуль:  [код модуля](https://github.com/murzinvit/8.4_my_collections/blob/main/devops6/own_modules/roles/mk_file/library/my_own_module.py) </br>
   
![screen]() </br>
