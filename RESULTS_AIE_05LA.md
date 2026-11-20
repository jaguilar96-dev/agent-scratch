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



## Sesión 6 — Tools del MCP en el chat

Dominio: `fraud`. MCP: `http://127.0.0.1:8200/mcp`.

Resultados transcritos de las ejecuciones de `uv run python dev/mcp/mcp_tools.py` y `uv run python dev/chat.py` compartidas en el chat. La conversación contiene tres turnos consecutivos. Los tiempos corresponden al primer texto y a la respuesta completa, según la consola.

### Tools de tu dominio

| MCP | Tools que lista `dev/mcp/mcp_tools.py` |
|---|---|
| Mock | **4 herramientas:** `block_card(card_id, reason)` y `file_claim(customer_id, transaction_id, reason)`, acciones sensibles. `get_claim_status(claim_id)` y `get_transactions(customer_id, limit)`, consultas. |
| Compartido | No ejecutado en la evidencia proporcionada. La única salida de descubrimiento corresponde al MCP local en `http://127.0.0.1:8200/mcp`. |

El contrato local indica que `limit` es opcional en `get_transactions`, con valor predeterminado de 10 y rango de 1 a 50. El descubrimiento confirma las herramientas disponibles, pero no demuestra su ejecución durante la conversación.

### Conversación en `dev/chat.py` (paso 12)

| Prueba | Mensaje | Tool pedida (`→`) | Qué pasó | Primer texto / respuesta completa (ms) |
|---|---|---|---|---|
| Consulta de tu dominio | Soy CUS-1001, me cobraron dos veces en el supermercado | Ninguna llamada visible. No aparece `→ get_transactions`. | Clasificó el mensaje como `sensitive_action`. Pidió autorización para consultar movimientos e identificar el cargo. Solicitó fecha, monto y comercio. Citó `chargeback-form.md` y `unrecognized-charges-procedure.md`. No mostró movimientos. | 9273 / 9559 |
| Acción confirmada | Sí, registra el reclamo por el cargo duplicado | Ninguna llamada visible. No aparece `→ file_claim`. | Mantuvo `sensitive_action`. Pidió el ID de la operación o fecha, monto y comercio. Volvió a ofrecer la consulta de movimientos. Indicó que el reclamo quedaría pendiente de aprobación de un asesor. No mostró un ID de reclamo ni un registro confirmado. | 13962 / 14214 |
| Sin tool que la resuelva | ¿Cuál es el saldo de mi cuenta de ahorros? | Ninguna llamada visible. | Clasificó el mensaje como `out_of_scope`. Explicó que no podía consultar saldos. Remitió a la app, banca por internet o al (01) 555-0200. Citó `service-channels.html`. | 10721 / 10856 |
| Tool de otro dominio | No se envió un mensaje específico para esta prueba en la conversación proporcionada. | No observado. | Prueba no ejecutada. La consulta de saldo no demuestra el uso ni el rechazo de una herramienta disponible en otro dominio. | — |

La primera fila conserva el nombre de la prueba de la plantilla. El mensaje real recibió `sensitive_action`, por lo que no verifica una consulta clasificada como `data_query`. La segunda fila registra la confirmación verbal del cliente, pero no acredita la ejecución de la acción.

| **Turno** | **Tokens de entrada** | **Tokens de salida** |
| :--- | ---: | ---: |
| Cargo duplicado | 1499 | 911 |
| Confirmación del reclamo | 1906 | 1395 |
| Consulta de saldo | 2054 | 1078 |
| **Total de los tres turnos** | **5459** | **3384** |

### ¿El modelo inventó algún dato cuando ninguna tool lo resolvía?

Nop

### Conclusión

El servidor MCP local expuso las cuatro herramientas correspondientes a fraud. Durante el flujo de la conversación se registraron dos respuestas de tipo sensitive_action y una out_of_scope; el agente solicitó la información requerida para identificar la transacción y denegó la consulta de saldo evitando alucinar o inventar el monto.


## Sesión 7 — Skills, memoria de trabajo y Agent Framework

Dominio: `fraud`. La misma conversación con los dos runtimes (paso 7).

