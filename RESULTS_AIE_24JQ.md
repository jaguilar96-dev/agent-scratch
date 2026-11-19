# S4
## En local
Tú: ¿Cuál es el plazo para presentar un reclamo?
  Agente [product_question]: Depende del tipo de reclamo: para una operación no reconocida tienes hasta 60 días calendario desde la fecha de la operación. Para reclamos por cobros de comisiones o intereses, el plazo es de 1 año desde el cobro. El reclamo es gratuito y puede presentarse por cualquier canal de atención.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo
  (primer texto en 11514 ms, respuesta completa en 11708 ms, 932 tokens de entrada, 605 de salida)
Tú: ¿y si es por fraude?
  Agente [product_question]: Si es por fraude u operación no reconocida, tienes hasta 60 días calendario desde la fecha de la operación para presentar el reclamo. El banco responde todo reclamo en un máximo de 15 días hábiles; las operaciones no reconocidas con tarjeta se resuelven en un máximo de 10 días hábiles. Si el caso depende de un comercio en el exterior, el plazo puede ampliarse una vez por 15 días hábiles. Si no entregas la información mínima requerida, el plazo se suspende hasta por 5 días hábiles; pasado eso el reclamo puede archivarse.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 4. Plazos de respuesta
   [3] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿En cuánto tiempo me responden?
   [4] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 4. Plazos de respuesta > 4.2 Excepciones
  (primer texto en 13308 ms, respuesta completa en 13595 ms, 1238 tokens de entrada, 1258 de salida)
Tú: ¿Qué es un contracargo?
  Agente [product_question]: En los fragmentos proporcionados no aparece una definición de “contracargo”.
  Fuentes:
   [1] credit-card-chargebacks.html · Contracargos con tarjeta de crédito > Plazos del contracargo
   [2] response-times.csv · response-times
   [3] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 4. Plazos de respuesta
  (primer texto en 18882 ms, respuesta completa en 18900 ms, 1638 tokens de entrada, 1251 de salida)
Tú: ¿Qué decía la política de bloqueo de 2022?
  Agente [product_question]: La política establecía que antes de ejecutar un bloqueo definitivo se debe confirmar con el titular el producto y el tipo de bloqueo. El titular no asume operaciones no reconocidas realizadas después del reporte; las operaciones anteriores se evalúan según el reglamento de reclamos. Los canales disponibles para bloquear son la app, la línea telefónica 24 h y agencias. Existían bloqueo temporal (se puede activar/desactivar desde la app) y bloqueo definitivo (no reversible, para robo/clonación/fraude confirmado, requiere reponer la tarjeta). La tarjeta se bloquea de inmediato cuando el titular reporta robo, pérdida, clonación u operación no reconocida; el banco también puede bloquear preventivamente y contacta al titular para confirmar.
  Fuentes:
   [1] card-blocking-policy.docx · Política de bloqueo de tarjetas > Confirmación obligatoria
   [2] card-blocking-policy.docx · Política de bloqueo de tarjetas > Responsabilidad por operaciones
   [3] card-blocking-policy.docx · Política de bloqueo de tarjetas > Canales de bloqueo
   [4] card-blocking-policy.docx · Política de bloqueo de tarjetas > Tipos de bloqueo
   [5] card-blocking-policy.docx · Política de bloqueo de tarjetas > Cuándo se bloquea una tarjeta
  (primer texto en 11609 ms, respuesta completa en 11927 ms, 1570 tokens de entrada, 996 de salida)
Tú: ¿A cuánto está el dólar hoy?
  Agente [out_of_scope]: Lo siento, eso está fuera del ámbito de fraude, bloqueo y reclamos. Para la cotización del dólar consulta la web o la app del banco, el Banco Central de Reserva o un portal financiero actualizado.
  (primer texto en 6541 ms, respuesta completa en 6697 ms, 1900 tokens de entrada, 486 de salida)

