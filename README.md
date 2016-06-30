# OpenShift Origin

## akt. Stand

TASK: [openshift_examples | Unarchive the OpenShift examples on the remote] *** 
<master.tagliateller.nu> ESTABLISH CONNECTION FOR USER: robert.bloy
<master.tagliateller.nu> EXEC ssh -C -tt -vvv -o ControlMaster=auto -o ControlPersist=60s -o ControlPath="/home/robert.bloy/.ansible/cp/ansible-ssh-%h-%p-%r" -o StrictHostKeyChecking=no -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 master.tagliateller.nu /bin/sh -c 'mkdir -p $HOME/.ansible/tmp/ansible-tmp-1467135342.26-246355111406819 && chmod a+rx $HOME/.ansible/tmp/ansible-tmp-1467135342.26-246355111406819 && echo $HOME/.ansible/tmp/ansible-tmp-1467135342.26-246355111406819'
fatal: [master.tagliateller.nu] => input file not found at /tmp/openshift-ansible-rXhgp49/openshift-examples.tar or /tmp/openshift-ansible-rXhgp49/openshift-examples.tar

FATAL: all hosts have already failed -- aborting

PLAY RECAP ******************************************************************** 
           to retry, use: --limit @/home/robert.bloy/config.retry

localhost                  : ok=13   changed=0    unreachable=0    failed=0   
master.tagliateller.nu     : ok=216  changed=8    unreachable=1    failed=0   

Die Datei /tmp/openshift-ansible-rXhgp49/openshift-examples.tar ist vorhanden, allerdings nur durch root lesbar, obwohl die flag r-r-r gesetzt sind.

FATAL: all hosts have already failed -- aborting

PLAY RECAP ******************************************************************** 
           to retry, use: --limit @/home/robert.bloy/config.retry

localhost                  : ok=13   changed=0    unreachable=0    failed=0   
master.tagliateller.nu     : ok=216  changed=8    unreachable=1    failed=0   

## akt. Stand 30.06.2016 openshift-ansible-3.2.8-1

PLAY [Deploy node certificates] ************************************************

TASK [setup] *******************************************************************
ok: [master.tagliateller.nu]

TASK [Ensure certificate directory exists] *************************************
ok: [master.tagliateller.nu]

TASK [Unarchive the tarball on the node] ***************************************
fatal: [master.tagliateller.nu]: FAILED! => {"changed": false, "failed": true, "msg": "path /etc/origin/node/./system:node:origin-machine.c.bubbly-hope-132123.internal.crt does not exist", "path": "/etc/origin/node/./system:node:origin-machine.c.bubbly-hope-132123.internal.crt", "state": "absent"}

NO MORE HOSTS LEFT *************************************************************
	to retry, use: --limit @playbooks/byo/config.retry

erste Feststellung: Path ist vorhanden, aber leer ...

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