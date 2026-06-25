--
-- PostgreSQL database dump
--

\restrict a1uOuI2VMe5wueWn1YAU0C8sAK1T7UISIuRstAkTP24hp715XAbK5XFA6N8IFF8

-- Dumped from database version 17.7
-- Dumped by pg_dump version 17.7

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: app_testimonial; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.app_testimonial (id, first_name, last_name, text, rating) FROM stdin;
1	Sarah	Christin	Ich war das erste Mal dort, um mir eine Neumodellage der Nägel machen zu lassen. Olga hat mir schnell geantwortet und mir einen kurzfristigen Termin anbieten können. Ich wurde freundlich empfangen und es wurde sich Zeit genommen meine Fragen und Wünsche zu besprechen. Ich kann wirklich nicht verstehen, warum das Kosmetikstudio so wenig Rezensionen hat, denn ich bin begeistert von dem Ergebnis. Olga hat meine Wünsche ganz genau so umgesetzt und war ganz akribisch und perfektionistisch am Werk. Ihre 15-jährige Erfahrung merkt man ihr definitiv an. Vielen Dank liebe Olga, für diese schönen, natürlichen Nägel! Ich bin sehr zufrieden. :)	5
2	Lene-Christine	Köstler	Super zufrieden vom 1. Tag an. Komme seitdem regelmäßig. Meine Nägel haben noch nie so lange gehalten und Olga ist einfach super nett! Auch auf die Hygiene wird peinlich genau geachtet. Kann ich zu 100% empfehlen!. Liebe Olga vielen Dank für meine schönen Nägel.	5
3	Viktoria	Wilhelm	Ich bin mit der Fusspflege von Olga sehr zufrieden. Sie ist eine sehr sympathische und entspannte Person. Sehr schnell und vor allem kompetent. Man kann sich mit ihr gut unterhalten, aber auch entspannen. Komme immer wieder gerne zu ihr. Vielen Dank! ❤️	5
4	Ellice	Heinz	Ich bin super zufrieden! Olga arbeitet hygienisch, bedacht und geht immer auf meine Wünsche ein! Wir unterhalten uns gerne aber bei Olga kann man auch schweigend sitzen und entspannen.	5
5	Gunda	Asendorf	Olga wurde mir empfohlen von meiner Freundin Lene. Sie hat sich nach meiner ersten SMS umgehend gemeldet und mir Terminvorschläge unterbreitet. Bin sehr zufrieden mit der Nagelmodellage. Tolle Lackfarben. Sehr sauber und hygienisch.	5
6	hildegunst	mythenschliff	Ich schreibe nie Rezensionen, aber hier ist es angebracht: Nach 15 (!) Anrufen bei Kosmetikstudios in ganz Oldenburg, die (Haut)Grießkörner nicht entfernen wollten, war Frau Eisner meine letzte Hoffnung.	5
7	Angela	Grumbach	War bisher nur zum Nägel machen dort und schwer begeistert. Super Ergebnis und total nett und zuvorkommend behandelt worden. Direkt weiter empfohlen 👍	5
8	Margaret	Pavlenko	Ich besuche dieses Kosmetikstudio schon fast 2 Jahre und bin immer zufrieden! Olga ist sehr nett, freundlich und professionell :) Die Atmosphäre ist angenehm und das Studio ist immer schön und sauber. Kann ich nur empfehlen!	5
9	Christine	Kleene	Alles super! Olga ist total nett und macht perfekte Arbeit :) würde immer wieder kommen!	5
10	Unbekannte	Kundin	Kann ich nur empfehlen. Ich bin sehr zufrieden. Professionell, sehr freundlich und sauber. Ich bin mehr als begeistert. 😊	5
11	Cora	Dallmann	Es lief alles sehr sauber und hygienisch ab. Ich war sehr zufrieden.	5
12	Petra	Frese	Sehr gut geschult, tolle Beratung, super freundlich – vielen Dank dafür! 🫶👋	5
13	Conny	Block	Sehr sauber, eine Wohlfühloase, sehr freundliches Personal und tolle Arbeit	5
14	Sonja	Benjamins	Sehr nette und professionelle Behandlung.	5
15	Laura	Morosow	Es war alles super, gerne wieder!	5
16	Natali	Menzer	Es war alles super, gerne wieder!	5
17	Marina	Zimin	Es war alles super, gerne wieder!	5
18	Janine	Henner	Es war alles super, gerne wieder!	5
19	Evgenia	Stefan	Es war alles super, gerne wieder!	5
\.


--
-- Name: app_testimonial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.app_testimonial_id_seq', 19, true);


--
-- PostgreSQL database dump complete
--

\unrestrict a1uOuI2VMe5wueWn1YAU0C8sAK1T7UISIuRstAkTP24hp715XAbK5XFA6N8IFF8

