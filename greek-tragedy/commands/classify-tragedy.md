---
description: Classify a Greek tragedy as Apollonian, Dionysiac, or a mixture using Nietzsche's aesthetic framework
argument-hint: "<tragedy title> [by <playwright>]"
---

# /classify-tragedy -- Greek Tragedy Aesthetic Classifier

Classify a Greek tragedy (or group of tragedies) as **Apollonian**, **Dionysiac**, or a **mixture** using the aesthetic framework from Nietzsche's *The Birth of Tragedy* (1872).

## Philosophy

*The categories are abstract. They describe the spirit of the form -- how the formal elements behave -- never the mythological furniture or the content they represent.*

A tragedy is not Dionysiac because it **depicts** ecstasy, madness, or dissolution. A tragedy is Dionysiac because its **formal elements themselves become ecstatic, dissolving, or boundary-breaking** -- even when their ostensible subject would not demand it. Conversely, a tragedy is Apollonian not because it depicts order, but because its formal elements **maintain measure, balance, and individuation** -- even when describing terrible or chaotic events.

The classification lives in the **spirit** of the chorus's verse, the hero's speech, the structure's movement -- never in what these elements describe.

## CRITICAL RULES

### Rule 1 -- The Mythological Fallacy

**NEVER classify a tragedy based on:**
- Whether Dionysus, Apollo, or their associated figures (maenads, Silenus, Pythia, Muses) appear as characters
- Whether satyrs, nymphs, or other mythological personnel associated with either god are present
- Whether the play references oracles, prophecy, or Apollonian temples as *plot elements*
- Whether gods associated with either pole are invoked in prayers or choral odes

### Rule 2 -- The Content Fallacy

**NEVER classify a tragedy based on what its formal elements describe. ALWAYS classify based on how they behave.**

- A chorus that **describes** ecstasy, frenzy, or dissolution is NOT Dionysiac for that reason. It is Dionysiac only if **the verse itself becomes ecstatic** -- if the meter breaks, the syntax floods, the strophic balance strains, the language overwhelms its own content
- A chorus that **describes** order, justice, or moderation is NOT Apollonian for that reason. It is Apollonian only if **the verse itself maintains measure** -- if the strophe/antistrophe balance holds, the language is gnomic, the syntax is controlled
- A messenger who **reports** a dismemberment is NOT Dionysiac for that reason. The speech is Dionysiac only if **the narration itself fragments or loses composure**
- A hero who **discusses** madness is NOT Dionysiac for that reason. The speech is Dionysiac only if **the speech itself behaves as intoxicated language** -- rhythmically overwhelming, syntactically dissolving, formally exceeding its own bounds

The subject matter is irrelevant. The spirit of the form is everything.

### What to classify by

**ALWAYS classify based on:**
- The **spirit** of the formal elements -- how the verse, the speech, the structure *behaves*, not what it *represents*
- The *structural and aesthetic qualities* defined in the Apollonian and Dionysiac skills
- The six diagnostic dimensions described below, applied to the **formal behavior** of each element

## Invocation

```
/classify-tragedy <title>
/classify-tragedy <title> by <playwright>
/classify-tragedy <title1>, <title2>, <title3>
```

Examples:
```
/classify-tragedy <title of a Greek tragedy>
/classify-tragedy <title> by <playwright>
/classify-tragedy <title1>, <title2>, <title3>
```

If no tragedy is provided, prompt the user to supply one. If the title is ambiguous (e.g., multiple playwrights wrote a tragedy with the same title), ask the user to specify the playwright.

## Workflow

### Step 1: Identify and Contextualize

Identify the tragedy (or tragedies). For each, establish:

- **Full title and playwright** (Aeschylus, Sophocles, Euripides, or other)
- **Approximate date** of first performance
- **Surviving status**: Complete text, fragmentary, or reconstructed from testimonia
- **Mythological cycle**: Which mythic tradition does it draw from (Trojan, Theban, Argive, Attic, etc.)
- **Brief synopsis**: 3-5 sentences covering the central action

If the tragedy survives only in fragments, note that the classification will be provisional and explain which aspects can and cannot be assessed.

#### Output Format

```
## The Tragedy

**Title**: [full title]
**Playwright**: [name] ([approximate dates])
**First performance**: c. [year] BCE
**Status**: [complete / fragmentary / lost -- known from testimonia]
**Mythological cycle**: [cycle name]

### Synopsis
[3-5 sentence summary of the central action]
```

### Step 2: Six-Dimensional Analysis

