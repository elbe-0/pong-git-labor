# Git-Labor: Pong

In diesem Labor üben Sie den Git- und GitHub-Workflow an einem kleinen, bereits lauffähigen Pong-Spiel.
Sie müssen kaum programmieren. Im Mittelpunkt stehen die **Git-Befehle**.

| | Inhalt | Arbeitsform | Zeit |
|---|---|---|---|
| Aufgabe 1 | Branch, Commit, Push, Pull Request, Review, Merge | Zweierteam (Person A und Person B) | ca. 30 Minuten |
| Aufgabe 2 | Merge-Konflikt lösen | Einzelarbeit | ca. 15 Minuten |

---

## 0. Vorbereitung (bitte vor dem Labor erledigen)

1. Legen Sie einen **GitHub-Account** an: <https://github.com/signup>
2. Prüfen Sie, ob **Git** installiert ist: `git --version`
3. Prüfen Sie, ob **Python mit Tk** installiert ist: `python3 -m tkinter` (unter Windows: `py -m tkinter`).
   Es muss sich ein kleines Fenster öffnen. Falls nicht:
   - macOS (Homebrew): `brew install python-tk`
   - Linux: `sudo apt install python3-tk`
   - Windows: Python von python.org erneut installieren und dabei „tcl/tk and IDLE“ auswählen
4. Hinterlegen Sie einmalig Ihren Namen und Ihre E-Mail-Adresse für Git:
   ```bash
   git config --global user.name "Vorname Nachname"
   git config --global user.email "ihre-github-email@example.com"
   ```
