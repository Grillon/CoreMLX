#!/usr/bin/env bash
# C'est une base pour installer / desinstaller des binaires
# a venir:
# autoriser la base en parametres 
base="${2:-$HOME/Documents/Exercices/GroupIA/CoreMLX/llama.cpp/build/bin}"
base="${base#$HOME}"
base="${HOME}${base}"
base="${base%/}"
base="${base}/"
cible="${HOME}/.local/bin/"
if [ "$1" == "-i" ];then
action="install"
elif [ "$1" == "-u" ];then
action="uninstall"
else 
echo "permet d'installer les binaires dans $cible ou de les desinstaller"
echo "$0 -u: uninstall; $0 -i: install"
echo "optionnel un second argument peut-être le dossier des binaires buildés"
echo "$0 -i $HOME/outils/llama.cpp/build/bin/"
exit 1
fi
for fichier_source in ${base}*
do 
  fichier_cible=${fichier_source#$base}
  if [ "${fichier_cible}" != "mybin.sh" ] && [ -x ${fichier_source} ];then
    if [ $action == "install" ];then
      echo "install -m 755 ${base}${fichier_cible} ${cible}${fichier_cible}"
      install -m 755 ${base}${fichier_cible} ${cible}${fichier_cible}
    elif [ $action == "uninstall" ];then
      echo "rm -f ${cible}${fichier_cible}"
      rm -f ${cible}${fichier_cible}
    fi
  else 
    echo "pas ${fichier_cible}"
  fi
done
