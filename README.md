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

-e "num_dbsrvs=1" usw. sollte gehen

$ ansible-playbook -e "num_dbsrvs=1 num_appsrvs=1 num_checkmksrvs=1 num_jmeterclts=1 num_devclts=1 cluster_id=tm1 ssh_key_name=acer_controller_box" -i ../openshift-ansible/inventory/aws/hosts/ec2.py playbooks/aws/ticketmonster-classic-launch.yml -u centos --ask-vault

TODO: Wie kann im Playbook die Adresse des App-Servers ermittelt werden ? test-appsrv ...

fatal: [54.153.89.195]: FAILED! => {"changed": false, "failed": true, "msg": "path /usr/share/apache-jmeter-3.0/bin/report-template/sbadmin2-1.0.7/bower_components/datatables/media/images/Sorting icons.psd does not exist", "path": "/usr/share/apache-jmeter-3.0/bin/report-template/sbadmin2-1.0.7/bower_components/datatables/media/images/Sorting icons.psd", "stat": {"exists": false}, "state": "absent"}

TODO: Hier muss bei appsrv die DataSource auf die MariaDB-Source umgelenkt werden. AUßerdem fehlt der Treiber für MariaDB !
[centos@ip-172-31-11-137 demo]$ less target/classes/META-INF/persistence.xml
[centos@ip-172-31-11-137 demo]$ less target/ticket-monster/WEB-INF/ticket-monster-ds.xml


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

TASK [ticketmonster-appsrv : add remote user] **********************************
fatal: [52.90.170.138]: FAILED! => {"changed": true, "cmd": ["bin/add-user.sh", "john", "remote"], "delta": "0:00:00.400656", "end": "2016-08-05 16:11:19.020783", "failed": true, "rc": 1, "start": "2016-08-05 16:11:18.620127", "stderr": "Exception in thread \"main\" java.lang.IllegalStateException: JBAS015232: No java.io.Console available to interact with user.\n\tat org.jboss.as.domain.management.security.AddPropertiesUser.<init>(AddPropertiesUser.java:100)\n\tat org.jboss.as.domain.management.security.AddPropertiesUser.<init>(AddPropertiesUser.java:111)\n\tat org.jboss.as.domain.management.security.AddPropertiesUser.main(AddPropertiesUser.java:155)\n\tat sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)\n\tat sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)\n\tat sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)\n\tat java.lang.reflect.Method.invoke(Method.java:606)\n\tat org.jboss.modules.Module.run(Module.java:260)\n\tat org.jboss.modules.Main.main(Main.java:291)", "stdout": "", "stdout_lines": [], "warnings": []}

In the same breadth, the --silent=true option in add-user.sh does not work anymore. Again has to do with the need for "theConsole" object being null.
--> ggf. true weglassen

Monitoring-Agent nicht vergessen. Das setzt voraus,  dass checkmk bereits installiert ist.

http://ec2-54-153-50-144.us-west-1.compute.amazonaws.com/ticketmonster/check_mk/agents/check-mk-agent-1.2.8p9-1.noarch.rpm
sudo yum localinstall ...

TODO Security-Group muss 6556 freischalten

## MariaDB

TODO: Anbindung an JBoss

https://github.com/PCextreme/ansible-role-mariadb

TASK [ticketmonster-dbsrv : Set root Password] *********************************
failed: [tm1-dbsrv-7a68b] (item=localhost) => {"failed": true, "item": "localhost", "msg": "unable to connect to database, check login_user and login_password are correct or /root/.my.cnf has the credentials. Exception message: (1045, \"Access denied for user 'root'@'localhost' (using password: YES)\")"}
failed: [tm1-dbsrv-7a68b] (item=127.0.0.1) => {"failed": true, "item": "127.0.0.1", "msg": "unable to connect to database, check login_user and login_password are correct or /root/.my.cnf has the credentials. Exception message: (1045, \"Access denied for user 'root'@'localhost' (using password: YES)\")"}
failed: [tm1-dbsrv-7a68b] (item=::1) => {"failed": true, "item": "::1", "msg": "unable to connect to database, check login_user and login_password are correct or /root/.my.cnf has the credentials. Exception message: (1045, \"Access denied for user 'root'@'localhost' (using password: YES)\")"}

### Performance / TPCC

#### AWS CentOS 7 t2.micro

```bash

sudo yum -y update
sudo yum -y install mariadb-server mariadb mariadb-devel mariadb-lib git
sudo systemctl start mariadb
sudo systemctl enable mariadb
sudo systemctl status mariadb

git clone https://github.com/tagliateller/tpcc-mysql.git
sudo yum -y groupinstall "Development Tools"
cd ~/tpcc-mysql/src
make

sudo mysqladmin create tpcc1000
cd ..
sudo mysql tpcc1000 < create_table.sql
./tpcc_load -h 127.0.0.1 -d tpcc1000 -u root -p "" -w 1000
```
### Einhängen des Volumens und Einspielen Backup

```bash
[centos@ip-172-31-12-214 ~]$ lsblk
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
xvda    202:0    0  250G  0 disk 
└─xvda1 202:1    0  250G  0 part /
xvdf    202:80   0   80G  0 disk 
[centos@ip-172-31-12-214 ~]$ sudo file -s /dev/xvdf
/dev/xvdf: Linux rev 1.0 ext4 filesystem data, UUID=f9e49a0b-a949-4c7d-acb6-435cd8a8e70d (extents) (64bit) (large files) (huge files)
[centos@ip-172-31-12-214 ~]$ sudo mkdir /backup
[centos@ip-172-31-12-214 ~]$ sudo mount /dev/xvdf /backup
[centos@ip-172-31-12-214 ~]$ ls /backup/
lost+found  tpcc1000_backup_ohne_indizes.sql
[centos@ip-172-31-12-214 ~]$ less /backup/tpcc1000_backup_ohne_indizes.sql 
[centos@ip-172-31-12-214 ~]$ mysql -u root -p -D tpcc1000 < /backup/tpcc1000_backup_ohne_indizes.sql 
Enter password: 
```

### Anpassung Config-Dateien

TODO

### Ausführung Tests

```bash
./tpcc_start -h127.0.0.1 -dtpcc1000 -uroot -p -w1000 -c32 -r10 -l10800 > ~/tpcc-output-ps-55-bpool-256.log
```

## Facts

ansible -i lab-inventory rdo-server.priv.tagliateller.nu -m setup

## OMD

https://github.com/sfromm/ansible-omdistro.git

Beachte bei Zugriff auf WebUI: http://sysadminsjourney.com/content/2010/02/01/apache-modproxy-error-13permission-denied-error-rhel/

Security-Group muss 80 freischalten

TODO: Anlegen eines Ordners in "Hosts"
Host eintragen und service discovery starten

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

Problem mit Samples: tat wird lokal gebaut und dann auf remote dir entpackt, am besten mal separat testen

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

# JMeter

To run Apache JMeter in NON_GUI mode and generate a report at end :
Open a command prompt (or Unix shell) and type:

jmeter.bat(Windows)/jmeter.sh(Linux) -n -t test-file [-p property-file] [-l log-file] -e -o [Path to output folder]

Konkreter Test: 
cd /usr/share/jmeter
bin/jmeter -n -t tests (tests ist das aktuelle Testfile, ggf. hier mehrere kopieren)

für einen Testlauf wie folgt vorgehen:
1. Datenbank IP ermitteln
2. IP der DB in JBoss eintragen (standalone kopieren)
3. JBoss neu starten
4. Testfiles kopieren
5. Test ausführen
6. Reportfile zurückübertragen



