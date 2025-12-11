# Vibe Code with Gemini 3 Pro - Competition Guide

> Hackathon Google DeepMind su Kaggle - $500,000 in premi

---

## Overview

| Info | Dettaglio |
|------|-----------|
| **Nome** | Vibe Code with Gemini 3 Pro in AI Studio |
| **Host** | Google DeepMind |
| **Piattaforma** | Kaggle |
| **Premio Totale** | $500,000 in Gemini API credits |
| **Premio per Vincitore** | $10,000 in API credits (Top 50 vincitori) |
| **Validità Crediti** | 1 anno dopo emissione |
| **Durata** | 7 giorni |
| **Inizio** | 5 Dicembre 2025 (5:00 PM UTC) |
| **Scadenza** | 12 Dicembre 2025 (11:59 PM UTC) |
| **Judging** | 13 Dic 2025 - 12 Gen 2026 |
| **Vincitori** | Inizio 2026 |
| **Link** | [kaggle.com/competitions/gemini-3](https://www.kaggle.com/competitions/gemini-3) |
| **Partecipanti** | 16,358 iscritti, 1,084 submission |
| **Team Max** | 5 persone |
| **Submission Max** | 1 per team |

---

## REGOLA FONDAMENTALE: Google AI Studio è OBBLIGATORIO

**Google AI Studio è l'UNICO punto di ingresso GRATUITO per questa competizione.**

### Cosa DEVI fare:
- Costruire l'app in [aistudio.google.com/build](https://aistudio.google.com/build)
- Generare il link pubblico cliccando "Share" dentro AI Studio
- Il link "Share App" è l'UNICO formato di submission accettato

### Cosa NON puoi fare:
- Submittare un'applicazione esterna costruita solo con API
- Usare solo Gemini CLI o API senza AI Studio
- Hostare il codice altrove (AI Studio è il compiler E l'hosting)

### Puoi usare Antigravity/VSCode?
**Sì**, ma il codice finale DEVE essere copiato in AI Studio e funzionare lì per generare il link "Share App".

### Backend e Database Esterni?
**Sì**, puoi connetterti a API esterne. AI Studio è client-side e non hosta codice server-side. I giudici valutano l'intera esperienza dell'app, non solo il frontend.

---

## Come Funziona AI Studio Build

1. Vai su [aistudio.google.com/build](https://aistudio.google.com/build)
2. Inserisci la tua idea in linguaggio naturale
3. Si apre un ambiente di coding AI
4. Puoi vedere preview, codice e fare modifiche
5. **Gemini 3 Pro Preview è il modello di default**

### Video Tutorial Ufficiali:
- [Overview vibe coding in AI Studio](https://www.youtube.com/watch?v=DePOMEBfvWQ)
- [Annotation Mode](https://www.youtube.com/watch?v=FyTB1vmgM00)
- [Vibe Code with your voice](https://www.youtube.com/watch?v=ZHpT3ev2XLA)
- [App Gallery for inspiration](https://www.youtube.com/watch?v=wByGcxJFRxk)

### Gallery Templates:
[aistudio.google.com/apps?source=showcase&showcaseTag=gemini-3](https://aistudio.google.com/apps?source=showcase&showcaseTag=gemini-3)

---

## Rate Limits e Free Tier

### Errore 429: RESOURCE_EXHAUSTED
Se vedi questo errore, hai raggiunto il rate limit del Free Tier.

**Controlla il tuo utilizzo**: [aistudio.google.com/usage?tab=rate-limit](https://aistudio.google.com/usage?tab=rate-limit)

### La Soluzione:
- C'è un limite **per minuto** e **per giorno**
- Di solito basta aspettare 1 minuto per il reset del limite breve
- Il limite giornaliero si resetta a **mezzanotte**

### Strategia Ibrida (CONSIGLIATA):
- Usa **Gemini 3 Pro** per il reasoning principale e la logica core
- Usa **Gemini 2.5 Flash** per task di supporto ad alto volume:
  - Processing di testo semplice
  - Text-to-Speech (TTS)
  - Task di background

Questo approccio "ibrido" permette di costruire app robuste dentro i limiti del Free Tier!

### NON serve carta di credito!
Non hai bisogno di un progetto a pagamento per usare Gemini 3 Pro in questa competizione. Se hai problemi con API Key, vai nelle impostazioni e assicurati di usare il Free Tier.

---

## Categorie (Track)

| Categoria | Descrizione |
|-----------|-------------|
| **Science** | Accelerare scoperte e ricerca |
| **Education** | Reinventare l'apprendimento |
| **Accessibility** | Strumenti che funzionano per tutti |
| **Health** | Migliorare vite e cura pazienti |
| **Business** | Reinventare workflow e obiettivi |
| **Technology** | Spingere i limiti del codice |

---

## Criteri di Valutazione

| Criterio | Peso | Descrizione |
|----------|------|-------------|
| **Impact** | 40% | Risolve un problema reale? Visione ispiratrice? Potenziale per cambiamento positivo? |
| **Technical Depth & Execution** | 30% | Funziona? Usa efficacemente Gemini 3 (multimodalità, reasoning, context)? È reale e non fake? |
| **Creativity** | 20% | Idea originale? Usa Gemini 3 in modi nuovi? Quante capacità usi e come funzionano insieme? |
| **Presentation Quality** | 10% | Video coinvolgente? Racconta una storia? Mostra bene il prodotto? Ha potenziale virale? |

### IMPORTANTE:
- I giudici vogliono vedere il **"WOW factor"**
- Il **VIDEO è la lente principale** di valutazione
- Il Writeup e l'app servono come verifica e profondità tecnica
- "Show, don't just tell" - Dimostra, non solo descrivere!

---

## Requisiti Submission (OBBLIGATORI)

### Devi Creare un Kaggle Writeup con:

#### 1. Writeup su Kaggle
- Summary di **COSA** stai submittando
- **COME** l'hai creato (con link all'app AI Studio)
- **PERCHÉ** è importante e l'impatto che crea
- Seleziona una track/categoria
- Titolo, sottotitolo e immagine thumbnail
- **MAX 250 parole** (penalità se superi)
- Scritto in [Markdown](https://github.com/showdownjs/showdown/wiki/Showdown's-Markdown-syntax)

#### 2. Video Demo (ALLEGATO OBBLIGATORIO)
- **Durata**: MAX 2 minuti (solo i primi 2 min vengono valutati!)
- **Visibilità**: Pubblico (YouTube, X/Twitter, Loom, etc.)
- **Accesso**: Visualizzabile senza login
- **Licenze**: Tutti i materiali devono essere ridistribuibili
- **Tip**: Fai impatto nei primi secondi!

#### 3. Link App AI Studio Pubblica (ALLEGATO OBBLIGATORIO)

**Come pubblicare l'app:**
1. In AI Studio Build, clicca **"Save"** in alto a destra
2. Clicca **"Share app"**
3. Nel popup: abilita **"Publish your app"** e **"Default to full screen"** ← **OBBLIGATORIO**
4. Copia il link e allegalo al Writeup

**TUTTI i link devono essere pubblici, senza login o paywall!**

---

## Come Submittare

1. Vai su [Writeups della competizione](https://www.kaggle.com/competitions/gemini-3/writeups)
2. Clicca **"New Writeup"**
3. Compila tutti i campi
4. Allega video demo (come link)
5. Allega link app AI Studio pubblica
6. Clicca **"Submit"** in alto a destra

**ATTENZIONE**:
- Writeup non submittati o in bozza alla deadline NON verranno considerati!
- Se alleghi risorse Kaggle private, diventano pubbliche dopo la deadline

---

## Judges

| Nome | Ruolo |
|------|-------|
| **Omar Sanseviero** | Developer Experience Lead, Google DeepMind |
| **Amit Vadi** | Developer Experience, Google DeepMind |
| **Paige Bailey** | AI DevEx, Google |
| **Seth Odoom** | Product Manager, Google AI Studio |
| **Joana Carrasqueira** | Vibe Coding Lead, Google DeepMind |

---

## Rules Importanti

### Eligibility
- 18+ anni
- NO residenti di: Crimea, DNR, LNR, Cuba, Iran, Syria, North Korea
- NO persone sotto sanzioni USA

### Team
- Max 5 persone per team
- 1 sola submission per team
- Puoi lavorare da solo

### Licenza Vincitori
- Se vinci, la tua submission sarà sotto licenza **CC BY 4.0**
- Devi poter redistribuire tutto il contenuto

### Dataset
- NON è fornito dataset dalla competizione
- Puoi usare QUALSIASI dataset pubblico
- Devi avere permesso di usarlo

---

## FAQ Ufficiali (da Discussion)

### Posso usare altri modelli oltre Gemini 3 Pro?
**Sì!** Il criterio "Technical Depth" cerca l'uso di Gemini 3 Pro per la logica core, ma puoi usare altri modelli (es. Gemini 2.5 Flash) per task di supporto.

### Posso usare Veo 3 per video?
Veo 3 richiede un progetto a pagamento. Per il Free Tier, usa alternative o fallback con immagini.

### I crediti premio scadono?
Sì, **1 anno** dopo l'emissione.

### C'è un certificato di partecipazione?
**No**, ma sei incoraggiato a condividere pubblicamente quello che hai costruito.

### Posso usare file .env per API esterne?
Da chiarire con gli organizzatori - alcuni utenti hanno chiesto nella discussion.

---

## PROGETTO DA CREARE: Agentic Workflow Architect

### Categoria: Technology

### Idea
Ricreare "Agentic Workflow Architect" in AI Studio:
- Input: scenario in linguaggio naturale
- Output: sistema multi-agente con definizioni e workflow

### Come Fare in AI Studio

1. **Vai su** [aistudio.google.com/build](https://aistudio.google.com/build)

2. **Prompt iniziale** (esempio):
```
Build a web app called "Agentic Workflow Architect" that:
- Takes a natural language description of a business process or task
- Uses Gemini 3 Pro to decompose it into specialized AI agents
- Generates for each agent: name, role description, capabilities, and operational prompt
- Shows a visual workflow diagram of how agents interact
- Allows editing each agent's details inline
- Exports the complete multi-agent system as Markdown or JSON
- Has a modern dark UI with animated cards for each agent
- Includes example scenarios to get started
```

3. **Itera con Gemini 3** per aggiungere features

4. **Pubblica**:
   - Save → Share app → Enable "Publish" + "Full screen"
   - Copia il link

5. **Registra video demo** di 2 minuti max

6. **Crea Writeup** su Kaggle (max 250 parole) e **SUBMIT**

---

## Timeline

| Data | Ora | Attività |
|------|-----|----------|
| **11 Dic** | Oggi | Creare app in AI Studio, testare, iterare |
| **12 Dic** | Prima delle 23:59 UTC | Registrare video, scrivere writeup, **SUBMIT** |

---

## Checklist Finale

- [ ] App creata in Google AI Studio Build
- [ ] Usa Gemini 3 Pro per la logica core
- [ ] App pubblicata con "Publish your app" + "Default to full screen"
- [ ] Link app funzionante e pubblico (no login)
- [ ] Video demo MAX 2 minuti, pubblico, senza login
- [ ] Writeup su Kaggle con MAX 250 parole
- [ ] Track/categoria selezionata
- [ ] Titolo, sottotitolo, thumbnail aggiunti
- [ ] Video allegato al Writeup
- [ ] Link app AI Studio allegato al Writeup
- [ ] Cliccato **"SUBMIT"** prima della deadline!

---

## Link Utili

| Risorsa | URL |
|---------|-----|
| **Competizione** | [kaggle.com/competitions/gemini-3](https://www.kaggle.com/competitions/gemini-3) |
| **AI Studio Build** | [aistudio.google.com/build](https://aistudio.google.com/build) |
| **Gallery Templates** | [aistudio.google.com/apps](https://aistudio.google.com/apps?source=showcase&showcaseTag=gemini-3) |
| **Controlla Rate Limits** | [aistudio.google.com/usage](https://aistudio.google.com/usage?tab=rate-limit) |
| **Writeups** | [kaggle.com/competitions/gemini-3/writeups](https://www.kaggle.com/competitions/gemini-3/writeups) |
| **Discussion** | [kaggle.com/competitions/gemini-3/discussion](https://www.kaggle.com/competitions/gemini-3/discussion) |
| **Rules** | [kaggle.com/competitions/gemini-3/rules](https://www.kaggle.com/competitions/gemini-3/rules) |

---

*Documento aggiornato con info ufficiali da Kaggle + FAQ dalla Discussion*
*Scadenza: 12 Dicembre 2025 - 23:59 UTC*
*Progetto: Agentic Workflow Architect → Technology Category*
