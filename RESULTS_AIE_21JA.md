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