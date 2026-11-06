-- Comparación temporal en los mismos pares de mes y día para cada año.
-- En el CSV actual, el corte común obtenido por intersección es el día 1
-- de cada mes; los valores se consultan y parametrizan, no se fijan en la app.
SELECT
    t.anio,
    COUNT(*) AS registros,
    COUNT(DISTINCT f.id_del_proceso) AS procesos_unicos,
    COALESCE(SUM(f.valor_total_adjudicacion_cop), 0) AS valor_adjudicado_cop
FROM fact_proceso AS f
JOIN dim_tiempo AS t
    ON t.tiempo_key = f.tiempo_key
JOIN dim_contratacion AS c
    ON c.contratacion_key = f.contratacion_key
JOIN dim_territorio AS r
    ON r.territorio_key = f.territorio_key
WHERE ((t.mes = :mes_1 AND t.dia = :dia_1)
   OR (t.mes = :mes_2 AND t.dia = :dia_2)
   OR (t.mes = :mes_3 AND t.dia = :dia_3)
   OR (t.mes = :mes_4 AND t.dia = :dia_4)
   OR (t.mes = :mes_5 AND t.dia = :dia_5)
   OR (t.mes = :mes_6 AND t.dia = :dia_6)
   OR (t.mes = :mes_7 AND t.dia = :dia_7)
   OR (t.mes = :mes_8 AND t.dia = :dia_8)
   OR (t.mes = :mes_9 AND t.dia = :dia_9)
   OR (t.mes = :mes_10 AND t.dia = :dia_10)
   OR (t.mes = :mes_11 AND t.dia = :dia_11)
   OR (t.mes = :mes_12 AND t.dia = :dia_12))
  AND (:modalidad IS NULL OR c.modalidad_de_contratacion = :modalidad)
  AND (:departamento IS NULL OR r.departamento_entidad = :departamento)
GROUP BY t.anio
ORDER BY t.anio;