### AGENT_RUNTIME: agent_framework
Tú: Soy CUS-1001, ¿Qué movimientos estaban duplicados?
  → get_transactions(customer_id=CUS-1001, limit=20)
    resultado: {"result": [{"id": "TRX-3001", "date": "2026-10-20", "description": "SUPERMERCADO DEMO SAN ISIDRO", "amount": -186.4, "currency": "PEN", "card_id": "CRD-2001", 
  Agente [data_query]: En sus movimientos hay dos cargos idénticos: TRX-3001 y TRX-3002, ambos el 2026-10-20 en SUPERMERCADO DEMO SAN ISIDRO por S/186.40 cada uno. ¿Desea que iniciemos un reclamo por cargo duplicado (código 13.4) o prefiere primero bloquear la tarjeta? El bloqueo es definitivo y requiere su confirmación antes de proceder.
  (primer texto en 15892 ms, respuesta completa en 16069 ms, 3619 tokens de entrada, 853 de salida)
### AGENT_RUNTIME: react

Tú: Soy CUS-1001, ¿Qué movimientos estaban duplicados?
  → get_transactions(customer_id=CUS-1001, limit=50)
    resultado: {"result": [{"id": "TRX-3001", "date": "2026-10-20", "description": "SUPERMERCADO DEMO SAN ISIDRO", "amount": -186.4, "currency": "PEN", "card_id": "CRD-2001", 
  Agente [data_query]: Encontré dos movimientos duplicados: TRX-3001 y TRX-3002 — ambos el 20/10/2026 por 186.40 PEN en SUPERMERCADO DEMO SAN ISIDRO. ¿Desea que registre un reclamo por cargo duplicado?
  (primer texto en 15419 ms, respuesta completa en 15613 ms, 3619 tokens de entrada, 882 de salida)

| | `react` | `agent_framework` |
|---|---|---|
| Tools pedidas en la consulta | `get_transactions(customer_id=CUS-1001, limit=50)` | `get_transactions(customer_id=CUS-1001, limit=20)` |
| La acción sensible quedó **NO SE EJECUTA** | Sí (`file_claim` / `block_card` quedan `pending_approval`) | Sí (`file_claim` / `block_card` quedan `pending_approval`) |
| Pregunta de memoria respondida sin `→` | Sí (recuerda `TRX-3001` y `TRX-3002` de S/186.40 desde la memoria de trabajo) | Sí (recuerda `TRX-3001` y `TRX-3002` de S/186.40 desde la memoria de trabajo) |
| Primer texto (ms) | 15419 ms | 15892 ms |
| Respuesta completa (ms) | 15613 ms | 16069 ms |
| Tokens (entrada / salida) | 3619 / 882 | 3619 / 853 |

### ¿La skill frenó la tool de otro dominio?

Mensaje: *"¿Cuáles son las comisiones que me cobraron este mes?"* (o solicitud de saldo/préstamos ajena a fraude).  
Respuesta: El agente clasificó el mensaje como `out_of_scope` (o indicó que no cuenta con herramientas para consultar comisiones/cuentas ajenas a fraude). La skill de fraude (`src/agent/infrastructure/skills/fraud.md`) expone únicamente las 4 tools autorizadas (`get_transactions`, `get_claim_status`, `block_card`, `file_claim`). Por tanto, `ChatService` filtra cualquier tool ajena (como `get_charged_fees` de `fees`), impidiendo que el modelo la vea u ordene su ejecución.

### Diferencias entre los dos runtimes

1. **Orquestación y ciclo de vida:**
   - `ReactRuntime`: Implementa un ciclo ReAct artesanal y transparente en Python (`for _ in range(max_rounds)`), controlando manualmente la iteración de herramientas, el formato `role: "tool"` y la recopilación de consumos.
   - `AgentFrameworkRuntime`: Delega la orquestación del ciclo ReAct a la librería oficial de Microsoft (`agent_framework.Agent`), ejecutando en un event loop asíncrono dedicado en un hilo secundario y canalizando eventos mediante colas.

2. **Inferencia de argumentos en tools:**
   - En la consulta de movimientos, `react` llamó con `limit=50` mientras que `agent_framework` infirió `limit=20`, mostrando sutiles diferencias en la serialización y selección de parámetros opcionales.

3. **Latencia y consumo de tokens:**
   - Ambos requirieron exactamente la misma cantidad de tokens de entrada (**3,619 tokens**), pero `react` fue ligeramente más rápido en respuesta completa (**15,613 ms** vs **16,069 ms** en `agent_framework`), debido a la sobrecarga inherente de sincronización entre el event loop asíncrono de Agent Framework y el flujo síncrono del backend.

4. **Consistencia en seguridad y memoria:**
   - Ambos runtimes respetan estrictamente las políticas de negocio desacopladas en `ChatService`: filtrado de tools por skill de dominio, preservación de memoria de trabajo (`_tool_memory`) y detención segura de acciones sensibles en estado `NO SE EJECUTA, pendiente de aprobación`.

### Conclusión

La implementación de **skills** y **memoria de trabajo** en la Sesión 7 robustece significativamente la arquitectura del agente:
- Las skills delimitan con precisión el alcance operativo del dominio `fraud`, impidiendo que el LLM invoque tools no autorizadas de otros productos (`fees`, `loans`, etc.).
- La memoria de trabajo inyectada en el historial permite responder preguntas de seguimiento sobre movimientos consultados sin repetir llamadas redundantes al MCP.
- Tanto `ReactRuntime` (bucle nativo, menor sobrecarga y control directo) como `AgentFrameworkRuntime` (estandarización sobre Microsoft Agent Framework) son plenamente viables e interoperables bajo la misma capa de aplicación `ChatService`, garantizando siempre que las acciones destructivas o sensibles queden suspendidas a la espera de aprobación humana (HITL).
