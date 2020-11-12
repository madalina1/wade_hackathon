import xlrd
from rdflib import Graph, Literal, RDF, URIRef, BNode
from rdflib.namespace import FOAF, XSD, Namespace, ClosedNamespace

# create a Graph
g = Graph()

EDORG = ClosedNamespace(
    uri=URIRef('https://schema.org/EducationalOrganization/'),
    terms=[
       "University", "Faculty", "legalName", "id",  "leiCode", "Place", "location", "county", "member", "memberCode",
		"doctoralSchool"
    ]
);

PLACE = ClosedNamespace(
    uri=URIRef('https://schema.org/Place/'),
    terms=[
       "county", "localty", "leiCode"
    ]
);


def extract_universities():
	workbook = xlrd.open_workbook('invatamant-superior-2020.xlsx')
	worksheet = workbook.sheet_by_name('Universitati')

	row = 3
	column = 1
	while(row < worksheet.nrows):
		id = int(worksheet.cell(row, 0).value)
		name = worksheet.cell(row, 1).value.replace("\"", "")
		code = worksheet.cell(row, 2).value
		county = worksheet.cell(row, 3).value
		county_id = int(worksheet.cell(row, 4).value)
		locality = worksheet.cell(row, 5).value
		locality_id = worksheet.cell(row, 6).value
		year = worksheet.cell(row, 7).value
		web_address = worksheet.cell(row, 8).value
		row += 1

		universityRef = URIRef("https://schema.org/EducationalOrganization/" + name.replace(" ", "-"))
		locationRef = URIRef("https://schema.org/Place/" + county)

		g.add((universityRef, RDF.type, EDORG.University))
		g.add((universityRef, EDORG.legalName, Literal(name)))
		g.add((universityRef, EDORG.id, Literal(id)))
		g.add((universityRef, EDORG.leiCode, Literal(code)))
		g.add((universityRef, EDORG.location, locationRef))
		g.add((locationRef, RDF.type, EDORG.Place))
		g.add((locationRef, EDORG.county, Literal(county)))
		g.add((locationRef, EDORG.leiCode, Literal(county_id)))

def extract_faculties():
	workbook = xlrd.open_workbook('invatamant-superior-2020.xlsx')
	worksheet = workbook.sheet_by_name('Facultati')

	row = 3
	column = 1
	while(row < worksheet.nrows):
		id = int(worksheet.cell(row, 0).value)
		name = worksheet.cell(row, 1).value.replace("\"", "")
		university_name = worksheet.cell(row, 2).value
		university_id = int(worksheet.cell(row, 3).value)
		doctoral_school = int(worksheet.cell(row, 4).value)
		year = int(worksheet.cell(row, 5).value)
		row += 1

		facultyRef = URIRef("https://schema.org/EducationalOrganization/" + name.replace(" ", "-"))

		g.add((facultyRef, RDF.type, EDORG.Faculty))
		g.add((facultyRef, EDORG.id, Literal(id)))
		g.add((facultyRef, EDORG.legalName, Literal(name)))
		g.add((facultyRef, EDORG.member, Literal(university_name)))
		g.add((facultyRef, EDORG.memberCode, Literal(university_id)))
		g.add((facultyRef, EDORG.doctoralSchool, Literal(doctoral_school)))

extract_universities()
# extract_faculties()

import io
with io.open("file.rdf", "w", encoding="utf-8") as f:
    f.write(g.serialize(format='turtle').decode("utf-8"))