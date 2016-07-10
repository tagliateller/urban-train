# Cloud Testing


## GCE

REM source ~/.gce/gce_credentials
source ~/.gce/gce_config
export GCE_INI_PATH=~/.gce/gce.ini
eval `ssh-agent`
ssh-add ~/.ssh/google_compute_engine
ansible-playbook -i inventory/gce/hosts playbooks/gce/ticketmonster-classic-launch.yml -u cloud-user
ODER
ansible-playbook -i ../openshift-ansible/inventory/gce/hosts playbooks/gce/ticketmonster-classic-launch.yml -u cloud-user

TODO Bildung des Namens noch nicht vollständig - Name steht in Scratch drin, aber nicht als Ergebnis
TODO Hinzufügen des Hosts - hier sind noch oo-Variablen drin. Ggf. das einfach weglassen und auf dyn. Inventory setzen

TASK [Launch instance(s)] ******************************************************
changed: [localhost]

TASK [Add new instances to groups and set variables needed] ********************
[DEPRECATION WARNING]: Using bare variables is deprecated. Update your playbooks so that the environment value uses the full variable syntax ('{{gce.instance_data |
default([], true)}}').
This feature will be removed in a future release. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
fatal: [localhost]: FAILED! => {"failed": true, "msg": "template error while templating string: no filter named 'oo_prepend_strings_in_list'. String: {{ item.tags | oo_prepend_strings_in_list('tag_') | join(',') }}"}
Debugger invoked
(debug) c
        to retry, use: --limit @playbooks/gce/ticketmonster-classic-launch.retry

PLAY RECAP *********************************************************************
localhost                  : ok=12   changed=1    unreachable=0    failed=1

[vagrant@localhost paas]$

## AWS

[vagrant@localhost openshift-ansible]$ source ~/.aws_config
[vagrant@localhost openshift-ansible]$ source ~/.aws_credentials
[vagrant@localhost openshift-ansible]$ eval `ssh-agent`
Agent pid 3822
[vagrant@localhost openshift-ansible]$ ssh-add ~/.ssh/id_rsa
Identity added: /home/vagrant/.ssh/id_rsa (/home/vagrant/.ssh/id_rsa)
[vagrant@localhost openshift-ansible]$

## Monitoring

TODO
https://github.com/sfromm/ansible-omdistro/blob/master/tasks/main.yml

## Wildfly / JBoss EAP

OK
https://github.com/ansible/ansible-examples/blob/master/jboss-standalone/roles/jboss-standalone/tasks/main.yml

TODO: Management-Real bin/add-user muss ausgeführt werden (Nutzer für Remote)
auf dem Client: 
mvn jboss-as:deploy -Djboss-as.hostname=104.197.166.59
oder mit Nutzername / Pwd ?
$ mvn jboss-as:deploy -Djboss-as.hostname=104.197.166.59 -Djboss-as.username=remote -Djboss-as.password=john - OK
clean package vorweg !

## MariaDB

TODO: Anbindung an JBoss

https://github.com/PCextreme/ansible-role-mariadb

## Facts

ansible -i lab-inventory rdo-server.priv.tagliateller.nu -m setup

## OMD

https://github.com/sfromm/ansible-omdistro.git

##Jenkins 

https://github.com/geerlingguy/ansible-role-jenkins.git

## Gitlab

https://github.com/geerlingguy/ansible-role-gitlab.git

## Nexus

https://github.com/jhinrichsen/ansible-nexus.git

## Sonstiges

https://github.com/2015-Middleware-Keynote/demo-ansible/blob/master/run.py

## AWS

cluster.py prüfen, ggf. werden keine openshift-variablen gesetzt ? Sonst auch DEBUG in 



