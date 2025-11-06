Objectif: Ce plan donne une idée sur la startégie chosie pour tester le code qui a le role de récupérer des points depuis un service "PointSetManager" et calculer leur triangulation. le but de ces tests est d'assurer la fiabilité et le bon finctionnement du code.

1) Tests unitaires:
   1.1. tester le décodage des points: La fonction attends une sortie comme : {(1.0, 1.0), (1.2 ,2.0), (4.0, 5.0)}, si elle reçoit des données incomplets ou mal formées elle lance une exception au lieu de planter le code.
   Comment : on écrit un test automatique une foction qui prend un flux bianire en entrée et compare avec la liste attendu s'il y a une erreur elle declenche une exception.
   pourquoi:ce teste garantie que le module parsing binaire fonctionne correctement et prend bien en charge les erreurs des formats sans bloquer le focntionnement du code.
   
   1.2.  Tetser l'ncodage de triangle: la focntion prend en entré une liste des triangles par exemple : [(1,2,3)] càd nous avons un seul triangle avec les points 1 2 3, et esaie de convertir ce triangle en format binaire.
   comment: on écrit un test automatique qui prend la liste des triangle en entrée et compare avec le flux binaire attendue, si ce n'est pas conforme elle déclenche une exception.
   pourquoi: ce teste nous montre si l'ecnodage fonctionne correctemet.
   
   1.3. Tester le calcul de triangulation:
   comment: dans ce cas on teste avec plusieur types de points ( 3 points alignés ce quoi donne un triangles, 4 points qui forment un carré ce qui donne 2 triangles, et des points alignés qui donne aucun triangle), on passe ces 3 cas au calcul triangulations (la focntion de triangulation) et on observe les résultats et on les compares avce les résultats attendus.
   pourquoi: ce teste nous garantit le bon fonctionnement  de la logique géométrique de l'algorithme.

2) Tests d'intégration:
   2.1. simulation de PointSetManager avec un mock http: pour vérifier si le triangulator récupère correctement le pointset auprès du PointSetManager depuis l'API et en utilisant la bonne URL avce le bon PointSetID.
      comment : utiliser des request-mock pour simuler les réponses de PointSetManager.
   pourquoi: pour tester que les micros services communiquet entre eux sans avoir besoin de réseau réel.

3) Tests de l'api triangulator (http): c'est pour vérifier si le triangulator réponds bien au requettes http.
   comment: on simule l'envoie des requettes vers l'api pour vérifier les réponses avec un client test par exemple si la réponse est 200: réponse binaire contient les triangles calculés, 400: signal des données non valides (problème de format ou mauvaises requettes) et 404: données non trouvées. 
   pourquoi: vérifier la conformité du service REST et assurer que l'api respecte les bonnes réponses et gère bien les erreurs.

4) Test de performance: c'est pour mesurer le temps de décodage et de triangulation.
   comment: on teste tous d'abord avec 10 points puis 100 points et on fini ce teste par les 1000 points et on mesure le temps avec une fonction de timing.
   pourquoi: ce test permet de detecter les obstacles qui limite la performance et le fonctionnment de notre code et de garantir la stabilité du système meme avec un volume tres grand.
   
6) Test de qualité: dans ce cas on utilise setPoint vide ou pointSetManager non disponible.
   comment: on simule des entrées anormales innatendues et on observe le focntionnement des exceptions.
   pourquoi: pour garantir la stabilité du système avec des envènements innatendus et assurer le traitement des erreurs sans bloquer le focntionnement du code.
   
   
   




   
   
