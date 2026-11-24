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

Ahora el agente consulta los movimientos del cliente con las tools y además sigue citando el corpus, así que la respuesta mezcla datos reales con el procedimiento de reclamos. Lo que más me llamó la atención fue el primer turno: el modelo pidió el `file_claim` sin que el cliente lo confirmara. No pasó nada porque las acciones sensibles se quedan en pendiente, pero queda claro que no se puede confiar solo en el modelo para eso. Pasar del mock al MCP compartido fue más fácil de lo que pensaba, solo cambié la URL y el scope en el `.env` (la URL tiene que terminar en `/mcp`, si no da Not Found). Lo malo es el tiempo: con tools la primera respuesta se demora entre 25 y 40 segundos.

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

En lo importante se portaron igual: usaron las mismas tools, el reclamo quedó sin ejecutar en los dos y los dos se acordaron de los movimientos. Las diferencias que vi son más del modelo que del runtime, por ejemplo react pidió `limit=20` y agent_framework `limit=10`, y en la consulta solo react citó una fuente (`chargeback-form.md`). En tiempos tampoco hubo mucha diferencia, todo anduvo entre 20 y 30 segundos, lo cual tiene sentido porque los dos usan el mismo `gpt-5-mini` por detrás.

### Conclusión

Me gustó que cambiar de runtime sea solo cambiar `AGENT_RUNTIME` en el `.env` y reiniciar. Como las reglas están en `ChatService` y no en el framework, con los dos se respetó lo mismo. La skill sí se notó: en la sesión 6 el modelo pedía el reclamo de frente, y ahora primero revisa los movimientos, me muestra los duplicados y espera a que confirme. La memoria de trabajo también funcionó, porque cuando le dije "registra el reclamo por el cargo duplicado" no volvió a consultar y ya sabía que era TRX-3002. Dejé el `.env` con `agent_framework` para la sesión 8.

## Sesión 8 — Aprobación humana, validación y reintentos

Dominio: `fraud` (paso 6), con Foundry real, Azure AI Search (`idx-team-03`) y el MCP compartido.

| Caso | Runtime | Mensaje | Qué pasó | Resultado o ID |
|---|---|---|---|---|
| Aprobar | `agent_framework` | `Soy CUS-1001, me cobraron dos veces en el supermercado` → `Sí, registra el reclamo por el cargo duplicado TRX-3002` | Turno 1: `get_transactions` encontró TRX-3001 y TRX-3002 y el agente pidió confirmación. Turno 2: `file_claim(customer_id=CUS-1001, transaction_id=TRX-3002, ...)` quedó **NO SE EJECUTA** (`action_id: call-b72b120a`). Respondí `s` como asesor y recién ahí se ejecutó | `CLM-9001`, `registered`, fecha límite de respuesta 2026-11-27 |
| Rechazar | `react` | Los mismos dos mensajes | `file_claim` sobre TRX-3002 quedó **NO SE EJECUTA** (`action_id: call_OKA6VDgpZMdA4JFmNXQg6jlY`). Respondí `n`: "rechazada por el asesor" y el agente dijo "El asesor rechazó la solicitud de reclamo por TRX-3002; la acción no se ejecutó." | sin ID: `rejected`, no llegó al MCP |
| Error de negocio (`CUS-9999`) | `agent_framework` | `Soy CUS-9999, me cobraron dos veces en el supermercado` | `get_transactions(customer_id=CUS-9999)` → `error: El cliente CUS-9999 no existe`. Sin reintento y sin 502: el agente explicó que el código no existe y pidió confirmarlo | `{"error": "El cliente CUS-9999 no existe"}` |
| Input inválido | `agent_framework` | `Mi número de cliente es 1001, ¿qué movimientos tengo en mi tarjeta?` | El modelo no mandó `1001`: lo convirtió a `CUS-1001` siguiendo el patrón `^CUS-\d{4}$` del schema y la consulta salió bien. La validación del paso 3 no tuvo que actuar; la cubre `test_invalid_arguments_never_reach_the_mcp` | `get_transactions ok` (TRX-3001 a TRX-3004) |

### La trayectoria en el log

```
trayectoria 7127c5fb-460e-4f91-a8c7-fb97ecc7bfcc: get_transactions ok → respuesta sensitive_action
trayectoria 7127c5fb-460e-4f91-a8c7-fb97ecc7bfcc: file_claim pending_approval → respuesta sensitive_action
trayectoria 7127c5fb-460e-4f91-a8c7-fb97ecc7bfcc: decisión del asesor → file_claim ok
trayectoria 06f1d70c-4476-42aa-845e-6819d4493dbc: get_transactions error → respuesta sensitive_action
trayectoria 867ca43c-ed84-4799-b3db-9daa3d2cfe29: get_transactions ok → respuesta data_query
trayectoria 91c434d6-b43c-4180-81d6-431554606da0: get_transactions ok → respuesta sensitive_action
trayectoria 91c434d6-b43c-4180-81d6-431554606da0: file_claim pending_approval → respuesta sensitive_action
trayectoria 91c434d6-b43c-4180-81d6-431554606da0: decisión del asesor → file_claim rejected
```

Las tres primeras son la aprobación (`agent_framework`), la cuarta el error de negocio, la quinta el input inválido y las tres últimas el rechazo (`react`). No apareció ninguna línea `falló (intento ...)`: el MCP compartido respondió siempre, así que el reintento solo se comprobó con los tests del paso 3.

### ¿Algo se ejecutó sin que lo aprobaras?

No. Con los dos runtimes, `file_claim` salió primero como **NO SE EJECUTA, pendiente de aprobación** y la trayectoria lo registra como `pending_approval`. El reclamo CLM-9001 apareció solo después de mi `s`, y con `n` la acción nunca llegó al MCP (`rejected`). Las consultas (`get_transactions`) sí se ejecutaron directo, como corresponde.

### Conclusión

Con esta sesión ya me siento más tranquilo con las acciones sensibles, porque nada se ejecuta hasta que alguien dice que sí. Lo probé aprobando con agent_framework y rechazando con react, y en los dos casos funcionó igual. Cuando aprobé, el agente le dijo al cliente que el reclamo CLM-9001 quedó registrado, pero no le prometió la devolución, que es lo correcto. Con CUS-9999 ya no sale un error 502, el agente simplemente le pide al cliente que revise su código. Las líneas de trayectoria del log me sirvieron bastante para seguir qué hizo en cada turno sin tener que leer todo. Lo que falta es que la acción pendiente se guarda en memoria, entonces si se reinicia el agente antes de decidir se pierde, y eso se arregla en la sesión 9 con Cosmos DB.