Apply the six diagnostic dimensions. For EACH dimension, assess where the tragedy falls on the spectrum from Apollonian to Dionysiac. Use the markers from both skill files as your guide.

#### Dimension 1: The Chorus

The chorus is the primary diagnostic instrument. Nietzsche argued that tragedy was born from the dithyramb -- the ecstatic choral song of the Dionysiac festival -- and the individual hero (the actor) was the Apollonian addition. To analyze the chorus is to ask how much of its dithyrambic origin survives.

**Analyze each choral part separately**, then classify the chorus as a whole:

Remember: classify the chorus by **how its verse behaves**, not by what it describes. A chorus singing about chaos in perfectly balanced strophe/antistrophe is Apollonian. A chorus singing about civic duty in ecstatic, astrophic, rhythmically overwhelming verse is Dionysiac.

| Choral Part | Apollonian Signature (how the verse behaves) | Dionysiac Signature (how the verse behaves) |
|-------------|----------------------------------------------|----------------------------------------------|
| **Parodos** (entry song) | The verse is measured and orderly; the chorus enters in formal lyric, announcing its presence with syntactic control | The verse itself is emotionally charged from the first line; the meter strains, the syntax floods, the language overwhelms its own subject -- regardless of what that subject is |
| **Stasima** (standing songs between episodes) | The verse maintains strophic balance; gnomic maxims organize the language; the ode *interprets* through controlled, thematic meditation -- even when reflecting on terrible events | The verse intensifies beyond interpretation; strophic structure is strained or broken; the language *enacts* rather than describes -- rhythm, repetition, and sound dominate over meaning |
| **Kommos** (lyric exchange with actor) | The chorus's verse maintains its own register distinct from the actor's; sympathy is controlled, and the formal boundary between choral and actor voice holds | The formal boundary between chorus and actor voice dissolves; the verse merges, the registers blur, the distinction between collective and individual voice breaks down |
| **Exodos** (closing passage) | The verse achieves formal closure; the language composes itself into gnomic summary or measured acceptance | The verse refuses formal closure; the language remains raw, fragmented, or overwhelmed -- the ending is a wound in the form, not a seal on it |
| **Strophe/Antistrophe/Epode** (metrical structure) | Each strophe is answered in corresponding meter; the triadic form holds | Astrophic passages appear -- irregular, unpaired lyric where the metrical order itself dissolves |

**Additional chorus questions:**

| Question | Apollonian Pole | Dionysiac Pole |
|----------|----------------|----------------|
| Does the chorus maintain its social identity? | Yes -- it remains a defined social group throughout, speaking from its assigned role | It loses its defined role and becomes a collective voice of raw emotion |
| Does the chorus drive the action or frame it? | Frames -- it stands outside the episodes and interprets | Drives -- the stasima are the emotional core, not a commentary |
| Does the chorus fragment or split? | It speaks as one unified voice | It divides, argues with itself, or loses its coherence |
| Does the chorus merge with the hero? | It preserves distance -- its grief is sympathetic, not shared | In the kommos, chorus and hero become indistinguishable |

#### Dimension 2: Individuation

Analyze the **formal behavior of the hero's speech and dramatic presence**, not just plot events:

| Question | Apollonian Pole (formal behavior) | Dionysiac Pole (formal behavior) |
|----------|-----------------------------------|----------------------------------|
| Does the hero's speech maintain rhetorical coherence? | The hero's language stays forensic, deliberative, and structured -- arguments are built, positions are held | The hero's language fragments, floods, or loses its deliberative structure -- speech becomes lyric, argument becomes incantation |
| Does the hero's dramatic presence remain bounded? | The hero occupies a defined dramatic position -- their scenes have clear structure, their identity is formally consistent | The hero's dramatic presence becomes unstable -- they speak in modes that contradict their position, or their formal role in the drama shifts or dissolves |
| Does the hero's agency shape the dramatic structure? | The hero's decisions organize the plot -- the action flows from deliberation and choice | The dramatic structure overwhelms the hero -- events arrive faster than deliberation can process, the plot escapes the hero's rational control |
| How does self-knowledge arrive formally? | Through structured dramatic means -- investigation, dialogue, recognition scenes that build logically | Through formal eruption -- the truth breaks into the dramatic structure rather than being deduced within it; the moment of knowledge ruptures the form |

#### Dimension 3: Suffering

Analyze the **formal behavior of the verse and structure when expressing suffering**, not the severity of the depicted events:

