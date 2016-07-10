# OpenShift Origin


## GCE

source ~/.gce/gce_credentials
source ~/.gce/gce_config
ansible-playbook playbooks/gce/ticketmonster-classic-launch.yml -u cloud-user

Bildung des Namens noch nicht vollständig - Name steht in Scratch drin, aber nicht als Ergebnis

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