5. Melden Sie sich bei GitHub an, damit `git push` funktioniert (eine Anmeldung per Passwort ist dort nicht mehr möglich):
   - Windows: Git for Windows öffnet beim ersten Push automatisch eine Anmeldung im Browser.
   - macOS und Linux: Installieren Sie die [GitHub CLI](https://cli.github.com) und führen Sie `gh auth login` aus
     (Auswahl: GitHub.com, HTTPS, Login with a web browser).

## Spiel starten

```bash
python3 pong.py      # unter Windows: py pong.py
```

Linker Schläger: **W** und **S**. Rechter Schläger: **Pfeil nach oben** und **Pfeil nach unten** (sobald Aufgabe 1 gelöst ist).

---

## Aufgabe 1: Zweiten Spieler freischalten (Zweierteam)

Der rechte Schläger lässt sich noch nicht bewegen. Person B ergänzt die Steuerung auf einem Feature-Branch.
Person A prüft die Änderung und übernimmt sie per Pull Request in `main`.

Ersetzen Sie in den folgenden Befehlen `A-NAME` durch den GitHub-Benutzernamen von Person A.

### Schritt 1 (Person A): Team-Repository anlegen

1. Klicken Sie oben auf dieser Seite auf **Use this template** und dann auf **Create a new repository**.
   Name: `pong-team`, Sichtbarkeit: **Public**.
2. Laden Sie Person B ein: **Settings > Collaborators > Add people**.
3. Schützen Sie den Branch `main`: **Settings > Branches > Add classic branch protection rule**.
   Tragen Sie als Branch name pattern `main` ein, aktivieren Sie **Require a pull request before merging** und klicken Sie auf **Create**.
   Danach kann niemand mehr direkt auf `main` pushen. Änderungen gelangen nur noch über einen Pull Request dorthin.
4. Klonen Sie das Repository und starten Sie das Spiel:
   ```bash
   git clone https://github.com/A-NAME/pong-team.git
   cd pong-team
   python3 pong.py
   ```

### Schritt 2 (Person B): Feature entwickeln

1. Nehmen Sie die Einladung an: <https://github.com/A-NAME/pong-team/invitations>
2. Klonen Sie das Repository und legen Sie einen Feature-Branch an:
   ```bash
   git clone https://github.com/A-NAME/pong-team.git
   cd pong-team
   git switch -c feature/right-paddle
   ```
3. Ergänzen Sie in `pong.py` die Funktion `on_key()` an der mit `TODO` markierten Stelle.
   Die Steuerung des linken Schlägers direkt darüber können Sie als Vorlage verwenden.
   Die Tasten heißen `"up"` und `"down"`, der rechte Schläger heißt `right`.
4. Testen Sie das Spiel: `python3 pong.py`
5. Sehen Sie sich Ihre Änderung an und committen Sie sie:
   ```bash
   git status
   git diff
   git add pong.py
   git commit -m "Rechten Schläger mit Pfeiltasten steuern"
   ```
6. Laden Sie den Branch auf GitHub hoch:
   ```bash
   git push -u origin feature/right-paddle
   ```
7. Auf GitHub erscheint ein gelber Hinweis. Klicken Sie auf **Compare & pull request**, tragen Sie rechts unter **Reviewers** Person A ein und klicken Sie auf **Create pull request**.

### Schritt 3 (Person A): Review und Merge

1. Holen Sie den Branch von Person B und probieren Sie ihn lokal aus:
   ```bash
   git fetch
   git switch feature/right-paddle
   python3 pong.py
   ```
2. Öffnen Sie den Pull Request auf GitHub und geben Sie ihn frei: **Files changed > Review changes > Approve > Submit review**.
3. Führen Sie den Merge durch: **Merge pull request > Confirm merge**. Löschen Sie anschließend den Branch mit **Delete branch**.
4. Aktualisieren Sie Ihren lokalen Branch `main` und sehen Sie sich die Historie an:
   ```bash
   git switch main
   git pull
   git log --oneline --graph
   ```

### Schritt 4 (Person B): Aufräumen

```bash
git switch main
git pull
git branch -d feature/right-paddle
```

**Die Aufgabe ist gelöst, wenn** sich bei beiden Personen auf `main` der rechte Schläger mit den Pfeiltasten bewegen lässt.

**Zusatzaufgabe:** Tauschen Sie die Rollen. Person A ändert auf einem neuen Branch zum Beispiel die Farbe des Balls (`fill="#facc15"`), Person B prüft den Pull Request und führt den Merge durch.

---

## Aufgabe 2: Merge-Konflikt lösen (Einzelarbeit)

Zwei Personen haben unabhängig voneinander eine Punkteanzeige programmiert:

- Der Branch `score-left` zeigt nur die Punkte des **linken** Spielers an.
- Der Branch `score-right` zeigt nur die Punkte des **rechten** Spielers an.

Beide haben **dieselbe Zeile** verändert. Führen Sie die beiden Branches so zusammen,
dass die Anzeige beide Punktestände enthält, zum Beispiel `3 : 2` (links : rechts).

Diese Aufgabe bearbeiten Sie nur lokal. Sie benötigen dafür kein eigenes Repository und pushen nichts.

1. Klonen Sie das Original-Repository in einen neuen Ordner (**nicht** innerhalb von `pong-team`):
   ```bash
   cd ..
   git clone https://github.com/elbe-0/pong-git-labor.git pong-merge
   cd pong-merge
   ```
2. Sehen Sie sich die Branches an und wechseln Sie auf `score-left`:
   ```bash
   git branch -a
   git switch score-left
   git log --oneline --graph --all
   python3 pong.py
   ```
3. Führen Sie den anderen Branch mit einem Merge in `score-left` zusammen:
   ```bash
   git merge origin/score-right
   ```
   Git meldet: `CONFLICT (content): Merge conflict in pong.py`
4. Prüfen Sie den aktuellen Zustand:
   ```bash
   git status
   ```
5. Öffnen Sie `pong.py` in einem Editor und suchen Sie die Stelle mit den Konfliktmarkierungen:
   ```
   <<<<<<< HEAD
   ... Version aus score-left ...
   =======
   ... Version aus score-right ...
   >>>>>>> origin/score-right
   ```
   Schreiben Sie eine Zeile, die **beide** Punktestände anzeigt, und löschen Sie alle drei Markierungszeilen.
6. Testen Sie das Spiel: `python3 pong.py`. Werden beide Punktestände angezeigt und bei einem Punktgewinn erhöht?
7. Markieren Sie den Konflikt als gelöst und schließen Sie den Merge ab:
   ```bash
   git add pong.py
   git commit --no-edit
   git log --oneline --graph
   ```

**Die Aufgabe ist gelöst, wenn** `git status` die Meldung „nothing to commit, working tree clean“ ausgibt und das Spiel beim Start `0 : 0` anzeigt.

---

## Hilfe bei typischen Problemen

| Problem | Lösung |
|---|---|
| Ein Editor mit `~`-Zeilen öffnet sich (vim). | `Esc` drücken, dann `:wq` eingeben und mit Enter bestätigen. |
| `ModuleNotFoundError: No module named '_tkinter'` | Siehe Vorbereitung, Punkt 3. |
| `git push` meldet *Permission denied* oder *403*. | Wurde die Einladung angenommen? Sind Sie bei GitHub angemeldet (Vorbereitung, Punkt 5)? |
| `git push` meldet *protected branch*. | Das ist so gewollt. Arbeiten Sie nicht direkt auf `main`, sondern auf einem Feature-Branch. |
| Sie haben versehentlich auf `main` committet. | `git switch -c feature/right-paddle` ausführen. Der Commit ist dann auch auf dem neuen Branch vorhanden. |
| Sie möchten den Merge-Konflikt noch einmal von vorn lösen. | `git merge --abort` ausführen (nur während eines laufenden Merges möglich). |
