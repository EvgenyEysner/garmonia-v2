--
-- PostgreSQL database dump
--

\restrict qiHmSIbDMsbRxhQxjidgWt05xtHczCvGQ4Mmd4EjoeOzR7PlrDvZzanG73bVooB

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
\.


--
-- Name: app_testimonial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.app_testimonial_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

\unrestrict qiHmSIbDMsbRxhQxjidgWt05xtHczCvGQ4Mmd4EjoeOzR7PlrDvZzanG73bVooB

