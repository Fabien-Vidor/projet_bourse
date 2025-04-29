# 📈 Projet Bourse - Pipeline de Données Temps Réel

Ce projet vise à construire un pipeline de données pour collecter, traiter et diffuser en temps réel des informations boursières, économiques, technologiques et politiques via Apache NiFi, Kafka et des scripts Python.

## 🚀 Objectifs

- Collecter les **cours de bourse** via `yfinance` et `yahooquery`
- Extraire les **actualités financières** via des **flux RSS**
- Automatiser l'ingestion avec **Apache NiFi**
- Router les données en streaming via **Kafka**
- Déployer le tout dans un environnement **Dockerisé**

---



### 1. Cloner le repo

git clone https://github.com/Fabien-Vidor/projet_bourse.git
cd projet_bourse
### 2. Créer un environnement virtuel Python

python -m venv venv
venv\Scripts\activate  
### 3. Installer les dépendances

pip install -r requirements.txt
### 4. Lancer les services avec Docker
docker-compose up -d

NiFi : http://localhost:8080/nifi