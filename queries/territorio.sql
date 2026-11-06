-- Drill-down territorial. :nivel debe provenir de una lista allowlist
-- (r.departamento_entidad o r.ciudad_entidad), nunca de entrada libre.
SELECT
    r.departamento_entidad AS departamento,
    r.ciudad_entidad AS ciudad,
    COUNT(*) AS registros,
    COUNT(DISTINCT f.id_del_proceso) AS procesos_unicos,
    COALESCE(SUM(f.valor_total_adjudicacion_cop), 0) AS valor_adjudicado_cop,
    AVG(f.precio_base_cop) AS precio_base_promedio_cop
FROM fact_proceso AS f
JOIN dim_territorio AS r
    ON r.territorio_key = f.territorio_key
JOIN dim_entidad AS e
    ON e.entidad_key = f.entidad_key
JOIN dim_contratacion AS c
    ON c.contratacion_key = f.contratacion_key
WHERE (:orden IS NULL OR e.orden_entidad = :orden)
  AND (:adjudicado IS NULL OR c.adjudicado = :adjudicado)
GROUP BY r.departamento_entidad, r.ciudad_entidad
ORDER BY registros DESC;
