![Workflow Status](https://github.com/RNagelhout/my-project/actions/workflows/run-tests.yml/badge.svg)


Github Versiebeheer:

Een van de voordelen van het gebruik van GitHub is dat deze mooi oplossingen biedt voor versieberheer van je project. Hierdoor is het mogelijk om wijzigingen in de code bij te houden, te vergelijken en te beheren.  

Github repository secrets:

In verband met veiligheid is het niet raadzaam om bepaalde gegevens welke nodig zijn om de verbinding te maken met de droplet zichtbaar te hebben in de repository.  Daarom heeft Github een optie om deze gegevens te encrypten. Met repository secrets kun je deze data opslaan. De naam van de secret wordt dan in het project gebruikt ipv de data.

SSH:

Door SSH-keys te gebruiken creëer je een beveiligde netwerkverbinding tussen je computer en bijv. een server(digital ocean). Op het systeem waarmee je verbinding wil maken wordt een ssh key(public-key) toegevoegd. Bij de verbinding tussen de computer en het systeem wordt er gecontroleerd of de private key bij het desbetreffende public-key hoort. Zo ja, dan wordt de verbinding gemaakt en is er toegang tot de server. Zo nee dan kan er geen verbinding worden gemaakt. 

Mijn 3 uitdagingen:

Uitdaging 1: Verbinding maken met nieuw project op de droplet.

Mijn grootste uitdaging was om mijn local project te koppelen met een nieuw project op de droplet van digital oceans. Na veel speurwerk op het internet en kwam ik erachter dat de poort waar ik mee wou verbinden al bezet/actief was. Door deze verbinding te “killen” kwam deze poort weer beschikbaar en kreeg ik uiteindelijk verbinding met de server.


Uitdaging 2: Uitvoering van deploy na goedkeuring test

Het uitvoeren van de deploy had ik eerst opgelost door middel van succeed(). Dit bleek niet geheel de lading te dekken en na wat speurwerk kwam ik bij de optie om “needs” toe te passen. Hierdoor is het mogelijk om pas als de test-job is goedgekeurd de deploy-job  mag worden uitgevoerd.  

Uitdaging 3: Syntax error ${{ secret. }}

Tijdens het toepassen van de secret keys in het .yml bestand kwam er een syntax error sign. Deze heb ik verholpen om fromJSON(toJSON( ervoor te zetten. 