| Question | Apollonian Pole (formal behavior) | Dionysiac Pole (formal behavior) |
|----------|-----------------------------------|----------------------------------|
| Does the language that expresses suffering maintain its form? | The verse holds its shape -- suffering is narrated through composed messenger speeches, contained laments, or measured dialogue | The verse exceeds its own containment -- language overflows, repetition builds beyond function, the form cracks under the pressure of what it carries |
| Does the dramatic structure extract meaning from suffering? | The structure organizes suffering into a comprehensible arc -- *pathei mathos* is enacted formally through plot architecture | The structure fails to contain suffering -- the dramatic arc warps, stalls, or refuses to convert pain into meaning; the form itself suffers |
| Does the language of pain maintain its rhetorical register? | Even intense grief is expressed through controlled lyric, formal lament, or dignified speech -- the register holds | The language of pain exceeds its register -- speech becomes cry, argument becomes incantation, the distinction between lyric and scream dissolves |
| Does the verse that describes physical events maintain composure? | The messenger speech paradigm: horror narrated through visually precise, syntactically controlled language | The narration itself loses composure -- the description of physical events fragments, overwhelms, or strains the syntax beyond coherent narration |

#### Dimension 4: Resolution

Analyze the **formal quality of the ending** -- does the dramatic structure achieve closure, or does it refuse to close?

| Question | Apollonian Pole (formal behavior) | Dionysiac Pole (formal behavior) |
|----------|-----------------------------------|----------------------------------|
| Does the dramatic structure achieve formal closure? | The play's architecture completes itself -- the ending shapes the material into a finished form, regardless of whether the outcome is happy | The structure refuses to close cleanly -- the ending feels forced, hollow, or formally incomplete; the form has an open wound |
| Does the verse at the ending compose itself? | The final speeches and choral passages achieve gnomic, measured, sententious composure -- the language settles | The final verse remains raw, fragmented, or overwhelmed -- the language never regains its balance |
| Does the ending organize the play's meaning? | The structural arc makes the play's events formally intelligible -- cause, consequence, and meaning are architecturally composed | The structural arc fails to organize meaning -- the events resist the ending's attempt to contain them; the form and its content remain at war |
| Does the exodos function as closure or as wound? | The chorus's final passage seals the form -- whether in wisdom, acceptance, or composed grief | The chorus's final passage is a wound in the form -- the play ends but the dramatic energy is not resolved, merely abandoned |

#### Dimension 5: Language and Music

This dimension is the most direct test of the Spirit Principle -- it asks purely about **how language behaves**:

| Question | Apollonian Pole (formal behavior) | Dionysiac Pole (formal behavior) |
|----------|-----------------------------------|----------------------------------|
| Does language serve its function or exceed it? | Language serves its argumentative, descriptive, or deliberative purpose -- words are tools for meaning | Language exceeds its function -- rhythm, sound, repetition, and incantatory force dominate over logical content; the verse overwhelms what it was "supposed to" say |
| Do speeches maintain their rhetorical structure? | Speeches are built as arguments -- stichomythia is balanced, *agon* scenes are structured, persuasion follows *logos* | Speeches lose their rhetorical architecture -- one voice drowns, syntax floods, the argumentative frame collapses into lyric, cry, or incantation |
| Does dialogue maintain formal balance? | Exchanges are measured -- point/counterpoint, balanced line lengths, controlled turn-taking | Exchanges become asymmetric -- one voice overwhelms, or both dissolve into shared lyric that erases the distinction between speakers |
| Does lyric stay within its formal boundaries? | Choral lyric is contained in its proper place (stasima); actor speech stays in its spoken register | Lyric invades speech, speech becomes song, the formal boundary between choral ode and episode dissolves -- the registers bleed into each other |

#### Dimension 6: Body and Boundaries

Analyze the **formal treatment** of physical events and categorical distinctions -- how does the verse *behave* when it encounters the body or a boundary?

