-- Describe si hay un NIT informado; no equivale a verificación de identidad.
SELECT
    CASE
        WHEN p.nit_del_proveedor_adjudicado IS NULL
          OR p.nit_del_proveedor_adjudicado = 'No Definido'
        THEN 'No identificado en la fuente'
        ELSE 'NIT reportado'
    END AS identificacion_en_fuente,
    COUNT(*) AS registros,
    COUNT(DISTINCT f.id_del_proceso) AS procesos_unicos,
    COALESCE(SUM(f.valor_total_adjudicacion_cop), 0) AS valor_adjudicado_cop
FROM fact_proceso AS f
JOIN dim_proveedor AS p
    ON p.proveedor_key = f.proveedor_key
JOIN dim_contratacion AS c
    ON c.contratacion_key = f.contratacion_key
JOIN dim_territorio AS r
    ON r.territorio_key = f.territorio_key
WHERE (:modalidad IS NULL OR c.modalidad_de_contratacion = :modalidad)
  AND (:departamento_proveedor IS NULL
       OR p.departamento_proveedor = :departamento_proveedor)
GROUP BY identificacion_en_fuente
ORDER BY registros DESC;
