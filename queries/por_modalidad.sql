-- Registros, procesos distintos, valor adjudicado y promedio de precio base.
-- Los filtros pueden enviarse como NULL para no aplicarlos.
SELECT
    c.modalidad_de_contratacion AS categoria,
    COUNT(*) AS registros,
    COUNT(DISTINCT f.id_del_proceso) AS procesos_unicos,
    COALESCE(SUM(f.valor_total_adjudicacion_cop), 0) AS valor_adjudicado_cop,
    AVG(f.precio_base_cop) AS precio_base_promedio_cop
FROM fact_proceso AS f
JOIN dim_contratacion AS c
    ON c.contratacion_key = f.contratacion_key
JOIN dim_territorio AS r
    ON r.territorio_key = f.territorio_key
WHERE (:departamento IS NULL OR r.departamento_entidad = :departamento)
  AND (:estado IS NULL OR c.estado_del_procedimiento = :estado)
GROUP BY c.modalidad_de_contratacion
ORDER BY registros DESC;