## Comparacion
### SEARCH_TOP_K = 2
Tú: ¿Cuál es el plazo para presentar un reclamo?
  Agente [product_question]: Depende del tipo de reclamo: para una operación no reconocida tiene hasta 60 días calendario desde la fecha de la operación; para reclamos por cobros de comisiones o intereses, el plazo es de 1 año desde el cobro.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
  (primer texto en 10003 ms, respuesta completa en 10156 ms, 690 tokens de entrada, 524 de salida)
Tú: ¿y si es por fraude?
  Agente [product_question]: Si es por fraude (operación no reconocida), tiene hasta 60 días calendario desde la fecha de la operación para presentar el reclamo. El banco responde en un máximo de 10 días hábiles para una operación no reconocida con tarjeta; si el caso depende de un comercio en el exterior, el plazo puede ampliarse una vez por 15 días hábiles.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿En cuánto tiempo me responden?
  (primer texto en 11335 ms, respuesta completa en 11506 ms, 974 tokens de entrada, 1231 de salida)

### SEARCH_TOP_K = 10
Tú: ¿Cuál es el plazo para presentar un reclamo?
  Agente [product_question]: Tienes hasta 60 días calendario desde la fecha de la operación para presentar un reclamo por una operación no reconocida. Para reclamos por cobros de comisiones o intereses, el plazo es de 1 año desde el cobro.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿Cuánto tiempo tengo para reclamar un cargo?
  (primer texto en 8892 ms, respuesta completa en 9072 ms, 1372 tokens de entrada, 396 de salida)
Tú: ¿y si es por fraude?
  Agente [product_question]: Si se trata de fraude u operación no reconocida tienes hasta 60 días calendario desde la fecha de la operación para presentar el reclamo. El banco debe responder en un plazo máximo de 10 días hábiles para operaciones no reconocidas con tarjeta; ese plazo puede ampliarse una sola vez por 15 días hábiles si se requiere información de terceros (marca de tarjeta o comercio en el exterior). Antes de reclamar conviene revisar los movimientos de los últimos 60 días en la app o estado de cuenta.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 4. Plazos de respuesta
   [3] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 4. Plazos de respuesta > 4.1 Ampliación del plazo
   [4] unrecognized-charges-procedure.md · Procedimiento ante cargos no reconocidos > Paso 2: revisar los movimientos
  (primer texto en 12112 ms, respuesta completa en 12404 ms, 1776 tokens de entrada, 1044 de salida)

## Contra AI Search
Tú: ¿Cuál es el plazo para presentar un reclamo?
  Agente [product_question]: Para operaciones no reconocidas: tienes hasta 60 días calendario desde la fecha de la operación. Para reclamos por cobros de comisiones o intereses: el plazo es de 1 año desde el cobro.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿Cuánto tiempo tengo para reclamar un cargo?
  (primer texto en 10826 ms, respuesta completa en 10978 ms, 915 tokens de entrada, 390 de salida)
Tú: ¿y si es por fraude?
  Agente [product_question]: Si es por fraude (operación no reconocida): tienes hasta 60 días calendario desde la fecha de la operación para presentar el reclamo. El banco responde en un plazo máximo de 10 días hábiles para operaciones no reconocidas.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 4. Plazos de respuesta
  (primer texto en 11621 ms, respuesta completa en 11792 ms, 1167 tokens de entrada, 1052 de salida)
