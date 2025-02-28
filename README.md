# Vuln-rabilit-Scan-Tool-
Un scanner de vulnérabilités détecte les failles de sécurité sur un réseau ou un système. Le projet implique de scanner les machines sur une plage d’IP, de vérifier les ports et services ouverts, d’identifier les vulnérabilités connues et de générer un rapport des failles détectées.
Un scanner de vulnérabilités permet d'identifier les failles de sécurité sur un réseau ou un système.

Plan du projet : Scanner de vulnérabilités
Scanner les machines connectées sur une plage d’IP.
Scanner les ports ouverts et identifier les services associés.
Détecter les versions des services et vérifier les vulnérabilités connues.
Générer un rapport des failles trouvées.
Technologies utilisées
Python (Automatisation)
nmap (Détection des services et des ports)
CVE API (Recherche des vulnérabilités connues)
SQLite (Stockage des résultats)
Flask ou Tkinter (Interface utilisateur, si besoin).

Structure du projet :

vulnerability_scanner/
│── scanner.py            
Fichier principal
│── network_scanner.py   
Scan des machines actives
│── port_scanner.py        
Scan des ports ouverts
│── vulnerability_checker.py  Vérification des vulnérabilités
│── report_generator.py    Génération du rapport

Cela va :
✅ Scanner la plage réseau 192.168.1.0/24
✅ Trouver les machines actives
✅ Identifier les ports ouverts et services actifs
✅ Vérifier les vulnérabilités connues
✅ Générer un rapport CSV

On peut modifier la plage d'Ip à notre guise.
