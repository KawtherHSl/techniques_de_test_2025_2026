RETEX - TP Techniques de Techniques de test
1. Introduction

L’objectif de ce projet était de développer un microservice Triangulator capable de récupérer des points depuis le PointSetManager, calculer leur triangulation et répondre via une API HTTP.  Mon rôle principal a été de mettre en place un ensemble de tests pour assurer la fiabilité, la justesse, la performance et la qualité du code.

Le TP m’a permis de travailler sur différents types de tests : unitaires, d’intégration, API, performance, ainsi que la gestion des erreurs et la couverture du code.

2. Ce que j’ai bien fait

Tests unitaires robustes pour le décodage des points et l'encodage des triangles :

    Verifier les données correctes et incorrectes.

    Gestion des cas particuliers comme points vides ou incomplets.

Tests d’intégration avec requests_mock :

    Simulation de PointSetManager pour vérifier la communication avec le Triangulator sans avoir besoin de réseau réel.

Tests d’API HTTP :

    Vérification des réponses correctes (200), et données non trouvées (404).

Tests de performance :

    Mesure du temps de décodage pour 1000 points et triangulation pour 2000 points.

Qualité et couverture du code :

   Utilisation de coverage pour mesurer la couverture.

   ruff pour assurer la qualité et la conformité des règles de coding.

Gestion des erreurs : 

   Données malformées, PointSet vide, invalides.

Ces tests ont permis de garantir la stabilité et la robustesse du service dans différents scénarios.

3. Difficultés rencontrées

 Format binaire : Comprendre comment encoder et décoder correctement les points et les triangles.

 Cas géométriques particuliers : points alignés (aucun triangle possible), carré (2 triangles), grande quantité de points.

 Performance : Assurer que le décodage et la triangulation restent rapides pour de grands ensembles de points.

 Tests automatisés : Prévoir tous les cas possibles avant même de commencer l’implémentation (“test first”).

4. Ce que j’aurais fait différemment

   Ajouter de tests pour des ensembles de points plus complexes.

   Optimiser l’algorithme de triangulation pour les ensembles très volumineux.

   Ajuster certaines fonctionnalités pour augmenter la compréhension et la facilité de maintenance du code.

5. Conclusion 

Ce TP m’a permis de renforcer mes compétences en tests unitaires et intégration, et le mocking avec requests_mock. comprendre mieux les formats binaires et conversion de données entre binaire et liste Python, utiliser des API REST avec Flask et communication entre microservices et mesurer performance et robustesse du code, ainsi que couverture de code et qualité.
