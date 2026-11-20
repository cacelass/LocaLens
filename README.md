# LocaLens

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-0.1.0-green)
![Author](https://img.shields.io/badge/Author-cacelass-blueviolet)

> Pedestrian Mobility Intelligence, Commercial Location Analysis & Opening Hours Optimization.

LocaLens es una plataforma de inteligencia geoespacial diseñada para
comprender la movilidad peatonal, evaluar ubicaciones comerciales,
predecir demanda y optimizar horarios de apertura.

Transforma datos agregados de movilidad en decisiones comerciales
accionables: dónde abrir, cuándo abrir y cuánta oportunidad comercial
existe.

**Mercado inicial:** España (Vigo, Galicia).

---

## Tabla de contenidos

- [Visión](#visión)
- [Módulos](#módulos)
- [Inicio rápido](#inicio-rápido)
- [Estructura del proyecto](#estructura-del-proyecto)
- [El arnés](#el-arnés)
- [Roadmap](#roadmap)

---

## Visión

LocaLens responde a tres preguntas interconectadas:

1. **¿Dónde debo abrir?** — Inteligencia geoespacial, movilidad peatonal,
   competencia, accesibilidad y scoring de ubicación.
2. **¿Cuándo debo abrir?** — Análisis histórico, predicción de demanda y
   optimización matemática de horarios.
3. **¿Cuánta oportunidad comercial existe?** — Exposición peatonal,
   analítica de conversión, supuestos comerciales, costes y escenarios.

Filosofía: LocaLens es una plataforma de soporte a la decisión, no solo
una visualización de datos de movilidad.

---

## Módulos

| Módulo | Descripción | Prioridad |
|--------|-------------|-----------|
| 01. Ingesta de datos | Conectores mobility, geo, weather, demographic | P0 |
| 02. Calidad y validación | Validación, categorías semánticas, provenance | P0 |
| 03. Motor geoespacial | H3, joins espaciales, red de calles, features | P0 |
| 04. Analítica de movilidad | Métricas, análisis temporal, visualización | P0 |
| 05. Predicción de movilidad | Baselines, ML, validación, incertidumbre | P0 |
| 06. Segmentación urbana | Clustering de áreas por movilidad/comercio | P1 |
| 07. Inteligencia de ubicación | Scoring, competencia, accesibilidad, explicabilidad | P0 |
| 08. Conversión peatón-tienda | Footfall, entradas, tasa de entrada | P1 |
| 09. Optimización de horarios | MILP, OR-Tools, restricciones, escenarios | P0/P1 |
| 10. Detección de anomalías | Cambios inusuales en movilidad | P2 |

---

## Inicio rápido

```bash
make setup     # uv sync --extra dev + hooks de pre-commit
make init      # la puerta: ¿el proyecto está sano?
make run       # ejecuta el paquete de ejemplo
make check     # lint + typecheck + test + arnés
```

Y para arrancar el ciclo de trabajo en tu asistente:

> Lee `AGENTS.md` y sigue el protocolo: ejecuta `./init.sh`, lee
> `harness/progress/` y elige la primera feature pendiente.

---

## Estructura del proyecto

```
localens/              ← TU código (paquete principal)
tests/                 ← tus tests
agents/                ← el sistema de agentes (arnés)
harness/               ← backlog con criterios de aceptación + progreso
vault/                 ← conocimiento estable del proyecto (Obsidian)
docs/                  ← Sphinx + spec + PRD
```

La especificación completa está en `docs/spec/LocaLens.md`.

---

## El arnés

Este repositorio incluye el arnés de agentes de MeshHarmes. Ver `AGENTS.md`.

---

## Roadmap

- **Phase 0** — Investigación de factibilidad y datos (CRÍTICO).
- **Phase 1** — Fundación de datos.
- **Phase 2** — Inteligencia de movilidad.
- **Phase 3** — Machine learning.
- **Phase 4** — Inteligencia comercial.
- **Phase 5** — Optimización de horarios.
- **Phase 6** — Integración del producto.

**MVP:** Explorador de movilidad + analizador de ubicación + optimizador
de horarios para Vigo.

---

## Restricciones clave

- No asumir que Google proporciona API gratuita para conteos peatonales.
- No confundir tráfico vehicular con peatonal.
- No confundir actividad de dispositivos móviles con conteos peatonales reales.
- No inventar datasets ni endpoints de proveedores.
- No falsificar precisión espacial.
- No crear predicciones de ingresos falsas.
- No estimar tasas de conversión sin datos o supuestos explícitos.
- No usar ML complejo sin ventaja medible.
- No usar algoritmos genéticos cuando MILP es suficiente.
- No mezclar datos observados, estimados y predichos.
- No ocultar la incertidumbre al usuario.

---

## Licencia

MIT. Ver `LICENSE`.