| Question | Apollonian Pole (formal behavior) | Dionysiac Pole (formal behavior) |
|----------|-----------------------------------|----------------------------------|
| How does the verse behave when addressing the body? | Violence is handled through formally composed narration (the messenger speech) -- visually precise, syntactically controlled, maintaining the distance of the image | The language that encounters the body loses its formal composure -- the narration strains, fragments, or becomes formally excessive; the body overwhelms the verse |
| Do the dramatic modes maintain their proper boundaries? | Episode and stasimon are formally distinct; spoken and sung modes stay separated; the chorus and actors occupy their proper registers | Dramatic modes bleed into each other -- lyric invades episode, the chorus enters the actor's dramatic space, the distinction between speech and song dissolves |
| Does the dramatic structure keep interiority inside? | The form maintains its walls -- what belongs offstage stays offstage, private speech stays private, the dramatic architecture respects the boundary between inside and outside | The form ruptures -- interiority erupts into the dramatic present, the offstage invades the onstage, the private becomes public not through revelation but through formal explosion |
| Does the dramatic form maintain stable categories? | The formal structure preserves its distinctions -- each character has a defined register, each scene has a defined mode, identities are formally consistent | The formal structure destabilizes its own categories -- registers cross, modes shift without transition, the form itself refuses to hold stable distinctions |

#### Output Format

For each dimension, write 2-4 sentences of analysis and assign a position:

```
## Six-Dimensional Analysis

### 1. The Chorus
[2-4 sentences analyzing the chorus's function in this specific tragedy]
**Position**: [Apollonian / Dionysiac / Mixed] -- [one-sentence justification]

### 2. Individuation
[2-4 sentences]
**Position**: [Apollonian / Dionysiac / Mixed] -- [one-sentence justification]

### 3. Suffering
[2-4 sentences]
**Position**: [Apollonian / Dionysiac / Mixed] -- [one-sentence justification]

### 4. Resolution
[2-4 sentences]
**Position**: [Apollonian / Dionysiac / Mixed] -- [one-sentence justification]

### 5. Language and Music
[2-4 sentences]
**Position**: [Apollonian / Dionysiac / Mixed] -- [one-sentence justification]

### 6. Body and Boundaries
[2-4 sentences]
**Position**: [Apollonian / Dionysiac / Mixed] -- [one-sentence justification]
```

### Step 3: The Tension

This is the most important step. Nietzsche's central insight is that great tragedy exists in the **tension** between Apollonian and Dionysiac impulses -- it is not simply one or the other, but a dynamic struggle.

Analyze:

1. **Where does the tension lie?** Which dimensions pull in opposite directions? Where does Apollonian formal measure strain against Dionysiac formal dissolution?
2. **Does one pole dominate?** If so, is the other pole absent or actively resisted?
3. **Is there a trajectory?** Does the play move from one pole toward the other across its arc (e.g., from Dionysiac chaos toward Apollonian resolution, or from Apollonian composure toward Dionysiac dissolution)?
4. **What makes this tragedy great (or interesting)?** Nietzsche argues that the greatest tragedies are those where the Apollonian veil is thinnest -- where beautiful form barely contains the abyss. Is that happening here?

#### Output Format

```
## The Tension

### Where the poles collide
[Analysis of where Apollonian and Dionysiac impulses are in active tension]

### The dominant current
[Which pole, if either, pulls more strongly -- and whether the other resists or submits]

### Trajectory
[Does the play move between poles across its arc?]

### What the tension reveals
[What is aesthetically or philosophically at stake in how this particular tragedy negotiates the Apollonian-Dionysiac divide]
```

### Step 4: Classification

Render the final classification. This is NOT a simple label -- it is a reasoned judgment with a summary scorecard.

#### Summary Scorecard

```
## Classification

### Scorecard

| Dimension | Position | Strength |
|-----------|----------|----------|
| Chorus | [A / D / M] | [strong / moderate / slight] |
| Individuation | [A / D / M] | [strong / moderate / slight] |
| Suffering | [A / D / M] | [strong / moderate / slight] |
| Resolution | [A / D / M] | [strong / moderate / slight] |
| Language | [A / D / M] | [strong / moderate / slight] |
| Body & Boundaries | [A / D / M] | [strong / moderate / slight] |

**Overall**: [APOLLONIAN / DIONYSIAC / MIXTURE]
```

#### Classification Statement

Write a **3-5 sentence classification statement** that captures the essence of the judgment. This should read as a critical thesis, not a bureaucratic verdict. It should reference specific moments, structural features, or thematic dynamics from the play.

The classification statement should read as a critical thesis, not a bureaucratic verdict. Aim for the tone of a scholar who sees the living tension in the work -- reference specific structural features, thematic dynamics, or formal choices from the play to justify the classification. The statement should make the reader *feel* why the play falls where it does on the Apollonian-Dionysiac spectrum.

#### Nietzsche's Own View (if available)

If Nietzsche discusses this specific tragedy in *The Birth of Tragedy* or other works, summarize his reading and note where the present analysis agrees or diverges.

