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
| [Orchestratore](com.github.copilot/agents/angular-bootstrap-italia-orchestrator.agent.md) | angular-developer per lavoro Angular; angular-bootstrap-italia quando è coinvolto il contratto della libreria; modern-css e web-typography per lavoro visivo | Scelta degli specialisti, riuso, implementazione e controlli |
| [Angular Architect](com.github.copilot/agents/angular-architect.agent.md) | angular-developer | Riuso o creazione, architettura, stato, form, lifecycle, SSR e test |
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

Gli specialisti sono di sola lettura. L'orchestratore implementa secondo il
percorso selezionato e richiede sempre una revisione del risultato finale ai soli
specialisti necessari. CSS moderno e tipografia rispettano il design system
esistente e i contratti di Bootstrap Italia; non ne sostituiscono i componenti
con implementazioni alternative.

## Percorso breve e percorso completo

Dopo l'ispezione, l'orchestratore registra `Workflow: SIMPLE_FIX` oppure
`Workflow: STANDARD`, con una motivazione. La scelta del percorso è distinta
dalla scelta degli specialisti: una modifica complessa solo Angular continua a
coinvolgere soltanto Angular Architect.

| Percorso | Condizioni | Flusso |
| --- | --- | --- |
| SIMPLE_FIX | Fix locale in un solo dominio, causa chiara, risultato verificabile, design e contratti invariati | Skill obbligatorie → implementazione → controlli pertinenti → review dello specialista |
| STANDARD | Nuovi componenti, scelte progettuali, più domini, rischi o incertezze | Analisi degli specialisti necessari → implementazione → controlli → review |

Il percorso breve esclude modifiche a API pubbliche, contratti dei consumatori,
lifecycle, gestione asincrona/cancellazione, SSR, sicurezza/permessi, contratti
dei dati e comportamento accessibile. Esclude anche modifiche a dipendenze o
configurazione. Una riga di codice non rende automaticamente semplice una fix.
I criteri completi sono nel contratto comune.

Una correzione locale di un calcolo Angular può quindi richiedere **una sola
chiamata** all'Angular Architect, per la review finale, se passa al primo tentativo.
Una correzione di spaziatura locale può seguire lo stesso percorso con SCSS,
purché non alteri altri contratti. Un problema di disposal Bootstrap Italia
rimane STANDARD con Angular e Bootstrap Italia.

Se emergono rischi, il flusso passa a STANDARD: lo specialista segnala
`WORKFLOW_ESCALATION_REQUIRED`, oppure `SCOPE_EXPANSION_REQUIRED` se serve un
nuovo dominio. L'orchestratore acquisisce l'analisi necessaria prima di ulteriori
modifiche dipendenti e riconcilia il codice già scritto. La prima review del
percorso breve non richiede un inesistente report di analisi.

Restano obbligatori tutte le skill assegnate, le evidenze, la review del codice
effettivo e i controlli pertinenti, inclusa la build per il lavoro Angular.
I report contengono evidenze delle skill, risultati/criticità e validazioni,
senza sezioni estranee alla fix. Un controllo necessario indisponibile blocca
il completamento; una skill obbligatoria non usata fa fallire il task.
Il percorso breve riduce le chiamate preventive, non garantisce tempi o costi.

## Riuso e delega condizionale

Prima di creare, sostituire o estendere un componente, l'orchestratore cerca
componenti esistenti, wrapper, direttive ed esempi d'uso nel progetto. Angular
Architect valuta API, comportamento e impatto sui consumatori. La decisione
esplicita è: riusare invariato, comporre/estendere, usare markup/direttiva oppure
creare un nuovo componente. Una nuova creazione richiede una motivazione concreta;
una fix parte dall'implementazione esistente e non introduce astrazioni speculative.

L'orchestratore sceglie gli specialisti secondo il comportamento interessato:

| Lavoro | Specialisti |
| --- | --- |
| Fix di stato, service, routing o validazione Angular senza impatto su presentazione e contratto della libreria | Solo Angular Architect |
| Riuso di un componente esistente tramite API invariata, senza nuovo lavoro visivo | Solo Angular Architect |
| Fix di inizializzazione o cleanup di un'istanza Bootstrap Italia, senza cambiamenti visivi | Angular Architect + Bootstrap Italia Specialist |
| Spaziatura o layout di elementi dell'applicazione, senza dipendenze da contratti della libreria o integrazione Angular | Solo SCSS Specialist |
| Nuovo wrapper Angular con markup Bootstrap Italia e nuovo layout visibile | Tutti e tre |

