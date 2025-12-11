# Kaggle Organizations - Guida Completa

> Come creare, usare e gestire profili organizzazione su Kaggle.

---

## Overview

Chiunque può creare un profilo organizzazione su Kaggle. Le organizzazioni permettono di trovare dataset, modelli e competizioni del tuo team in un unico posto.

### Cosa SONO le Organizzazioni

- Landing page per contenuti pubblicati
- Link unico per condividere tutto il lavoro del team
- Vetrina per dataset, modelli e competizioni

### Cosa NON SONO le Organizzazioni

- **NON** sono tool di collaborazione
- Per collaborare usa [Kaggle Groups](https://www.kaggle.com/groups)
- I membri NON possono gestire contenuti degli altri

---

## Chi Dovrebbe Usarle

| Chi | Uso Consigliato |
|-----|-----------------|
| Research Labs | Organizzare modelli e dataset pubblicati |
| Aziende | Mostrare competizioni hostate |
| Università | Landing page per pubblicazioni |
| Professori | Usa **Groups** invece (più adatto per classi) |

---

## Creare un'Organizzazione

### Step 1: Richiesta

1. Login su Kaggle
2. Compila [Organization Request Form](https://www.kaggle.com/contact#/organizations/request-creation)

### Informazioni Richieste

| Campo | Descrizione |
|-------|-------------|
| **Name** | Nome dell'organizzazione |
| **URL** | Slug corto (apparirà in tutti i link) |
| **Moderation Details** | Prove esistenza, scopo, tuo ruolo |

### Dopo Creazione (Configurabili)

- **Overview**: Bio/descrizione lunga
- **Tagline**: Descrizione breve
- **Website**: URL sito web
- **Image**: Logo 400x400px

### Step 2: Review

La richiesta viene revisionata dal team Kaggle.

**Domande/Appelli**: [kaggle.com/contact](https://www.kaggle.com/contact#/other/issue)

### Step 3: Approvazione

Riceverai email/notifica. Potrai:
- Creare dataset/modelli/competizioni come organizzazione
- Rendere contenuti pubblici
- Invitare membri

---

## Permessi dei Membri

### Membri

| Azione | Permesso |
|--------|:--------:|
| Creare dataset/modelli/competizioni come org | ✅ |
| Vedere contenuti privati di altri | ❌ |
| Modificare/eliminare contenuti di altri | ❌ |
| Vedere competizioni non lanciate | ❌ |
| Aggiungere nuovi membri | ❌* |

*Solo se l'owner condivide il link di invito

### Admin

Tutto ciò che possono fare i membri, PIÙ:
- Aggiungere/rimuovere membri
- Trasferire ownership
- Modificare info organizzazione (logo, tagline, etc.)

---

## Creare Contenuti come Organizzazione

### Competizioni

1. Click "+Create" → "Competition"
2. Scegli organizzazione da "Creating As" dropdown
3. Il logo org appare nella competizione
4. La competizione appare nel tab "Competitions" della org

**Nota**: Altri membri NON possono vedere/gestire la tua competizione.

### Dataset e Modelli

1. Click "+Create" → "Dataset" o "Model"
2. Scegli organizzazione da "Creating As"
3. Appare nel tab corrispondente della org page

**Nota**: Per dare accesso ad altri membri, aggiungili come collaboratori nelle Settings.

### Trasferire Risorse

1. Vai alla detail page della risorsa
2. Settings → Sharing → "Transfer Ownership"
3. Seleziona organizzazione
4. Click "Done"

⚠️ **Irreversibile!** Non puoi tornare indietro.

---

## Model Gating per Organizzazioni

### Cos'è

Richiedi agli utenti di:
- Accettare agreement specifico
- Fornire informazioni
- Prima di accedere al modello

### Setup

1. Contatta Kaggle per permessi
2. Abilita gating nel tab "Settings" del modello
3. Configura in YAML:
   - Review mode (automatic/manual)
   - Privacy policy URL
   - Agreement content
   - Form fields

### Gestire Consent

#### Via UI
Gestisci approvazioni dalla pagina del modello.

#### Via API

**List Consents**
```
GET /api/v1/models/{owner_slug}/{model_slug}/user-consents
    ?review_status=pending|accepted|rejected
    &is_user_request_data_expired=true|false
    &next_page_token=...
```

**Review Consent**
```
POST /api/v1/models/{owner_slug}/{model_slug}/user-consents/review
Body: {
    "user_name": "username",
    "review_status": "accepted",
    "publisher_notes": "optional"
}
```

**Auth**: HTTP Basic con `KAGGLE_USERNAME:KAGGLE_KEY`

---

## Best Practices

### Per Team AI

1. **Crea organizzazione** per il team
2. **Pubblica modelli** fine-tuned come org
3. **Documenta** con model cards complete
4. **Condividi competizioni** vinte
5. **Usa gating** per modelli con licenze speciali

### Visibilità

- Logo professionale 400x400px
- Tagline chiara e descrittiva
- Overview dettagliato con:
  - Chi siete
  - Focus areas
  - Link a risorse esterne

---

## Link Utili

- [Crea Organizzazione](https://www.kaggle.com/contact#/organizations/request-creation)
- [Kaggle Groups](https://www.kaggle.com/groups) - Per collaborazione
- [Model Gating JSON Schema](https://www.kaggle.com/model-gating-json-schema)

---

*Documento per Team AI - Costruisci la tua presenza professionale su Kaggle!*
