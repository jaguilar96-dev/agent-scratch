chunks más chicos	$env:INGEST_CHUNK_MAX_CHARS = "800", luego uv run ingest build y uv run ingest publish	recall y hechos

Resultado:
Resumen de 31 casos (juez local):
  recall@5: 0.96   intención: 0.97   fuentes: 0.94   hechos: 0.89
  apoyo: 4.9/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 1
  tokens: 29711 de entrada, 16859 de salida

$env:SEARCH_TOP_K = "3"
Resultado:
Resumen de 31 casos (juez local):
  recall@3: 0.96   intención: 0.97   fuentes: 0.97   hechos: 0.89
  apoyo: 4.9/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 0
  tokens: 24391 de entrada, 15542 de salida

$env:SEARCH_TOP_K = "8"
Resultado:
Resumen de 31 casos (juez local):
  recall@8: 0.96   intención: 0.97   fuentes: 0.94   hechos: 0.86
  apoyo: 4.9/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 1
  tokens: 38030 de entrada, 16704 de salida


base local, sin reranker	uv run ingest publish --target local, luego $env:KNOWLEDGE_BASE = "local"	recall y apoyo: cuánto aporta el reranker de AI Search
Resultado:
Resumen de 31 casos (juez local):
  recall@8: 0.96   intención: 0.97   fuentes: 0.97   hechos: 0.86
  apoyo: 4.9/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 0
  tokens: 35884 de entrada, 16694 de salida

Comparativa:
    Azure:
        Resumen de 31 casos (juez azure_evaluation):
          recall@8: 0.96   intención: 0.97   fuentes: 0.94   hechos: 0.86
          apoyo: 4.9/5   relevancia: 4.8/5   cita correcta: 1.0
          fugas de datos personales: 0   citas de fuentes prohibidas: 1
          tokens: 35925 de entrada, 17571 de salida
    AIE_05LA:
        Resumen de 1 casos (juez local):
          recall@8: 0.00   intención: 0.00   fuentes: 0.00   hechos: 0.00
          apoyo: 3.0/5   relevancia: 2.0/5   cita correcta: 0.0
          fugas de datos personales: 0   citas de fuentes prohibidas: 0
          tokens: 1293 de entrada, 490 de salida

¿Las notas de apoyo y de cita correcta van en la misma dirección?

**Sí, en general guardan correlación positiva, pero con matices según la presencia de citas:**
- En la corrida de **Azure (31 casos)**, ambas métricas son sobresalientes y van de la mano: el **apoyo es de 4.9/5** (el contenido está fielmente respaldado por los fragmentos) y la **cita correcta es de 1.0** (las fuentes citadas sustentan exactamente lo que afirma el agente).
- En el caso aislado de **AIE_05LA (1 caso)**, el apoyo cayó a **3.0/5** (mencionó temas permitidos del dominio, pero incluyó advertencias no textuales y no contestó de fondo), mientras que la cita correcta se fue a **0.0** porque el agente no citó ninguna fuente (`cited_sources: []`). 
- **Conclusión:** Aunque ambas métricas descienden ante una mala respuesta, la nota de *cita correcta* es más penalizante y sensible a la ausencia total de citas (cae a 0), mientras que el *apoyo* evalúa la proporción de verdad de las afirmaciones dentro del contexto recuperado.

¿Cuánto tardó cada corrida?

Revisando las latencias registradas en los reportes de evaluación (`data/eval/`):

- **Azure (31 casos, juez `azure_evaluation` / `decision-1`):**
  - **Tiempo total:** **151.92 segundos** (~2 minutos con 32 segundos).
  - **Promedio por caso:** **4,901 ms** (~4.90 s / caso).
  - **Tokens consumidos:** 35,925 de entrada y 17,571 de salida.

- **AIE_05LA (1 caso, juez `local` / `g-eval`):**
  - **Tiempo total:** **5.23 segundos** (5,225 ms).
  - **Tokens consumidos:** 1,293 de entrada y 490 de salida.

*(Como referencia comparativa con las corridas anteriores de 31 casos: chunks 800 tardó 179.12 s, top_k=3 tardó 155.14 s, top_k=8 tardó 162.95 s y base local tardó 159.20 s).*


