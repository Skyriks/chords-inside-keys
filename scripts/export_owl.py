"""Export the Turtle source as RDF/XML for opening as an .owl file."""
from pathlib import Path
from rdflib import Graph
from rdflib.compare import isomorphic

root = Path(__file__).resolve().parents[1]
graph = Graph().parse(root / "ontology/chords.ttl", format="turtle")
output = root / "ontology/chords.owl"
graph.serialize(output, format="xml")
assert isomorphic(graph, Graph().parse(output, format="xml"))
print("Wrote", output.name, "and checked that the triples match.")
