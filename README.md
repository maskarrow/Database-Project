# Database-Project

Creaţi o aplicaţie care să conţină o bază de date creată în PostgreSQL şi o interfaţă pentru

aceasta. La crearea interfeţei se va folosi tehnologia Python Django. Baza de date va fi

compusă din următoarele tabele:

• Clienti(ClientID, Nume, Prenume, Adresa);

• ProdusAlimentar(ProdusID, Denumire, DataProducere, DataExpirare);

• Producatori(ProducatorID, Denumire, TaraOrigine, Adresa);

Asocierile între tabele sunt următoarele:

• între tabela Clienti şi tabela ProdusAlimentar – asociere de tipul M:N.

• între tabela ProdusAlimentar şi tabela Producatori – asociere de tipul M:N.

Interfaţa va trebui sa permită utilizatorului să facă următoarele operaţii pe toate tabele:

vizualizare, adăugare, modificare, ştergere. Vizualizarea tabelelor de legătură va presupune

vizualizarea datelor referite din celelalte tabele.

