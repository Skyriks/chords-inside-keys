# Chords inside keys

First OWL draft for the music theory project. I kept five chords and four keys
so the group can check the modelling before adding the rest.

The main example is C major. It has notes C, E and G. `C_in_C` gives it the
tonic role in C major; `C_in_G` gives it the subdominant role in G major.
The chord itself has no single harmonic function.

## Files

- `ontology/chords.ttl`: the source ontology, with a few comments.
- `ontology/chords.owl`: the same ontology in RDF/XML, for opening in Protege.
- `notes/modelling.md`: choices, limits and questions for the group.
- `notes/competency-questions.md`: what works in this sample and what is left.
- `notes/introduction-draft.tex`: a short section to discuss for the report.
- `scripts/check_examples.py`: selected reasoning and query checks.
- `scripts/export_owl.py`: regenerate the `.owl` file after editing the Turtle.
- `queries/examples.rq`: a query to try, with a second example commented out.

## Try it

```sh
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/check_examples.py
```

Or open `ontology/chords.owl` in Protege and start HermiT. The Python checks use
OWL RL reasoning; they do not replace a full OWL DL consistency check.
HermiT has not been run on this draft yet.

To edit, change `ontology/chords.ttl`, run the checks, then run:

```sh
python scripts/export_owl.py
```

## Left for the group

- Compare this with Emre's current OWL file before merging.
- Decide how to represent intervals between two named notes.
- Add the remaining chord and key examples.
- Decide what "compatible" means in question 7.
- Check the definitions in Protege and record the results for the report.

The full report and evaluation are still open. This folder was built from the
terms pasted into the discussion, not from the live Overleaf project.
