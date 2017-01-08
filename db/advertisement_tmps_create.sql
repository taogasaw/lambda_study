CREATE SEQUENCE public.advertisement_tmps_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.advertisement_tmps_id_seq
    OWNER TO *************;


-- Table: public.advertisement_tmps

-- DROP TABLE public.advertisement_tmps;

CREATE TABLE public.advertisement_tmps
(
    id bigint NOT NULL DEFAULT nextval('advertisement_tmps_id_seq'::regclass),
    name character varying COLLATE pg_catalog."default" NOT NULL DEFAULT ''::character varying,
    telephone character varying COLLATE pg_catalog."default",
    import_source_index integer NOT NULL,
    CONSTRAINT advertisement_tmps_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.advertisement_tmps
    OWNER to ************;