Tú: ¿Qué es un contracargo?
  Agente [product_question]: Un contracargo es la devolución de una compra con tarjeta de crédito que el banco gestiona ante la marca de la tarjeta cuando el comercio no entregó el producto, cobró un monto distinto o la operación no fue autorizada por el titular. Se inicia mediante el Formulario de Solicitud de Contracargo y Desconocimiento de Operaciones y aplica en casos como producto/servicio no recibido, cobro duplicado, suscripción cancelada que siguió cobrando u operación no reconocida. Existen códigos para clasificar el motivo (por ejemplo: fraude tarjeta ausente, fraude tarjeta presente, servicio no recibido, cargo duplicado).
  Fuentes:
   [1] credit-card-chargebacks.html · Contracargos con tarjeta de crédito > Qué es un contracargo
   [2] chargeback-form.md · Formulario de Solicitud de Contracargo y Desconocimiento de Operaciones > 1. Propósito del Documento
   [3] credit-card-chargebacks.html · Contracargos con tarjeta de crédito > Casos que aplican
   [4] chargeback-form.md · Formulario de Solicitud de Contracargo y Desconocimiento de Operaciones > 4. Clasificación del Motivo del Contracargo (Tipos de Fraude)
  (primer texto en 9831 ms, respuesta completa en 10134 ms, 1405 tokens de entrada, 828 de salida)
Tú: ¿Qué decía la política de bloqueo de 2022?
  Agente [product_question]: La política indicaba que la tarjeta se bloquea de inmediato si el titular reporta robo, pérdida, clonación o una operación no reconocida; el banco también puede bloquearla preventivamente si detecta patrones de fraude y contacta al titular. El titular no asume las operaciones no reconocidas realizadas después del reporte; las operaciones previas al reporte se evalúan según el reglamento de reclamos. Existían dos tipos de bloqueo: temporal (se puede activar y desactivar desde la app, útil si no encuentra la tarjeta) y definitivo (irreversible, se aplica por robo, clonación o fraude confirmado y requiere reponer la tarjeta). Además, el primer paso ante un cargo no reconocido es bloquear la tarjeta; el bloqueo temporal desde la app es suficiente mientras se revisan los movimientos.
  Fuentes:
   [1] card-blocking-policy.docx · Política de bloqueo de tarjetas > Cuándo se bloquea una tarjeta
   [2] card-blocking-policy.docx · Política de bloqueo de tarjetas > Responsabilidad por operaciones
   [3] card-blocking-policy.docx · Política de bloqueo de tarjetas > Tipos de bloqueo
   [4] unrecognized-charges-procedure.md · Procedimiento ante cargos no reconocidos > Paso 1: bloquear la tarjeta
  (primer texto en 13979 ms, respuesta completa en 14319 ms, 1602 tokens de entrada, 1274 de salida)
Tú: ¿A cuánto está el dólar hoy?
  Agente [out_of_scope]: Eso está fuera de mi alcance: no tengo acceso a cotizaciones en tiempo real. Para la cotización actual revisa la web o la app del banco, o una casa de cambio. ¿Necesitas ayuda con bloqueo de tarjeta, movimientos no reconocidos o un reclamo?
  (primer texto en 9523 ms, respuesta completa en 9694 ms, 2123 tokens de entrada, 621 de salida)

# S5
## Línea base (S5)
Resumen de 30 casos (juez local):
  recall@5: 1.00   intención: 1.00   fuentes: 0.97   hechos: 0.85
  apoyo: 5.0/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 1
  tokens: 28729 de entrada, 15469 de salida
Detalle de cada caso: C:\lab3\agent-scratch\data\eval\fraud-20261117-023805.json

## Línea base + mi pregunta (fraud-AIE24JQ)
Resumen de 31 casos (juez local):
  recall@5: 1.00   intención: 1.00   fuentes: 0.97   hechos: 0.82
  apoyo: 5.0/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 1
  tokens: 29831 de entrada, 16706 de salida
Detalle de cada caso: C:\lab3\agent-scratch\data\eval\fraud-20261117-024633.json

## Resultado del juez
Resumen de 31 casos (juez azure_evaluation):
  recall@5: 1.00   intención: 1.00   fuentes: 1.00   hechos: 0.89
  apoyo: 4.9/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 0
  tokens: 29615 de entrada, 17672 de salida
Detalle de cada caso: C:\lab3\agent-scratch\data\eval\fraud-20261117-025313.json

