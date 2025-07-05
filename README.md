# 🎞️ AsciiGifPlayer

Transforme un GIF animé en **ASCII coloré** directement dans ton **terminal**.  
Parfait pour des intros stylées dans tes scripts Python ou juste pour le fun en ligne de commande.

---

## 📦 Fonctionnalités

- 🖼️ Conversion GIF -> ASCII couleur (truecolor ANSI)
- 📏 Redimension automatique pour le terminal
- 🔁 Lecture en boucle personnalisable
- 🧼 Nettoyage automatique du terminal entre les frames
- ⚙️ Facile à intégrer dans n'importe quel script Python

---

## 🧑‍💻 Installation

Installe la dépendance nécessaire :

```bash
pip install pillow
```
## ⚙️ Exemple d'utilisation dans un script Python

```python
from ascii_gif_player import AsciiGifPlayer

player = AsciiGifPlayer(
    gif_path="chemin/vers/ton.gif",
    width=80,           # Largeur du GIF en caractères
    frame_delay=0.05,   # Délai entre les frames (secondes)
    loop=2              # Nombre de boucles (répétitions)
)
player.play()
```
---

## 📜 Licence

Ce projet est sous licence **MIT** — tu peux l'utiliser, le modifier et le partager librement.  
Aucune restriction, tant que tu mentionnes l’auteur original.

---

## ✨ Créé par

**Gab12online ⚡**  
📺 page : [Gab12Online](https://gab12online.pages.dev/%E2%97%84)

---

## ⭐ Supporte le projet

Si tu aimes ce projet :

- Laisse une ⭐ sur le repo
- Partage-le à tes amis
- Utilise-le dans tes scripts pour un style rétro cool 😎

---

Merci d’avoir utilisé **AsciiGifPlayer** !
