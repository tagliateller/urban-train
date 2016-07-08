# GCE

## Installation Cluster

ANSIBLE_HOST_KEY_CHECKING auf False setzen
GCE_INI_PATH setzen
Richtiges Zertifikat ermitteln und mit ssh-agent / ssh-add setzen
Richtigen SSH-User ermitteln und in die INI eintragen

Firewall-Rules in GCE nicht vergessen

bin/cluster create gce origin-v3

--> OK

## Aufruf Webconsole

--> OK

## Installation Authentification

ssh master
$ sudo yum -y install httpd-tools
sudo mkdir -p /etc/origin/master
sudo htpasswd -cb /etc/origin/master/htpasswd ${USERNAME} ${PASSWORD}
sudo vi /etc/origin/master/master-config.yaml

´´´
oauthConfig:
  assetPublicURL: https://104.155.33.50:8443/console/
  grantConfig:
    method: auto
  identityProviders:
  - challenge: true
    login: true
    mappingMethod: claim
    name: allow_all
    provider:
      apiVersion: v1
      kind: AllowAllPasswordIdentityProvider # HTPasswdPasswordIdentityProvider 
  masterCA: ca.crt
´´´

sudo systemctl restart origin-master.service
sudo systemctl status origin-master.service

--> OK

## Test

oc get nodes
oadm diagnostics

--> OK mit Fehler: Kein Zugriff auf master-config.yaml ??

## Install Registry

oadm registry --selector=type=infra

--> OK

## Install Ticketmonster

Beachte: git-branch 2.7.0.Final, directory /demo

### Export des Templates

https://docs.openshift.org/latest/dev_guide/templates.html#export-as-template

oc login # as project user
oc project tm # project wechseln
oc export all --as-template=ticketmonster > ticketmonster.template
--> hier im repo unter templates/


## Login in interne Registry

--> geht noch nicht lt. https://docs.openshift.org/latest/dev_guide/managing_images.html#accessing-the-internal-registry

[cloud-user@origin-dev-master-ba797 ~]$ oc whoami .t
john
[cloud-user@origin-dev-master-ba797 ~]$ oc whoami -t
zG_5VoUo6LJmn-NU3N-jqbVQLATaLkA8gH6q6fQNn3g
[cloud-user@origin-dev-master-ba797 ~]$ docker login -u john -e john@example.com -p zG_5VoUo6LJmn-NU3N-jqbVQLATaLkA8gH6q6fQNn3g 172.30.199.110:5000
Cannot connect to the Docker daemon. Is the docker daemon running on this host?
[cloud-user@origin-dev-master-ba797 ~]$ sudo docker login -u john -e john@example.com -p zG_5VoUo6LJmn-NU3N-jqbVQLATaLkA8gH6q6fQNn3g 172.30.199.110:5000
Error response from daemon: invalid registry endpoint "http://172.30.199.110:5000/v0/". HTTPS attempt: unable to ping registry endpoint https://172.30.199.110:5000/v0/
v2 ping attempt failed with error: Get https://172.30.199.110:5000/v2/: dial tcp 172.30.199.110:5000: i/o timeout
 v1 ping attempt failed with error: Get https://172.30.199.110:5000/v1/_ping: dial tcp 172.30.199.110:5000: i/o timeout. HTTP attempt: unable to ping registry endpoint http://172.30.199.110:5000/v0/
v2 ping attempt failed with error: Get http://172.30.199.110:5000/v2/: dial tcp 172.30.199.110:5000: i/o timeout
 v1 ping attempt failed with error: Get http://172.30.199.110:5000/v1/_ping: dial tcp 172.30.199.110:5000: i/o timeout


## Providing Applications across Env

https://blog.openshift.com/promoting-applications-across-environments/

## Neustart Cluster

--> wird durch neu vergebene IP verhindert. TODO !

## Login as Admin-User

sudo oc login -u system:admin -n default --config=/etc/origin/master/admin.kubeconfig

## Playbook htpasswd (dynamic inv)

inventory/gce/hosts/gce.py --list # OK
[vagrant@localhost paas]$ ansible-playbook -i inventory/gce/hosts playbooks/origin-set-htpasswd.yml
No handlers could be found for logger "libcloud.common.google"

ERROR! The file inventory/gce/hosts/gce.py is marked as executable, but failed to execute correctly. If this is not supposed to be an executable script, correct this with `chmod -x inventory/gce/hosts/gce.py`.
failed to parse executable inventory script results from /home/vagrant/workspace/paas/inventory/gce/hosts/gce.py: Syntax Error while loading YAML.


The error appears to have been in '<string>': line 4, column 24, but may
be elsewhere in the file depending on the exact syntax problem.

inventory/gce/hosts/gce.py:19: Error parsing host definition ''''': No closing quotation

OK - das wiederum geht:

[vagrant@localhost openshift-ansible]$ cd ..
[vagrant@localhost workspace]$ cd paas/
[vagrant@localhost paas]$ ansible-playbook -i ../openshift-ansible/inventory/gce/hosts playbooks/origin-set-htpasswd.yml

PLAY [tag_host-type-master] ****************************************************

TASK [setup] *******************************************************************
fatal: [origin-dev-master-ba797]: UNREACHABLE! => {"changed": false, "msg": "Failed to connect to the host via ssh.", "unreachable": true}
        to retry, use: --limit @playbooks/origin-set-htpasswd.retry

PLAY RECAP *********************************************************************
origin-dev-master-ba797    : ok=0    changed=0    unreachable=1    failed=0

[vagrant@localhost paas]$

???? WARUM ????

 






