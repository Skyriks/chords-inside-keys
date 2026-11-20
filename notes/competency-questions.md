# Competency questions so far

These answers cover the small sample, not every possible chord or key.

| Question | Current position |
| --- | --- |
| 1. Notes of C major | C, E, G. Query included. |
| 2. Chord from a set of notes | C-E-G finds CMajorChord; its MajorChord type is inferred from the entered intervals. No general chord recognition yet. |
| 3. Interval between two notes | Open. Needs a note-pair representation and a spelling/direction convention. |
| 4. Chords in a key | Can query the entered ChordInKey examples. The list is incomplete. |
| 5. Keys containing a chord | C major has occurrences in C major and G major in this sample. Other keys have not all been linked. |
| 6. C major's role in G major | Subdominant, through C_in_G. |
| 7. Compatible chords | Open. The group needs to define compatible first. |
| 8. Two keys with the same notes | C major and A natural minor. Query included. |
| 9. Root of a chord | C for CMajorChord, via hasRoot. Roots are entered, not inferred from unordered notes. |
| 10. Dominant chord of a key | G major for C major. Query included. |
| 11. Different roles in different keys | C major is tonic in C major and subdominant in G major. Query included. |
| 12. Keys with exactly the same notes | Same example as question 8. |
| 13. Chords with a given note | C major, F major and A minor contain C in the sample. Query included. |

The draft declares 17 named classes, 12 object properties and 38 named individuals (67 terms). Some declared intervals do not have examples yet.
