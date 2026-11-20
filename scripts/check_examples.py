"""Check the small example and print the answers it can give so far."""
from pathlib import Path

from rdflib import Graph, Namespace, RDF, OWL, URIRef
from owlrl import DeductiveClosure, OWLRL_Semantics

ROOT = Path(__file__).resolve().parents[1]
M = Namespace("https://example.org/chords-inside-keys#")


def load():
    return Graph().parse(ROOT / "ontology/chords.ttl", format="turtle")


def short(term):
    return str(term).split("#")[-1]


def main():
    graph = load()
    source_size = len(graph)
    assert (M.CMajorChord, RDF.type, M.MajorChord) not in graph
    inferred = Graph()
    inferred += graph
    DeductiveClosure(OWLRL_Semantics).expand(inferred)
    for chord in (M.CMajorChord, M.FMajorChord, M.GMajorChord):
        assert (chord, RDF.type, M.MajorChord) in inferred
    assert (M.AMinorChord, RDF.type, M.MinorChord) in inferred
    assert (M.BDiminishedChord, RDF.type, M.DiminishedChord) in inferred
    assert (M.C_in_C, RDF.type, M.TonicChord) in inferred
    assert (M.C_in_G, RDF.type, M.SubdominantChord) in inferred
    assert (M.G_in_C, RDF.type, M.DominantChord) in inferred
    assert (M.C_in_G, RDF.type, M.PrimaryChord) in inferred
    assert (M.C, M.isRootOf, M.CMajorChord) in inferred
    assert (M.AMinorKey, M.hasRelativeKey, M.CMajorKey) in inferred
    assert (M.CMajorChord, M.hasFunction, M.Tonic) not in inferred

    for chord in (M.CMajorChord, M.FMajorChord, M.GMajorChord,
                  M.AMinorChord, M.BDiminishedChord):
        assert len(set(inferred.objects(chord, M.hasNote))) == 3
    for use in graph.subjects(RDF.type, M.ChordInKey):
        chords = list(graph.objects(use, M.hasChord))
        keys = list(graph.objects(use, M.belongsToKey))
        assert len(chords) == len(keys) == 1
        assert set(graph.objects(chords[0], M.hasNote)) <= set(
            graph.objects(keys[0], M.containsNote))

    # This checks selected inferences. It is not a full OWL DL consistency check.
    assert not list(inferred.subjects(RDF.type, OWL.Nothing))
    print(f"Parsed {source_size} triples; example checks passed.")
    print("CQ1:", ", ".join(sorted(short(n) for n in graph.objects(M.CMajorChord, M.hasNote))))
    queries = {
        "CQ2, exact C-E-G set": """
            SELECT DISTINCT ?chord WHERE {
              ?chord a :Triad ; :hasNote :C, :E, :G .
              FILTER NOT EXISTS {
                ?chord :hasNote ?other . FILTER (?other NOT IN (:C, :E, :G))
              }
            }""",
        "CQ6 and CQ11": """
            SELECT ?key ?function WHERE {
              ?use :hasChord :CMajorChord ; :belongsToKey ?key ; :hasFunction ?function .
            } ORDER BY ?key""",
        "CQ10, dominant of C major": """
            SELECT ?chord WHERE {
              ?use :belongsToKey :CMajorKey ; :hasFunction :Dominant ; :hasChord ?chord .
            }""",
        "CQ13, chords with C": """
            SELECT ?chord WHERE { ?chord :hasNote :C } ORDER BY ?chord""",
        "CQ8 and CQ12, equal note sets": """
            SELECT ?a ?b WHERE {
              ?a a :Key . ?b a :Key . FILTER(STR(?a) < STR(?b))
              FILTER EXISTS { ?a :containsNote ?n }
              FILTER NOT EXISTS {
                ?a :containsNote ?n . FILTER NOT EXISTS { ?b :containsNote ?n }
              }
              FILTER NOT EXISTS {
                ?b :containsNote ?n . FILTER NOT EXISTS { ?a :containsNote ?n }
              }
            }""",
    }
    results = {}
    prefix = f"PREFIX : <{M}>\n"
    for label, query in queries.items():
        rows = list(inferred.query(prefix + query))
        results[label] = {tuple(short(v) for v in row) for row in rows}
        print(label + ":", sorted(results[label]))
    assert results["CQ2, exact C-E-G set"] == {("CMajorChord",)}
    assert results["CQ6 and CQ11"] == {("CMajorKey", "Tonic"), ("GMajorKey", "Subdominant")}
    assert results["CQ10, dominant of C major"] == {("GMajorChord",)}
    assert results["CQ8 and CQ12, equal note sets"] == {("AMinorKey", "CMajorKey")}
    assert results["CQ13, chords with C"] == {("AMinorChord",), ("CMajorChord",), ("FMajorChord",)}
    print("The query answers above use only the examples entered so far.")
    print("Full DL consistency and the remaining questions still need review in Protege.")


if __name__ == "__main__":
    main()