### Step 5: Textual Evidence (REQUIRED -- minimum 5 passages)

The classification must be grounded in the actual text. Present a minimum of **5 passages** from the tragedy -- drawn from choral odes, actor speeches, kommos, or messenger speeches -- that serve as concrete evidence for the Apollonian and Dionysiac dimensions identified in Step 2.

For each passage:
1. **Identify the source**: Which choral part (parodos, stasimon 1/2/3, kommos, exodos) or episode it comes from
2. **Quote or closely paraphrase** the passage (in translation)
3. **Classify it**: Mark it as Apollonian, Dionysiac, or the point where the two collide
4. **Explain why**: In 1-2 sentences, connect the passage to the specific dimension it exemplifies

The passages should represent **both poles** -- show the reader where the text is Apollonian and where it is Dionysiac. If the tragedy is classified as a mixture, the evidence should make visible exactly where the tension lives in the language.

#### Output Format

```
## Textual Evidence

### Passage 1: [Source -- e.g., "Parodos", "Second Stasimon", "Kommos", "Episode 3"]
**Classification**: [Apollonian / Dionysiac / Collision point]
> [Quoted or closely paraphrased passage in translation]

**Why**: [1-2 sentences connecting this passage to a specific dimension from Step 2]

---

### Passage 2: [Source]
[...]

[Repeat for minimum 5 passages, ideally including at least 2 choral passages and at least 1 from each pole]
```

#### Selection Guidelines

- **At least 2 passages must come from the chorus** (parodos, stasima, kommos, or exodos)
- **At least 1 passage must come from actor speech** (episode dialogue, messenger speech, or monologue)
- **Both poles must be represented** -- if the play is classified Dionysiac, still show where Apollonian form appears (and vice versa)
- **Prefer passages that show the tension** -- moments where Apollonian formal measure and Dionysiac formal dissolution coexist in the same verse, or where the spirit of the form contradicts the content it carries
- For plays that survive only in fragments, use whatever passages are available and note the limitation

### Step 6: Comparative Context (Optional -- for multiple tragedies)

If the user has requested classification of multiple tragedies, provide a comparative overview:

```
## Comparative Overview

| Tragedy | Playwright | Overall | Dominant Dimension | Key Tension |
|---------|-----------|---------|-------------------|-------------|
| [title] | [name] | [A/D/M] | [which dimension is most decisive] | [one-sentence summary] |

### Spectrum
[Place the tragedies on a continuum from most Apollonian to most Dionysiac, with brief justification]
```

### Step 7: Export to Markdown

Save the complete analysis as a `.md` file.

1. **Filename**: `classify-tragedy-<title-kebab-case>.md`
   - For multiple tragedies: `classify-tragedy-comparison-<first-title-kebab-case>.md`
2. **Location**: Save to the user's current working directory
3. **YAML frontmatter**:
   ```
   ---
   title: "Tragedy Classification: [Title]"
   playwright: [name]
   date: [YYYY-MM-DD]
   classification: [apollonian/dionysiac/mixture]
   type: classify-tragedy
   tags: [greek-tragedy, nietzsche, apollonian-dionysiac, playwright-name]
   ---
   ```
4. **Content**: The full analysis from Steps 1-6
5. Provide the user with a direct link to the file after saving

This export step is NOT optional -- every `/classify-tragedy` invocation MUST produce a `.md` file.

## Notes

- **Fragments**: For fragmentary tragedies, assess what can be assessed and mark uncertain dimensions explicitly. A fragmentary analysis is still valuable.
- **Lost tragedies**: If only the title and a few testimonia survive, offer what classification is possible from the evidence and be transparent about the limits.
- **Satyr plays**: The presence of satyrs does NOT make a play Dionysiac -- this is the same mythological fallacy. If the user asks about a satyr play, apply the same six-dimensional framework as for any other play. Classify by structural and aesthetic qualities, not by genre label or mythological personnel.
- **Non-Greek tragedy**: If the user asks about Roman, Renaissance, neoclassical, or modern tragedy, the framework can be applied but note that Nietzsche developed it specifically for Attic tragedy. Flag any adjustments needed.
- **No playwright bias**: Do not pre-classify any playwright as inherently Apollonian or Dionysiac. Each play by each playwright must be analyzed on its own structural and aesthetic merits through the six dimensions. A single playwright's corpus may contain plays at every point on the spectrum.
- **Trilogy structure**: For connected trilogies, note that the classification may shift across plays. Analyze each play individually AND the trajectory of the whole.
