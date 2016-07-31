# Cloud Testing


## GCE

```bash
REM source ~/.gce/gce_credentials
source ~/.gce/gce_config
ODER
source ~/.gce_creds
export GCE_INI_PATH=~/.gce/gce.ini
eval `ssh-agent`
ssh-add ~/.ssh/google_compute_engine
ansible-playbook -i inventory/gce/hosts playbooks/gce/ticketmonster-classic-launch.yml -u cloud-user
ODER
ansible-playbook -i ../openshift-ansible/inventory/gce/hosts playbooks/gce/ticketmonster-classic-launch.yml -u cloud-user
```

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

die globalen Variablen gehen so noch nicht ...
[vagrant@localhost paas]$ ansible-playbook "-e 'num_dbsrvs=1 cluster_id=tm1'" -i ../openshift-ansible/inventory/aws/hosts/ec2.py playbooks/aws/ticketmonster-classic-launc
h.yml -u ec2-user --ask-vault

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

TASK [ticketmonster-dbsrv : Set root Password] *********************************
failed: [tm1-dbsrv-7a68b] (item=localhost) => {"failed": true, "item": "localhost", "msg": "unable to connect to database, check login_user and login_password are correct or /root/.my.cnf has the credentials. Exception message: (1045, \"Access denied for user 'root'@'localhost' (using password: YES)\")"}
failed: [tm1-dbsrv-7a68b] (item=127.0.0.1) => {"failed": true, "item": "127.0.0.1", "msg": "unable to connect to database, check login_user and login_password are correct or /root/.my.cnf has the credentials. Exception message: (1045, \"Access denied for user 'root'@'localhost' (using password: YES)\")"}
failed: [tm1-dbsrv-7a68b] (item=::1) => {"failed": true, "item": "::1", "msg": "unable to connect to database, check login_user and login_password are correct or /root/.my.cnf has the credentials. Exception message: (1045, \"Access denied for user 'root'@'localhost' (using password: YES)\")"}

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

## Unicorn Test

#sudo yum -y install ruby
#sudo yum -y group install "Development Tools"
#gem install unicorn

http://tecadmin.net/install-ruby-2-2-on-centos-rhel/#

### App-Server

```bash
[robert.bloy@instance-1 app]$ history
    1  sudo yum install gcc-c++ patch readline readline-devel zlib zlib-devel
    2  sudo yum -y install libyaml-devel libffi-devel openssl-devel make
    3  sudo yum -y install bzip2 autoconf automake libtool bison iconv-devel sqlite-devel
    4  sudo curl -sSL https://rvm.io/mpapis.asc | gpg --import -
    5  sudo curl -L get.rvm.io | bash -s stable
    6  curl -sSL https://rvm.io/mpapis.asc | gpg --import -
    7  curl -L get.rvm.io | bash -s stable
    8  source /etc/profile.d/rvm.sh
    9  source ~/.profile 
   10  source /etc/profile.d/rvm.sh
   11  rvm reload
   12  rvm requirements run
   13  rvm install 2.2.4
   14  rvm use 2.2.4 --default
   15  ruby --version
   16  gem install unicorn
   17  unicorn
   18  gem install rack
   19  unicorn
   20  mkdir app
   21  cd app/
   22  vi config.ru
   23  unicorn
   24  history
[robert.bloy@instance-1 app]$ 
```

```ruby
app = proc do |env|

  Math.sqrt rand
  [200, {}, %w(hello world)]
end
run app
```




