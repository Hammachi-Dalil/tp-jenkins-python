from app import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2
```

---

**Étape C — Récupérer l'URL du dépôt**

Sur la page de votre dépôt GitHub, cliquez **"Code" → copiez l'URL HTTPS**, elle ressemble à :
```
https://github.com/votre-username/tp-jenkins-python.git
