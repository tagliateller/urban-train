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

...

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




