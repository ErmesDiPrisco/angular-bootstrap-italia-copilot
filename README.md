# Angular Bootstrap Italia Copilot

Plugin per GitHub Copilot che coordina tre specialisti per creare e revisionare
componenti Angular basati su Bootstrap Italia. L'agente da selezionare è
**Angular Bootstrap Italia Orchestrator**.

## Installazione in VS Code

Usare una versione di VS Code e GitHub Copilot che supporti Agent Plugins 1.0 e
custom subagents. Abilitare i plugin e registrare **la radice completa** del
repository nelle impostazioni utente, sostituendo il percorso di esempio:

```json
{
  "chat.plugins.enabled": true,
  "chat.pluginLocations": {
    "C:/percorso/angular-bootstrap-italia-copilot": true
  }
}
```

Aprire il progetto Angular destinatario e una nuova chat. Nelle personalizzazioni
verificare quattro agenti e sei skill; nel selettore utente deve comparire
l'orchestratore, mentre i tre specialisti sono riservati alla delega. Controllare
eventuali errori nella diagnostica delle personalizzazioni.

Non basta aprire questo repository: la cartella `com.github.copilot/agents/` è
caricata come parte del plugin. Non copiare soltanto gli agenti in `.github/agents`:
i collegamenti relativi alle skill e al contratto comune richiedono il pacchetto
completo. [Documentazione ufficiale dei plugin VS Code](https://code.visualstudio.com/docs/agent-customization/agent-plugins).

Il progetto Angular deve avere dipendenze installate, script di build/test e
l'accesso ai tool necessari. Il plugin non include Angular, Bootstrap Italia o
un browser runner e non modifica automaticamente le impostazioni personali.

## Copilot CLI e altri host

Il formato è riconosciuto anche da Copilot CLI:

```sh
copilot plugin install /percorso/angular-bootstrap-italia-copilot
copilot plugin list
```

La disponibilità dei tool e della delega dipende dall'host. Verificare il test
operativo descritto sotto prima di usare il plugin in un nuovo host; il caricamento
del pacchetto da solo non certifica il workflow. GitHub.com e altri IDE non sono
implicitamente certificati da questa configurazione.
[Riferimento ufficiale Copilot CLI](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference).

## Agenti, skill e responsabilità

| Agente | Skill di dominio obbligatorie | Ruolo |
| --- | --- | --- |
| [Orchestratore](com.github.copilot/agents/angular-bootstrap-italia-orchestrator.agent.md) | angular-developer, angular-bootstrap-italia; modern-css e web-typography per lavoro visivo | Delega, implementazione, esecuzione dei controlli |
| [Angular Architect](com.github.copilot/agents/angular-architect.agent.md) | angular-developer | Architettura, stato, form, lifecycle, SSR e test |
| [Bootstrap Italia Specialist](com.github.copilot/agents/bootstrap-italia-specialist.agent.md) | angular-bootstrap-italia | API pubbliche, markup, accessibilità, fattibilità |
| [SCSS Specialist](com.github.copilot/agents/scss-specialist.agent.md) | modern-css, web-typography | Stili, responsive, token, tipografia |

Tutti leggono e applicano anche Ponytail Full e Caveman Ultra. Le skill sono
incluse in [skills](skills/): non occorre installarle separatamente o inizializzare
`external/` per usare il plugin. `refactoring-ui` e `top-design` sono riferimenti
facoltativi upstream, non dipendenze incluse.

Il [contratto di esecuzione](com.github.copilot/execution-contract.md) impone la
lettura dei file reali e delle referenze pertinenti, con evidenze per ogni skill.
Una skill obbligatoria assente, non letta o non applicata rende il task **FAILED**.
Le sole frasi “skill usata” non bastano. Una ripetizione correttiva deve effettuare
il lavoro mancante; non può limitarsi ad aggiungere una conferma.

Gli specialisti sono di sola lettura. L'orchestratore implementa dopo le analisi
accettate e richiede una revisione del risultato finale. I nuovi componenti
visibili coinvolgono tutti e tre gli specialisti. CSS moderno e tipografia
rispettano il design system esistente e i contratti di Bootstrap Italia; non ne
sostituiscono i componenti con implementazioni alternative.

## Esempio d'uso

Selezionare l'orchestratore nel progetto Angular e chiedere:

> Crea un componente card responsive basato su Bootstrap Italia, con titolo,
> descrizione e link Angular Router. Riutilizza i token del progetto. Verifica
> tastiera, focus e layout mobile. Esegui build e test pertinenti; riporta le
> evidenze delle skill usate da ciascuno specialista.

Il flusso è: ispezione del progetto, analisi Angular e Bootstrap Italia,
verifica della fattibilità, analisi SCSS/tipografia, implementazione, controlli,
review degli specialisti. Versioni e API si verificano nel progetto; non vengono
aggiornate automaticamente. L'assenza di un controllo necessario impedisce di
dichiarare il risultato completo.

## Verifica del pacchetto

Python 3.10+ è necessario solo per questi controlli di manutenzione:

```sh
python -m pip install -r scripts/requirements-validation.txt
python scripts/validate-plugin.py
python -m unittest discover -s scripts -p "test_*.py"
```

Il validatore controlla manifest essenziale, YAML, identità degli agenti,
permessi dei tool, deleghe, collegamenti locali, sei skill e metadati Git copiati
per errore. Segue le referenze Markdown raggiungibili dalle istruzioni; non
verifica URL remoti, anchor Markdown o la validità tecnica di tutti gli esempi
upstream. Non è una validazione completa dello schema Agent Plugins né esegue
Copilot. I test includono i casi negativi di agente duplicato, skill/referenza
mancante e permessi errati.

Con PowerShell disponibile vengono eseguiti anche tre test della sincronizzazione
in cartelle temporanee isolate: sorgente mancante, `-WhatIf`, copia da una directory
di lavoro diversa senza metadati Git. Senza PowerShell questi tre test sono skipped.

Prima di distribuire, assicurarsi che tutti i file del pacchetto siano inclusi
nel commit/archivio, in particolare `skills/modern-css/`. Eseguire il validatore
anche sul checkout o archivio destinato ai colleghi: i file locali non tracciati
non arrivano automaticamente in un'installazione da Git.

## Test operativo prima dell'adozione

In un'applicazione Angular di prova, verificare:

1. La richiesta card sopra invoca i tre agenti reali, ciascuno con letture e
   applicazioni verificabili delle proprie skill, prima di modificare i file.
2. La build e i test dell'applicazione sono eseguiti; gli specialisti revisionano
   i file finali e gli esiti. I controlli visivi mancanti risultano esplicitamente
   bloccanti, senza dichiarazioni di successo.
3. In una **copia di prova** del plugin, rendere indisponibile modern-css prima
   di una nuova sessione: il validatore fallisce e il task deve riportare FAILED,
   senza implementazione sostitutiva. Ripetere rendendo indisponibile un agente.
4. Una richiesta non supportata dalle API pubbliche produce una spiegazione
   verificata e alternative; non genera patch della libreria o hack CSS.

Registrare versioni di VS Code/Copilot, modello, Angular e Bootstrap Italia,
tracce di delega, comandi e risultati. Il protocollo è basato su istruzioni:
le autodichiarazioni non possono garantire da sole il comportamento del modello.
I controlli statici non sostituiscono questo collaudo nell'host reale.

## Manutenzione delle skill

[sync-skills.ps1](scripts/sync-skills.ps1) serve solo ai manutentori con le sorgenti
upstream disponibili in `external/`, come indicato da `.gitmodules`. Prima della
sincronizzazione controllare eventuali modifiche locali: le copie in `skills/`
vengono sostituite. Lo script valida tutte le sorgenti prima di rimuovere le copie
e non distribuisce i loro metadati Git. Dopo la sincronizzazione rieseguire i
controlli e revisionare i cambiamenti delle istruzioni upstream.

Per vedere prima le operazioni previste:

```powershell
./scripts/sync-skills.ps1 -WhatIf
```

La licenza del codice del plugin è [MIT](LICENSE); le skill di terzi conservano
le proprie licenze e attribuzioni: [fonti e avvisi](THIRD_PARTY_NOTICES.md).