## Detalle por caso
### Juez local (31 casos)
```
caso         tipo           recall intención fuentes hechos apoyo relevancia  cita  datos personales
fraud-01     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-02     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-03     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-04     answerable       ok      ok       ok      NO     5.0        5.0   1.0  ok
fraud-05     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-06     answerable       ok      ok       ok      ok     4.0        5.0   0.8  ok
fraud-07     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-08     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-09     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-10     answerable       ok      ok       ok      NO     5.0        5.0   1.0  ok
fraud-11     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-12     answerable       ok      ok       ok      NO     5.0        5.0   0.8  ok
fraud-13     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-14     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-15     answerable       ok      ok       ok      NO     5.0        5.0   1.0  ok
fraud-16     answerable       ok      ok       ok      NO     5.0        5.0   1.0  ok
fraud-17     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-18     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-19     follow_up        ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-20     follow_up        ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-21     follow_up        ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-22     expired          ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-23     expired          ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-24     expired          ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-25     noise            -       ok       NO      -        -          -     -  ok
fraud-26     noise            ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-27     out_of_scope     -       ok       ok      -        -          -     -  ok
fraud-28     out_of_scope     -       ok       ok      -        -          -     -  ok
fraud-29     personal_data    ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-30     personal_data    ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-AIE24JQ answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
```

### Juez azure_evaluation (31 casos)
```
caso         tipo           recall intención fuentes hechos apoyo relevancia  cita  datos personales
fraud-01     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-02     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-03     answerable       ok      ok       ok      ok     4.9        5.0   1.0  ok
fraud-04     answerable       ok      ok       ok      NO     5.0        5.0   0.9  ok
fraud-05     answerable       ok      ok       ok      ok     5.0        4.9   1.0  ok
fraud-06     answerable       ok      ok       ok      ok     4.9        4.8   1.0  ok
fraud-07     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-08     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-09     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-10     answerable       ok      ok       ok      NO     5.0        5.0   1.0  ok
fraud-11     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-12     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-13     answerable       ok      ok       ok      ok     4.9        5.0   1.0  ok
fraud-14     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-15     answerable       ok      ok       ok      ok     4.1        5.0   0.9  ok
fraud-16     answerable       ok      ok       ok      NO     5.0        5.0   1.0  ok
fraud-17     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-18     answerable       ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-19     follow_up        ok      ok       ok      ok     4.9        5.0   1.0  ok
fraud-20     follow_up        ok      ok       ok      ok     4.8        4.9   0.9  ok
fraud-21     follow_up        ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-22     expired          ok      ok       ok      ok     5.0        4.9   1.0  ok
fraud-23     expired          ok      ok       ok      ok     4.9        5.0   1.0  ok
fraud-24     expired          ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-25     noise            -       ok       ok      -        -          -     -  ok
fraud-26     noise            ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-27     out_of_scope     -       ok       ok      -        -          -     -  ok
fraud-28     out_of_scope     -       ok       ok      -        -          -     -  ok
fraud-29     personal_data    ok      ok       ok      ok     5.0        5.0   1.0  ok
fraud-30     personal_data    ok      ok       ok      ok     5.0        4.8   1.0  ok
fraud-AIE24JQ answerable       ok      ok       ok      ok     4.7        5.0   1.0  ok
```

## Sesión 6 — Tools del MCP en el chat

Dominio: `fraud`. MCP: el mock (`http://127.0.0.1:8200/mcp`) y el compartido (`bank-mcp`).

### Tools de tu dominio

| MCP | Tools que lista `dev/mcp/mcp_tools.py` |
|---|---|
| Mock | 4: `block_card` (acción sensible), `file_claim` (acción sensible), `get_claim_status` (consulta), `get_transactions` (consulta) |
| Compartido | 4: las mismas, con los mismos parámetros (`block_card`, `file_claim`, `get_claim_status`, `get_transactions`) |

