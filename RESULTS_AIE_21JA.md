# S4
## En local
Tú: ¿Cuál es el plazo para presentar un reclamo?
  Agente [product_question]: Tiene hasta 60 días calendario desde la fecha de la operación para reclamar una operación no reconocida. Para reclamos por cobros de comisiones o intereses, el plazo es de 1 año desde el cobro.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
  (primer texto en 8076 ms, respuesta completa en 8280 ms, 932 tokens de entrada, 325 de salida)
Tú: ¿y si es por fraude?
  Agente [product_question]: Si es por fraude (operación no reconocida): tiene hasta 60 días calendario desde la fecha de la operación para presentar el reclamo. El banco responde todo reclamo en un máximo de 15 días hábiles; las operaciones no reconocidas con tarjeta se resuelven en un máximo de 10 días hábiles.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿En cuánto tiempo me responden?
   [3] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 4. Plazos de respuesta
  (primer texto en 13576 ms, respuesta completa en 13841 ms, 1194 tokens de entrada, 1323 de salida)
Tú: ¿Qué es un contracargo?
  Agente [product_question]: No hay una definición de “contracargo” en los fragmentos proporcionados.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 4. Plazos de respuesta
   [3] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿Cuánto tiempo tengo para reclamar un cargo?
   [4] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿En cuánto tiempo me responden?
   [5] response-times.csv · response-times
  (primer texto en 14322 ms, respuesta completa en 14454 ms, 1449 tokens de entrada, 1372 de salida)
Tú: ¿Qué decía la política de bloqueo de 2022?
  Agente [product_question]: La política indicaba que el titular no asume las operaciones no reconocidas realizadas después del reporte de bloqueo. Las operaciones realizadas antes del reporte se evalúan según el reglamento de atención de reclamos.
  Fuentes:
   [1] card-blocking-policy.docx · Política de bloqueo de tarjetas > Responsabilidad por operaciones
  (primer texto en 10430 ms, respuesta completa en 10606 ms, 1532 tokens de entrada, 1061 de salida)
Tú: ¿A cuánto está el dólar hoy?
  Agente [out_of_scope]: Lo siento, eso está fuera de mi área. No puedo proporcionar cotizaciones del dólar. Consulta la página web o la app del banco, o fuentes oficiales como el Banco Central (BCR) para la cotización del día.
  (primer texto en 7140 ms, respuesta completa en 7370 ms, 1515 tokens de entrada, 609 de salida)

## Comparacion
### SEARCH_TOP_K = 2
(agent) PS D:\github\agent-scratch> uv run python dev/chat.py                                         
Conversación con el agente. Escribe "nueva" para otra sesión o "salir" para terminar.
Tú: ¿Cuál es el plazo para presentar un reclamo?
  Agente [product_question]: Tiene hasta 60 días calendario desde la fecha de la operación para reclamar una operación no reconocida. Para reclamos por cobros de comisiones o intereses, el plazo es de 1 año desde el cobro. Si el reclamo es por un cobro duplicado del propio banco, el plazo no se amplía. Si no entrega la información mínima, el plazo se suspende hasta que la complete por un máximo de 5 días hábiles; pasado ese plazo el reclamo se archiva y puede presentarlo nuevamente.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 4. Plazos de respuesta > 4.2 Excepciones
  (primer texto en 11322 ms, respuesta completa en 11612 ms, 690 tokens de entrada, 647 de salida)
Tú: ¿y si es por fraude?
  Agente [product_question]: Para casos de fraude (operación no reconocida) tiene hasta 60 días calendario desde la fecha de la operación para presentar el reclamo.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿Cuánto tiempo tengo para reclamar un cargo?
  (primer texto en 11729 ms, respuesta completa en 11875 ms, 1047 tokens de entrada, 985 de salida)

### SEARCH_TOP_K = 10
Tú: ¿Cuál es el plazo para presentar un reclamo?
  Agente [product_question]: Para operaciones no reconocidas tienes hasta 60 días calendario desde la fecha de la operación para presentar el reclamo. Para reclamos por cobros de comisiones o intereses, el plazo es de 1 año desde el cobro.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
  (primer texto en 11677 ms, respuesta completa en 11841 ms, 1372 tokens de entrada, 456 de salida)
