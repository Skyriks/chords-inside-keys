# Modelling notes

## Classes and individuals

`Note`, `Chord`, `Key`, `Interval` and `HarmonicFunction` are classes.
`C`, `CMajorChord`, `CMajorKey`, `MajorThird` and `Tonic` are individuals.
The model keeps note spellings and ignores octaves. It does not yet merge
sharp and flat spellings that sound the same.

I kept `hasRoot`, `hasThird` and `hasFifth` separate. They also count as
`hasNote` links. An interval on a chord means an interval above its root.
Those intervals are entered by hand; OWL does not calculate them from the notes.

## A chord's role depends on its key

`ChordInKey` links one chord, one key and its function. For example:

```turtle
:C_in_G a :ChordInKey ;
    :hasChord :CMajorChord ;
    :belongsToKey :GMajorKey ;
    :hasFunction :Subdominant .
```

Putting `hasFunction Tonic` directly on `CMajorChord` would lose that context.
The names `TonicChord`, `SubdominantChord` and `DominantChord` therefore classify
these occurrences, not the standalone chords. The group should confirm these names.
Only the primary roles I, IV and V in major, and i in the minor example, are used.

## Definitions

`MajorChord` is defined as a `Triad` with a major third and a perfect fifth above
its root. Minor and diminished chords use the matching interval pairs. These are
complete definitions for this small model: they let the reasoner add the type.

`Triad` only has a partial definition: it must be a chord with exactly three
distinct note values. Three arbitrary notes are not enough to infer a triad.
The examples are explicitly marked as triads, and their note names are distinct.
The current definitions trust the entered root intervals; they do not prove that
those intervals match the entered notes. That still needs a separate check.

`DiatonicChord` is also partial. It is a `ChordInKey` occurrence whose notes fit
the key. Membership is currently asserted for the five examples and checked in
Python. A general comparison between all chord notes and a key's notes is left
for a query or rule. It is not inferred by the present OWL definitions.

## Missing facts do not mean false facts

OWL uses an open world. If a note is not listed, that alone does not prove it is
absent. The four example keys have both their note facts and a restriction that
limits them to those notes. Triads have exactly three notes. SPARQL queries that
compare note sets are only reliable here because these example sets are complete.
C major and A natural minor have the same note set, but remain different keys.

## Still to agree

- The draft uses natural minor. A major dominant in a minor key needs the raised
  leading note, so harmonic minor would change the current scope.
- `PerfectOctave` is kept as a term, but an octave interval cannot be recovered
  from octave-free notes alone.
- `Tritone` is used for the diminished fifth in the example. It is not a general
  solution to spelling-dependent interval names.
- The list had 9 note names, not 7, and the repeated appendix labels need fixing.
- Questions 8 and 12 both ask about equal note sets; one could be removed.

## Sources checked

- [W3C OWL 2 Primer](https://www.w3.org/TR/owl2-primer/): classes, restrictions,
  definitions and the open-world assumption.
- [W3C n-ary relation patterns](https://www.w3.org/TR/swbp-n-aryRelations/):
  using an extra individual to hold the context of a relation.
- [Open Music Theory, triads](https://open-musictheory.github.io/docs/fundamentals/triads/):
  triad qualities and Roman numerals in major keys.
