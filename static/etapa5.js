(() => {
    const page = document.querySelector("[data-etapa5-view]");
    if (!page) return;

    const apiUrl = page.dataset.apiUrl;
    const indicators = page.querySelector('[data-role="indicators"]');
    const charts = page.querySelector('[data-role="charts"]');
    const matrix = page.querySelector('[data-role="matrix"]');
    const matrixCaption = page.querySelector('[data-role="matrix-caption"]');
    const insights = page.querySelector('[data-role="insights"]');
    const selection = page.querySelector('[data-role="selection"]');
    const operationHelp = page.querySelector('[data-role="operation-help"]');
    const errorMessage = page.querySelector('[data-role="error"]');
    const limitation = page.querySelector('[data-role="limitation"]');
    const decision = page.querySelector('[data-role="decision"]');
    const filters = [
        page.querySelector('[data-role="filter-one"]'),
        page.querySelector('[data-role="filter-two"]'),
    ];
    const filterLabels = [
        page.querySelector('[data-role="filter-one-label"]'),
        page.querySelector('[data-role="filter-two-label"]'),
    ];
    const filterHelp = [
        page.querySelector('[data-role="filter-one-help"]'),
        page.querySelector('[data-role="filter-two-help"]'),
    ];
    const numberFormat = new Intl.NumberFormat("es-CO", {
        maximumFractionDigits: 0,
    });
    const currencyFormat = new Intl.NumberFormat("es-CO", {
        style: "currency",
        currency: "COP",
        maximumFractionDigits: 0,
    });
    let level = 0;
    let operation = "dice";
    let requestId = 0;

    function element(tag, className, text) {
        const node = document.createElement(tag);
        if (className) node.className = className;
        if (text !== undefined) node.textContent = text;
        return node;
    }

    function formatValue(value, unit) {
        const numericValue = Number(value);
        if (!Number.isFinite(numericValue)) return String(value ?? "—");
        if (unit === "COP") return currencyFormat.format(numericValue);
        if (unit === "%") {
            return `${new Intl.NumberFormat("es-CO", {
                maximumFractionDigits: 1,
            }).format(numericValue)}%`;
        }
        return numberFormat.format(numericValue);
    }

    function renderIndicators(items) {
        indicators.replaceChildren();
        for (const item of items) {
            const card = element("article", "etapa5-indicador");
            card.append(
                element("span", "", item.label),
                element(
                    "strong",
                    item.unit === "COP" ? "etapa5-indicador-valor--moneda" : "",
                    formatValue(item.value, item.unit),
                ),
                element("small", "", `${item.unit} · ${item.denominator}`),
            );
            indicators.append(card);
        }
    }

    function renderCharts(items) {
        charts.replaceChildren();
        for (const chart of items) {
            const card = element("article", "etapa5-grafico");
            card.append(
                element("h2", "", chart.title),
                element("p", "etapa5-nota", chart.denominator),
            );
            const list = element("ol", "etapa5-barras");
            const values = chart.rows.map((row) => Number(row[chart.metric]) || 0);
            const maximum = Math.max(...values, 0);

            for (const row of chart.rows) {
                const value = Number(row[chart.metric]) || 0;
                const item = element("li", "etapa5-barra");
                const heading = element("div", "etapa5-barra-cabecera");
                heading.append(
                    element("span", "etapa5-barra-etiqueta", row.label),
                    element("strong", "etapa5-barra-valor", formatValue(value, chart.unit)),
                );
                const track = element("span", "etapa5-barra-pista");
                const fill = element("span", "etapa5-barra-relleno");
                fill.style.width = `${maximum ? Math.max(0, value / maximum * 100) : 0}%`;
                track.append(fill);
                item.append(heading, track);
                if (Number.isFinite(Number(row.share_percent))) {
                    item.append(element(
                        "small",
                        "etapa5-barra-participacion",
                        `${new Intl.NumberFormat("es-CO", {
                            maximumFractionDigits: 1,
                        }).format(row.share_percent)}% del corte`,
                    ));
                }
                list.append(item);
            }
            if (!chart.rows.length) {
                list.append(element("li", "etapa5-nota", "Sin datos para esta selección."));
            }
            card.append(list);
            charts.append(card);
        }
    }

    function renderMatrix(data) {
        matrixCaption.textContent =
            `Filas: ${data.row_label} · Columnas: ${data.column_label}`;
        matrix.replaceChildren();
        if (!data.rows.length || !data.columns.length) {
            matrix.append(element("p", "etapa5-nota", "Sin datos para esta selección."));
            return;
        }
        const table = element("table");
        const thead = element("thead");
        const headerRow = element("tr");
        headerRow.append(element("th", "", data.row_label));
        for (const column of data.columns) {
            headerRow.append(element("th", "", column));
        }
        headerRow.append(element("th", "", "Total visible"));
        thead.append(headerRow);
        const tbody = element("tbody");
        for (const row of data.rows) {
            const tableRow = element("tr");
            tableRow.append(element("th", "", row.label));
            for (const value of row.cells) {
                tableRow.append(element("td", "", numberFormat.format(value)));
            }
            tableRow.append(element("td", "", numberFormat.format(row.total)));
            tbody.append(tableRow);
        }
        table.append(thead, tbody);
        matrix.append(table);
    }

    function renderInsights(items) {
        insights.replaceChildren();
        for (const insight of items) {
            const card = element("article", "etapa5-conocimiento");
            const dimensions = insight.dimensions
                .map((item) => `${item.dimension}: ${item.attribute}`)
                .join(" · ");
            const measures = insight.measures.join(" · ");
            const activeFilters = insight.active_filters.length
                ? insight.active_filters.join(" · ")
                : "Sin filtros adicionales";
            card.append(
                element("h3", "", insight.title),
                element("p", "etapa5-conocimiento-dimensiones", `Dimensiones: ${dimensions}`),
                element("p", "etapa5-conocimiento-medidas", `Medidas: ${measures}`),
                element(
                    "p",
                    "etapa5-conocimiento-contexto",
                    `Nivel OLAP ${insight.level.index} de ${insight.level.count}: ` +
                    `${insight.level.dimension} · Filtros: ${activeFilters}`,
                ),
                element("p", "", insight.finding),
                element("p", "", insight.procedure),
                element("p", "", insight.evidence),
                element("p", "", insight.interpretation),
                element("p", "", insight.utility),
                element("p", "", `Limitación: ${insight.limitation}`),
            );
            insights.append(card);
        }
    }

    function renderFilters(items) {
        items.forEach((filter, index) => {
            filterLabels[index].textContent = filter.label;
            filterHelp[index].textContent =
                index === 0
                    ? `Filtra por ${filter.label.toLowerCase()}. Slice usa solo este filtro; ` +
                      "Dice lo combina con el otro."
                    : `Filtra por ${filter.label.toLowerCase()}. Dice lo combina con el primero; ` +
                      "Slice ignora este filtro.";
            const select = filters[index];
            select.replaceChildren();
            select.append(new Option("Todas las categorías", ""));
            for (const option of filter.options) {
                select.append(new Option(option.label, option.value));
            }
            select.value = filter.selected ?? "";
        });
    }

    function renderSelection(data) {
        const appliedFilters = data.active_filters.length
            ? data.active_filters.join(" · ")
            : "Sin filtros adicionales";
        selection.textContent =
            `Operación: ${data.operation} · Nivel ${data.level + 1} de ${data.level_count} ` +
            `(${data.active_dimension}) · ${appliedFilters}`;
        page.querySelector('[data-operation="roll-up"]').disabled = data.level === 0;
        page.querySelector('[data-operation="drill-down"]').disabled =
            data.level >= data.level_count - 1;
        page.querySelectorAll("[data-operation]").forEach((button) => {
            button.classList.toggle(
                "etapa5-operacion-activa",
                button.dataset.operation === data.operation,
            );
        });

        const selectedOption = (index) =>
            filters[index].selectedOptions[0]?.textContent ?? "Todas las categorías";
        const previousLevel = data.operation === "drill-down"
            ? Math.max(data.level - 1, 0)
            : Math.min(data.level + 1, data.hierarchy.length - 1);
        const previousDimension = data.hierarchy[previousLevel];
        const activeDimension = data.hierarchy[data.level];

        if (data.operation === "drill-down") {
            operationHelp.textContent =
                `Drill-down: detalle de ${previousDimension} a ${activeDimension}. ` +
                `Los indicadores y gráficos se recalcularon para los grupos detallados. Filtros: ${appliedFilters}.`;
        } else if (data.operation === "roll-up") {
            operationHelp.textContent =
                `Roll-up: agrupación de ${previousDimension} a ${activeDimension}. ` +
                `Los indicadores y gráficos se recalcularon en el nivel superior. Filtros: ${appliedFilters}.`;
        } else if (data.operation === "slice") {
            const ignoredFilter = selectedOption(1);
            operationHelp.textContent =
                `Slice: se aplica solo «${filterLabels[0].textContent} = ${selectedOption(0)}». ` +
                (filters[0].value
                    ? "El segundo filtro no afecta estos resultados. "
                    : "El primer filtro está en «Todas las categorías», así que no reduce los datos. ") +
                (filters[1].value
                    ? `«${filterLabels[1].textContent} = ${ignoredFilter}» está seleccionado, pero Slice lo ignora.`
                    : "El segundo filtro no se aplica en Slice.");
        } else if (data.operation === "dice") {
            operationHelp.textContent = data.active_filters.length
                ? `Dice: se consultan los registros que cumplen simultáneamente: ${appliedFilters}.`
                : "Dice: ambos filtros están en «Todas las categorías»; se consulta todo el conjunto.";
        } else {
            operationHelp.textContent =
                `Pivot: se intercambiaron las filas y columnas de la matriz ` +
                `(${matrixCaption.textContent}). Se mantienen las selecciones y se aplican ambos filtros ` +
                `igual que en Dice. Filtros activos: ${appliedFilters}.`;
        }
    }

    async function loadData(nextOperation = operation) {
        operation = nextOperation;
        const currentRequest = ++requestId;
        const parameters = new URLSearchParams({
            operation,
            level: String(level),
            filter_one: filters[0].value,
            filter_two: filters[1].value,
        });
        errorMessage.hidden = true;
        errorMessage.textContent = "";

        try {
            const response = await fetch(`${apiUrl}?${parameters}`, {
                headers: { Accept: "application/json" },
            });
            const payload = await response.json();
            if (!response.ok) {
                throw new Error(payload.error || `La consulta falló (${response.status}).`);
            }
            if (currentRequest !== requestId) return;

            level = payload.level;
            renderFilters(payload.filters);
            renderIndicators(payload.indicators);
            renderCharts(payload.charts);
            renderMatrix(payload.matrix);
            renderInsights(payload.insights);
            renderSelection(payload);
            limitation.textContent = payload.limitation;
            decision.textContent = payload.decision;
        } catch (error) {
            if (currentRequest !== requestId) return;
            errorMessage.textContent = `No se pudo actualizar el análisis: ${error.message}`;
            errorMessage.hidden = false;
        }
    }

    page.querySelector(".etapa5-acciones").addEventListener("click", (event) => {
        const button = event.target.closest("[data-operation]");
        if (!button || button.disabled) return;
        loadData(button.dataset.operation);
    });

    filters.forEach((filter) => {
        filter.addEventListener("change", () => loadData("dice"));
    });

    loadData();
})();
