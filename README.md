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

## akt. Stand 3.7.16

[vagrant@localhost openshift-ansible]$ bin/cluster update aws origin-v3
================================================================================
ATTENTION: You are running a community supported utility that has not been
tested by Red Hat. Visit https://docs.openshift.com for supported installation
instructions.
================================================================================

This is destructive and could corrupt origin-v3 cluster. Continue? [y/N] y

PLAY [localhost] ***************************************************************

TASK [include_vars] ************************************************************
ok: [localhost]

TASK [include_vars] ************************************************************
ok: [localhost]

TASK [add_host] ****************************************************************
[DEPRECATION WARNING]: Using bare variables is deprecated. Update your playbooks so that the environment value uses the full variable syntax ('{{g_all_hosts}}').
This
feature will be removed in a future release. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
changed: [localhost] => (item=54.87.210.19)
changed: [localhost] => (item=52.91.121.42)
changed: [localhost] => (item=54.89.28.170)
changed: [localhost] => (item=54.152.164.184)

PLAY [l_oo_all_hosts] **********************************************************

TASK [include_vars] ************************************************************
ok: [54.87.210.19]
ok: [52.91.121.42]
ok: [54.89.28.170]
ok: [54.152.164.184]

TASK [include_vars] ************************************************************
ok: [54.87.210.19]
ok: [52.91.121.42]
ok: [54.89.28.170]
ok: [54.152.164.184]

PLAY [Update - Populate oo_hosts_to_update group] ******************************

TASK [Update - Evaluate oo_hosts_to_update] ************************************
[DEPRECATION WARNING]: Using bare variables is deprecated. Update your playbooks so that the environment value uses the full variable syntax ('{{g_all_hosts |
default([])}}').
This feature will be removed in a future release. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
changed: [localhost] => (item=54.87.210.19)
changed: [localhost] => (item=52.91.121.42)
changed: [localhost] => (item=54.89.28.170)
changed: [localhost] => (item=54.152.164.184)

PLAY [Populate config host groups] *********************************************

TASK [fail] ********************************************************************
skipping: [localhost]

TASK [fail] ********************************************************************
skipping: [localhost]

TASK [fail] ********************************************************************
skipping: [localhost]

TASK [fail] ********************************************************************
skipping: [localhost]

TASK [fail] ********************************************************************
skipping: [localhost]

TASK [fail] ********************************************************************
skipping: [localhost]

TASK [Evaluate oo_all_hosts] ***************************************************
[DEPRECATION WARNING]: Using bare variables is deprecated. Update your playbooks so that the environment value uses the full variable syntax ('{{g_all_hosts |
default([])}}').
This feature will be removed in a future release. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
changed: [localhost] => (item=54.87.210.19)
changed: [localhost] => (item=52.91.121.42)
changed: [localhost] => (item=54.89.28.170)
changed: [localhost] => (item=54.152.164.184)

TASK [Evaluate oo_masters] *****************************************************
changed: [localhost] => (item=52.91.121.42)

TASK [Evaluate oo_etcd_to_config] **********************************************

TASK [Evaluate oo_masters_to_config] *******************************************
changed: [localhost] => (item=52.91.121.42)

TASK [Evaluate oo_nodes_to_config] *********************************************
changed: [localhost] => (item=54.87.210.19)
changed: [localhost] => (item=54.89.28.170)
changed: [localhost] => (item=54.152.164.184)

TASK [Evaluate oo_nodes_to_config] *********************************************
skipping: [localhost] => (item=52.91.121.42)

TASK [Evaluate oo_first_etcd] **************************************************
skipping: [localhost]

TASK [Evaluate oo_first_master] ************************************************
changed: [localhost]

TASK [Evaluate oo_lb_to_config] ************************************************

TASK [Evaluate oo_nfs_to_config] ***********************************************

PLAY [oo_hosts_to_update] ******************************************************

TASK [setup] *******************************************************************
ok: [54.152.164.184]
ok: [52.91.121.42]
ok: [54.89.28.170]
ok: [54.87.210.19]

TASK [openshift_facts : Verify Ansible version is greater than or equal to 1.9.4] ***
skipping: [54.87.210.19]
skipping: [54.89.28.170]
skipping: [54.152.164.184]
skipping: [52.91.121.42]

TASK [openshift_facts : Detecting Operating System] ****************************
skipping: [54.87.210.19]
skipping: [52.91.121.42]
skipping: [54.152.164.184]
skipping: [54.89.28.170]

TASK [openshift_facts : set_fact] **********************************************
skipping: [52.91.121.42]
skipping: [54.152.164.184]
skipping: [54.87.210.19]
skipping: [54.89.28.170]

TASK [openshift_facts : set_fact] **********************************************
skipping: [52.91.121.42]
skipping: [54.87.210.19]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [openshift_facts : Ensure PyYaml is installed] ****************************
skipping: [52.91.121.42]
skipping: [54.87.210.19]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [openshift_facts : Ensure yum-utils is installed] *************************
skipping: [54.87.210.19]
skipping: [52.91.121.42]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [openshift_facts : Gather Cluster facts and set is_containerized if needed] ***
skipping: [54.87.210.19]
skipping: [52.91.121.42]
skipping: [54.152.164.184]
skipping: [54.89.28.170]

TASK [rhel_subscribe : set_fact] ***********************************************
skipping: [54.152.164.184]
skipping: [54.89.28.170]
skipping: [54.87.210.19]
skipping: [52.91.121.42]