Tú: ¿y si es por fraude?
  Agente [product_question]: El cliente tiene hasta 60 días calendario, contados desde la fecha de la operación, para reclamar una operación no reconocida (fraude).
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿Cuánto tiempo tengo para reclamar un cargo?
  (primer texto en 11964 ms, respuesta completa en 12101 ms, 1763 tokens de entrada, 1160 de salida)

## Contra AI Search
  Tú: ¿Cuál es el plazo para presentar un reclamo?
  Agente [product_question]: Tienes hasta 60 días calendario, contados desde la fecha de la operación, para presentar un reclamo por una operación no reconocida. Para reclamos sobre cobros de comisiones o intereses, el plazo es de 1 año desde el cobro.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿Cuánto tiempo tengo para reclamar un cargo?
  (primer texto en 8863 ms, respuesta completa en 9024 ms, 915 tokens de entrada, 400 de salida)
Tú: ¿y si es por fraude?
  Agente [product_question]: Si es por fraude (operación no reconocida) tienes hasta 60 días calendario desde la fecha de la operación para presentar el reclamo. El banco responde en un plazo máximo de 10 días hábiles para operaciones no reconocidas con tarjeta; ese plazo puede ampliarse una vez por 15 días hábiles si depende de la marca o del comercio.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿En cuánto tiempo me responden?
   [3] response-times.csv · response-times
  (primer texto en 13066 ms, respuesta completa en 13240 ms, 1289 tokens de entrada, 1390 de salida)
Tú: ¿Qué es un contracargo?
  Agente [product_question]: Un contracargo es la devolución de una compra con tarjeta que el banco gestiona ante la marca de la tarjeta cuando el comercio no entregó el producto, cobró un monto distinto o la operación no fue autorizada por el titular.
  Fuentes:
   [1] credit-card-chargebacks.html · Contracargos con tarjeta de crédito > Qué es un contracargo
  (primer texto en 13376 ms, respuesta completa en 13524 ms, 1533 tokens de entrada, 1204 de salida)
Tú: ¿Qué decía la política de bloqueo de 2022?
  Agente [product_question]: No encontré la “política de bloqueo de 2022” en los fragmentos proporcionados. Si quieres, indica qué aspecto te interesa (bloqueo preventivo, plazos, requisitos) o sube el documento y lo reviso.
  (primer texto en 11913 ms, respuesta completa en 12120 ms, 1778 tokens de entrada, 1152 de salida)
Tú: ¿A cuánto está el dólar hoy?
  Agente [out_of_scope]: No puedo proporcionar cotizaciones en tiempo real. Para conocer el tipo de cambio hoy, revisa la web o la app del Banco Demo, la página del Banco Central de Reserva del Perú o consulta una casa de cambio autorizada.
  (primer texto en 7840 ms, respuesta completa en 7999 ms, 1687 tokens de entrada, 610 de salida) 

# S5
## Línea base (S5)
Resumen de 30 casos (juez local):
  recall@5: 1.00   intención: 0.93   fuentes: 0.97   hechos: 0.93
  apoyo: 5.0/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 1
  tokens: 28589 de entrada, 15210 de salida
Detalle de cada caso: D:\github\agent-scratch\data\eval\fraud-20261110-103547.json

## Línea base + 3 preguntas
Resumen de 33 casos (juez local):
  recall@5: 0.97   intención: 1.00   fuentes: 0.94   hechos: 0.80
  apoyo: 5.0/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 1
  tokens: 31144 de entrada, 18452 de salida
Detalle de cada caso: D:\github\agent-scratch\data\eval\fraud-20261110-105557.json

## Resultado del juez
Resumen de 33 casos (juez azure_evaluation):
  recall@5: 0.97   intención: 1.00   fuentes: 0.94   hechos: 0.83
  apoyo: 4.9/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 1
  tokens: 31191 de entrada, 17916 de salida
Detalle de cada caso: D:\github\agent-scratch\data\eval\fraud-20261113-085356.json

# S6
## Sesión 6 — Tools del MCP en el chat

