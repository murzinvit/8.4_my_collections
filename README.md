# 8.4_my_collections
====================================</br>
В шаблон модуля добавил функцию - `def mk_file()`, которая берёт значения из `dict module_args` </br>
`dict module_args и module = AnsibleModule`, вынес из функции `def run_module()` для общего доступа </br>
Значения параметров модуля по умолчанию заданы в роли в папке `defaults/main.yml - name, new, path, content` </br>
Сам модуль поместил в папку `library` в папке роли `mk_file` </br>
После выполнения роль по умолчанию создаёт файл `My_File.txt` в папке /home, с текстом Hi,there! </br>
Установка `collection: ansible-galaxy collection install mk_file_collection.tar.gz` </br>
Далее, либо добавить путь к роли в `ansible.cfg`, либо скопировть папку с ролью в папку с playbook </br>


Модуль:  [код модуля](https://github.com/murzinvit/8.4_my_collections/blob/main/devops6/own_modules/roles/mk_file/library/my_own_module.py) </br>
    
Архив collection:  [archive]() </br>
   
![screen]() </br>