Paso 7 con el mock: `get_transactions customer_id=CUS-1001 limit=2` devolvió TRX-3001 y TRX-3002 (SUPERMERCADO DEMO SAN ISIDRO, -186.40 PEN, el cargo duplicado). `block_card card_id=CRD-2002` bloqueó la tarjeta y la segunda vez respondió `La tarjeta CRD-2002 ya está bloqueada`. Con `DOMAIN=loans` se ven 3 tools (`get_credit_profile`, `simulate_installment`, `submit_loan_application`).

### Conversación en `dev/chat.py` (paso 12)

| Prueba | Mensaje | Tool pedida (`→`) | Qué pasó | Primer texto / respuesta completa (ms) |
|---|---|---|---|---|
| Consulta de tu dominio | Soy CUS-1001, me cobraron dos veces en el supermercado | `get_transactions(customer_id=CUS-1001, limit=20)` y luego `file_claim(customer_id=CUS-1001, transaction_id=TRX-3002, ...)` | Encontró TRX-3001 y TRX-3002. En vez de solo ofrecer el reclamo, lo pidió en el mismo turno; `file_claim` NO SE EJECUTÓ (pendiente de aprobación) y la respuesta lo dijo así | 39106 / 39366 |
| Acción confirmada | Sí, registra el reclamo por el cargo duplicado TRX-3002 | `file_claim(customer_id=CUS-1001, transaction_id=TRX-3002, reason=Cobro duplicado...)` | NO SE EJECUTÓ: quedó pendiente de aprobación de un asesor. La respuesta no dijo "registré", y citó el procedimiento de reclamos del corpus | 25255 / 25537 |
| Sin tool que la resuelva | ¿Cuál es el saldo de mi cuenta de ahorros? | ninguna | Respondió que no puede consultar saldos y sugirió app, cajero, banca telefónica o agencia | 11964 / 12122 |
| Tool de otro dominio | `mcp_tools.py simulate_installment amount=20000 term_months=24` | `simulate_installment` | `Error de la tool: Unknown tool: 'simulate_installment'`: para fraud esa tool no existe | — |

### ¿El modelo inventó algún dato cuando ninguna tool lo resolvía?

No. Con el saldo de ahorros no pidió ninguna tool ni dio un monto: dijo que no puede consultarlo y ofreció los canales del banco. En los turnos con tools, los datos (TRX-3001, TRX-3002, el comercio y el monto) salieron del resultado de `get_transactions`.

### Conclusión

El agente usa las tools del MCP de su dominio y combina sus datos con el RAG (citas del procedimiento de reclamos). Las acciones sensibles nunca llegan al MCP: `_run` las deja pendientes de aprobación, y eso importó en el primer turno, donde el modelo pidió `file_claim` sin esperar la confirmación del cliente. La sesión 8 (aprobación humana) es la que cierra ese hueco. Cambiar del mock al MCP compartido fue solo cambiar `MCP_URL` (con `/mcp` al final) y `MCP_SCOPE` en el `.env`: aparecieron las mismas 4 tools. Con tools, el primer texto tarda entre 25 y 40 s, porque cada vuelta del ciclo es otra llamada a un modelo que razona.

## Sesión 7 — Skills, memoria de trabajo y Agent Framework

Dominio: `fraud`. La misma conversación con los dos runtimes (paso 7), con Foundry real, Azure AI Search (`idx-team-03`) y el MCP compartido (4 tools: `get_transactions`, `get_claim_status`, `block_card`, `file_claim`). Mensajes, en orden: `Soy CUS-1001, me cobraron dos veces en el supermercado` → `Sí, registra el reclamo por el cargo duplicado` → `¿Cuál es el saldo de mi cuenta de ahorros?` → `¿Qué movimientos estaban duplicados?` → `Simúlame la cuota de un préstamo de 20000 soles a 24 meses`.