Dominio: `fraud`. MCP: el mock (`http://127.0.0.1:8200/mcp`) y, si ya tienes `MCP_URL`, el compartido (`https://ca-mcp-server.icybush-2ea2dfc1.eastus2.azurecontainerapps.io/mcp`).

### Tools de tu dominio

| MCP | Tools que lista `dev/mcp/mcp_tools.py` |
|---|---|
| Mock | block_card¬ acción sensible¬ card_id, reason ; file_claim¬ acción sensible¬ customer_id, transaction_id, reason ; get_claim_status¬ consulta¬ claim_id ; get_transactions¬ consulta¬ customer_id, limit |
| Compartido | get_transactions, get_claim_status, block_card, file_claim |

### Conversación en `dev/chat.py` (paso 12)

| Prueba | Mensaje | Tool pedida (`→`) | Qué pasó | Primer texto / respuesta completa (ms) |
|---|---|---|---|---|
| Consulta de tu dominio | Soy CUS-1001, ¿puedo subir la línea de mi tarjeta CRD-2001 a 4000? | → get_transactions(customer_id=CUS-1001, limit=10) | La respuesta se clasifica como sensitive_action, el agente identifica que ha visto dos cargos en el supermercado SUPERMERCADO DEMO SAN ISIDRO (TRX-3001 y TRX-3002) | 17974 ms / 19749 ms |
| Acción confirmada | Sí, registra el reclamo por el cargo duplicado | No invoca a ninguna tool | Pide confirmar por cuál transacción se ingresará el reclamo (TRX-3001 y TRX-3002), indica lo que ocurrirá y cita las fuentes consultadas | 18089 ms / 18491 ms |
| Acción confirmada | Confirmo que deseo reclamar la transacción TRX-3002. El motivo es que me cobraron dos veces en el supermercado. Solicito registrar el reclamo. | → file_claim(customer_id=CUS-1001, transaction_id=TRX-3002, reason=Me cobraron dos veces en el supermercado; solicito reclamo por cargo duplicado.) | Respuesta NO SE EJECUTA, pendiente de aprobacion. Devuelve un json con status pendiente_aporbacion e indica que ha solicitado el reigstro delreclamo y queda pendinete aprobación por un asesor. | 25334 ms / 25481 ms |
| Sin tool que la resuelva | ¿Cuál es el saldo de mi cuenta de ahorros? | No invoca a ninguna tool | Indica que no puede ver saldos y se marca como out_of_scope. Cita la fuente service-channels.html | 12806 ms / 13062 ms |
| Tool de otro dominio | Soy CUS-1001, quiero solicitar un préstamo personal de S/ 20,000 a 24 meses. ¿Cuánto pagaría mensualmente? | El agente responde out_of_scope, indica que el alcance de este canal es fraude, bloqueo y reclamos. | No invoca a ninguna tool | 12911 ms / 13728 ms |

### ¿El modelo inventó algún dato cuando ninguna tool lo resolvía?

No. Al consultar el saldo de una cuenta de ahorros, el agente identificó correctamente que la solicitud estaba fuera de las capacidades disponibles para el dominio fraud y clasificó la respuesta como out_of_scope.

No inventó un saldo ni intentó obtenerlo mediante una tool que no correspondía. En su lugar, explicó la limitación y orientó al usuario hacia los canales bancarios disponibles, citando como fuente el documento service-channels.html.

### Conclusión

Las pruebas realizadas permitieron verificar la integración del agente con las tools MCP del dominio fraud, tanto en el servidor mock como en el compartido.

El agente utilizó correctamente get_transactions para identificar dos cargos duplicados (TRX-3001 y TRX-3002), correspondientes a un consumo de S/ 186.40 en SUPERMERCADO DEMO SAN ISIDRO.

Ante la solicitud de registrar un reclamo, el agente solicitó identificar la transacción afectada y proporcionar una descripción del problema antes de continuar. No ejecutó ninguna acción sensible durante la conversación observada.

Asimismo, frente a una consulta que no podía resolver, como el saldo de una cuenta de ahorros, reconoció sus limitaciones sin inventar información y proporcionó orientación respaldada por el corpus documental.

En general, el comportamiento observado demuestra que el agente puede consultar información mediante MCP, conservar el contexto conversacional y reconocer solicitudes fuera de su alcance.