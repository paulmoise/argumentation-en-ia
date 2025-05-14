# 🧠 Argumentation en IA – TP de calcul des sémantiques

Ce projet a été réalisé dans le cadre d’un TP sur l’**argumentation en intelligence artificielle**. Il consiste à concevoir et implémenter un algorithme capable de déterminer les **ensembles d’arguments acceptables** dans un graphe d’argumentation selon différentes **sémantiques formelles**.

## 🗂️ Contenu

- Implémentation de l’algorithme de calcul des **extensions argumentatives**
- Support des sémantiques :
  - **Sémantique ancrée** (*grounded semantics*)
  - **Sémantique complète** (*complete semantics*)
  - **Sémantique préférée** (*preferred semantics*)
- Prise en charge :
  - Des graphes **sans cycle**
  - Des graphes **avec cycle**

## 📥 Format d’entrée

Le graphe d’argumentation est fourni sous forme déclarative :

```prolog
arg(a).
arg(b).
arg(c).
att(a,b).
att(b,c).
```

Les nœuds (`arg(x)`) sont les arguments abstraits, et les arcs (`att(x,y)`) représentent une attaque de `x` vers `y`.

## ✅ Objectif

Pour un graphe donné, retourner les **extensions acceptables** selon les différentes sémantiques. Exemple de sortie attendue :

```txt
Extension CO semantics : {a, c}
Extension GR semantics : {a, c}
Extension PR semantics : {a, c}
```

## 🔍 Détails des étapes

### Étape 1 — Graphes sans cycle

- Parcours des arguments et construction des ensembles admissibles
- Calcul des extensions selon les sémantiques GR, CO et PR

### Étape 2 — Graphes avec cycle

- Détection de cycles
- Calcul partiel ou total des extensions selon les contraintes de chaque sémantique

## 📄 Rapport

Un court rapport de 2 pages accompagne ce projet, détaillant :
- La conception de l’algorithme
- Les principales étapes de l’implémentation
- Quelques cas de test illustratifs

## 📅 Deadline initiale

11 avril 2023 (TP universitaire)

## 🚀 Lancement (exemple Python)

```bash
python grounded_sematic.py
```

## 🧠 Références

- Dung, P.M. (1995). On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning, Logic Programming and n-Person Games.
- Cours d’IA – Université d’Avignon (2023)
