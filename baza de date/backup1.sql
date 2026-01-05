--
-- PostgreSQL database dump
--

\restrict OQxy2JPjSUEj6R4biwgkF28Zicv97cwEcW8bIrW0BzMwsqsMEIkwEbRbc5awefX

-- Dumped from database version 18.1
-- Dumped by pg_dump version 18.1

-- Started on 2026-01-05 19:05:35

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 225 (class 1259 OID 16428)
-- Name: client_produs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.client_produs (
    clientid integer NOT NULL,
    produsid integer NOT NULL
);


ALTER TABLE public.client_produs OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16396)
-- Name: clienti; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clienti (
    clientid integer NOT NULL,
    nume character varying(100) NOT NULL,
    prenume character varying(100) NOT NULL,
    adresa character varying(255)
);


ALTER TABLE public.clienti OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16395)
-- Name: clienti_clientid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.clienti_clientid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.clienti_clientid_seq OWNER TO postgres;

--
-- TOC entry 5044 (class 0 OID 0)
-- Dependencies: 219
-- Name: clienti_clientid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.clienti_clientid_seq OWNED BY public.clienti.clientid;


--
-- TOC entry 222 (class 1259 OID 16406)
-- Name: producatori; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producatori (
    producatorid integer NOT NULL,
    denumire character varying(150) NOT NULL,
    taraorigine character varying(100),
    adresa character varying(255)
);


ALTER TABLE public.producatori OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16405)
-- Name: producatori_producatorid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.producatori_producatorid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.producatori_producatorid_seq OWNER TO postgres;

--
-- TOC entry 5045 (class 0 OID 0)
-- Dependencies: 221
-- Name: producatori_producatorid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.producatori_producatorid_seq OWNED BY public.producatori.producatorid;


--
-- TOC entry 226 (class 1259 OID 16445)
-- Name: produs_producator; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produs_producator (
    produsid integer NOT NULL,
    producatorid integer NOT NULL
);


ALTER TABLE public.produs_producator OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16417)
-- Name: produsalimentar; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produsalimentar (
    produsid integer NOT NULL,
    denumire character varying(150) NOT NULL,
    dataproducere date NOT NULL,
    dataexpirare date NOT NULL,
    CONSTRAINT produsalimentar_check CHECK ((dataexpirare > dataproducere))
);


ALTER TABLE public.produsalimentar OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16416)
-- Name: produsalimentar_produsid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.produsalimentar_produsid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.produsalimentar_produsid_seq OWNER TO postgres;

--
-- TOC entry 5046 (class 0 OID 0)
-- Dependencies: 223
-- Name: produsalimentar_produsid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.produsalimentar_produsid_seq OWNED BY public.produsalimentar.produsid;


--
-- TOC entry 4874 (class 2604 OID 16399)
-- Name: clienti clientid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clienti ALTER COLUMN clientid SET DEFAULT nextval('public.clienti_clientid_seq'::regclass);


--
-- TOC entry 4875 (class 2604 OID 16409)
-- Name: producatori producatorid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producatori ALTER COLUMN producatorid SET DEFAULT nextval('public.producatori_producatorid_seq'::regclass);


--
-- TOC entry 4876 (class 2604 OID 16420)
-- Name: produsalimentar produsid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produsalimentar ALTER COLUMN produsid SET DEFAULT nextval('public.produsalimentar_produsid_seq'::regclass);


--
-- TOC entry 4885 (class 2606 OID 16434)
-- Name: client_produs client_produs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client_produs
    ADD CONSTRAINT client_produs_pkey PRIMARY KEY (clientid, produsid);


--
-- TOC entry 4879 (class 2606 OID 16404)
-- Name: clienti clienti_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clienti
    ADD CONSTRAINT clienti_pkey PRIMARY KEY (clientid);


--
-- TOC entry 4881 (class 2606 OID 16415)
-- Name: producatori producatori_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producatori
    ADD CONSTRAINT producatori_pkey PRIMARY KEY (producatorid);


--
-- TOC entry 4887 (class 2606 OID 16451)
-- Name: produs_producator produs_producator_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produs_producator
    ADD CONSTRAINT produs_producator_pkey PRIMARY KEY (produsid, producatorid);


--
-- TOC entry 4883 (class 2606 OID 16427)
-- Name: produsalimentar produsalimentar_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produsalimentar
    ADD CONSTRAINT produsalimentar_pkey PRIMARY KEY (produsid);


--
-- TOC entry 4888 (class 2606 OID 16435)
-- Name: client_produs client_produs_clientid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client_produs
    ADD CONSTRAINT client_produs_clientid_fkey FOREIGN KEY (clientid) REFERENCES public.clienti(clientid) ON DELETE CASCADE;


--
-- TOC entry 4889 (class 2606 OID 16440)
-- Name: client_produs client_produs_produsid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client_produs
    ADD CONSTRAINT client_produs_produsid_fkey FOREIGN KEY (produsid) REFERENCES public.produsalimentar(produsid) ON DELETE CASCADE;


--
-- TOC entry 4890 (class 2606 OID 16457)
-- Name: produs_producator produs_producator_producatorid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produs_producator
    ADD CONSTRAINT produs_producator_producatorid_fkey FOREIGN KEY (producatorid) REFERENCES public.producatori(producatorid) ON DELETE CASCADE;


--
-- TOC entry 4891 (class 2606 OID 16452)
-- Name: produs_producator produs_producator_produsid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produs_producator
    ADD CONSTRAINT produs_producator_produsid_fkey FOREIGN KEY (produsid) REFERENCES public.produsalimentar(produsid) ON DELETE CASCADE;


-- Completed on 2026-01-05 19:05:35

--
-- PostgreSQL database dump complete
--

\unrestrict OQxy2JPjSUEj6R4biwgkF28Zicv97cwEcW8bIrW0BzMwsqsMEIkwEbRbc5awefX

