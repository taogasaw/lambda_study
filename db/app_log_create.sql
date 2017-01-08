CREATE SEQUENCE public.app_logs_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.app_logs_id_seq
    OWNER TO ***********;


-- Table: public.app_logs

-- DROP TABLE public.app_logs;

CREATE TABLE public.app_logs
(
    id bigint NOT NULL DEFAULT nextval('app_logs_id_seq'::regclass),
    created_at timestamp with time zone NOT NULL DEFAULT now(),
    title character varying COLLATE pg_catalog."default" NOT NULL DEFAULT ''::character varying,
    message text COLLATE pg_catalog."default",
    CONSTRAINT app_logs_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.app_logs
    OWNER to ***********;

-- Index: index_app_logs_on_created_at

-- DROP INDEX public.index_app_logs_on_created_at;

CREATE INDEX index_app_logs_on_created_at
    ON public.app_logs USING btree
    (created_at)
    TABLESPACE pg_default;