Il fatto che Bootstrap Italia sia installato o che un componente esistente lo
usi internamente non basta a coinvolgere lo specialista della libreria. Il
contenuto della modifica conta più dell'estensione del file: una modifica solo
TypeScript può cambiare il lifecycle della libreria, mentre un binding HTML può
correggere soltanto la logica Angular.

Gli agenti non pertinenti non vengono chiamati neppure per confermare l'esclusione
o per la review finale. Le loro skill e i loro report non sono richiesti per quel
task. Ogni agente selezionato deve comunque leggere e applicare tutte le skill
assegnate. La mancata disponibilità di un agente necessario resta un fallimento.
Il pacchetto completo deve continuare a includere tutte e sei le skill.

La selezione viene ricalcolata anche per **ogni correzione**, indipendentemente
dagli agenti coinvolti all'inizio. Le review già accettate restano valide finché
non cambiano i comportamenti, i contratti o le dipendenze che hanno verificato:

| Difetto da correggere, con gli altri ambiti invariati | Agenti richiamati |
| --- | --- |
| Logica, stato o service Angular | Solo Angular Architect |
| Opzione pubblica Bootstrap Italia, senza impatto sull'integrazione Angular o sugli stili | Solo Bootstrap Italia Specialist |
| Spaziatura CSS/SCSS dell'applicazione | Solo SCSS Specialist |
| Lifecycle Angular collegato al disposal Bootstrap Italia | Angular Architect + Bootstrap Italia Specialist |

Conta l'impatto della correzione, non chi ha segnalato il difetto né la sola
estensione del file. Una review mai eseguita o fallita deve ancora essere
completata; una review accettata e non invalidata non richiede nuove conferme.
L'orchestratore passa al revisore il difetto, il diff della correzione e gli esiti
pertinenti, senza ricominciare l'intera analisi.

Ogni agente riutilizza le skill complete già disponibili e invariate nel proprio
contesto. Le rilegge se sono cambiate o non più disponibili; un nuovo contesto
deve comunque caricarle. Il riassunto di un altro agente non sostituisce le skill.
Si rieseguono i controlli mancanti, falliti o invalidati dalle modifiche: una
correzione SCSS può richiedere una nuova build senza richiamare Angular Architect.
Quando le review necessarie sono accettate e i controlli sono validi, il ciclo
termina senza un ulteriore giro di conferme.

Se durante analisi o review emerge una nuova dipendenza, l'orchestratore aggiorna
la selezione e acquisisce l'analisi mancante prima di accettare la modifica.
Build e test pertinenti rimangono obbligatori; una fix solo Angular non richiede
controlli visivi o di lifecycle Bootstrap Italia estranei al cambiamento.

## Esempio d'uso

Selezionare l'orchestratore nel progetto Angular e chiedere:

> Crea un componente card responsive basato su Bootstrap Italia, con titolo,
> descrizione e link Angular Router. Riutilizza i token del progetto. Verifica
> tastiera, focus e layout mobile. Esegui build e test pertinenti; riporta le
> evidenze delle skill usate da ciascuno specialista.

Per questa creazione il flusso STANDARD è: ispezione del progetto, scelta degli
specialisti, decisione di riuso, analisi dei domini coinvolti, implementazione,
controlli e review dei soli specialisti necessari. La fattibilità Bootstrap Italia viene
verificata quando il suo contratto è coinvolto. Versioni e API pertinenti si
verificano nel progetto; non vengono
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

1. La richiesta card sopra cerca prima componenti riutilizzabili e motiva la
   scelta. Se richiede un nuovo wrapper con markup Bootstrap Italia e layout,
   invoca i tre agenti reali con evidenze delle rispettive skill prima di
   modificare i file. Se trova un componente compatibile, ne usa l'API pubblica
   senza duplicarlo e coinvolge soltanto i domini effettivamente interessati.