| | `react` | `agent_framework` |
|---|---|---|
| Tools pedidas en la consulta | `get_transactions(customer_id=CUS-1001, limit=20)`; encontró TRX-3001 y TRX-3002 y pidió confirmación antes del reclamo | `get_transactions(customer_id=CUS-1001, limit=10)`; encontró TRX-3001 y TRX-3002 y pidió confirmación antes del reclamo |
| La acción sensible quedó **NO SE EJECUTA** | Sí: `file_claim(customer_id=CUS-1001, transaction_id=TRX-3002, ...)` sin un `get_transactions` previo (TRX-3002 salió de la memoria) | Sí: `file_claim(customer_id=CUS-1001, transaction_id=TRX-3002, ...)` sin un `get_transactions` previo (TRX-3002 salió de la memoria) |
| Pregunta de memoria respondida sin `→` | Sí: "TRX-3001 y TRX-3002 (ambos del 2026-10-20, SUPERMERCADO DEMO SAN ISIDRO), por -186.40 PEN cada uno" | Sí: "TRX-3001 y TRX-3002: ambos el 2026-10-20 en SUPERMERCADO DEMO SAN ISIDRO por 186.4 PEN cada uno" |
| Primer texto (ms) | consulta 27326 · acción 28006 · memoria 18214 | consulta 23308 · acción 29956 · memoria 18938 |
| Respuesta completa (ms) | consulta 27641 · acción 28734 · memoria 18919 | consulta 23469 · acción 30089 · memoria 19088 |
| Tokens (entrada / salida) | consulta 3705 / 1465 · acción 4717 / 2875 · memoria 3364 / 1570 | consulta 3705 / 1568 · acción 4887 / 2418 · memoria 3357 / 1588 |

Sin tool que la resuelva (`¿Cuál es el saldo de mi cuenta de ahorros?`): con los dos runtimes respondió `out_of_scope`, sin ninguna `→` y sin inventar un saldo (react: 13638 / 13859 ms; agent_framework: 16113 / 16264 ms).

### ¿La skill frenó la tool de otro dominio?

Mensaje: `Simúlame la cuota de un préstamo de 20000 soles a 24 meses` (la tool `simulate_installment` es de `loans`). Respuesta: con los dos runtimes, ninguna `→` y `out_of_scope`: "Lo siento, eso está fuera del alcance de este canal. No puedo simular préstamos..." (react) y "Lo siento, no puedo ayudar con simulaciones de préstamos aquí..." (agent_framework). No inventó una cuota: el modelo nunca vio esa tool, porque ni el MCP (filtrado por `X-Bank-Domain`) ni la skill de fraud la ofrecen.

### Diferencias entre los dos runtimes

Ninguna en el comportamiento: las mismas tools, el mismo `NO SE EJECUTA`, la misma memoria y el mismo streaming (`→`, resultado, intención y respuesta en pedazos). Cambian detalles que decide el modelo en cada corrida: `limit=20` con react y `limit=10` con agent_framework, la redacción del motivo del reclamo y que agent_framework no citó fuentes en la consulta (react citó `chargeback-form.md`). Los tiempos y los tokens son del mismo orden (20 a 30 s el primer texto con tools), porque los dos llaman al mismo deployment `gpt-5-mini`; agent_framework fue algo más rápido en la consulta y algo más lento en la acción y en la pregunta sin tool.

### Conclusión

Cambiar quién conduce el turno fue una línea del `.env` (`AGENT_RUNTIME`): las reglas (lista blanca de la skill, `max_tool_rounds` y acción sensible pendiente) viven en `ChatService` y se cumplieron igual con los dos runtimes. La skill de fraud corrigió lo que se vio en la sesión 6: ahora el modelo consulta, muestra los duplicados y pide confirmación antes de `file_claim`, en vez de pedir el reclamo en el primer turno. La memoria de trabajo permitió "registra el reclamo por el cargo duplicado" y "¿qué movimientos estaban duplicados?" sin volver a llamar a `get_transactions`. El `.env` queda con `AGENT_RUNTIME=agent_framework` para la sesión 8.
