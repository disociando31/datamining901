PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS dim_tiempo (
    tiempo_key INTEGER PRIMARY KEY,
    clave_natural TEXT NOT NULL UNIQUE,
    fecha_publicacion TEXT,
    anio INTEGER,
    trimestre INTEGER CHECK (trimestre BETWEEN 1 AND 4),
    mes INTEGER CHECK (mes BETWEEN 1 AND 12),
    dia INTEGER CHECK (dia BETWEEN 1 AND 31)
);

CREATE TABLE IF NOT EXISTS dim_entidad (
    entidad_key INTEGER PRIMARY KEY,
    clave_natural TEXT NOT NULL UNIQUE,
    codigo_entidad TEXT,
    nit_entidad TEXT,
    nombre_entidad TEXT,
    orden_entidad TEXT
);

CREATE TABLE IF NOT EXISTS dim_territorio (
    territorio_key INTEGER PRIMARY KEY,
    clave_natural TEXT NOT NULL UNIQUE,
    departamento_entidad TEXT,
    ciudad_entidad TEXT
);

CREATE TABLE IF NOT EXISTS dim_contratacion (
    contratacion_key INTEGER PRIMARY KEY,
    clave_natural TEXT NOT NULL UNIQUE,
    modalidad_de_contratacion TEXT,
    tipo_de_contrato TEXT,
    subtipo_de_contrato TEXT,
    fase TEXT,
    estado_del_procedimiento TEXT,
    adjudicado TEXT
);

CREATE TABLE IF NOT EXISTS dim_proveedor (
    proveedor_key INTEGER PRIMARY KEY,
    clave_natural TEXT NOT NULL UNIQUE,
    nit_del_proveedor_adjudicado TEXT,
    nombre_del_proveedor TEXT,
    departamento_proveedor TEXT,
    ciudad_proveedor TEXT
);

CREATE TABLE IF NOT EXISTS fact_proceso (
    hecho_key INTEGER PRIMARY KEY,
    numero_registro_origen INTEGER NOT NULL UNIQUE CHECK (numero_registro_origen > 0),
    huella_origen TEXT NOT NULL UNIQUE,
    tiempo_key INTEGER NOT NULL REFERENCES dim_tiempo(tiempo_key),
    entidad_key INTEGER NOT NULL REFERENCES dim_entidad(entidad_key),
    territorio_key INTEGER NOT NULL REFERENCES dim_territorio(territorio_key),
    contratacion_key INTEGER NOT NULL REFERENCES dim_contratacion(contratacion_key),
    proveedor_key INTEGER NOT NULL REFERENCES dim_proveedor(proveedor_key),
    id_del_proceso TEXT,
    referencia_del_proceso TEXT,
    nombre_del_procedimiento TEXT,
    descripcion_del_procedimiento TEXT,
    duracion INTEGER CHECK (duracion IS NULL OR duracion >= 0),
    unidad_de_duracion TEXT,
    ciudad_de_la_unidad_de TEXT,
    precio_base_cop INTEGER CHECK (precio_base_cop IS NULL OR precio_base_cop >= 0),
    proveedores_invitados INTEGER CHECK (proveedores_invitados IS NULL OR proveedores_invitados >= 0),
    proveedores_con_invitacion INTEGER CHECK (proveedores_con_invitacion IS NULL OR proveedores_con_invitacion >= 0),
    respuestas_al_procedimiento INTEGER CHECK (respuestas_al_procedimiento IS NULL OR respuestas_al_procedimiento >= 0),
    conteo_de_respuestas_a_ofertas INTEGER CHECK (conteo_de_respuestas_a_ofertas IS NULL OR conteo_de_respuestas_a_ofertas >= 0),
    proveedores_unicos_con INTEGER CHECK (proveedores_unicos_con IS NULL OR proveedores_unicos_con >= 0),
    numero_de_lotes INTEGER CHECK (numero_de_lotes IS NULL OR numero_de_lotes >= 0),
    valor_total_adjudicacion_cop INTEGER CHECK (
        valor_total_adjudicacion_cop IS NULL OR valor_total_adjudicacion_cop >= 0
    ),
    codigo_principal_de_categoria TEXT,
    urlproceso TEXT
);

CREATE INDEX IF NOT EXISTS idx_fact_tiempo ON fact_proceso(tiempo_key);
CREATE INDEX IF NOT EXISTS idx_fact_entidad ON fact_proceso(entidad_key);
CREATE INDEX IF NOT EXISTS idx_fact_territorio ON fact_proceso(territorio_key);
CREATE INDEX IF NOT EXISTS idx_fact_contratacion ON fact_proceso(contratacion_key);
CREATE INDEX IF NOT EXISTS idx_fact_proveedor ON fact_proceso(proveedor_key);
CREATE INDEX IF NOT EXISTS idx_fact_id_proceso ON fact_proceso(id_del_proceso);

CREATE TABLE IF NOT EXISTS etl_carga (
    carga_key INTEGER PRIMARY KEY CHECK (carga_key = 1),
    archivo_origen TEXT NOT NULL,
    registros_csv INTEGER NOT NULL CHECK (registros_csv >= 0),
    registros_hecho INTEGER NOT NULL CHECK (registros_hecho >= 0),
    duplicados_exactos_omitidos INTEGER NOT NULL CHECK (duplicados_exactos_omitidos >= 0),
    cargado_en_utc TEXT NOT NULL
);