2. La build e i test dell'applicazione sono eseguiti; gli specialisti revisionano
   i file finali e gli esiti. I controlli visivi mancanti risultano esplicitamente
   bloccanti, senza dichiarazioni di successo.
3. In una **copia di prova** del plugin, rendere indisponibile modern-css prima
   di una nuova sessione: il validatore del pacchetto fallisce e un task che
   richiede SCSS deve riportare FAILED, senza implementazione sostitutiva.
   Ripetere rendendo indisponibile un agente necessario. Una fix solo Angular
   non deve essere bloccata a runtime da una skill di un dominio non coinvolto.
4. Una richiesta non supportata dalle API pubbliche produce una spiegazione
   verificata e alternative; non genera patch della libreria o hack CSS.
5. Una fix locale di un calcolo Angular con causa nota, design, API, UI e
   integrazione della libreria invariati usa SIMPLE_FIX: solo Angular Architect
   in REVIEW dopo implementazione e controlli, senza ANALYSIS preventiva.
   Non legge le skill Bootstrap Italia/SCSS e non richiede i loro report.
   Esegue comunque build e verifiche di regressione pertinenti. Se la review
   passa, la traccia deve mostrare una sola invocazione specialistica.
6. Una fix inizialmente classificata Angular-only che rivela un problema di
   disposal Bootstrap Italia aggiunge lo specialista della libreria prima di
   proseguire. Non aggiunge SCSS se non emergono implicazioni visive.
7. Un componente condiviso simile ma incompatibile viene scartato con motivazione
   basata sui suoi contratti. Il nuovo componente ha una responsabilità distinta;
   un'estensione compatibile verifica invece i consumatori esistenti.
8. Dopo una prima implementazione che coinvolge tutti e tre gli specialisti,
   far emergere un difetto solo Angular: la correzione e la nuova review
   coinvolgono soltanto Angular Architect; le approvazioni valide degli altri
   due restano acquisite. Ripetere separatamente con un difetto solo SCSS e con
   un'opzione Bootstrap Italia senza impatto sugli altri ambiti. Verificare le
   invocazioni effettive, non solo il resoconto dell'orchestratore.
9. Dopo una correzione che cambia più domini, verificare che vengano richiamati
   tutti e soli gli specialisti interessati. Controllare che un test già passato
   venga ripetuto quando cambia un suo input e che non venga rilanciato su input
   invariati senza una nuova ragione. Una build dopo modifiche SCSS è pertinente.
10. Nello stesso contesto con skill complete e invariate, verificare che non
    vengano rilette solo per una nuova fase. In un nuovo contesto, verificare
    invece il caricamento delle skill obbligatorie. Non considerare questo
    comportamento garantito dai soli test statici del pacchetto.

11. Una fix locale di spaziatura su un elemento dell'applicazione, senza impatto
    su geometria della libreria, binding, semantica o comportamento accessibile,
    usa SIMPLE_FIX con sola review SCSS. Mantiene tutte e quattro le sue skill,
    diagnostica tipografica compatta e controlli di layout pertinenti; non
    avvia un audit dell'intera applicazione.
12. Una modifica di una riga a focus, API pubblica o lifecycle usa STANDARD:
    non salta l'analisi perché il diff è piccolo. Se il rischio emerge durante
    una review SIMPLE_FIX, questa segnala l'escalation; il flusso acquisisce
    l'analisi mancante prima di proseguire, senza coinvolgere domini estranei.
13. Nel percorso breve, una review con skill mancante/non usata produce FAILED
    senza approvazione sostitutiva dell'orchestratore. Un controllo necessario
    non eseguibile produce BLOCKED; una build fallita impedisce PASSED.
14. Una prima review individua un difetto locale: viene corretta e riesaminata
    solo l'area interessata, con i controlli invalidati ripetuti. Non si promette
    una sola chiamata quando il primo risultato richiede correzioni.

Per confrontare con la versione precedente, usare lo stesso task e stato iniziale
dell'applicazione in sessioni nuove, con modello e ambiente uguali. Annotare
correttezza del risultato, chiamate per fase/dominio, letture delle skill,
verifiche duplicate su input invariati, durata e consumo mostrato dall'host.
Confrontare sia fix semplici sia un componente completo; meno chiamate non basta
se si perdono difetti o si dichiara successo con controlli mancanti.

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
