# Kaggle Groups - Guida alla Collaborazione

> Come creare e usare gruppi per condividere risorse con il tuo team.

---

## Overview

I gruppi permettono di condividere facilmente risorse Kaggle (notebook, dataset, modelli) con un gruppo di membri.

### Differenza tra Groups e Organizations

| Aspetto | Groups | Organizations |
|---------|--------|---------------|
| Scopo | Collaborazione | Vetrina pubblica |
| Ownership risorse | Mai | Sì |
| Visibilità | Privati | Pubblici |
| Invito | Solo invito | Pubblico |

---

## Creare un Gruppo

### Steps

1. Login su Kaggle
2. Click avatar → "Your Groups"
3. Click "New Group"

### Informazioni Richieste

| Campo | Descrizione |
|-------|-------------|
| **Name** | Nome del gruppo |
| **URL** | URL unico (basato sul nome) |
| **Description** | Visibile ai membri |

---

## Invitare Membri

### Metodo 1: Link di Invito

1. Vai al tab "Invite"
2. Attiva "Invite via link"
3. Condividi il link
4. Chi clicca diventa **member**

⚠️ **Attenzione**: Chiunque con il link può unirsi. Non condividere in forum pubblici!

### Metodo 2: Invito Diretto

1. Vai al tab "Invite"
2. Inserisci username Kaggle
3. Scegli ruolo: **member** o **admin**
4. Click "Send invites"

L'utente riceve email + notifica Kaggle.

### Reinviare Inviti

1. Vai al gruppo
2. Seleziona "Pending Members"
3. Click "More" → "Resend invitation"

---

## Ruoli e Permessi

### Owner

| Azione | Permesso |
|--------|:--------:|
| Condividere risorse | ✅ |
| Aggiungere/rimuovere membri | ✅ |
| Modificare info gruppo | ✅ |
| Trasferire ownership | ✅ |
| Eliminare gruppo | ✅ |

### Admin

| Azione | Permesso |
|--------|:--------:|
| Condividere risorse | ✅ |
| Aggiungere/rimuovere membri | ✅ |
| Modificare info gruppo | ✅ |
| Edit link sharing | ✅ |
| Trasferire ownership | ❌ |
| Eliminare gruppo | ❌ |

### Member

| Azione | Permesso |
|--------|:--------:|
| Condividere proprie risorse | ✅ |
| Aggiungere membri | ❌* |
| Modificare info gruppo | ❌ |

*Può solo condividere link se abilitato

### Modificare Permessi

- Owner e Admin possono modificare ruoli in qualsiasi momento
- Per diventare member, l'owner deve prima trasferire ownership

---

## Condividere Risorse

### Come Condividere

1. Vai alla risorsa (notebook, dataset, model)
2. Sezione "Collaborators"
3. Cerca nome del gruppo
4. Scegli permessi:
   - **Can View**: Solo visualizzazione
   - **Can Edit**: Può modificare
   - **Can Administrate**: Controllo completo

### Notifiche

I membri ricevono notifica quando una risorsa viene condivisa.

**Gestire notifiche:**
- Per gruppo singolo: tab "Settings" del gruppo
- Tutte le notifiche: "Settings" → "Notifications"

### Trovare Risorse Condivise

Vai su "Your Work" → "All of Your Work"

Puoi filtrare/cercare per trovare items condivisi.

---

## Privacy dei Gruppi

- I gruppi sono **privati** e **solo su invito**
- NON appaiono in ricerche o directory
- Altri vedono solo il nome del gruppo se condividi una risorsa con loro

---

## FAQ

### Come Trasferire Ownership?

1. Vai al tab "People"
2. Seleziona un membro
3. Dropdown ruolo → "Transfer Ownership"

⚠️ Azione permanente!

### Posso Avere Più Gruppi?

Sì, puoi creare e partecipare a più gruppi.

### Cosa Succede se Lascio un Gruppo?

Le risorse che hai condiviso rimangono condivise con il gruppo.

---

## Use Cases per Team AI

### Team di Competizione

```
Gruppo: "Titanic Team"
├── Notebook: EDA condiviso (Can Edit)
├── Notebook: Feature Engineering (Can Edit)
├── Notebook: Model Training (Can Edit)
└── Dataset: Preprocessed Data (Can View)
```

### Workflow Consigliato

1. **Crea gruppo** per la competizione
2. **Invita** tutti i teammates
3. **Condividi** notebook con "Can Edit"
4. **Itera** insieme sul codice
5. **Condividi** risultati finali

### Organizzazione Risorse

```
Gruppo: "AI Team Knowledge Base"
├── Models/
│   ├── BERT Fine-tuned (Can View)
│   └── Custom CNN (Can View)
├── Datasets/
│   ├── Training Data v1 (Can View)
│   └── Augmented Data (Can View)
└── Notebooks/
    ├── Best Practices (Can View)
    └── Competition Templates (Can Edit)
```

---

## Best Practices

1. **Nomi Descrittivi**: "Competition-X-Team" non "Group1"
2. **Permessi Minimi**: Dai "Can View" di default, "Can Edit" solo se necessario
3. **Documenta**: Usa la descrizione del gruppo per spiegare scopo e regole
4. **Organizza**: Crea gruppi separati per scopi diversi
5. **Pulisci**: Rimuovi membri inattivi periodicamente

---

## Link Utili

- [Your Groups](https://www.kaggle.com/groups) - Gestisci i tuoi gruppi
- [Documentation](https://www.kaggle.com/docs/groups)

---

*Documento per Team AI - Collabora efficacemente con il tuo team!*
