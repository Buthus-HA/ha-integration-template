# Modèle d'intégration Home Assistant (Buthus-HA)

Dépôt modèle : **Use this template → Create a new repository**, puis suivre la checklist.

## Checklist après création

1. Choisir le *domain* (minuscules, `_` autorisés, unique) — ex. `meteo_stand`.
2. Renommer `custom_components/mon_integration/` en `custom_components/<domain>/`.
3. Remplacer partout `mon_integration` par `<domain>`, `Mon intégration` par le vrai nom
   et `ha-mon-integration` par le nom du dépôt :
   ```bash
   grep -rl "mon_integration\|Mon intégration\|ha-mon-integration" . --exclude-dir=.git \
     | xargs sed -i "s/mon_integration/<domain>/g; s/Mon intégration/<Nom>/g; s/ha-mon-integration/<depot>/g"
   ```
4. Sur GitHub : renseigner la **description** et des **topics** (ex. `home-assistant`, `hacs`) — exigés par la validation HACS.
5. Remplacer ce README par la doc de l'intégration.

## Publier une version

1. Mettre à jour `version` dans `manifest.json` (seul endroit) et ajouter une section dans `CHANGELOG.md`.
2. Committer, puis : `git tag v0.2.0 && git push --follow-tags`
3. Le workflow **Release** vérifie que le tag correspond au manifest et crée la release ; HACS la propose ensuite dans HA.

## Développement

```bash
pip install pytest-homeassistant-custom-component home-assistant-frontend
pytest -q
```
Le workflow **Validate** lance hassfest, la validation HACS et les tests à chaque push.

Règles d'or : tout en `async` (jamais de `requests` ni de `time.sleep`), aucun secret dans le dépôt,
les identifiants passent par le formulaire de configuration.
