# Hackathon 1

For the first hackathon, we generated a RDF model for all the universities from <https://data.gov.ro/dataset/reteaua-unitatilor-de-invatamant-universitar-2020-2021>. 

In the file.rdf you can find the output of the rdf-generator.py. We created a RDF, which contains all the universities, where we adopted schema.org constructs (like EducationalOrganization concept):
- university id, represented by ID RMU
- university name (legal name - the official name of the organization) - Nume
- university code (lei code - an organization identifier that uniquely identifies a legal entity as defined in ISO 17442) - Cod Universitate
- university location (location - the location where an organization is located) - where we used the Place concept.

Also, at the end of the file, all the Places are represented with their countyCode and leiCode. 