TASK [rhel_subscribe : fail] ***************************************************
skipping: [54.87.210.19]
skipping: [52.91.121.42]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [rhel_subscribe : fail] ***************************************************
skipping: [54.87.210.19]
skipping: [52.91.121.42]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [rhel_subscribe : fail] ***************************************************
skipping: [54.87.210.19]
skipping: [52.91.121.42]
skipping: [54.152.164.184]
skipping: [54.89.28.170]

TASK [rhel_subscribe : Satellite preparation] **********************************
skipping: [52.91.121.42]
skipping: [54.87.210.19]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [rhel_subscribe : RedHat subscriptions] ***********************************
skipping: [52.91.121.42]
skipping: [54.87.210.19]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [rhel_subscribe : Retrieve the OpenShift Pool ID] *************************
skipping: [52.91.121.42]
skipping: [54.87.210.19]
skipping: [54.152.164.184]
skipping: [54.89.28.170]

TASK [rhel_subscribe : Determine if OpenShift Pool Already Attached] ***********
skipping: [52.91.121.42]
skipping: [54.87.210.19]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [rhel_subscribe : fail] ***************************************************
skipping: [54.87.210.19]
skipping: [52.91.121.42]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [rhel_subscribe : Attach to OpenShift Pool] *******************************
skipping: [52.91.121.42]
skipping: [54.87.210.19]
skipping: [54.152.164.184]
skipping: [54.89.28.170]

TASK [rhel_subscribe : include] ************************************************
skipping: [52.91.121.42]
skipping: [54.87.210.19]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [openshift_facts : Verify Ansible version is greater than or equal to 1.9.4] ***
skipping: [54.87.210.19]
skipping: [52.91.121.42]
skipping: [54.152.164.184]
skipping: [54.89.28.170]

TASK [openshift_facts : Detecting Operating System] ****************************
skipping: [54.87.210.19]
skipping: [52.91.121.42]
skipping: [54.152.164.184]
skipping: [54.89.28.170]

TASK [openshift_facts : set_fact] **********************************************
skipping: [54.87.210.19]
skipping: [52.91.121.42]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [openshift_facts : set_fact] **********************************************
skipping: [54.87.210.19]
skipping: [52.91.121.42]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [openshift_facts : Ensure PyYaml is installed] ****************************
skipping: [54.87.210.19]
skipping: [52.91.121.42]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [openshift_facts : Ensure yum-utils is installed] *************************
skipping: [54.87.210.19]
skipping: [52.91.121.42]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [openshift_facts : Gather Cluster facts and set is_containerized if needed] ***
skipping: [54.87.210.19]
skipping: [52.91.121.42]
skipping: [54.89.28.170]
skipping: [54.152.164.184]

TASK [openshift_repos : assert] ************************************************
fatal: [54.87.210.19]: FAILED! => {"failed": true, "msg": "The conditional check 'not openshift.common.is_containerized | bool' failed. The error was: error while evaluating conditional (not openshift.common.is_containerized | bool): 'openshift' is undefined\n\nThe error appears to have been in '/home/vagrant/workspace/openshift-ansible/roles/openshift_repos/tasks/main.yaml': line 10, column 3, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n\n- assert:\n  ^ here\n"}
fatal: [52.91.121.42]: FAILED! => {"failed": true, "msg": "The conditional check 'not openshift.common.is_containerized | bool' failed. The error was: error while evaluating conditional (not openshift.common.is_containerized | bool): 'openshift' is undefined\n\nThe error appears to have been in '/home/vagrant/workspace/openshift-ansible/roles/openshift_repos/tasks/main.yaml': line 10, column 3, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n\n- assert:\n  ^ here\n"}
fatal: [54.89.28.170]: FAILED! => {"failed": true, "msg": "The conditional check 'not openshift.common.is_containerized | bool' failed. The error was: error while evaluating conditional (not openshift.common.is_containerized | bool): 'openshift' is undefined\n\nThe error appears to have been in '/home/vagrant/workspace/openshift-ansible/roles/openshift_repos/tasks/main.yaml': line 10, column 3, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n\n- assert:\n  ^ here\n"}
fatal: [54.152.164.184]: FAILED! => {"failed": true, "msg": "The conditional check 'not openshift.common.is_containerized | bool' failed. The error was: error while evaluating conditional (not openshift.common.is_containerized | bool): 'openshift' is undefined\n\nThe error appears to have been in '/home/vagrant/workspace/openshift-ansible/roles/openshift_repos/tasks/main.yaml': line 10, column 3, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n\n- assert:\n  ^ here\n"}

NO MORE HOSTS LEFT *************************************************************
        to retry, use: --limit @playbooks/aws/openshift-cluster/update.retry

PLAY RECAP *********************************************************************
52.91.121.42               : ok=3    changed=0    unreachable=0    failed=1
54.152.164.184             : ok=3    changed=0    unreachable=0    failed=1
54.87.210.19               : ok=3    changed=0    unreachable=0    failed=1
54.89.28.170               : ok=3    changed=0    unreachable=0    failed=1
localhost                  : ok=9    changed=7    unreachable=0    failed=0

ACTION [update] failed: Command 'ansible-playbook  -i inventory/aws/hosts -e 'cluster_id=origin-v3 cluster_env=dev deployment_type=origin' playbooks/aws/openshift-cluster/update.yml' returned non-zero exit status 2
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



