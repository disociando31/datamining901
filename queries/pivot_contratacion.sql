-- Matriz de registros por modalidad y tipo de contrato.
-- Revertir filas y columnas cambia los atributos agrupados, no la medida.
SELECT
    c.modalidad_de_contratacion AS fila,
    c.tipo_de_contrato AS columna,
    COUNT(*) AS registros,
    COUNT(DISTINCT f.id_del_proceso) AS procesos_unicos,
    COALESCE(SUM(f.valor_total_adjudicacion_cop), 0) AS valor_adjudicado_cop,
    AVG(f.precio_base_cop) AS precio_base_promedio_cop
FROM fact_proceso AS f
JOIN dim_contratacion AS c
    ON c.contratacion_key = f.contratacion_key
JOIN dim_territorio AS r
    ON r.territorio_key = f.territorio_key
JOIN dim_entidad AS e
    ON e.entidad_key = f.entidad_key
WHERE (:departamento IS NULL OR r.departamento_entidad = :departamento)
  AND (:orden IS NULL OR e.orden_entidad = :orden)
GROUP BY c.modalidad_de_contratacion, c.tipo_de_contrato
ORDER BY registros DESC;
