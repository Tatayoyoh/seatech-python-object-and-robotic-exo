# seatech-python-object-and-robotic-exo

Exercices liés aux cours

## Créer son compte Github

https://github.com/signup

## Paramétrer son utilisateur Git

Créer un certificat SSH
```bash
ssh-keygen
# choisir la localisation par défaut /home/seatech/.ssh/id_rsa
# entrer votre mot de passe 2x
```

Afficher le certificat généré
```bash
cat /home/seatech/.ssh/id_rsa.pub
# copier le contenu affiché
```

Créer une nouvelle clé SSH sur Github ici : https://github.com/settings/keys

Coller le contenu du fichier `id_rsa.pub`, puis sauvegarder

## Paramétrer son utilisateur Git

```bash
git config --global user.name '<MON PSEUDO GITHUB>'
git config --global user.email '<MON EMAIL>'
```
