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








